import keyboard
import time

def detect():
    while True:
        try:
            if keyboard.is_pressed('1'):
                return 1
            elif keyboard.is_pressed('2'):
                return 2
            elif keyboard.is_pressed('3'):
                return 3
            elif keyboard.is_pressed('4'):
                return 4
        except:
            pass

def main():
    while True:
        if detect() == 1:
            keyboard.press_and_release("win+ctrl+left")
        elif detect() == 2:
            keyboard.press_and_release("win+ctrl+right")
        elif detect() == 3:
            keyboard.press_and_release("win+ctrl+d")
        elif detect() == 4:
            keyboard.press_and_release("alt+tab")
        time.sleep(2)


if __name__ == '__main__':
    main()
    print("hello ")