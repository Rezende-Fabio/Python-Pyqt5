from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from templates.Cadastro import Ui_Cadastro
from bd.conexaoBanco import *
from Modulos.Gerador_de_senha import Gerador


class TelaCadastrar(QDialog):
    def __init__(self, usuarios, *args, **argvs):
        super(TelaCadastrar, self).__init__(*args, **argvs)
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        self.ui.gerarSenha.clicked.connect(self.gerarSenha)
        self.ui.limparCad.clicked.connect(self.limpar)
        self.ui.cancelarCad.clicked.connect(self.voltarMenu)
        self.ui.slavarCad.clicked.connect(self.inserir)
        self.carregaInfo = usuarios

        quit = QtWidgets.QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
 
 
    def closeEvent(self,event):
        self.carregaInfo()

    def inserir(self):
        nomeCad = self.ui.nome.text().upper()
        usuarioCad = self.ui.usuarioCad.text().upper()
        senhaCad = self.ui.senhaCad.text().upper()
        conexao = Conexao.crinado_conexao()
        insert = Querys.inserir_usuario(conexao, nomeCad, usuarioCad, senhaCad)
        
        if insert == True: mBox = QMessageBox.information(self,"AVISO!!", "Usuário inserido com sucesso")
        else: mBox = QMessageBox.information(self,"AVISO!!", "Falha ao inserir Usuário")

        self.limpar()
        self.closeEvent(self)

    def limpar(self):
        self.ui.nome.clear()
        self.ui.usuarioCad.clear()
        self.ui.senhaCad.clear()

    def voltarMenu(self):
        self.closeEvent(self)
        TelaCadastrar.hide(self)
    
    def gerarSenha(self):
        senhaStr = Gerador.gera_senha()
        self.ui.senhaCad.clear()
        self.ui.senhaCad.insert(senhaStr)