from dict_dialog import Dict_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
import sys


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dict_Dialog()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
