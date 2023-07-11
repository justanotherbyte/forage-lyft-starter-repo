from . import Tire

class OctoprimeTire(Tire):
    def needs_service(self) -> bool:
        return sum(self.values) >= 3