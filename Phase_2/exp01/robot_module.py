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