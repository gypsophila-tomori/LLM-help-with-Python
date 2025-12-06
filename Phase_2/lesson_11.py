class Robot:
    def __init__(self, name, battery = 100):
        self.name = name
        self.battery = battery
        print(f"{self.name} is powered on! Battery: {self.battery}%")

    def perform_task(self, task_name):
        if self.battery > 10:
            print(f"{self.name} is performing task: {task_name}")
            self.battery -= 10
        else:
            print(f"{self.name} perform task: {task_name} failed, please recharge")
    
    def recharge(self):
        self.battery = 100
        print(f"{self.name} is fully charged!")

class SurveillanceDrone(Robot):
    def __init__(self, name, battery=100, max_altitude = 500):
        super().__init__(name, battery)
        self.max_altitude = max_altitude
    
    def fly_to(self, altitude):
        if altitude <= self.max_altitude:
            print(f"{self.name} is flying to {altitude} meters")
        else:
            print(f"Altitude is too high! max altidude is {self.max_altitude}")

ground_bot = Robot("ATRI")
drone = SurveillanceDrone("SkyEye", 80, 500)

ground_bot.perform_task("move")
drone.perform_task("surveil")

drone.fly_to(300)
drone.fly_to(600)