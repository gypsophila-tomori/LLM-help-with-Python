# 任务：重构Basic_Grammar里的年龄计算器exp02

def validate_years(birth_year, currnet_year):
    """验证年份是否有效"""
    if birth_year < 0 or currnet_year <0:
        print("年份不能为负数！")
        return False
    elif birth_year > currnet_year:
        print("出生年份不能大于当前年份！")
        return False
    elif currnet_year - birth_year >150:
        print("你好老啊，真的能活到150岁以上吗？不要骗我")
        return False
    else:
        return True

def get_year_input(prompt):
    """获取用户输入"""
    check = 0
    while (check == 0):
        try:
            return int(prompt)
        except ValueError:
            return False

def main():
    print("======年龄计算器======")
    check = 0
    while (check == 0):
        user_input1 = input("请输入出生年份：")  # 先保存输入
        user_input2 = input("请输入当前年份：")
        
        print(f"调试：用户输入1='{user_input1}'，输入2='{user_input2}'")
        
        birth_year = get_year_input(user_input1)
        current_year = get_year_input(user_input2)
        
        print(f"调试：转换后 birth_year={birth_year}(类型{type(birth_year)}), "
              f"current_year={current_year}(类型{type(current_year)})")
        
        if validate_years(birth_year, current_year):
            age = current_year - birth_year
            print(f"你现在的年龄是：{age}")
            check = 1
        else:
            print("验证失败，重新输入")
            check = 0


if __name__ == "__main__":
    main()

# 有大问题，debug请看test02