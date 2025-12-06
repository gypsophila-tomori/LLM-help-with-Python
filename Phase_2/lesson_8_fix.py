class Robot:
    def __init__(self, name, battery = 100):
        self.name = name
        self.battery = battery
        print(f"{self.name} is powered on! Battery: {self.battery}%")

robot1 = Robot("ATRI")
robot2 = Robot("CV-Bot-2")
