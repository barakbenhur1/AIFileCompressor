from PyQt6.QtWidgets import *
from compressor import compress
from decompressor import decompress
from pathlib import Path

class CompressorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AI File Compressor")

        tabs = QTabWidget(self)

        # Compression Tab
        comp_tab = QWidget()
        comp_layout = QVBoxLayout()
        self.comp_input = QLineEdit()
        comp_browse = QPushButton('Browse')
        comp_browse.clicked.connect(self.browse_comp)
        comp_btn = QPushButton('Compress')
        comp_btn.clicked.connect(self.compress_file)
        self.comp_log = QTextEdit()
        self.comp_log.setReadOnly(True)

        comp_layout.addWidget(self.comp_input)
        comp_layout.addWidget(comp_browse)
        comp_layout.addWidget(comp_btn)
        comp_layout.addWidget(self.comp_log)
        comp_tab.setLayout(comp_layout)
        tabs.addTab(comp_tab, "Compress")

        # Decompression Tab
        decomp_tab = QWidget()
        decomp_layout = QVBoxLayout()
        self.decomp_input = QLineEdit()
        decomp_browse = QPushButton('Browse')
        decomp_browse.clicked.connect(self.browse_decomp)
        decomp_btn = QPushButton('Decompress')
        decomp_btn.clicked.connect(self.decompress_file)
        self.decomp_log = QTextEdit()
        self.decomp_log.setReadOnly(True)

        decomp_layout.addWidget(self.decomp_input)
        decomp_layout.addWidget(decomp_browse)
        decomp_layout.addWidget(decomp_btn)
        decomp_layout.addWidget(self.decomp_log)
        decomp_tab.setLayout(decomp_layout)
        tabs.addTab(decomp_tab, "Decompress")

        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)
        self.resize(600, 400)

    def browse_comp(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select file to compress")
        if file_path:
            self.comp_input.setText(file_path)

    def browse_decomp(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select .aip file to decompress")
        if file_path:
            self.decomp_input.setText(file_path)

    def compress_file(self):
        input_path = self.comp_input.text()
        if not input_path:
            return
        output = compress(input_path)
        self.comp_log.append(f"Compressed to: {output}")

    def decompress_file(self):
        input_path = self.decomp_input.text()
        if not input_path or not Path(input_path).suffix == '.aip':
            self.decomp_log.append("Invalid .aip file")
            return
        output = decompress(input_path)
        self.decomp_log.append(f"Decompressed to: {output}")

if __name__ == "__main__":
    app = QApplication([])
    gui = CompressorGUI()
    gui.show()
    app.exec()
