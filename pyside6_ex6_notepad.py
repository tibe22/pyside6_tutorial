from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_pyside6_ex6_designer_notepad import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_W.triggered.connect(self.add_window)
        self.action_O.triggered.connect(self.open_file)
        self.action_S.triggered.connect(self.save_file)
        self.action_A.triggered.connect(self.saveas_file)
        self.action_X.triggered.connect(self.close)
        self.windows=[]
        self.opend = False
        self.open_file_path = '제목없음'

    def save_changed_data(self):
        msg_box = QMessageBox()
        msg_box.setText(f'변경내용을 {self.open_file_path}에 저장하시겠습니까?')
        msg_box.addButton("저장",QMessageBox.YesRole) #0
        msg_box.addButton("저장 안함",QMessageBox.NoRole) #1
        msg_box.addButton("취소",QMessageBox.RejectRole) #2
        ret = msg_box.exec()
        if ret == 2:
            return ret

    def closeEvent(self, event):
        ret = self.save_changed_data()
        if ret == 2:
            event.ignore()

        print(f'close event')

    def savefile(self,fname):
        text = self.plainTextEdit.toPlainText()
        with open(fname, 'w', encoding='UTF-8') as f:
            f.write(text)
        print(f'save file : {fname}')

    def openfile(self, fname):
        with open(fname, encoding='UTF-8') as f:
            text = f.read()
        self.plainTextEdit.setPlainText(text)
        self.opend = True
        self.open_file_path = fname
        print(f'open file : {fname}')


    def add_window(self):
        '''new window'''
        add_window = MainWindow()
        self.windows.append(add_window)
        add_window.show()

    def open_file(self):
        '''open file'''
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.openfile(filename[0])
            # with open(filename[0].pop(),encoding='UTF-8') as f:
            # with open(filename[0].pop(),encoding='UTF-8') as f:



    def save_file(self):
        if self.opend:
            self.savefile(self.open_file_path)
        else:
            self.saveas_file()

    def saveas_file(self):
        filename = QFileDialog.getSaveFileName(self)
        if filename[0]:
            self.savefile(filename[0])



app = QApplication()
window = MainWindow()
window.show()
app.exec()
