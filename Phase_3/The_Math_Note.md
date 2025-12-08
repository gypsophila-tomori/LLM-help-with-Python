# 第十三课：NumPy 基础 - 图像就是矩阵

- NumPy是Python科学计算的基石。它提供了强大的多维数组对象 ndarray 以及一系列操作这些数组的函数
- 一张灰度图像就是一个二维数组（高度 x 宽度），彩色图像是三维数组（高度 x 宽度 x 颜色通道）

## 核心概念
- 数组创建：``np.array([1,2,3])``, ``np.zeros((3,4))``, ``np.ones((2,2,2))``
- 数组形状：``.shape``属性
- 基础操作：元素级运算(``+``,``-``,``*``,``/``),矩阵乘法(``@`` 或者 ``np.dot``)
- 索引与切片：和Python列表类似，但可以多维度操作

## 基本操作
```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5]) # 从列表创建
zeros = np.zeros((3, 4)) # 3行4列的全0数组
ones = np.ones((2, 2, 3)) # 2x2x3的全1数组（三维！）
random_arr = np.random.rand(5, 5) # 5x5的随机数组（值在0~1之间）

# 形状和维度
print(arr.shape) # (5,) 一维，5个元素
print(zeros.shape) # (3, 4) 二维，3行4列

# 索引和切片 (和列表非常相似，但可以多维)
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_2d[0, 1]) # 第0行，第1列 -> 2
print(arr_2d[:, 1]) # 所有行，第1列 -> [2, 5, 8]

# 向量化运算
arr = np.array([1,2,3])
print(arr + 10) # [11, 12, 13] 每个元素都加10
print(arr * 2) # [2, 4, 6] 每个元素都乘2
```






# 第十四课：PyTorch 张量 (Tensor) - 深度学习的血液

NumPy很好，但PyTorch的 ``Tensor`` 才是深度学习领域的标准数据结构。它继承了NumPy数组的几乎所有接口，并额外添加了两个革命性特性:
- **GPU加速**：可以轻松将计算转移到显卡上，速度提升数十至数百倍
- **自动求导 (Autograd)**：这是神经网络能够“学习”的核心。系统会自动计算梯度，用于反向传播

## Tensor 与 NumPy Array 的相似性与转换
```python
import torch

# 创建Tensor
x = torch.tensor([1, 2, 3, 4])          # 从列表创建
y = torch.zeros(2, 3)                   # 2x3的全0张量
z = torch.rand(3, 3)                    # 3x3的随机张量（均匀分布，0~1）
w = torch.randn(3, 3)                   # 3x3的随机张量（标准正态分布）

# 形状和类型
print(x.shape)      # torch.Size([4])
print(y.dtype)      # torch.float32 (默认类型)

# 与NumPy互转（非常常用！）
import numpy as np
np_array = np.ones((2, 2))
torch_tensor = torch.from_numpy(np_array)  # NumPy -> Tensor
back_to_numpy = torch_tensor.numpy()       # Tensor -> NumPy

# 设备转移（CPU/GPU）
if torch.cuda.is_available():
    device = torch.device("cuda")
    tensor_gpu = torch_tensor.to(device)   # 转移到GPU
```