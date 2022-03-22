import ui
from passwd import input_password
from face import face_recognition
from unlock import unlock_door
from ui import *


if __name__ == "__main__":

    clear_screen()

    result = face_recognition()

    if result == "success":
        unlock_door()
    elif result == "error":
        ui.show_title("FAILED TO UNLOCK!")


