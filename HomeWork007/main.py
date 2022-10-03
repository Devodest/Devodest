import sys
import threading

from PyQt5.QtWidgets import QApplication

import controller
import interface

app = QApplication(sys.argv)
window = interface.Window()
window.show()


def logic():
    global window
    controller.start()


logicThread = threading.Thread(target=logic)
logicThread.start()

sys.exit(app.exec_())
