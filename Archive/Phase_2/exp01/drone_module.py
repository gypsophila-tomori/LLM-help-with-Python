from robot_module import Robot

class SurveillanceDrone(Robot):
    def __init__(self, name, battery=100, max_altitude = 500):
        super().__init__(name, battery)
        self.max_altitude = max_altitude
    
    def fly_to(self, altitude):
        if altitude <= self.max_altitude:
            print(f"{self.name} is flying to {altitude} meters")
        else:
            print(f"Altitude is too high! max altidude is {self.max_altitude}")