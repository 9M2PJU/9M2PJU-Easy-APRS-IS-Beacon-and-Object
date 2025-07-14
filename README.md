# 9M2PJU Easy APRS-IS Beacon and Object GUI

A simple Python GUI to send APRS-IS beacon and object packets using PyQt6, with YAML-based configuration. Designed for amateur radio operators who want a graphical way to manage APRS objects and beaconing.

![9M2PJU Easy APRS](9m2pju-aprs.png)

---

## 📡 Features

- ✅ APRS-IS login and beaconing
- 🧭 Supports fixed-position beacons and additional object beacons
- 🗺 Symbol and comment configuration per object
- 🧪 "Dry Run" mode to test without transmitting
- 🔁 Staggered beaconing intervals
- 💾 YAML config file for easy editing/saving
- 🖥 Simple and responsive PyQt6 GUI

---

## 🔧 Requirements

- Python 3.8+
- PyQt6
- `yaml` (PyYAML)

Install requirements with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

Make sure you're in your virtual environment or have dependencies installed:

```bash
python gui.py
```

To start the beacon from CLI:

```bash
python 9m2pju-aprs-beacon.py
```

---

## 🛠 Configuration File (`config.yaml`)

This file is auto-managed by the GUI but can be manually edited.

```yaml
callsign: 9M2PJU
passcode: 12970
latitude: 3.0738
longitude: 101.4457
comment: Main station 9M2PJU
symbol_table: /
symbol: r
interval: 10
dry_run: false
staggered: true

beacons:
  - name: DIGI01
    latitude: 3.1234
    longitude: 101.5678
    symbol_table: /
    symbol: #
    comment: Digi at hill
    interval: 15

  - name: REPEATER
    latitude: 3.1415
    longitude: 101.6789
    symbol_table: /
    symbol: R
    comment: 147.500MHz
    interval: 30
```

---

## 🔐 Passcode Note

Your **APRS-IS passcode** is required for transmission. This is based on your callsign and is used for authentication. You can generate it using APRS-IS tools or calculators online.

---

## 💻 Development

To contribute:

```bash
git clone git@github.com:9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object.git
cd 9M2PJU-Easy-APRS-IS-Beacon-and-Object
python gui.py
```

---

## 📜 License

MIT License — free for anyone to use or improve.

---

## 📞 Contact

- **Callsign**: 9M2PJU
- GitHub: [github.com/9M2PJU](https://github.com/9M2PJU)
