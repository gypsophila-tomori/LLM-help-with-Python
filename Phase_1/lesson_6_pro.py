robot_config = {"camera_topic": "/camera/rgb", "model_path": "./weights/yolov5s.pt", "confidence_threshold": 0.6, "img_size": [640, 480]}

print(robot_config["model_path"])
print(robot_config.get("use_gpu", True))    # 设置默认值

print(robot_config["img_size"][1])

robot_config["confidence_threshold"] = 0.7  # 存在的键值进行修改
robot_config["device"] = "cuda:0"   # 不存在的键值直接创建

for key, value in robot_config.items():
    print(key, value)