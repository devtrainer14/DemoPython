from PyQt5 import QtWidgets, uic
 
import sys
 
app = QtWidgets.QApplication([])
 
win = uic.loadUi("form.ui") #specify the location of your .ui file
 
win.show()
 
sys.exit(app.exec())