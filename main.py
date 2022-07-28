from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import os, sys
from Modulos.login import Login

if (QDialog.Accepted == True):
    app = QApplication(sys.argv)
    window = Login()
    window.show()
sys.exit(app.exec_())