"""Module defining the Corn crop."""

from farm.crop import Crop


class Corn(Crop):
    """A corn crop."""

    def water(self):
        """Add 10 grains."""
        self.grains += 10
