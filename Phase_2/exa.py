# 1. 定义图纸（类）
class Robot:
    # 2. 构造函数：制造零件时必须执行的步骤
    def __init__(self, name):
        # self 指代正在被制造的那个“零件本身”
        self.name = name  # 为这个机器人起名
        self.battery = 100  # 初始化电量为100%

# 3. 根据图纸制造具体零件（对象）
my_robot = Robot("T-800")
your_robot = Robot("Wall-E")

# 4. 访问对象的属性
print(my_robot.name)   # 输出: T-800
print(your_robot.battery) # 输出: 100
