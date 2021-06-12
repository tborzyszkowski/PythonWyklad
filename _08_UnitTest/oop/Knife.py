from .Tool import *


class Knife(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        return False

    def can_cut(self):
        return True

    def can_sweep(self):
        return False
