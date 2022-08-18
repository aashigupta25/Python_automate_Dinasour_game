# from ast import If, main
# from email.mime import image
import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

# def draw():

def isCollide(data):
    for i in range(300,315):
        for j in range(600, 650): 
            if data[i, j] < 100:
                return True
    return False
    

if __name__ == "__main__":
    print("Hey.... Dino game start very soon")
    time.sleep(1)
    hit('up')
    
    while True:   
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        # print(asarray(image))
        

    # image.show()