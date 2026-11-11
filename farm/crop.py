"""Module defining the generic Crop parent class."""
# pylint: disable=too-few-public-methods


class Crop:
    """Base class holding behaviour shared by all crops."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if the crop has at least 15 grains."""
        return self.grains >= 15
