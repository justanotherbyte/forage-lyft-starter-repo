from datetime import timedelta

from . import Battery

class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date) >= timedelta(days=365 * 2)
    
