test = 0

while (test == 0):
    try:
        check = 0
        while(check == 0):
            birth_str = input("请输入你的出生年份: ")
            this_str = input("请输入当前年份: ")
            birth = int(birth_str)
            this = int(this_str)
            if birth > this:
                print("year error!")
            elif birth < 0 | this <0: # 或是这样写的吗
                print("ha? year error!")
            elif this - birth >150:
                print("wow, a spuer old man! I refuse to calculate!")
            else:
                age = this - birth
                check = 1
        test = 1
    except ValueError:
        print("are you serious ?please enter number!")  

print(f"your age is: {age}")