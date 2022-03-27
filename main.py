import gui
import face
from unlock import unlock_door

if __name__ == "__main__":

    result = face.recognition()

    if result == "success":
        unlock_door()
    elif result == "error":
        print("FAILED TO UNLOCK!")

    a = input("按回车键退出程序...")
