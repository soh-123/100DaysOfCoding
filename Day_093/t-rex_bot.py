import pyautogui

class Dinosaur:
 
    def __init__(self):
        self.jumps = 0
 
    def jump(self):
        pyautogui.keyDown('up')
        pyautogui.sleep(.2)
        pyautogui.keyUp('up')
        self.jumps += 1
 
    def sees_obstacle_ahead(self) -> bool:
        x = 715 + int(self.jumps * .3)
        pixel = pyautogui.pixel(x, 389)
        for color in pixel:
            if color < 100:
                return True
        return False
 
 
def main():
 
    dino = Dinosaur()
 
    while True:
        if dino.sees_obstacle_ahead():
            dino.jump()
 
 
if __name__ == '__main__':
    main()