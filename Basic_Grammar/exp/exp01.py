# 第一个交互程序

birth_year_str = input("please input your bitrh year: ")
current_year_str = input("please input this year: ")

birth_year = int(birth_year_str)
current_year = int(current_year_str)

age = current_year - birth_year

print(f"your age is:", age)
