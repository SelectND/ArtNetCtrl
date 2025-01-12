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

    This script connects a serial input device with an Art-Net node to control
    DMX lighting channels. It reads potentiometer input values via the serial
    device and maps them to DMX channels using the Highest Takes Precedence (HTP)
    rule, sending the data to the Art-Net node for lighting control.
"""

import asyncio
import art_net_node
import serial_input
import time
import sys
import signal


def sigint_handler(signal, frame):
    """
    Handles the SIGINT (Ctrl+C) signal to safely terminate the program.

    Args:
        signal: The signal number.
        frame: The current stack frame (unused).
    """
    print('Interrupted')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)  # Attach SIGINT signal to the handler to enable safe program exit

if __name__ == '__main__':
    """
    Main entry point of the script. Initializes the Art-Net node and the serial
    input device and processes DMX channel values using potentiometer inputs.
    Applies the Highest Takes Precedence (HTP) rule to merge DMX values across
    active scenes and sends the output to the Art-Net node.
    """
    # Initialize Art-Net node for controlling DMX devices
    node = art_net_node.ArtNet()
    asyncio.run(node.create_node())  # Asynchronously set up the node

    # Initialize the serial input device for reading potentiometer data
    serial_device = serial_input.SerialInput()
    scene_count = max(node.config["scenes"]) + 1  # Calculate total number of scenes

    while 1:  # Start the main loop
        pot_values = serial_device.read_serial()  # Read potentiometer values
        htp_values = {}  # Dictionary for storing merged DMX values
        scene_config = node.config["scenes"]  # Configuration of scenes from Art-Net node

        # Process each scene to generate HTP values
        for scene in scene_config:
            for dmx_values in scene_config[scene]:
                channel, value = next(iter(dmx_values.items()))  # Extract channel and value
                multiplied_value = value * pot_values[scene - 1]  # Scale value using potentiometer
                if channel not in htp_values or htp_values[channel] < multiplied_value:
                    htp_values[channel] = multiplied_value  # Apply HTP rule

        # Update DMX values in the Art-Net node
        for channel in htp_values:
            node.dmx_values[channel] = int(htp_values[channel])

        # Send the updated DMX values to the lighting controller
        asyncio.run(node.send_dmx())
        time.sleep(0.01)  # Small delay to control loop timing
