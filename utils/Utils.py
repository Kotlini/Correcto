from pynput import keyboard


def replace_text(textReplaced):
    controller = keyboard.Controller()
    controller.press(keyboard.Key.backspace)
    controller.release(keyboard.Key.backspace)
    for element in textReplaced:
        controller.press(element)
        controller.release(element)
