from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from templates.Login import Ui_Dialog
from Modulos.menu import TelaPrincipal
from bd.conexaoBanco import *

class Login(QDialog):
    def __init__(self, *args, **argvs):
        super(Login,self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.usuairo.setFocus()
        self.ui.Entrar.clicked.connect(self.login)

    def login(self):

        user = self.ui.usuairo.text().lower()
        pssd = self.ui.senha.text().lower()
        conexao = Conexao.crinado_conexao()
        validLogin = Querys.verica_login(conexao, user, pssd)

        if validLogin == True:
            self.window = TelaPrincipal()
            self.window.show()
            Login.hide(self)
        else:
            mBox = QMessageBox.information(self,"AVISO!!", "USUÁRIO\SENHA INVALIDO!")
            self.limpar()
    
    def limpar(self):
        self.ui.usuairo.clear()
        self.ui.senha.clear()