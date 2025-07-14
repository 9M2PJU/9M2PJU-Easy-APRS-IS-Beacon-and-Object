# 9M2PJU Easy APRS-IS Beacon and Object

-----

<img width="1008" height="732" alt="image" src="https://github.com/user-attachments/assets/59aa861c-8867-499f-8e91-cc7a18de4d91" />

The **9M2PJU Easy APRS-IS Beacon and Object** is a user-friendly, Python-based application built with **PyQt6** designed to simplify **APRS-IS beacon and object packet transmission** for amateur radio operators. This intuitive tool provides a visual interface to manage your APRS objects and beaconing activities with ease.

-----

## 🌟 Key Features

  * **Effortless APRS-IS Integration**: Seamlessly log in and transmit beacons to the APRS-IS network.
  * **Versatile Beaconing**: Supports both **fixed-position and multiple object beacons**, catering to diverse operational needs.
  * **Customizable Objects**: Configure unique **symbols** and **comments** for each object, allowing for detailed identification.
  * **"Dry Run" Mode**: Test your configurations safely without transmitting, ensuring accuracy before going live.
  * **Intelligent Staggered Intervals**: Optimize your beaconing with staggered transmission times to avoid congestion and improve network efficiency.
  * **YAML Configuration**: Easy-to-edit and persistent settings managed through a `config.yaml` file, simplifying setup and modifications.
  * **Modern PyQt6 GUI**: A responsive and user-friendly graphical interface for an enhanced user experience.

-----

## ⚙️ Prerequisites

This application requires **Python 3.8+**. For a clean and isolated environment, using a Python **virtual environment** is highly recommended.

### Setting Up a Virtual Environment and Installing Dependencies

1.  **Create a Virtual Environment**:
    Open your terminal or command prompt, navigate to your project directory, and execute:

    ```bash
    python -m venv .venv
    ```

    This command creates a `.venv` directory (a common convention) within your project, housing a private Python interpreter and package installations.

2.  **Activate the Virtual Environment**:
    Before installing dependencies or running the application, you must activate the virtual environment.

      * **On Windows**:
        ```bash
        .\.venv\Scripts\activate
        ```
      * **On macOS/Linux**:
        ```bash
        source ./.venv/bin/activate
        ```

    Upon activation, you'll typically see `(.venv)` or similar text in your terminal prompt, indicating that the virtual environment is active.

3.  **Install Required Libraries**:
    With your virtual environment activated, install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    This command installs `PyQt6` and `PyYAML` within your isolated `.venv` environment.

-----

## 🚀 Getting Started

Once your environment is set up and dependencies are installed, you're ready to use the application\!

To launch the **graphical interface**:

```bash
python gui.py
```

To initiate **beaconing directly from the command line** (ideal for automated setups):

```bash
python 9m2pju-aprs-beacon.py
```

-----

## 🛠 Configuration (`config.yaml`)

The `config.yaml` file is **auto-managed by the GUI**, providing an incredibly user-friendly experience. You can also fine-tune your settings manually if preferred.

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

Your **APRS-IS passcode** is crucial for successful transmission. This unique code is derived from your callsign and is used for authenticating with the APRS-IS network. If you don't have one, you can easily generate it at [https://pass.hamradio.my](https://pass.hamradio.my).

-----

## 💻 Contribution

Contributions from the community are warmly welcomed\! If you'd like to get involved, follow these steps:

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

Have questions, suggestions, or just want to say hello? Don't hesitate to reach out\!

  * **Callsign**: 9M2PJU
  * **GitHub**: [github.com/9M2PJU](https://github.com/9M2PJU)
