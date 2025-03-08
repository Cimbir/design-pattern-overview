# the bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from its implementation so that the two can vary independently"
# The bridge uses encapsulation, aggregation, and can use inheritance to separate responsibilities into different classes.
# When a class varies often, the features of object-oriented programming become very useful because changes to a program's code can be made easily with minimal prior knowledge about the program.
# The bridge pattern is useful when both the class and what it does vary often. The class itself can be thought of as the implementation and what the class can do as the abstraction.

from typing import Protocol

class Device(Protocol):
    def toggle_power(self):
        pass
    
    def volume_up(self, amount: int):
        pass
    
    def volume_down(self, amount: int):
        pass
    
    def channel_up(self, amount: int):
        pass
    
    def channel_down(self, amount: int):
        pass
    
    
class TV(Device):
    def __init__(self):
        self.power = False
        self.volume = 0
        self.channel = 0
        
    def toggle_power(self):
        self.power = not self.power
        print(f"TV is {'on' if self.power else 'off'}")
        
    def volume_up(self, amount: int):
        self.volume += amount
        print(f"TV Volume: {self.volume}")
        
    def volume_down(self, amount: int):
        self.volume -= amount
        print(f"TV Volume: {self.volume}")
        
    def channel_up(self, amount: int):
        self.channel += amount
        print(f"TV Channel: {self.channel}")
        
    def channel_down(self, amount: int):
        self.channel -= amount
        print(f"TV Channel: {self.channel}")
        
        
class Radio(Device):
    def __init__(self):
        self.power = False
        self.volume = 0
        self.channel = 0
        
    def toggle_power(self):
        self.power = not self.power
        print(f"Radio is {'on' if self.power else 'off'}")
        
    def volume_up(self, amount: int):
        self.volume += amount
        print(f"Radio Volume: {self.volume}")
        
    def volume_down(self, amount: int):
        self.volume -= amount
        print(f"Radio Volume: {self.volume}")
        
    def channel_up(self, amount: int):
        self.channel += amount
        print(f"Radio Channel: {self.channel}")
        
    def channel_down(self, amount: int):
        self.channel -= amount
        print(f"Radio Channel: {self.channel}")
    

class Controller(Protocol):
    def toggle_power(self):
        pass
        
    def volume_up(self, amount: int):
        pass
            
    def volume_down(self, amount: int):
        pass
        
    def channel_up(self, amount: int):
        pass
        
    def channel_down(self, amount: int):
        pass
    
class DistantController(Controller):
    def __init__(self, device: Device):
        self.device = device
        
    def toggle_power(self):
        self.device.toggle_power()
        
    def volume_up(self, amount: int):
        self.device.volume_up(amount)
        
    def volume_down(self, amount: int):
        self.device.volume_down(amount)
        
    def channel_up(self, amount: int):
        self.device.channel_up(amount)
        
    def channel_down(self, amount: int):
        self.device.channel_down(amount)
        
class OnDeviceController(Controller):
    def __init__(self, device: Device):
        self.device = device
        
    def toggle_power(self):
        self.device.toggle_power()
        
    def volume_up(self, amount: int):
        self.device.volume_up(amount * 10)
        
    def volume_down(self, amount: int):
        self.device.volume_down(amount * 10)
        
    def channel_up(self, amount: int):
        self.device.channel_up(amount)
        
    def channel_down(self, amount: int):
        self.device.channel_down(amount)
        

tv = TV()
radio = Radio()
tv_controller = DistantController(tv)
radio_controller = OnDeviceController(radio)

tv_controller.toggle_power()
tv_controller.volume_up(10)
tv_controller.channel_up(5)

radio_controller.toggle_power()
radio_controller.volume_up(10)
