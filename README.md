# 🚀 9M2PJU Easy APRS-IS Beacon and Object

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0) 
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub Release](https://img.shields.io/github/v/release/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object)](https://github.com/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object/releases/latest)
[![Issues](https://img.shields.io/github/issues/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object)](https://github.com/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object/issues)
[![Contributors](https://img.shields.io/github/contributors/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object)](https://github.com/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object/graphs/contributors)

---

![App Screenshot](https://github.com/user-attachments/assets/59aa861c-8867-499f-8e91-cc7a18de4d91)

**9M2PJU Easy APRS-IS Beacon and Object** is a Python-powered desktop app built with **PyQt6**, crafted to streamline direct beacon and object to the APRS-IS for amateur radio enthusiasts. Its clean and intuitive GUI lets you manage APRS objects and beaconing effortlessly — no more fuss, just simple and effective operation.

---

## ✨ Features at a Glance

- 🚀 **Seamless APRS-IS Connectivity**  
  Log in and transmit beacons directly to the APRS-IS network with zero hassle.

- 📍 **Flexible Beacon Modes**  
  Support for fixed-location beacons *and* multiple dynamic objects.

- 🎨 **Object Configuration**  
  Assign unique symbols, tables, and descriptive comments per object.

- 🛑 **Safe "Dry Run" Mode**  
  Validate your setups without transmitting, for peace of mind.

- ⏱️ **Smart Staggered Intervals**  
  Avoid network congestion by automatically staggering beacon intervals.

- 📝 **Human-Friendly YAML Configuration**  
  Easily tweak settings through a clean `config.yaml` file.

- 🖥️ **Modern PyQt6 GUI**  
  Responsive, intuitive interface designed for smooth user experience.

---

## ⚙️ Prerequisites

- 🐍 Python 3.8 or higher  
- 🔧 Recommended: use a Python **virtual environment** for clean dependency management.

### Quick Setup Guide

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🚀 How to Run

Launch the graphical interface:

```bash
python gui.py
```

Or run beaconing from the command line (great for automated or headless setups):

```bash
python 9m2pju-aprs-beacon.py
```

---

## 📝 Configuration (`config.yaml`)

The GUI manages this file for you, but manual editing is always an option.

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
    symbol: "#"
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

## 📦 Standalone AppImage Release

🎉 **Pre-built standalone AppImage available for Linux users!**

No need to install Python or dependencies — just download and run.

**Download the latest release:**
[![Latest Release](https://img.shields.io/github/v/release/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object?label=Download%20AppImage)](https://github.com/9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object/releases/latest)

### Running the AppImage

```bash
chmod +x 9M2PJU_Easy_APRS-IS_Beacon_and_Object-x86_64.AppImage
./9M2PJU_Easy_APRS-IS_Beacon_and_Object-x86_64.AppImage
```

---

## 🔐 APRS-IS Passcode

Your APRS-IS passcode authenticates you on the network and is essential for transmission. Generate yours easily at:
[https://pass.hamradio.my](https://pass.hamradio.my)

---

## 🤝 Contributing

Love open source? So do we! 🚀

Feel free to:

* 🐞 File issues
* 💡 Suggest features
* 🔧 Submit pull requests

Your contributions make this project better for everyone!

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.
See the [`LICENSE`](LICENSE) file for full details.

---

## 📬 Stay Connected

Got questions, feedback, or just want to chat? Reach out!

* **Callsign:** 9M2PJU
* **GitHub:** [https://github.com/9M2PJU](https://github.com/9M2PJU)
* **Email:** [9m2pju@hamradio.my](mailto:9m2pju@hamradio.my)

---

Made with ❤️ by amateur radio enthusiasts, for amateur radio enthusiasts worldwide.
