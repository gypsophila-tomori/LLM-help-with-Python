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