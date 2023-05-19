import sys

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QApplication,
    QLineEdit
)
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dancho Voice Assistant")
        self.setWindowIcon(QIcon(r'img/ai.png'))
        self.setGeometry(650, 300, 400, 150)
        self.setMaximumWidth(400)
        self.setMaximumHeight(150)

        """Add custom font"""
        font = QFontDatabase.addApplicationFont(r'fonts/good timing.otf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
        else:
            print("Error loading fonts!")

        text_label = QLabel()
        text_label.setText("Type in your name")
        text_label.setFont(QFont(fonts[0], 16))
        text_label.setAlignment(Qt.AlignCenter)

        text_box = QLineEdit()
        text_box.setFont(QFont(fonts[0], 16))
        text_box.setAlignment(Qt.AlignCenter)


        main_layout = QVBoxLayout()
        main_layout.addWidget(text_label)
        main_layout.addWidget(text_box)
        self.setLayout(main_layout)
        self.show()


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()
