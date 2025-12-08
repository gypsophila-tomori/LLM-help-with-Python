# 第八课：类（Class）与对象（Object） - 蓝图与实物
在现实世界中，我们可以根据一张汽车设计图（蓝图） 制造出许多辆具体的汽车。
在面向对象编程中：

- 类（Class） 就是那张设计图。它定义了这类事物应有的属性（如颜色、型号）和功能（如启动、刹车）。
- 对象（Object） 就是根据设计图制造出来的具体实物。每一辆汽车都是独立的

**定义一个类**  
```python
class Robot:
    # 这是类的“蓝图”部分
    pass
```
**根据蓝图创建具体对象（实例化）**
```python
my_robot = Robot() # my_robot 现在是一个具体的Robot对象
```

# 第九课：类的初始化方法 __init__ 与实例属性

一张真正的汽车设计图，必须规定新车出厂时的**初始状态**，比如默认颜色、发动机型号。在Python类中，这个工作由 ``__init__`` 方法来完成

``__init__`` 是一个特殊的魔法方法（双下划线开头和结尾）。当你创建对象时（Robot()），Python会自动调用它，对新生对象进行初始化

## 为对象添加属性：
在 ``__init__`` 方法内部，我们使用 ``self.attribute_name = value`` 的语法来给对象绑定属性。self 代表**正在被创建的那个对象本身**
```python
class Robot:
    def __init__(self, name, battery=100): # 参数：self, 和你想初始化的属性
        # 将传入的name参数，赋值给当前对象的.name属性
        self.name = name
        self.battery = battery
        print(f"{self.name} is powered on! Battery: {self.battery}%")
```

# 第十课：实例方法（Instance Method） - 对象的行为

对象不仅要有状态（属性），还要有行为（方法）。实例方法就是定义在类内部，用于操作对象自身数据的函数。它的第一个参数永远是 self，通过 self 可以访问该对象的所有属性和其他方法

这就像给汽车设计图添加了“启动引擎”、“打开车灯”等功能说明

**定义实例的方法** 
```python
class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100

    def say_hello(self): # 这是一个实例方法
        print(f"Hello, I'm {self.name}. Battery: {self.battery}%")

    def move(self, distance):
        # 假设移动会消耗电量，每单位距离消耗1%
        cost = distance * 1
        if self.battery >= cost:
            self.battery -= cost
            print(f"{self.name} moved {distance} units. Battery left: {self.battery}%")
        else:
            print(f"{self.name} cannot move. Not enough battery!")
```

**调用实例方法**
```python
my_robot = Robot("Bot")
my_robot.say_hello() # 调用时不需要传递self参数，Python会自动传入
my_robot.move(5)
```

# 第十一课：继承（Inheritance） - 构建类家族

在机器人领域，我们有不同种类的机器人：移动机器人、机械臂、无人机...它们有共同的特性（如名字、电量），也有各自独特的功能。我们不需要为每个机器人从头重写代码。继承允许我们基于一个已有的**类（父类/基类）**来创建新**类（子类/派生类）** 

**子类自动获得父类的所有属性和方法**，并且可以：
- 添加自己特有的属性和方法
- 重写父类的方法，以改变其行为

这就像在“通用机器人设计图”的基础上，绘制更具体的“无人机设计图”

# 语法
```python
class ParentClass:
    # 父类的定于
    pass
class ChildClass(ParentClass): # 括号内指定父类
    # 子类的定义
    pass
```

# 第十二课：模块化与导入（Modularity & Import）- 管理大型项目

当项目变大时，我们不能把所有代码都写在一个文件里。我们需要将代码拆分到不同的 ``.py`` 文件中，每个文件负责一个特定的功能（模块），然后通过 ``import`` 语句将它们组合起来。这正是PyTorch、YOLO等大型项目组织代码的方式

## 核心概念
- **模块（Module）**：一个 .py 文件就是一个模块
- **导入（Import）**：在一个模块中使用另一个模块中的代码

## 基本语法
```python
# 导入整个模块
import module_name
# 使用模块中的类
obj = module_name.ClassName()

# 从模块中导入特定的类/函数
from module_name import ClassName
# 直接使用类名
obj = ClassName()

# 给导入的模块或类起别名（常用于长名字）
import very_long_module_name as vlmn
from torch import nn as neural_network
```