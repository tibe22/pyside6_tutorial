from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!!")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(300,200))

app = QApplication()
window = MainWindow()
window.show()
app.exec_()
