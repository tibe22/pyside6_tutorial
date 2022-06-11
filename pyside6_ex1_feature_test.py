import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
button = QPushButton(icon=QIcon("home.png"),text='Click me!!',parent=window)
window.show()
app.exec()
