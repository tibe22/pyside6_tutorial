from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_pyside6_ex6_designer_notepad import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_W.triggered.connect(self.add_window)
        self.action_O.triggered.connect(self.open_file)
        self.action_S.triggered.connect(self.save_file)
        self.windows=[]

    def add_window(self):
        '''new window'''
        add_window = MainWindow()
        self.windows.append(add_window)
        add_window.show()

    def open_file(self):
        '''open file'''
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            # with open(filename[0].pop(),encoding='UTF-8') as f:
            # with open(filename[0].pop(),encoding='UTF-8') as f:
            with open(filename[0],encoding='UTF-8') as f:
                text = f.read()

            self.plainTextEdit.setPlainText(text)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self)
        if filename[0]:
            text = self.plainTextEdit.toPlainText()
            with open(filename[0],'w',encoding='UTF-8') as f:
                f.write(text)



app = QApplication()
window = MainWindow()
window.show()
app.exec()
