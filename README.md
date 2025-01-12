# ArtNetCtrl

## Overview

This Project enables you to control an ArtNet node using a physical controller.

To get started, view the installation guide

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional): Create and activate a virtual environment to isolate the package dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

## Usage

To execute the project, follow these steps:

1. Ensure all required dependencies are installed.
2. Flash the Arduino/Arduino.ino file to your Arduino and adjust the pin assignment for your needs
3. Adjust the config.yaml file as needed
4Run the project script by using:
   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please follow the standard Git workflow:

- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Push changes to your fork.
- Open a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Acknowledgements
This project incorporates the Art-Net™ protocol. "Art-Net™ Designed by and Copyright Artistic Licence Engineering Ltd". For more information about Art-Net, visit the [Artistic Licence Website]("https://artisticlicence.com/")
## Disclaimer
This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Artistic Licence Engineering Ltd, or any of its subsidiaries or its affiliates. The name Art-Net™ as well as related names, marks, emblems, and images are registered trademarks of their respective owners

---