import keyboard
import mouse

def pressright():
    if(mouse.is_pressed(button='right')):
        # release
        mouse.release(button='right')

    else:
        # press
        mouse.press(button='right')

def pressleft():
    if(mouse.is_pressed(button='left')):
        # release
        mouse.release(button='left')

    else:
        # press
        mouse.press(button='left')
keyboard.add_hotkey(']',pressright)
keyboard.add_hotkey('[',pressleft)
keyboard.wait('end')