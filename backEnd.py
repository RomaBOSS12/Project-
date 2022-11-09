# importing libraries
import AboutWindow 
import ImageProcessing
import FileRetrieval
import os 
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
    QPushButton,
    QHBoxLayout,
    QGridLayout,
)


class Window(QMainWindow):                 #QMainWindow
  
    def __init__(self):
        super().__init__()
        self.control = 0
        # self = QWidget()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 900, 500)
       
        self.VerticalLayout = QVBoxLayout() 
        self.gridLayout = QGridLayout() 
        self.gridLayout.setSpacing(5) 
        self.HorizontalLayout = QGridLayout()

        scene = QGraphicsScene(0, 0, 450, 200)
        self.dataplot = QGraphicsView(scene) 
        self.HorizontalLayout.addWidget(self.dataplot, 0, 0, Qt.AlignLeft)
        self.Pixelplot = QGraphicsView(scene)
        self.HorizontalLayout.addWidget(self.Pixelplot, 0, 1, Qt.AlignRight)

        self.FileButton = QPushButton(self, text='Select File')
        self.FileButton.clicked.connect(self.clickedSlot)

        self.PuzzleButton = QPushButton(self, text='Save Puzzle')
        self.PuzzleButton.clicked.connect(self.clickedSave)

        self.FileNameLabel = QLabel(' <Filename>')
        self.FileNameLabel.setGeometry(20, 10, 50, 20)
        self.SizeLabel = QLabel('Puzzle Size  ') 
        self.SizeLabel.setGeometry(20, 10, 50, 20)

        self.AboutButton = QPushButton(self, text='About')
        self.AboutButton.clicked.connect(self.clickedAbout)

        self.BatchButton = QPushButton(self, text='Batch')
        self.BatchButton.clicked.connect(self.clickedBatch) 


        self.gridLayout.addWidget(self.FileButton, 0, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(self.FileNameLabel, 0, 1, Qt.AlignLeft)
        self.gridLayout.addWidget(self.SizeLabel, 0, 6)
        self.gridLayout.addWidget(self.PuzzleButton, 1, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(self.AboutButton, 0, 10, Qt.AlignRight)
        self.gridLayout.addWidget(self.BatchButton, 1, 10, Qt.AlignRight)

        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setColumnStretch(3, 10)
        self.gridLayout.setColumnStretch(4, 10)
        self.gridLayout.setColumnStretch(9, 10)
        
    

        self.VerticalLayout.addLayout(self.gridLayout)
        self.VerticalLayout.addLayout(self.HorizontalLayout)

        
        
        # calling method
        self.UiComponents()

        # setting initial value
        self.value = 5

        widget = QWidget()
        widget.setLayout(self.VerticalLayout)
        self.setCentralWidget(widget)
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating spin box
        self.spin = QSpinBox(self)
  
        # setting geometry to spin box
        self.spin.setGeometry(100, 100, 100, 40)
  
        # adding action to the spin box
        self.spin.valueChanged.connect(self.show_result)

        self.gridLayout.addWidget(self.spin, 0, 7)

        # setting value to the spin box
        self.spin.setValue(5) 
        

        # setting prefix to spin
        self.spin.setPrefix(str(self.value) + " x ")

        # setting single step size
        self.spin.setSingleStep(5)

        # setting range
        self.spin.setRange(5, 90) 

        # creating the check-box
        self.checkbox = QCheckBox('No Empty Rows', self)
  
        # setting geometry of check box
        self.checkbox.setGeometry(200, 150, 100, 30)

        self.checkbox.stateChanged.connect(self.clickBox)

        self.gridLayout.addWidget(self.checkbox, 1, 7)
  
        # setting check box state to checked
        self.checkbox.setChecked(False) 
        self.state = False 

  
    # method called by spin box
    def show_result(self):
        print("***************************************************************************************")
        # getting current value

        path = "Batch"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:

            # Create a new directory because it does not exist
            os.makedirs(path)
            print("The new directory is created!")

        self.value = self.spin.value()
        
        # setting prefix to spin
        self.spin.setPrefix(str(self.value) + " x ")
        if self.control == 1:
            ImageProcessing.ImageP(self.Batch, self.value, self.state)  
            print("ggggggggggggggggggggggg",self.Batch[13:])
        
            
        
            label2 = QLabel()
            # map the picture on the dataplot as a label
            self.Pixelplot = QPixmap('Batch/re' + self.Batch[13:])  
            label2.setPixmap(self.Pixelplot) 
            print("What happened")
            # # set the layout 
            self.HorizontalLayout.addWidget(label2, 0 , 1, Qt.AlignRight)
        
  
    
    def clickedSlot(self):
        # retrieve file and open it
        RetrieveFile = FileRetrieval.App()
        Photo = RetrieveFile.FileName 
        self.FileNameLabel.setText(Photo)
        print('Select the file')
        im = Image.open(Photo)
        # resize the image accodring to the size of the widget
        im_resize = im.resize((450, 450))
        print(Photo)
        print("/")
        print(Photo.rfind("/"))
        # get the name of the file from directory
        NameOfFile = Photo [ Photo.rfind("/") + 1 :]
        # and add batch to it in order to save it in Batch Folder
        self.Batch = 'Batch/resized' + NameOfFile
        self.NameOfFile = NameOfFile   
        print(self.Batch) 
        # save the photo in the batch folder
        Resized = im_resize.save(self.Batch) 
        # create a label 
        label = QLabel()
        # map the picture on the dataplot as a label
        self.dataplot = QPixmap(self.Batch)  
        label.setPixmap(self.dataplot)
        # set the layout 
        self.HorizontalLayout.addWidget(label, 0 , 0, Qt.AlignLeft)
        print("RRRRRRRRRRRRRRR ", self.Batch) 


        ImageProcessing.ImageP(self.Batch, self.value, self.state)   
        print("ggggggggggggggggggggggg",self.Batch)
       
        
       
        label2 = QLabel()
        # map the picture on the dataplot as a label
        self.Pixelplot = QPixmap('Batch/re' + self.Batch[13:])  
        label2.setPixmap(self.Pixelplot) 
        print("What happened")
        # # set the layout 
        self.HorizontalLayout.addWidget(label2, 0 , 1, Qt.AlignRight)
        self.control = 1
        
    def clickedSave(self):
            print('Puzzle has been saved')


    def clickedAbout(self):
            print("Here is what we are about") 
            self.about = AboutWindow.About() 

    def clickedBatch(self):
            print("Here is your batch") 
            path = "Batch"
            # Check whether the specified path exists or not
            isExist = os.path.exists(path)
            if not isExist:

                # Create a new directory because it does not exist
                os.makedirs(path)
                print("The new directory is created!")
            os.startfile(path) 
        
    def clickBox(self, state): 
        if state == QtCore.Qt.Checked:
            print('Checked')
            self.state = True 
        else:
            print('Unchecked')
            self.state = False 

    

  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
window.show()
  
# start the app
sys.exit(App.exec()) 







