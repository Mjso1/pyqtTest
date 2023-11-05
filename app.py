import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from datetime import datetime

form_class = uic.loadUiType("main.ui")[0]
print(form_class)

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.BtnTest1.clicked.connect(self.functionTest1) 
        self.BtnTest2.clicked.connect(self.functionTest2) 
        self.BtnExit.clicked.connect(self.functionBtnExit) 

    def functionTest1(self):
      date_s = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
      print("Click Test 1 : ",date_s)

    def functionTest2(self):
      print("Click Test 2 : ",1+2)

    def functionBtnExit(self):
        sys.exit()
      
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()

    app.exec_()