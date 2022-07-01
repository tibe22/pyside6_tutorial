import os
import time
from torrent import torrent
import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui
import PySide6.QtCore as QtCore

class FileTable(QtWidgets.QTableWidget):
    '''table for find result'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["FileName", "ext", "Path", "Size", "Time"])
        self.horizontalHeader().setStretchLastSection(True)
        self.setColumnWidth(0, 300)
        self.setColumnWidth(1, 120)
        self.setColumnWidth(2, 520)
        self.setColumnWidth(3, 120)
        self.setColumnWidth(4, 120)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.data = None
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.resizeRowsToContents()
        self.setAutoScroll(False)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setWordWrap(False)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.selectionModel().selectionChanged.connect(self.select_change)


    def select_change(self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection):
        print('handle selected file')


    def set_data(self, list_find_files):
        print(f"file_table set_data {list_find_files}")
        self.clearContents()
        self.setRowCount(0)
        self.window().text_out.setPlainText("")

        for f in list_find_files:
            print(f"set table {f}")
            index = self.rowCount()
            self.insertRow(index)
            file_name = QtWidgets.QTableWidgetItem()
            file_name.setText(f"{os.path.basename(f)}")
            file_ext = QtWidgets.QTableWidgetItem()
            file_ext.setText(f"{os.path.splitext(f)[1]}")
            file_path = QtWidgets.QTableWidgetItem()
            file_path.setText(f"{os.path.dirname(f)}")
            file_size = QtWidgets.QTableWidgetItem()
            file_size.setText(f"{os.path.getsize(f)}")
            file_time = QtWidgets.QTableWidgetItem()
            file_time.setText(f"{time.ctime(os.path.getctime(f))}")
            self.setItem(index, 0, file_name)
            self.setItem(index, 1, file_ext)
            self.setItem(index, 2, file_path)
            self.setItem(index, 3, file_size)
            self.setItem(index, 4, file_time)

        self.resizeRowsToContents()
        print('set_data')

    def get_icon(self, datatype: int) -> QtGui.QIcon:
        print('get_icon')

    def get_selected_row(self):
        if len(self.selectedItems()) > 0:
            return self.selectedItems()[0].row()
        else:
            return -1
