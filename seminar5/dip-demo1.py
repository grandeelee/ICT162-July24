from abc import ABC, abstractmethod

# Abstraction
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Low-level module
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

# Low-level module
class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

# High-level module
class LightSwitch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate_switch(self, cmd):
        if cmd == "on":
            self.device.turn_on()
        elif cmd == "off":
            self.device.turn_off()



if __name__ == "__main__":
    light_bulb = LightBulb()
    fan = Fan()

    light_switch = LightSwitch(light_bulb)
    light_switch.operate_switch("on")
    light_switch.operate_switch("off")

    fan_switch = LightSwitch(fan)
    fan_switch.operate_switch("on")
    fan_switch.operate_switch("off")
