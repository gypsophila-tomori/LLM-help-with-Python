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

robot1 = Robot("ATRI", 90)
robot2 = Robot("CV-Bot-2", 8)

robot1.perform_task("patrol")
robot2.perform_task("inspect")

print(f"ATRI's battery is {robot1.battery}")

robot1.recharge()

print(f"ATRI's battery is {robot1.battery}")