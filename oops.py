"""
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
>>> car.acceleration
10
>>> car.tyre_friction
3
>>> car.max_speed
250
>>> car.color
Red
"""


class Car:
    # TODO: write your code here
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction



if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    print("-".join([car.color, str(car.max_speed), str(car.acceleration),
                    str(car.tyre_friction)]))
                    
       
