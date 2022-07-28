from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from templates.Menu import Ui_MainWindow
from Modulos.cadastro import TelaCadastrar
from bd.conexaoBanco import *
from Modulos.altera import TelaAltera

class TelaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pesquisa.setFocus()
        self.ui.tableWidget.setColumnWidth(0, 445)
        self.ui.actionCadastrar.triggered.connect(self.cadastrar)
        self.ui.actionSair.triggered.connect(self.sair)
        self.usuarios()
        self.ui.btnPesquisa.clicked.connect(self.pesquisa_usuarios)
        self.ui.actionEditar.triggered.connect(self.altera)

    def cadastrar(self):
        self.window = TelaCadastrar(self.usuarios)
        self.window.show()
    
    def altera(self):
        self.window = TelaAltera()
        self.window.show()

    def sair(self):
        self.window = TelaPrincipal()
        self.close()
    
    def usuarios(self):
        conexao = Conexao.crinado_conexao()
        cursor = conexao.cursor()
        comando = "SELECT u.nome, u.usuario, u.senha1, u.senha2, u.senha3 FROM usuario u WHERE u.ativo = 1 ORDER BY u.nome"
        usuarios = cursor.execute(comando)
        self.ui.tableWidget.setRowCount(0)
        
        for linha, dados in enumerate(usuarios):
            self.ui.tableWidget.insertRow(linha)
            for coluna, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(dados)))

    def pesquisa_usuarios(self):
        nome_pesquisa = self.ui.pesquisa.text().upper()
        conexao = Conexao.crinado_conexao()
        cursor = conexao.cursor()
        comando = f"SELECT u.nome, u.usuario, u.senha1, u.senha2, u.senha3 FROM usuario u WHERE u.nome like '%{nome_pesquisa}%' and u.ativo = 1 ORDER BY u.nome"
        usuarios = cursor.execute(comando)
        self.ui.tableWidget.setRowCount(0)
        
        for linha, dados in enumerate(usuarios):
            button = QtWidgets.QPushButton()
            self.ui.tableWidget.insertRow(linha)
            for coluna, dados in enumerate(dados):
                self.ui.tableWidget.setCellWidget(1, 1, button)
                self.ui.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(dados)))  