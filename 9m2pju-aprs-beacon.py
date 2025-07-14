#!/usr/bin/env python3
"""
9M2PJU Easy APRS Beacon - Fixed Version with Proper Login Parsing
"""

import time
import yaml
import socket
import threading
import signal
import sys
import random
from datetime import datetime


class APRSBeacon:
    def __init__(self, config_file="config.yaml"):
        self.config_file = config_file
        self.config = {}
        self.running = False
        self.threads = []
        self.aprs_socket = None
        self.login_callsign = ""
        self.beacon_callsign = ""
        self.aprs_servers = []

        self.load_config()
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config = yaml.safe_load(f)

            self.login_callsign = self.config.get('callsign', '').strip().upper()
            self.beacon_callsign = self.config.get('beacon_callsign', self.login_callsign).strip().upper()
            self.aprs_servers = self.config.get("aprs_servers", [
                {"host": "aprs.hamradio.my", "port": 14580},
                {"host": "rotate.aprs.net", "port": 14580}
            ])

            self.log("✅ Configuration loaded successfully")
        except Exception as e:
            self.log(f"❌ Error loading config: {e}")
            sys.exit(1)

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
        sys.stdout.flush()

    def signal_handler(self, signum, frame):
        self.log("🛑 Shutdown signal received")
        self.stop()

    def connect_aprs_is(self):
        callsign = self.login_callsign
        passcode = str(self.config.get('passcode', ''))

        for server in self.aprs_servers:
            host = server['host']
            port = server['port']
            try:
                self.log(f"🔗 Connecting to APRS-IS server: {host}:{port}")
                self.aprs_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.aprs_socket.settimeout(30)
                self.aprs_socket.connect((host, port))
                self.log("✅ TCP connection established")

                login_str = f"user {callsign} pass {passcode} vers ManualLogin 1.0\r\n"
                time.sleep(1.0)
                self.log(f"📤 Sending login: {login_str.strip()}")
                self.aprs_socket.sendall(login_str.encode('utf-8'))

                # Receive multiple lines from server
                response = ""
                self.aprs_socket.settimeout(5.0)
                try:
                    while True:
                        chunk = self.aprs_socket.recv(1024).decode("utf-8")
                        if not chunk:
                            break
                        response += chunk
                        if "logresp" in response.lower():
                            break
                except socket.timeout:
                    pass

                self.log("📥 Server response:\n" + response.strip())

                if "logresp" in response.lower() and "verified" in response.lower():
                    self.log(f"✅ Logged in as {callsign}")
                    return True
                else:
                    self.log(f"❌ Login rejected")
                    self.aprs_socket.close()
                    self.aprs_socket = None
            except Exception as e:
                self.log(f"❌ Connection failed: {e}")
                self.aprs_socket = None

        self.log("❌ All APRS-IS connection attempts failed")
        return False

    def disconnect_aprs_is(self):
        if self.aprs_socket:
            try:
                self.aprs_socket.close()
                self.log("🔌 Disconnected from APRS-IS")
            except:
                pass
            self.aprs_socket = None

    def format_coordinate(self, coord, is_longitude=False):
        degrees = int(abs(coord))
        minutes = (abs(coord) - degrees) * 60
        if is_longitude:
            direction = 'E' if coord >= 0 else 'W'
            return f"{degrees:03d}{minutes:05.2f}{direction}"
        else:
            direction = 'N' if coord >= 0 else 'S'
            return f"{degrees:02d}{minutes:05.2f}{direction}"

    def create_position_packet(self, callsign, lat, lon, symbol_table, symbol, comment):
        lat_str = self.format_coordinate(lat, False)
        lon_str = self.format_coordinate(lon, True)
        return f"{callsign}>APRS,TCPIP*:={lat_str}{symbol_table}{lon_str}{symbol}{comment}"

    def create_object_packet(self, callsign, obj_name, lat, lon, symbol_table, symbol, comment):
        lat_str = self.format_coordinate(lat, False)
        lon_str = self.format_coordinate(lon, True)
        obj_name_padded = f"{obj_name:<9}"[:9]
        return f"{callsign}>APRS,TCPIP*:;{obj_name_padded}*111111z{lat_str}{symbol_table}{lon_str}{symbol}{comment}"

    def send_packet(self, packet):
        if self.config.get('dry_run', False):
            self.log(f"🔍 DRY RUN: {packet}")
            return True

        try:
            if not self.aprs_socket:
                if not self.connect_aprs_is():
                    return False

            self.aprs_socket.sendall((packet + "\r\n").encode('utf-8'))
            self.log(f"📡 Sent: {packet}")
            return True
        except Exception as e:
            self.log(f"❌ Send failed: {e}")
            self.disconnect_aprs_is()
            return False

    def beacon_main_station(self):
        lat = self.config.get('latitude', 0)
        lon = self.config.get('longitude', 0)
        symbol_table = self.config.get('symbol_table', '/')
        symbol = self.config.get('symbol', 'r')
        comment = self.config.get('comment', '')
        interval = self.config.get('interval', 10) * 60

        while self.running:
            packet = self.create_position_packet(self.beacon_callsign, lat, lon, symbol_table, symbol, comment)
            self.send_packet(packet)
            time.sleep(interval)

    def beacon_object(self, obj_config):
        name = obj_config.get('name', '')
        lat = obj_config.get('latitude', 0)
        lon = obj_config.get('longitude', 0)
        symbol_table = obj_config.get('symbol_table', '/')
        symbol = obj_config.get('symbol', 'r')
        comment = obj_config.get('comment', '')
        interval = obj_config.get('interval', 10) * 60

        while self.running:
            packet = self.create_object_packet(self.beacon_callsign, name, lat, lon, symbol_table, symbol, comment)
            self.send_packet(packet)
            time.sleep(interval)

    def start(self):
        if not self.connect_aprs_is():
            return False

        self.running = True
        main_thread = threading.Thread(target=self.beacon_main_station, daemon=True)
        main_thread.start()
        self.threads.append(main_thread)

        for obj in self.config.get('beacons', []):
            thread = threading.Thread(target=self.beacon_object, args=(obj,), daemon=True)
            thread.start()
            self.threads.append(thread)

        self.log(f"✅ Started {len(self.threads)} beacon threads")
        return True

    def stop(self):
        self.running = False
        self.disconnect_aprs_is()
        for thread in self.threads:
            thread.join(timeout=5)
        self.log("🛑 Beacon stopped")

    def run(self):
        self.log("🚀 Starting APRS beacon...")
        self.log(f"   Login Callsign: {self.login_callsign}")
        self.log(f"   Beacon Callsign: {self.beacon_callsign}")
        self.log(f"   Latitude: {self.config.get('latitude')}")
        self.log(f"   Longitude: {self.config.get('longitude')}")
        self.log(f"   Dry Run: {self.config.get('dry_run', False)}")
        self.log(f"   Objects: {len(self.config.get('beacons', []))}")

        if not self.start():
            sys.exit(1)

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.log("🛑 Keyboard interrupt")
        finally:
            self.stop()


if __name__ == "__main__":
    beacon = APRSBeacon()
    beacon.run()
