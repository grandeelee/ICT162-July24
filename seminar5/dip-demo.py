class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan:
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class LightSwitch:
    def __init__(self, thing):
        self._bulb = thing

    def operate_switch(self, cmd):
        if cmd == "on":
            self._bulb.turn_on()
        elif cmd == "off":
            self._bulb.turn_off()

if __name__ == "__main__":
    bulb = LightBulb()
    fan = Fan()
    switch = LightSwitch(bulb)
    switch.operate_switch("on")
    switch.operate_switch("off")


