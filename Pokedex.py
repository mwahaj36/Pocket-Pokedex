import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QMainWindow
)
from PyQt5.QtGui import QPixmap, QFontDatabase,QFont,QIcon
from PyQt5.QtCore import Qt
from io import BytesIO



class Pokedex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pocket Pokedex")
        self.setGeometry(100, 100, 900, 500)
        self.Title = QLabel("Pocket Pokedex", self)
        self.setWindowIcon(QIcon("src/logo.png"))
        self.InitUI()

    def InitUI(self):
        font_id=QFontDatabase.addApplicationFont("src/Pokemon.ttf")
        fontFamily=QFontDatabase.applicationFontFamilies(font_id)[0]
        myFont=QFont(fontFamily)
        self.Title.setFont(myFont)
        self.setStyleSheet("background-color: #141414")
        self.Title.setStyleSheet(f"""
            color: white;
            font-size: 50px;      
        """)
        self.Title.setGeometry(0, 0, 900, 100)
        self.Title.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())
