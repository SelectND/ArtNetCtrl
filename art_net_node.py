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

import asyncio
from pyartnet import ArtNetNode
import yaml
import numpy as np


class ArtNet:
    """
    A class to manage Art-Net communication for DMX lighting control.

    This class provides methods to initialize an Art-Net node, configure
    universes and channels, send DMX control values, and perform testing
    of DMX devices. It reads the configuration values from `config.yaml`.

    Attributes:
        node (ArtNetNode): The main Art-Net node for communication.
        universe: The universe added to the Art-Net node.
        channel: An individual channel within the universe.
        dmx_values (numpy.ndarray): An array to hold DMX-512 lighting control values.
        config (dict): Configuration data loaded from `config.yaml`.

    Methods:
        __init__(): Initializes the class, reading configuration values.
        create_node(): Creates and configures the Art-Net node, universes, and channels.
        send_dmx(): Sends DMX values to the Art-Net device.
        test_dmx(): Performs a functional test of the DMX configuration using random values.
    """

    def __init__(self):
        """ Initialize the node configuration """
        self.node = None
        self.universe = None
        self.channel = None
        self.dmx_values = np.zeros(512)
        with open("config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    async def create_node(self):
        """ Create the artnet node """
        self.node = ArtNetNode(self.config["ip"], self.config["ip_port"])
        self.universe = self.node.add_universe(self.config["universe"])
        self.channel = self.universe.add_channel(self.config["channel_start"], self.config["channel_width"])
        await self.channel

    async def send_dmx(self):
        """Send dmx values to the artnet device """
        self.channel.add_fade(self.dmx_values, 0)
        await self.channel

    async def test_dmx(self):
        """ Test DMX functionality with random values """
        for i in range(10):
            self.dmx_values = np.random.randint(0, 255, self.config["channel_width"])
            await self.send_dmx()
            await asyncio.sleep(0.1)
        self.dmx_values = np.zeros(self.config["channel_width"])
        await self.send_dmx()
