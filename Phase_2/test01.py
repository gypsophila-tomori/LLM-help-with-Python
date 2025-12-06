'''
    函数：
    各部分的意义
    def <function name>(参数1, 参数2, ......):
        """函数用途说明，写好注释方便检查"""
        <具体操作>
        结果 = 参数1 + 参数2    #例子
        return 结果
    
    如何调用？
    <函数名>(输入参数1, 输入参数2)
'''
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
    """主函数"""
    print("======年龄计算器======")
    check = 0
    while (check == 0):
        birth_year = get_year_input(input("请输入出生年份："))
        current_year = get_year_input(input("请输入当前年份："))
        if validate_years(birth_year, current_year):
            age = current_year - birth_year
            print(f"你现在的年龄是：{age}")
            check = 1
        else:
            check = 0
    print("======程序结束！======")
if __name__ == "__main__":
    main()

# 有大问题，debug请看test02
