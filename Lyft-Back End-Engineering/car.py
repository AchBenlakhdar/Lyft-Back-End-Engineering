from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine=engine
        self.battery=battery

    def needs_service(self):
        self.engine.needs_service() or self.battery.needs_service()
        
