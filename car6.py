"""
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
>>> car.sound_horn()
"Car not started yet"
>>> car.start_engine()
>>> car.sound_horn()
"Beep Beep"
"""


class Car:
    # TODO: write your code here
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = acceleration
        self.tyre_friction = tyre_friction
        self.engine = 0
        
    def accelerate(self):
        if self.engine == 0:
            pass
        else:
            self.current_speed = acceleration
    def start_engine(self):
        self.engine = 1
    def apply_brakes(self):
        self.current_speed -= tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed
    def sound_horn(self):
        if self.engine == 0:
            print('Car not started yet')
        else:
            print('Beep Beep')


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    car.sound_horn()
    car.start_engine()
    car.sound_horn()
