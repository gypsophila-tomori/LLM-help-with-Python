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

class PanoramicCamera(Camera):
    def __init__(self, resolution, fps = 30, field_of_view = 360):
        super().__init__(resolution, fps)
        self.field_of_view = field_of_view

    def get_view_info(self):
        print(f"this is a {self.resolution}p PanoramicCamera!,the field of view is {self.field_of_view}")


def main():
    p_camera = PanoramicCamera(2160)
    p_camera.start_recording()
    p_camera.get_view_info()
    print(f"father method is ok, ths fps is {p_camera.fps}")

if __name__ == "__main__":
    main()