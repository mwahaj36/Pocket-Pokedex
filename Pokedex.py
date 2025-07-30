import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QMainWindow
)
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont, QIcon
from PyQt5.QtCore import Qt
from io import BytesIO


class Pokedex(QMainWindow):
    def __init__(self):
        super().__init__()

        # Central Widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)

        # Window Settings
        self.setWindowTitle("Pocket Pokedex")
        self.setGeometry(100, 100, 900, 500)
        self.setWindowIcon(QIcon("src/logo.png"))

        # Title
        self.Title = QLabel("Pocket Pokedex")
        self.Title.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.Title)

        # Input
        inputLayout = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter Pokemon Name (e.g. pikachu)")
        self.searchButton = QPushButton("GO")
        self.searchButton.clicked.connect(self.getPokemon)
        self.input.returnPressed.connect(self.searchButton.click)  # search on Enter key

        inputLayout.addWidget(self.input)
        inputLayout.addWidget(self.searchButton)
        self.mainLayout.addLayout(inputLayout)

        # Main Body
        self.displayLayout = QHBoxLayout()
        self.image = QLabel("Pokemon Will Appear Here")
        self.image.setAlignment(Qt.AlignCenter)
        self.displayLayout.addWidget(self.image, 1)

        self.infoLayout = QVBoxLayout()
        self.info = QLabel("Search for a Pokemon to see their details")
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setWordWrap(True)
        self.infoLayout.addWidget(self.info)
        self.displayLayout.addLayout(self.infoLayout, 2)

        self.mainLayout.addLayout(self.displayLayout)

        self.InitUI()

    def getPokemon(self):
        name = self.input.text().strip().lower()
        if not name:
            return  # no api call for empty input

        url = f"https://pokeapi.co/api/v2/pokemon/{name}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.displayPokemon(data)

        except Exception:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERROR")
            msg.setText(f"COULD NOT FIND THE POKEMON '{name}' in the Pokeapi Database")
            msg.setStyleSheet("""
                QLabel {
                    color: red;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #ff4d4d;
                    color: white;
                    padding: 6px 12px;
                    border: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #ff1a1a;
                }
            """)
            msg.exec_()

    def displayPokemon(self, data):
        self.info.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        name = data['name'].capitalize()
        types = [t['type']['name'] for t in data['types']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        sprite_url = data['sprites']['front_default']

        # Format Pokemon Details
        info_text = f"<b>{name}</b><br><br>"
        info_text += f"<b>Type:</b> {', '.join(types)}<br><br>"
        info_text += "<b>Base Stats:</b><br>"
        for stat_name, value in stats.items():
            info_text += f"{stat_name.title()}: {value}<br>"

        self.info.setText(info_text)

        # Load Pokémon Sprite
        if sprite_url:
            img_data = requests.get(sprite_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(img_data).read())
            self.image.setPixmap(pixmap.scaled(300, 500, Qt.KeepAspectRatio))
        else:
            self.image.setText("No image available.")

    def InitUI(self):
        # Load custom font
        font_id = QFontDatabase.addApplicationFont("src/Pokemon.ttf")
        if font_id != -1:
            fontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]
            myFont = QFont(fontFamily)
            self.Title.setFont(myFont)

        # Styles
        self.setStyleSheet("background-color: #141414")

        self.Title.setStyleSheet("""
            color: white;
            font-size: 50px;
        """)
        
        self.image.setStyleSheet("""
            border: 3px solid #2e2e2e;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)

        self.info.setStyleSheet("""
            border: 3px solid #2e2e2e;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)

        self.input.setStyleSheet("""
            background-color: #2e2e2e;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)

        self.searchButton.setStyleSheet("""
            QPushButton {
                background-color: #a8030c;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 11px;
            }
            QPushButton:hover {
                background-color: white;
                color: #a8030c;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())
