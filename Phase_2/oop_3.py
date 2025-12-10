class Camera:
    def __init__(self, resolution, fps = 30):
        self.resolution = resolution
        self.fps = fps
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        print(f"Camera {self.resolution}p start!")

    def stop_recording(self):
        self.is_recording = False
        print(f"Camera {self.resolution}p stop!")

    def set_fps(self, new_fps):
        self.fps = new_fps
        print("fps set to ", new_fps)

    def __str__(self):
        status = "录制中" if self.is_recording else "待机"
        return f"Camera {self.resolution}p 状态：{status} FPS：{self.fps}"

    def  __call__(self, duration):
        print(f"Camera {self.resolution}p 开始快速录制")
        self.start_recording()
        print(f"录制持续 {duration}s")
        self.stop_recording()


cam_test = Camera(1920)
print(cam_test)
cam_test(5)