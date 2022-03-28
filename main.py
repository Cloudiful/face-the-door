import gui
import face
import threading

if __name__ == "__main__":

    # tGUI = threading.Thread(target=gui.init, args=())
    # tFace = threading.Thread(target=face.capture, args=())
    #
    # tGUI.start()
    # tFace.start()

    gui.init()

    a = input('a')
