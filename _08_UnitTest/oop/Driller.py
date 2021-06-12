from .Tool import *


class Driller(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        return True

    def can_cut(self):
        return False

    def can_sweep(self):
        return False
