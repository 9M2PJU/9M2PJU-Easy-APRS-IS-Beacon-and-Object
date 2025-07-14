# 9M2PJU Easy APRS-IS Beacon and Object

Presenting a sleek, Python-based graphical interface crafted with PyQt6, designed to simplify **APRS-IS beacon and object packet transmission**. This intuitive application is tailored for amateur radio operators seeking a streamlined, visual method to manage their APRS objects and beaconing activities.

<img width="1008" height="732" alt="image" src="https://github.com/user-attachments/assets/8fe80209-5ee0-4338-8dbb-475909af4ab4" />

-----

## 🌟 Key Features

  * **Effortless APRS-IS Integration**: Seamless login and beaconing capabilities.
  * **Versatile Beaconing**: Supports both fixed-position and multiple object beacons.
  * **Customizable Objects**: Configure unique symbols and comments for each object.
  * **"Dry Run" Mode**: Test your configurations safely without transmitting.
  * **Intelligent Staggered Intervals**: Optimize your beaconing with staggered transmission times.
  * **YAML Configuration**: Easy-to-edit and persistent settings via a YAML file.
  * **Modern PyQt6 GUI**: A responsive and user-friendly graphical interface.

-----

## ⚙️ Prerequisites

Ensure you have **Python 3.8+** installed along with the following libraries:

  * `PyQt6`
  * `PyYAML` (`yaml`)

Install these dependencies swiftly using:

```bash
pip install -r requirements.txt
```

-----

## 🚀 Getting Started

Navigate to your project directory and execute the following:

To launch the graphical interface:

```bash
python gui.py
```

To initiate beaconing directly from the command line:

```bash
python 9m2pju-aprs-beacon.py
```

-----

## 🛠 Configuration (`config.yaml`)

While the GUI manages this file automatically, you can always fine-tune your settings manually.

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

-----

## 🔐 Important: APRS-IS Passcode

Your **APRS-IS passcode** is crucial for successful transmission. This unique code is derived from your callsign and is essential for authenticating with the APRS-IS network. If you don't have one, you can generate it using various online APRS-IS tools or calculators.

-----

## 💻 Contribution

We welcome contributions\! To get involved:

```bash
git clone git@github.com:9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object.git
cd 9M2PJU-Easy-APRS-IS-Beacon-and-Object
python gui.py
```

-----

## 📜 License

This project is released under the **GNU General Public License v3.0 (GPLv3)**. Feel free to use, modify, and distribute it in accordance with the terms of the license.

-----

## 📞 Get in Touch

  * **Callsign**: 9M2PJU
  * **GitHub**: [github.com/9M2PJU](https://github.com/9M2PJU)

-----

Do you have any questions about setting up the application or its features?
