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
        #Central Widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Main layout
        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.setWindowTitle("Pocket Pokedex")
        self.setGeometry(100, 100, 900, 500)
        self.Title = QLabel("Pocket Pokedex")
        self.setWindowIcon(QIcon("src/logo.png"))


        #Input
        inputLayout=QHBoxLayout()
        self.input=QLineEdit()
        self.input.setPlaceholderText("Enter Pokemon Name (e.g. pikachu)")
        self.searchButton=QPushButton()
        self.searchButton.setText("GO")
        self.searchButton.clicked.connect(self.getPokemon)
        inputLayout.addWidget(self.input)
        inputLayout.addWidget(self.searchButton)


        #Body
        self.displayLayout=QHBoxLayout()
        self.image=QLabel("Pokemon Will Appear Here")
        self.image.setAlignment(Qt.AlignCenter)
        self.displayLayout.addWidget(self.image,2)


        #combining all layout to the main one
        self.mainLayout.addWidget(self.Title)
        self.mainLayout.addLayout(self.displayLayout)
        self.mainLayout.addLayout(inputLayout)
        self.InitUI()
    def getPokemon(self):
        pass
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
        
        self.Title.setAlignment(Qt.AlignCenter)
        self.input.setStyleSheet("""
                                background-color: #2e2e2e;
                                color: white;
                                border-radius: 5px;
                                padding: 10px

                                 """)
        self.searchButton.setStyleSheet("""
                                background-color: #a8030c;
                                color: white;
                                font-weight: bold;
                                border-radius: 5px;
                                padding: 11px
                                 """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())
