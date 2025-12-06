my_number = 42
my_text = "Hello World"
my_truth = True

print(type(my_number))
print(type(my_text))
print(type(my_truth))

result1 = my_number + 10
result2 = my_text + "Python"
# result3 = my_number + my_text
# 出现TypeError，因为int不能与str相加

print("result1:", result1)
print("result2:", result2)
# print("result3:", result3)


combined1 = str(my_number) + my_text
print("way 1:", combined1)

combined2 = f"{my_number}{my_text}"
print("way 2:", combined2)

number_text = "100"
real_number = int(number_text)
print("转换后数字：",real_number)