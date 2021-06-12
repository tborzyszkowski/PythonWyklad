from .Tool import *


class Broom(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        return False

    def can_cut(self):
        return False

    def can_sweep(self):
        return True
