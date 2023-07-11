from datetime import datetime

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
        wear_values: tuple[float, float, float, float]
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(wear_values)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
        wear_values: tuple[float, float, float, float]
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(wear_values)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(
        current_date: datetime,
        last_service_date: datetime,
        warning_light_on: bool,
        wear_values: tuple[float, float, float, float]
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(wear_values)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
        wear_values: tuple[float, float, float, float]
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(wear_values)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_thovex(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
        wear_values: tuple[float, float, float, float]
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(wear_values)
        return Car(engine, battery, tires)