import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication()
window = QMainWindow()
window.setWindowTitle("My App")

'''who calls'''
button = QPushButton(text="Press Me!!", parent=window)

window.show()
app.exec_()