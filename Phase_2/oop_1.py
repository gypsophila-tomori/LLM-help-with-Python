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
        new_fps = int(input("please set a new fps"))
        self.fps = new_fps



def main():
    cam1 = Camera(1080)
    cam2 = Camera(720)

    print(cam1.resolution)
    print(cam2.fps)


if __name__ == "__main__":
    main()