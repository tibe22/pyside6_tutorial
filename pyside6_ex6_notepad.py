from PySide6.QtWidgets import QApplication, QMainWindow
from ui_pyside6_ex6_designer_notepad import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.new_window.triggered.connect(self.add_window)
        self.windows=[]

    def add_window(self):
        add_widow = MainWindow()
        self.windows.append(add_widow)
        add_widow.show()


app = QApplication()
window = MainWindow()
window.show()
app.exec_()
