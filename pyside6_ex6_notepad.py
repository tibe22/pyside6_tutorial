from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog
from ui_pyside6_ex6_designer_notepad import Ui_MainWindow
from ui_pyside6_ex6_designer_notepad_find import Ui_Dialog

class findWindow(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        '''https://www.pythonguis.com/tutorials/pyside6-creating-dialogs-qt-designer/'''
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_W.triggered.connect(self.add_window)
        self.action_O.triggered.connect(self.openFunction)
        self.action_S.triggered.connect(self.saveFunction)
        self.action_A.triggered.connect(self.saveasFunction)
        self.action_X.triggered.connect(self.close)

        self.action_U_2.triggered.connect(self.undoFunction)
        self.action_T.triggered.connect(self.cutFunction)
        self.action_C.triggered.connect(self.copyFunction)
        self.action_P_2.triggered.connect(self.pasteFunction)
        self.action_F.triggered.connect(self.findFunction)

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
        if ret == 0:
            self.saveFunction()
        else:
            return ret

    def ischanged(self):
        if not self.opend:
            if self.plainTextEdit.toPlainText().strip():
                return True
            return False
        current_data = self.plainTextEdit.toPlainText()

        with open(self.open_file_path, encoding='utf-8') as f:
            file_data = f.read()
        if current_data == file_data:
            return False
        else:
            return True
    def closeEvent(self, event):
        if self.ischanged():
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

    def openFunction(self):
        '''open file'''
        if self.ischanged():
            ret = self.save_changed_data()
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.openfile(filename[0])
            # with open(filename[0].pop(),encoding='UTF-8') as f:
            # with open(filename[0].pop(),encoding='UTF-8') as f:



    def saveFunction(self):
        if self.opend:
            self.savefile(self.open_file_path)
        else:
            self.saveasFunction()

    def saveasFunction(self):
        filename = QFileDialog.getSaveFileName(self)
        if filename[0]:
            self.savefile(filename[0])

    def undoFunction(self):
        self.plainTextEdit.undo()

    def copyFunction(self):
        self.plainTextEdit.copy()

    def cutFunction(self):
        self.plainTextEdit.cut()

    def pasteFunction(self):
        self.plainTextEdit.paste()

    def findFunction(self):
        finddlg = findWindow(self)
        finddlg.exec()



app = QApplication()
window = MainWindow()
window.show()
app.exec()
