from datetime import datetime

from serviceable import Serviceable

class Battery(Serviceable):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

        super().__init__()