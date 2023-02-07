from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine
import unittest





class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        
        current_mileage = 66000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        

        current_mileage = 60000
        last_service_mileage = 1
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestCapuletEngine(unittest.TestCase):
    
    def test_needs_service_true(self):
        current_mileage = 33000
        last_service_mileage = 200
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 33000
        last_service_mileage = 200
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())



class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())