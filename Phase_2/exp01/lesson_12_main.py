from drone_module import SurveillanceDrone

drone = SurveillanceDrone("SkyEye")

drone.perform_task("surveil")
drone.fly_to(300)
drone.fly_to(600)