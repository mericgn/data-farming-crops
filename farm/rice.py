"""Module defining the Rice crop."""

from farm.crop import Crop


class Rice(Crop):
    """A rice crop."""

    def water(self):
        """Add 5 grains."""
        self.grains += 5

    def transplant(self):
        """Add 10 grains."""
        self.grains += 10
