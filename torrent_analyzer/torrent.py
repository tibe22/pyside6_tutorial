import sys

import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import bencoder
import file_table

class torrent(QtWidgets. QMainWindow):
    def __init__(self):
        super().__init__()

        self.app = QtWidgets.QApplication.instance()
        self.settings = QtCore.QSettings()

        self.initial_style = self.app.style().name()
        self.app.setStyle("fusion")

        # use_native_style = self.settings.value(
        #     "view/native_style", False, bool)

        # if not use_native_style:
        #     self.app.setStyle("fusion")

        # Set up main window
        self.resize(1200, 700)
        self.setWindowTitle(f"torrent analyzer")

        # Restore window geometry from settings
        self.restoreGeometry(self.settings.value( "view/geometry", QtCore.QByteArray()))

        # self.tree = key_tree.KeyTree(self)
        # self.find_dialog = find_dialog.FindDialog(self)

        # Set up file menu
        file_menu = QtWidgets.QMenu("&File", self)
        open_action = QtGui.QAction("Open dat File", self)
        open_action.setShortcut(QtGui.QKeySequence.Open)
        open_action.triggered.connect(self.show_open_file)
        file_menu.addAction(open_action)

        close_action = QtGui.QAction("Close File", self)
        close_action.setShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT | QtCore.Qt.Key_Delete))
        open_action.triggered.connect(self.close_file)
        # close_action.triggered.connect(self.tree.remove_selected_hive)
        file_menu.addAction(close_action)

        export_action = QtGui.QAction("Export File", self)
        open_action.triggered.connect(self.export_file)
        # export_action.setShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT | QtCore.Qt.Key_Delete))
        # close_action.triggered.connect(self.tree.remove_selected_hive)
        file_menu.addAction(export_action)

        copy_action = QtGui.QAction("Copy File", self)
        copy_action.triggered.connect(self.copy_file)
        # export_action.setShortcut(QtGui.QKeySequence(QtCore.Qt.SHIFT | QtCore.Qt.Key_Delete))
        # close_action.triggered.connect(self.tree.remove_selected_hive)
        file_menu.addAction(copy_action)
        # file_menu.addSeparator()
        # quit_action = QtGui.QAction("Quit", self)
        # quit_action.triggered.connect(self.close)
        # file_menu.addAction(quit_action)
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
        self.native_style_action = QtGui.QAction("Use native style", self)
        # self.native_style_action.setCheckable(True)
        # self.native_style_action.setChecked(use_native_style)
        # self.native_style_action.toggled.connect(self.toggle_style)
        view_menu.addAction(self.native_style_action)
        self.menuBar().addMenu(view_menu)

        # Set up help menu
        help_menu = QtWidgets.QMenu("&Help", self)
        self.version_action = QtGui.QAction("Version", self)
        self.version_action.triggered.connect(self.show_version)
        help_menu.addAction(self.version_action)

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
        # close_action.triggered.connect(self.tree.remove_selected_hive)
        toolbar.addAction(close_action)
        # close_all_action = QtGui.QAction(
        #     QtGui.QIcon(helpers.resource_path("img/close_all.png")), "Close All Hives", toolbar)
        # close_all_action.triggered.connect(self.tree.remove_all_hives)
        # toolbar.addAction(close_all_action)
        find_action = QtGui.QAction( QtGui.QIcon("img/find.png"), "Find", toolbar)
        find_action.triggered.connect(self.show_find)
        toolbar.addAction(find_action)
        # find_next_action = QtGui.QAction(
        #     QtGui.QIcon(helpers.resource_path("img/find_next.png")), "Find Next", toolbar)
        # find_next_action.triggered.connect(self.find_dialog.handle_find)
        # toolbar.addAction(find_next_action)
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

        # tree_container = QtWidgets.QWidget()
        # tree_container_layout = QtWidgets.QVBoxLayout(tree_container)
        # tree_container_layout.setContentsMargins(0, 0, 0, 0)
        # tree_container.setLayout(tree_container_layout)

        # tree_container_layout.addWidget(self.file_table)
        # self.tree.setSizePolicy(
        #     QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        # self.hive_info = hive_info_table.HiveInfoTable(tree_container)
        # hive_geometry = self.hive_info.geometry()
        # hive_geometry.setHeight(5)
        # self.hive_info.setGeometry(hive_geometry)
        # self.hive_info.setMinimumHeight(10)
        # self.hive_info.setSizeAdjustPolicy(
        #     self.hive_info.SizeAdjustPolicy.AdjustToContents)
        # tree_container_layout.addWidget(self.hive_info)

        value_splitter = QtWidgets.QSplitter( QtGui.Qt.Orientation.Vertical)
        # value_splitter = QtWidgets.QSplitter(main_widget)
        value_splitter.addWidget(self.file_table)
        self.value_hex = QtWidgets.QPlainTextEdit()
        mono_font = QtGui.QFont()
        mono_font.setFamilies(["Courier New", "Monospaced"])
        mono_font.setStyleHint(QtGui.QFont.Monospace)
        self.value_hex.setFont(mono_font)
        self.value_hex.setLineWrapMode(self.value_hex.LineWrapMode.NoWrap)
        value_splitter.addWidget(self.value_hex)
        value_splitter.setStretchFactor(0, 2)
        value_splitter.setStretchFactor(1, 1)
        value_splitter.setChildrenCollapsible(False)
        main_layout.addWidget(value_splitter)

        # main_splitter = QtWidgets.QSplitter(main_widget)
        # main_splitter.addWidget(tree_container)
        # main_splitter.addWidget(value_splitter)
        # main_splitter.setStretchFactor(0, 4)
        # main_splitter.setStretchFactor(1, 5)
        # main_splitter.setChildrenCollapsible(False)
        # main_layout.addWidget(main_splitter)
        self.setCentralWidget(main_widget)

        self.progress_bar = QtWidgets.QProgressBar(self.statusBar())
        self.progress_bar.setMaximumWidth(100)
        self.progress_bar.hide()
        self.statusBar().addPermanentWidget(self.progress_bar)

    def show_about(self):
        QtWidgets.QMessageBox().about( self, f"About torrent analyzer", f"use bencoder")

    def show_version(self):
        QtWidgets.QMessageBox().about(self,f"",f'version 0.0.1')

    def show_find(self):
        print(f'find dialog')
        # self.find_dialog.exec()

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