"""
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
>>> car.start_engine()
>>> car.is_engine_started
True
>>> car.stop_engine()
>>> car.is_engine_started
False
"""


class Car:
    # TODO: write your code here
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
    def start_engine(self):
        if self.is_engine_started == 0:
            self.is_engine_started = True
            


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    is_engine_started_1 = car.is_engine_started
    car.start_engine()
    is_engine_started_2 = car.is_engine_started

    print("-".join([str(is_engine_started_1), str(is_engine_started_2)]))
