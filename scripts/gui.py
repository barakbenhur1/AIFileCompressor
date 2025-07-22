import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTextEdit, QFileDialog,
    QMessageBox
)
from PyQt5.QtGui import QFont
from compressor import compress_file, decompress_file

class DropTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFixedHeight(40)
        self.file_path = None

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().urls()[0].toLocalFile()
        self.file_path = path
        self.setText(path)
        # no return

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI File Compressor")
        self.resize(600, 400)

        main_layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Compress Tab
        comp_tab = QWidget()
        comp_layout = QVBoxLayout(comp_tab)
        hb1 = QHBoxLayout()
        self.c_drop = DropTextEdit()
        btn_browse_c = QPushButton("Browse…")
        btn_browse_c.clicked.connect(self.browse_compress)
        hb1.addWidget(self.c_drop)
        hb1.addWidget(btn_browse_c)
        comp_layout.addLayout(hb1)
        self.c_btn = QPushButton("Start Compression")
        self.c_btn.setEnabled(False)
        self.c_btn.clicked.connect(self.start_compress)
        self.c_log = QTextEdit()
        self.c_log.setReadOnly(True)
        self.c_log.setFont(QFont("Courier"))
        self.c_log.setStyleSheet("padding:5px;")
        comp_layout.addWidget(self.c_btn)
        comp_layout.addWidget(self.c_log)

        # Decompress Tab
        decomp_tab = QWidget()
        decomp_layout = QVBoxLayout(decomp_tab)
        hb2 = QHBoxLayout()
        self.d_drop = DropTextEdit()
        btn_browse_d = QPushButton("Browse…")
        btn_browse_d.clicked.connect(self.browse_decompress)
        hb2.addWidget(self.d_drop)
        hb2.addWidget(btn_browse_d)
        decomp_layout.addLayout(hb2)
        self.d_btn = QPushButton("Start Decompression")
        self.d_btn.setEnabled(False)
        self.d_btn.clicked.connect(self.start_decompress)
        self.d_log = QTextEdit()
        self.d_log.setReadOnly(True)
        self.d_log.setFont(QFont("Courier"))
        self.d_log.setStyleSheet("padding:5px;")
        decomp_layout.addWidget(self.d_btn)
        decomp_layout.addWidget(self.d_log)

        self.tabs.addTab(comp_tab, "Compress")
        self.tabs.addTab(decomp_tab, "Decompress")
        main_layout.addWidget(self.tabs)

        # Signals for enabling buttons
        self.c_drop.textChanged.connect(lambda: self.c_btn.setEnabled(bool(self.c_drop.file_path)))
        self.d_drop.textChanged.connect(lambda: self.d_btn.setEnabled(self.d_drop.file_path and self.d_drop.file_path.endswith(".aic")))

    def log(self, area, text):
        ts = datetime.now().strftime("[%H:%M:%S] ")
        area.append(ts + text)

    def browse_compress(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Select file to compress")
        if fname:
            self.c_drop.file_path = fname
            self.c_drop.setText(fname)
        else:
            QMessageBox.warning(self, "No file", "Please select a file to compress")

    def browse_decompress(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Select .aic file", filter="AIC Files (*.aic)")
        if fname and fname.endswith(".aic"):
            self.d_drop.file_path = fname
            self.d_drop.setText(fname)
        else:
            QMessageBox.warning(self, "Invalid file", "Please select a valid .aic file")

    def start_compress(self):
        path = self.c_drop.file_path
        self.log(self.c_log, f"➡️ Compressing: {path}")
        try:
            out, warning = compress_file(path)
            if warning:
                self.log(self.c_log, warning)
            self.log(self.c_log, f"✅ Saved: {out}")
        except Exception as ex:
            self.log(self.c_log, f"❌ Error: {ex}")

    def start_decompress(self):
        path = self.d_drop.file_path
        self.log(self.d_log, f"➡️ Decompressing: {path}")
        try:
            out = decompress_file(path)
            self.log(self.d_log, f"✅ Saved: {out}")
        except Exception as ex:
            self.log(self.d_log, f"❌ Error: {ex}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
