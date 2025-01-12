"""
    Copyright (C) 2025 Valentin König

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import serial
import yaml
import time


class SerialInput:
    """
    A class to manage serial communication with a connected device.

    This class reads data from a serial port, using configurations provided
    in a YAML configuration file. It processes the received data and converts
    it into a list of floating-point values for further use.
    """

    def __init__(self):
        """ Initialize the serial connection """
        with open("config.yaml", "r") as file:
            self.config = yaml.safe_load(file)
        self.port = self.config["port"]
        self.baud = self.config["baud"]

    def read_serial(self):
        """ Read the data from the serial device and return a list of floats """
        with serial.Serial(self.port, self.baud) as ser:
            pot_values = ser.readline()
        time.sleep(0.01)  # Wait for reception to finish
        pot_values = pot_values.decode("utf-8")
        pot_values = pot_values.split("|")
        pot_values[-1] = pot_values[-1].replace("\r\n", "")
        pot_values = (float(pot_value) for pot_value in pot_values)
        return list(pot_values)
