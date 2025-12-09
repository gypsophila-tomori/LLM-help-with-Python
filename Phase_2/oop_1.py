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



''' def main():
    cam1 = Camera(1080)
    cam2 = Camera(720)

    print(cam1.resolution)
    print(cam2.fps)
    '''
def main():
    cam1 = Camera(1080)
    cam1.start_recording()
    cam1.set_fps(60)
    print(cam1.fps)

if __name__ == "__main__":
    main()