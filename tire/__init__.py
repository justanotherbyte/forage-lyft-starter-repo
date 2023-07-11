from serviceable import Serviceable

class Tire(Serviceable):
    def __init__(self, values: tuple[float, float, float, float]):
        self.values = values