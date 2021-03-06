import sys
import os
import time
import platform

import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import bencoder
import file_table
import openpyxl

class torrent(QtWidgets. QMainWindow):
    def __init__(self):
        super().__init__()
        self.os_name = platform.system()
        self.find_root_path=""
        if self.os_name == 'Windows':
            self.find_root_path="F:\\acj\\programming\\"
        else:
            self.find_root_path="/Users"


        self.app = QtWidgets.QApplication.instance()
        self.settings = QtCore.QSettings()

        self.initial_style = self.app.style().name()
        self.app.setStyle("fusion")


        # Set up main window
        self.resize(1200, 700)
        self.setWindowTitle(f"torrent analyzer")

        # Restore window geometry from settings
        self.restoreGeometry(self.settings.value( "view/geometry", QtCore.QByteArray()))

        # Set up file menu
        file_menu = QtWidgets.QMenu("&File", self)
        open_action = QtGui.QAction("Open dat File", self)
        open_action.setShortcut(QtGui.QKeySequence.Open)
        open_action.triggered.connect(self.show_open_file)
        file_menu.addAction(open_action)

        close_action = QtGui.QAction("Close File", self)
        close_action.setShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT | QtCore.Qt.Key_Delete))
        open_action.triggered.connect(self.close_file)
        file_menu.addAction(close_action)

        export_action = QtGui.QAction("Export File", self)
        export_action.triggered.connect(self.export_file)
        file_menu.addAction(export_action)

        copy_action = QtGui.QAction("Copy File", self)
        copy_action.triggered.connect(self.copy_file)
        # export_action.setShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT | QtCore.Qt.Key_Delete))
        file_menu.addAction(copy_action)
        if self.os_name == 'Windows':
            file_menu.addSeparator()
            quit_action = QtGui.QAction("Quit", self)
            quit_action.triggered.connect(self.close)
            file_menu.addAction(quit_action)
        self.menuBar().addMenu(file_menu)

        # Set up find menu
        find_menu = QtWidgets.QMenu("Fin&d", self)
        find_action = QtGui.QAction("Find...", self)
        find_action.setShortcut(QtGui.QKeySequence.Find)
        find_action.triggered.connect(self.show_find)
        find_menu.addAction(find_action)
        self.menuBar().addMenu(find_menu)

        # Set up view menu
        view_menu = QtWidgets.QMenu("&View", self)
        self.native_style_action = QtGui.QAction("status bar", self)
        view_menu.addAction(self.native_style_action)
        self.menuBar().addMenu(view_menu)

        # Set up help menu
        help_menu = QtWidgets.QMenu("&Help", self)
        self.version_action = QtGui.QAction("Version", self)
        self.version_action.triggered.connect(self.show_version)
        help_menu.addAction(self.version_action)

        if self.os_name == 'Windows':
            about_action = QtGui.QAction("About", self)
            about_action.triggered.connect(self.show_about)
            help_menu.addAction(about_action)
        self.menuBar().addMenu(help_menu)
        self.menuBar().setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.statusBar()

        # Set up toolbar
        toolbar = QtWidgets.QToolBar("Main", self)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.toggleViewAction().setEnabled(False)
        toolbar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        open_action = QtGui.QAction( QtGui.QIcon("img/open.png"), "Open File", toolbar)
        open_action.triggered.connect(self.show_open_file)
        toolbar.addAction(open_action)
        close_action = QtGui.QAction( QtGui.QIcon("img/close.png"), "Close Selected File", toolbar)
        toolbar.addAction(close_action)
        find_action = QtGui.QAction( QtGui.QIcon("img/find.png"), "Find", toolbar)
        find_action.triggered.connect(self.show_find)
        toolbar.addAction(find_action)

        export_action = QtGui.QAction( QtGui.QIcon("img/export.png"), "export excel", toolbar)
        export_action.triggered.connect(self.export_data)
        toolbar.addAction(export_action)
        self.addToolBar(toolbar)

        # Set up main layout
        main_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_widget.setLayout(main_layout)

        self.file_table = file_table.FileTable(main_widget)

        # self.uri_textbox = QtWidgets.QLineEdit(main_widget)
        # self.uri_textbox.returnPressed.connect(self.tree.handle_uri_change)
        # main_layout.addWidget(self.uri_textbox)


        self.statusBar().setStyleSheet(
            "QStatusBar QLabel { border-color: lightgray; border-style: solid; border-width: 0 1px 0 0; }")

        value_splitter = QtWidgets.QSplitter( QtGui.Qt.Orientation.Vertical)
        # value_splitter = QtWidgets.QSplitter(main_widget)
        value_splitter.addWidget(self.file_table)

        self.text_out = QtWidgets.QPlainTextEdit()
        mono_font = QtGui.QFont()
        mono_font.setFamilies(["Courier New", "Monospaced"])
        mono_font.setStyleHint(QtGui.QFont.Monospace)
        self.text_out.setFont(mono_font)
        self.text_out.setLineWrapMode(self.text_out.LineWrapMode.NoWrap)
        self.text_out.setReadOnly(True)
        value_splitter.addWidget(self.text_out)
        value_splitter.setStretchFactor(0, 1)
        value_splitter.setStretchFactor(1, 2)
        value_splitter.setChildrenCollapsible(False)
        main_layout.addWidget(value_splitter)

        self.setCentralWidget(main_widget)

        self.progress_bar = QtWidgets.QProgressBar(self.statusBar())
        self.progress_bar.setMaximumWidth(100)
        self.progress_bar.hide()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.findfiles = []
        self.parse_data= []

    def show_about(self):
        QtWidgets.QMessageBox().about( self, f"About torrent analyzer", f"use bencoder")

    def show_version(self):
        QtWidgets.QMessageBox().about(self,f"",f'version 0.0.1')

    def show_find(self):
        name = "resume.dat"
        self.findfiles.clear()
        self.statusBar().showMessage("Loading...")
        self.statusBar().repaint()
        for dirpath, dirname, filename in os.walk(self.find_root_path):
            if name in filename:
                self.findfiles.append(os.path.join(dirpath,name))

        self.parse_torrent_dat(self.findfiles[0])
        self.window().file_table.set_data(self.findfiles)
        for text in self.parse_data:
            self.text_out.appendPlainText(text)
        self.statusBar().clearMessage()
        print(f'find dialog : {self.findfiles}')



    def export_data(self):
        if(self.parse_data):
            filename = QtWidgets.QFileDialog.getSaveFileName(self, "Title", "", "EXCEL (*.xlsx)")
            print(f'excel : {filename}')
            if(filename[0]):
                export_excel = openpyxl.Workbook()
                ws = export_excel.active
                ws1 = export_excel.create_sheet()
                ws.title = 'resume.dat'
                ws1.title = 'filelist'
                resume_header = ["File_Name","Added_On","Completed_On","Downloaded","Uploaded","Path","Seedtime"]
                filelist_header = ["FileName", "ext", "Path", "Size", "Time"]
                ws.append(resume_header)
                for data in self.parse_data:
                    ws.append(data.split(','))
                ws1.append(filelist_header)
                # ws1.append(data.split(','))
                export_excel.save(filename[0])
                export_excel.close()

        print(f'export data to excel file')


    def show_open_file(self):
        """Show the open file dialog"""
        file_selection = QtWidgets.QFileDialog.getOpenFileNames( self, "Open Torrent File")
        self.statusBar().showMessage("Loading...")
        self.statusBar().repaint()

        if isinstance(file_selection, tuple) and len(file_selection) > 0 and len(file_selection[0]) > 0:
            for file in file_selection[0]:
                self.open_file(file)

        self.statusBar().clearMessage()

    def open_file(self, filename: str):
        print(f'open file')

    def close_file(self, filename: str):
        print(f'close file')

    def copy_file(self, filename: str):
        print(f'copy file')

    def export_file(self, filename: str):
        print(f'export file')

    def parse_torrent_dat(self,filename: str):
        print(f"{filename} parsing....")
        f = open(filename, "rb")
        d = bencoder.decode(f.read())

        def convert(epoch):
            return time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(epoch))

        print("File_Name," + "Added_On," + "Completed_On," + "Downloaded," + "Uploaded," + "Path," + "Seedtime")
        for key in d:
            if key == b'.fileguard':
                print("Ignore this!")
            elif key == b'rec':
                print("Ignore this!")
            else:
                fileName = str(key.decode('utf8')).strip()
                added_on = str(convert(d[key][b'added_on']))
                completed_on = str(convert(d[key][b'completed_on']))
                downloaded = str(d[key][b'downloaded'])
                uploaded = str(d[key][b'uploaded'])
                path = str((d[key][b'path']).decode('utf8')).strip()
                seedtime = str(d[key][b'seedtime']).strip()
                print(f'{fileName}:{type(key)}, {added_on}, {completed_on}, {downloaded}, {uploaded}, {path}, {seedtime}')
                self.parse_data.append(f'{fileName}, {added_on}, {completed_on}, {downloaded}, {uploaded}, {path}, {seedtime}')

        f.close()

    def closeEvent(self, event):
        """Save the current geometry of the application"""
        self.settings.setValue("view/geometry", self.saveGeometry())
        event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)

    torrent_analyzer = torrent()

    torrent_analyzer.show()

    # Process command-line file(s)
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            torrent_analyzer.open_file(filename)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()