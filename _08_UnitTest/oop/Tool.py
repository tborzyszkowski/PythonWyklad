class Tool:
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        pass

    def can_cut(self):
        pass

    def can_sweep(self):
        pass

    def capability(self):
        result = {"drill": self.can_drill(), "cut": self.can_cut(), "sweep": self.can_sweep()}
        return result
