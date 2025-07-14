import sys, yaml, subprocess, threading, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtGui import QTextCursor
from datetime import datetime


class ProcessMonitor(QObject):
    output_received = pyqtSignal(str)

    def __init__(self, process):
        super().__init__()
        self.process = process
        self.running = True

    def monitor(self):
        while self.running and self.process.poll() is None:
            try:
                line = self.process.stdout.readline()
                if line:
                    self.output_received.emit(line.strip())
                else:
                    time.sleep(0.1)
            except:
                break


class APRSGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("9M2PJU Easy APRS Beacon and Object")
        self.setGeometry(200, 200, 1000, 700)
        self.config = {}
        self.aprs_process = None
        self.process_monitor = None
        self.monitor_thread = None

        self.init_ui()
        self.load_config()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.status_label = QLabel("Status: Ready")
        self.status_label.setStyleSheet("QLabel { background-color: #f0f0f0; padding: 5px; border: 1px solid #ccc; }")
        main_layout.addWidget(self.status_label)

        form_layout = QFormLayout()
        self.callsign_input = QLineEdit()
        self.passcode_input = QLineEdit()
        self.lat_input = QLineEdit()
        self.lon_input = QLineEdit()
        self.comment_input = QLineEdit()
        self.symbol_table_input = QLineEdit()
        self.symbol_input = QLineEdit()
        self.interval_input = QSpinBox()
        self.interval_input.setMinimum(1)
        self.interval_input.setMaximum(1440)
        self.interval_input.setValue(10)
        self.dry_run_check = QCheckBox("Dry Run (Test Mode)")
        self.staggered_check = QCheckBox("Staggered beacon delay")

        form_layout.addRow("Callsign:", self.callsign_input)
        form_layout.addRow("Passcode:", self.passcode_input)
        form_layout.addRow("Latitude:", self.lat_input)
        form_layout.addRow("Longitude:", self.lon_input)
        form_layout.addRow("Comment:", self.comment_input)
        form_layout.addRow("Symbol Table:", self.symbol_table_input)
        form_layout.addRow("Symbol:", self.symbol_input)
        form_layout.addRow("Interval (minutes):", self.interval_input)
        form_layout.addRow(self.dry_run_check)
        form_layout.addRow(self.staggered_check)

        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels([
            "Name", "Latitude", "Longitude", "Interval", "Comment", "Symbol Table", "Symbol"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)

        add_btn = QPushButton("➕ Add Object")
        remove_btn = QPushButton("➖ Remove Selected")
        save_btn = QPushButton("💾 Save Config")
        self.start_btn = QPushButton("▶ Start")
        self.stop_btn = QPushButton("⏹ Stop")
        clear_log_btn = QPushButton("🗑 Clear Log")

        self.start_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        self.stop_btn.setStyleSheet("QPushButton { background-color: #f44336; color: white; font-weight: bold; }")
        self.stop_btn.setEnabled(False)

        add_btn.clicked.connect(self.add_beacon_row)
        remove_btn.clicked.connect(self.remove_selected_row)
        save_btn.clicked.connect(self.save_config)
        self.start_btn.clicked.connect(self.start_beaconing)
        self.stop_btn.clicked.connect(self.stop_beaconing)
        clear_log_btn.clicked.connect(self.clear_log)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(clear_log_btn)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setMaximumHeight(200)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(QLabel("Object Beacons:"))
        main_layout.addWidget(self.table)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(QLabel("Beacon Process Log:"))
        main_layout.addWidget(self.log_box)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.check_process_status)
        self.status_timer.start(1000)

    def log(self, msg):
        self.log_box.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
        cursor = self.log_box.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.log_box.setTextCursor(cursor)
        self.log_box.ensureCursorVisible()

    def clear_log(self):
        self.log_box.clear()
        self.log("Log cleared")

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)

    def show_info(self, title, message):
        QMessageBox.information(self, title, message)

    def add_beacon_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col in range(7):
            self.table.setItem(row, col, QTableWidgetItem(""))

    def remove_selected_row(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def load_config(self):
        try:
            with open("config.yaml", "r") as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            self.log(f"No existing config found: {e}")
            return

        self.callsign_input.setText(self.config.get("callsign", ""))
        self.passcode_input.setText(str(self.config.get("passcode", "")))
        self.lat_input.setText(str(self.config.get("latitude", "")))
        self.lon_input.setText(str(self.config.get("longitude", "")))
        self.comment_input.setText(self.config.get("comment", ""))
        self.symbol_table_input.setText(self.config.get("symbol_table", "/"))
        self.symbol_input.setText(self.config.get("symbol", "r"))
        self.interval_input.setValue(self.config.get("interval", 10))
        self.dry_run_check.setChecked(self.config.get("dry_run", False))
        self.staggered_check.setChecked(self.config.get("staggered", False))

        for beacon in self.config.get("beacons", []):
            self.add_beacon_row()
            row = self.table.rowCount() - 1
            self.table.setItem(row, 0, QTableWidgetItem(beacon.get("name", "")))
            self.table.setItem(row, 1, QTableWidgetItem(str(beacon.get("latitude", ""))))
            self.table.setItem(row, 2, QTableWidgetItem(str(beacon.get("longitude", ""))))
            self.table.setItem(row, 3, QTableWidgetItem(str(beacon.get("interval", ""))))
            self.table.setItem(row, 4, QTableWidgetItem(beacon.get("comment", "")))
            self.table.setItem(row, 5, QTableWidgetItem(beacon.get("symbol_table", "/")))
            self.table.setItem(row, 6, QTableWidgetItem(beacon.get("symbol", "r")))

    def save_config(self):
        if not self.callsign_input.text().strip():
            self.show_error("Validation Error", "Callsign is required")
            return

        if not self.dry_run_check.isChecked():
            if not self.passcode_input.text().strip():
                self.show_error("Validation Error", "Passcode is required")
                return
            try:
                float(self.lat_input.text())
                float(self.lon_input.text())
            except ValueError:
                self.show_error("Validation Error", "Latitude/Longitude must be valid numbers")
                return

        beacons = []
        for row in range(self.table.rowCount()):
            try:
                name = self.table.item(row, 0).text() if self.table.item(row, 0) else ""
                if not name:
                    continue
                beacons.append({
                    "name": name,
                    "latitude": float(self.table.item(row, 1).text()),
                    "longitude": float(self.table.item(row, 2).text()),
                    "interval": int(self.table.item(row, 3).text()),
                    "comment": self.table.item(row, 4).text() or "",
                    "symbol_table": self.table.item(row, 5).text() or "/",
                    "symbol": self.table.item(row, 6).text() or "r"
                })
            except Exception as e:
                self.show_error("Validation Error", f"Error in row {row + 1}: {e}")
                return

        self.config = {
            "callsign": self.callsign_input.text().strip().upper(),
            "passcode": self.passcode_input.text().strip(),
            "latitude": float(self.lat_input.text()) if self.lat_input.text() else 0,
            "longitude": float(self.lon_input.text()) if self.lon_input.text() else 0,
            "comment": self.comment_input.text(),
            "symbol_table": self.symbol_table_input.text() or "/",
            "symbol": self.symbol_input.text() or "r",
            "interval": self.interval_input.value(),
            "dry_run": self.dry_run_check.isChecked(),
            "staggered": self.staggered_check.isChecked(),
            "beacons": beacons,
            "aprs_servers": [
                {"host": "aprs.hamradio.my", "port": 14580},
                {"host": "rotate.aprs.net", "port": 14580}
            ]
        }

        try:
            with open("config.yaml", "w") as f:
                yaml.safe_dump(self.config, f, default_flow_style=False)
            self.log("✅ Configuration saved successfully")
        except Exception as e:
            self.show_error("Save Error", f"Failed to save config: {e}")

    def start_beaconing(self):
        try:
            self.save_config()
            self.aprs_process = subprocess.Popen(
                [sys.executable, "9m2pju-aprs-beacon.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            self.process_monitor = ProcessMonitor(self.aprs_process)
            self.process_monitor.output_received.connect(self.log)
            self.monitor_thread = threading.Thread(target=self.process_monitor.monitor, daemon=True)
            self.monitor_thread.start()
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.status_label.setText("Status: Running")
            self.status_label.setStyleSheet("QLabel { background-color: #4CAF50; color: white; padding: 5px; border: 1px solid #ccc; }")
        except Exception as e:
            self.show_error("Start Error", f"Failed to start beacon: {e}")

    def stop_beaconing(self):
        if self.aprs_process:
            self.aprs_process.terminate()
            try:
                self.aprs_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.aprs_process.kill()
        self.aprs_process = None
        if self.process_monitor:
            self.process_monitor.running = False
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.status_label.setText("Status: Stopped")
        self.status_label.setStyleSheet("QLabel { background-color: #f44336; color: white; padding: 5px; border: 1px solid #ccc; }")

    def check_process_status(self):
        if self.aprs_process and self.aprs_process.poll() is not None:
            self.log(f"⚠ Beacon process terminated with code: {self.aprs_process.returncode}")
            self.stop_beaconing()

    def closeEvent(self, event):
        if self.aprs_process:
            self.stop_beaconing()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = APRSGui()
    gui.show()
    sys.exit(app.exec())
