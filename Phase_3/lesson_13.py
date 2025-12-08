import numpy as np

image = np.random.randint(0, 256, (5, 5))

print(image[2, :])
print(image[:, 3])

print(image)

image[1:4, 1:4] = 255 # 中间 3x3设置为255

print(image)