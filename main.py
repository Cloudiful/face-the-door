import face
import passwd
import face
from unlock import unlock_door
import ui

if __name__ == "__main__":

    ui.clear_screen()

    if face.capture() == 'pwd':
        password = passwd.input_passwd()
        print(password)
        if password == "123456":
            unlock_door()
        else:
            pass

    # result = face.recognition()
    #
    # if result == "success":
    #     unlock_door()
    # elif result == "error":
    #     ui.show_title("FAILED TO UNLOCK!")
    #     ui.draw_screen()

    a = input("按回车键退出程序...")
