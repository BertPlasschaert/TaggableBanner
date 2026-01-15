# buildin modules
from dataclasses import dataclass


@dataclass
class FontBB:
    name: str
    height_size_ratio: float  # Magic numbers, not perfect
    width_size_ratio: float  # Magic numbers, not perfect
