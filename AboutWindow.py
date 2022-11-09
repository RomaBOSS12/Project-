from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


class About(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        object = QLabel("This program was built as a back end suplement for the game project called - Nonogram. This program takes some raw pictures and photos from the internet")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        
        object = QLabel("and turn them into nonograms, japanese puzzles of different extensions. Below you can the simple GUI of this application. It has the *select file* button.")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)
        
        label1 = QLabel()
        pixmap = QPixmap('MainWindow.jpg')
        label1.setPixmap(pixmap) 
        self.vbox.addWidget(label1)

        object = QLabel("It allows you to select any picture from the catalog.")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        label2 = QLabel()
        pixmap = QPixmap('OpenFile.jpg')
        label2.setPixmap(pixmap) 
        self.vbox.addWidget(label2)

        object = QLabel("We also have two large windows of the same size. When a file is chosen, on the left side you'll see")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)
        
        object = QLabel("the image of the3 file and on the right side you will see the puzzle of that image as illustrated below. ")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        label3 = QLabel()
        pixmap = QPixmap('SizeChange.jpg')
        label3.setPixmap(pixmap) 
        self.vbox.addWidget(label3)

        object = QLabel("You can also change the extnsion of the puzzle using the spin box. The change occurs in real time to increase the interaction with developer")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        label4 = QLabel()
        pixmap = QPixmap('PandaExample.jpg')
        label4.setPixmap(pixmap) 
        self.vbox.addWidget(label4)

        object = QLabel("Also, use buttons *save puzzle* and *batch* to save the puzzle as a jpg file in a newly created Batch folder and check for the list of puzzles")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        object = QLabel("Thank you for your attention and enjoy the app!!!")
        self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Read about this app')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = About()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()