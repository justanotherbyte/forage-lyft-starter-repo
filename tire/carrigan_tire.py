from . import Tire

class CarriganTire(Tire):
    def needs_service(self) -> bool:
        return any(value >= 0.9 for value in self.values)