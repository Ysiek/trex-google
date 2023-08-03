import pyautogui
import time


class Trex:
    def __init__(self):
        self.trex = pyautogui.locateOnScreen("Capture.PNG")
        time.sleep(2)
        print(self.trex)
        print(self.trex.left, self.trex.top)
        self.offset = 90
        self.jump()

    def jump(self):
        pyautogui.press("space")

    def cactus_in_front_of(self):
        while True:
            if pyautogui.pixelMatchesColor(int(self.trex.left + 25) + int(self.offset), int(self.trex.top), (130, 130, 130), tolerance=70) or pyautogui.pixelMatchesColor(int(self.trex.left + 25) + int(self.offset), int(self.trex.top + 32), (130, 130, 130), tolerance=70):
                print("jump ")
                self.jump()
                self.offset += 0.7


trex_manager = Trex()
trex_manager.cactus_in_front_of()
