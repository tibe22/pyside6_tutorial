import struct

from torrent import torrent
import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui
import PySide6.QtCore as QtCore



class FileData(QtWidgets.QTableWidgetItem):
    def __init__(self, raw_data: bytes, value, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.raw_data = raw_data
        self.file = value


class FileTable(QtWidgets.QTableWidget):
    """File table that shows the files of the finded files"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Name", "Type", "Size", "Time"])
        self.horizontalHeader().setStretchLastSection(True)
        self.setColumnWidth(0, 180)
        self.setColumnWidth(1, 120)
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

        self.selectionModel().selectionChanged.connect(self.handle_selection_change)


    def handle_selection_change(self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection):
        print('handle selected file')
        if len(selected.indexes()) < 1:
            return


    def set_data(self, reg_values: "list[Registry.RegistryValue]"):
        print('set_data')

    def get_icon(self, datatype: int) -> QtGui.QIcon:
        print('get_icon')

    def reg_type_to_str(self, datatype: int) -> str:
        print(f'reg_tupe_to_str')

    def reg_data_to_str(self, datatype: int, raw_data: bytes, value) -> str:
        print(f'reg_data_to_str')

    def select_value(self, value: str):
        for i in range(self.rowCount()):
            if (value == self.item(i, 0).text()):
                self.clearSelection()
                self.selectRow(i)
                self.scrollToItem(self.item(i, 0))
                self.setFocus()

    def get_selected_row(self):
        if len(self.selectedItems()) > 0:
            return self.selectedItems()[0].row()
        else:
            return -1
