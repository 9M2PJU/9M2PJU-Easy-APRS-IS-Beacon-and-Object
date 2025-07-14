# 9M2PJU Easy APRS-IS Beacon and Object

Python-based graphical interface crafted with **PyQt6**, designed to simplify **APRS-IS beacon and object packet transmission**. This intuitive application is tailored for amateur radio operators seeking a streamlined, visual method to manage their APRS objects and beaconing activities.

<img width="1008" height="732" alt="image" src="https://github.com/user-attachments/assets/b87d5e8e-f843-4944-8132-7e5a651e249c" />

---

## 🌟 Key Features

* **Effortless APRS-IS Integration**: Seamless login and beaconing capabilities.
* **Versatile Beaconing**: Supports both **fixed-position and multiple object beacons**.
* **Customizable Objects**: Configure unique **symbols** and **comments** for each object.
* **"Dry Run" Mode**: Test your configurations safely without transmitting.
* **Intelligent Staggered Intervals**: Optimize your beaconing with staggered transmission times.
* **YAML Configuration**: Easy-to-edit and persistent settings via a `config.yaml` file.
* **Modern PyQt6 GUI**: A responsive and user-friendly graphical interface.

---

## ⚙️ Prerequisites

This application requires **Python 3.8+**. To ensure a clean and isolated development environment, it's highly recommended to use a Python **virtual environment**.

### Setting Up a Virtual Environment and Installing Dependencies

1.  **Create a Virtual Environment**:
    Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    python -m venv .venv
    ```
    This command creates a new directory named `.venv` (a common convention) within your project, which will contain a private Python interpreter and package installations.

2.  **Activate the Virtual Environment**:
    Before installing dependencies or running the application, you need to activate the virtual environment.
    * **On Windows**:
        ```bash
        .\.venv\Scripts\activate
        ```
    * **On macOS/Linux**:
        ```bash
        source ./.venv/bin/activate
        ```
    You'll typically see `(.venv)` or similar text appear in your terminal prompt, indicating that the virtual environment is active.

3.  **Install Required Libraries**:
    With your virtual environment activated, install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    This will install `PyQt6` and `PyYAML` within your isolated `.venv` environment.

---

## 🚀 Getting Started

Once your environment is set up and dependencies are installed, you're ready to go!

To launch the **graphical interface**:

```bash
python gui.py
````

To initiate **beaconing directly from the command line** (useful for automated setups):

```bash
python 9m2pju-aprs-beacon.py
```

-----

## 🛠 Configuration (`config.yaml`)

This crucial file is **auto-managed by the GUI**, making it incredibly easy to use. However, you can also fine-tune your settings manually if you prefer.

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

Your **APRS-IS passcode** is absolutely essential for successful transmission. This unique code is derived from your callsign and is used for authenticating with the APRS-IS network. If you don't have one, you can easily generate it using various **online APRS-IS tools or calculators**.

-----

## 💻 Contribution

We warmly welcome contributions from the community\! If you'd like to get involved, follow these steps:

```bash
git clone git@github.com:9M2PJU/9M2PJU-Easy-APRS-IS-Beacon-and-Object.git
cd 9M2PJU-Easy-APRS-IS-Beacon-and-Object
python gui.py
```

Feel free to open issues, submit pull requests, or suggest new features. Your input helps make this project even better\!

-----

## 📜 License

This project is released under the **GNU General Public License v3.0 (GPLv3)**. You are free to use, modify, and distribute this software in accordance with the terms of the license. For more details, see the `LICENSE` file in the repository.

-----

## 📞 Get in Touch

Have questions, suggestions, or just want to say hello? Don't hesitate to reach out!

  * **Callsign**: 9M2PJU
  * **GitHub**: [github.com/9M2PJU](https://github.com/9M2PJU)

