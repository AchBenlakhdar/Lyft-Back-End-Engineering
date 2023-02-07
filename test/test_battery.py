from battery import NubbinBattery
from battery import SpindlerBattery
import unittest, datetime


class TestNubbinBattery(unittest.TestCase):
    
    
    
    def test_needs_service_true(self):    
        
        current_date = datetime.datetime(2023,1,1)
        last_service_date = datetime.datetime(2010,1,1)
        battery = NubbinBattery(current_date, last_service_date)
        
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        
        current_date = datetime.datetime(2023,1,1)
        last_service_date = datetime.datetime(2022,1,1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2018,1,1)
        
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023, 1, 1)
        last_service_date = datetime.datetime(2022,1,1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())