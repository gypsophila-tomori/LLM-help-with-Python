while(1):
    battery_level = input("please input battery level: ")
    battery_level = int(battery_level)
    if battery_level >= 80:
        print("battery status: High")
    elif battery_level >= 20:
        print("battery status: Medium")
    else:
        print("battery status: Low Please recharge")