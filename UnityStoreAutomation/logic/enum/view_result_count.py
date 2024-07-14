from enum import Enum


class AssetsPerPageOptions(Enum):
    """
    Enum to represent the options for the number of assets displayed per page in the Unity Asset Store.

    Attributes:
        TWENTY_FOUR (int): Option to display 24 assets per page.
        FORTY_EIGHT (int): Option to display 48 assets per page.
        SEVENTY_TWO (int): Option to display 72 assets per page.
        NINETY_SIX (int): Option to display 96 assets per page.
    """
    TWENTY_FOUR = 24
    FORTY_EIGHT = 48
    SEVENTY_TWO = 72
    NINETY_SIX = 96
