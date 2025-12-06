robot_status = {"name": "CV-Bot-1", "battery": 85, "position_x": 3.14, "is_online": True}

robot_status["position_x"] = 5.0
robot_status["task"] = "patrolling"

print(robot_status["name"], robot_status["task"])