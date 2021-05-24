

import sys

import pyowm
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel,QDialog,QTextEdit
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import pyqtSlot






class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Weather Detector '
        self.left = 720
        self.top = 200
        self.width =550
        self.height =600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setStyleSheet("background-color:BLACK")
        self.setWindowIcon(QIcon("C:/Users/ankur/PycharmProjects/weather_decter/logos/PhotoCutPasteBackgroundChanger59202012704PM.jpg"))

        # set python logo
        self.labelimg = QLabel(self)
        self.pixmap = QPixmap("C:/Users/ankur/PycharmProjects/weather_decter/logos/PhotoCutPasteBackgroundChanger592020102035AM.png")
        self.labelimg.setPixmap(self.pixmap)
        self.labelimg.setGeometry(220, 0, 100, 110)

        #label

        self.label = QLabel('Weather Dectector', self)
        self.label.setStyleSheet('color:white;  font-size:30px')
        self.label.move(150,120)

        #create textbar
        self.input=QLineEdit(self)
        self.input.move(20,260)
        self.input.setPlaceholderText("Enter your city name")
        self.input.setFont(QFont('Arial',12))
        self.input.resize(400,60)
        self.input.setStyleSheet("background-color:white")




        # Create a button in the window
        self.button = QPushButton('search', self)
        self.button.move(430,260)
        self.button.setFont(QFont('Arial', 12))
        self.button.resize(100,60)
        self.button.setStyleSheet("background-color:lightgrey")


        # connect button to function on_click
        self.button.clicked.connect(self.dected_weather)


        self.show()

    @pyqtSlot()
    def dected_weather(self):
        try:
          self.txt = self.input.text()
          dlg = QDialog(self)
          dlg.setGeometry(200, self.top, 500, 500)
          dlg.setWindowTitle("Weather Information")
          dlg.setFixedWidth(500)
          dlg.setFixedHeight(500)


          # set  logo
          self.labelimg = QLabel(dlg)
          self.pixmap = QPixmap("C:/Users/ankur/PycharmProjects/weather_decter/logos/PhotoCutPasteBackgroundChanger592020102035AM.png")
          self.labelimg.setPixmap(self.pixmap)
          self.labelimg.setGeometry(200, 0, 100, 110)

          # label
          self.label = QLabel('Weather Information', dlg)
          self.label.setStyleSheet('color:white;  font-size:30px')
          self.label.move(140, 120)

          #get weather
          owm = pyowm.OWM('c4c33b7910c61511296bd0024a3fa313')
          observ = owm.weather_at_place(self.txt)
          w = observ.get_weather()

          #get wind speed
          wind = w.get_wind()['speed']
          #get temperature
          Tem =w.get_temperature('celsius')['temp']
          # get max temperature
          Max = w.get_temperature('celsius')['temp_max']
        # get minimum temperature
          Minimum = w.get_temperature('celsius')['temp_min']



          text = QTextEdit(dlg)
          text.setStyleSheet('Color:white; font-size:20px; border:0px')
          text.setGeometry(0, 200, 500, 400)
          text.setReadOnly(True)
          text.insertHtml(f' <p style="text-align:center;">Temperature:{Tem} C<br>')
          text.insertHtml(f'Maximum Temp:{Max} C<br>')
          text.insertHtml(f' Minimum Temp:{Minimum} C<br><br>')
          text.insertHtml(f' Wind Speed:{wind}</p>')
          dlg.exec_()

        except:pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
