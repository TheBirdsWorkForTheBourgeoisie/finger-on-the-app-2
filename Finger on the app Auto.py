import pyautogui
from PIL import Image
from pytesseract import *
import pyscreenshot as ImageGrab
import mouse
import time


time.sleep(2)
mouse.move(70, 300, absolute=True, duration=.1)
mouse.press(button='left')


def my_function():
  print("Play Again?")

  im = ImageGrab.grab(bbox=(165,355,280,405))
  im.save("box.png")
  img = Image.open('box.png')

  pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

  line = pytesseract.image_to_string(img,lang='eng')

  line = "".join(line.splitlines())
  print(line)

  if line == 'PLAY AGAIN':
        print("Game Over")
        mouse.release(button='left')
        mouse.move(230, 375, absolute=True, duration=.4)
        mouse.click(button='left')
        mouse.move(70, 300, absolute=True, duration=.4)
        time.sleep(2)
        mouse.press(button='left')
        

try: 
    while True:
        my_function()
        mouse.move(70, 300, absolute=True, duration=.4)

        mouse.move(380, 300, absolute=True, duration=.4)

   

        mouse.move(70, 450, absolute=True, duration=.4)

        mouse.move(380, 450, absolute=True, duration=.4)



        mouse.move(70, 600, absolute=True, duration=.4)

        mouse.move(380, 600, absolute=True, duration=.4)

        

        mouse.move(70, 750, absolute=True, duration=.4)

        mouse.move(380, 750, absolute=True, duration=.4)
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
