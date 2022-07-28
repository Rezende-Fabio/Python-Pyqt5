from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from templates.Altera_usuario import Ui_Dialog
from bd.conexaoBanco import *
from Modulos.Gerador_de_senha import Gerador
from Modulos.cadastro import TelaCadastrar


class TelaAltera(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaAltera, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 0)
        self.ui.tableWidget.setColumnWidth(1, 250)
        self.usuarios()
        self.ui.tableWidget.itemSelectionChanged.connect(self.preenche_automatico)
        self.ui.btnPesquisaEdit.clicked.connect(self.pesquisa_usuarios)
        self.ui.limparEdit.clicked.connect(self.limpar)
        self.ui.salvarEdit.clicked.connect(self.altera)
        self.ui.sair.clicked.connect(self.sair)
        self.ui.gerarSenha.clicked.connect(self.gerar_senha)

    def sair(self):
        TelaAltera.hide(self)

    def usuarios(self):
        conexao = Conexao.crinado_conexao()
        cursor = conexao.cursor()
        comando = "SELECT u.id_usuario, u.nome, u.usuario, u.senha1, u.senha2, u.senha3 FROM usuario u ORDER BY u.nome"
        usuarios = cursor.execute(comando)
        self.ui.tableWidget.setRowCount(0)
        
        for linha, dados in enumerate(usuarios):
            self.ui.tableWidget.insertRow(linha)
            for coluna, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(dados)))
    
    def pesquisa_usuarios(self):
        nome_pesquisa = self.ui.pesquisaEdit.text().upper()
        conexao = Conexao.crinado_conexao()
        cursor = conexao.cursor()
        comando = f"SELECT u.id_usuario, u.nome, u.usuario, u.senha1, u.senha2, u.senha3 FROM usuario u WHERE u.nome like '%{nome_pesquisa}%' ORDER BY u.nome"
        usuarios = cursor.execute(comando)
        self.ui.tableWidget.setRowCount(0)

        for linha, dados in enumerate(usuarios):
            self.ui.tableWidget.insertRow(linha)
            for coluna, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(dados)))  

    def preenche_automatico(self):
        self.limpar()
        id = self.seleciona_id_banco()
        if id != None:
            conexao = Conexao.crinado_conexao()
            cursor = conexao.cursor()
            comando = f"SELECT u.id_usuario, u.nome, u.usuario, u.senha1, u.senha2, u.senha3 FROM usuario u WHERE u.id_usuario = {id}"
            usuario_selcionado = cursor.execute(comando)
            for x in usuario_selcionado:
                nome = x[1]
                usuario = x[2]
                senha1 = x[3]
                senha2 = x[4]
                senha3 = x[5]
            
            self.ui.nomeEdit.insert(nome)
            self.ui.usuarioEdit.insert(usuario)
            self.ui.senhaEdit.insert(senha1)
            self.ui.senhaEdit_2.insert(senha2)
            self.ui.senhaEdit_3.insert(senha3)

    def seleciona_id_tabela(self):
        return self.ui.tableWidget.currentRow() 
    
    def seleciona_id_banco(self):
        valor = self.ui.tableWidget.item(self.seleciona_id_tabela(), 0)
        return valor.text() if not valor is None else valor
    
    def limpar(self):
        self.ui.nomeEdit.clear()
        self.ui.usuarioEdit.clear()
        self.ui.senhaEdit.clear()
        self.ui.senhaEdit_2.clear()
        self.ui.senhaEdit_3.clear()
        self.ui.senhaEdit_4.clear()

    def altera(self):
        try:
            id = self.seleciona_id_banco()
            nome = self.ui.nomeEdit.text().upper()
            usuario = self.ui.usuarioEdit.text().upper()
            senha1 = self.ui.senhaEdit.text().upper()
            senha2 = self.ui.senhaEdit_2.text().upper()
            senha3 = self.ui.senhaEdit_3.text().upper()
            conexao = Conexao.crinado_conexao()
            cursor = conexao.cursor()
            comando = f"""UPDATE usuario SET nome = '{nome}', usuario = '{usuario}', senha1 = '{senha1}', senha2 = '{senha2}', senha3 = '{senha3}' where id_usuario = {id}"""
            cursor.execute(comando)
            cursor.commit()
        except:
            mBox = QMessageBox.information(self,"AVISO!!", "Falha ao aleterar Usuário!")
        else: 
            mBox = QMessageBox.information(self,"AVISO!!", "Usuário alterado com sucesso!")
            self.usuarios()
        
    def gerar_senha(self):
        senhaStr = Gerador.gera_senha()
        self.ui.senhaEdit_4.clear()
        self.ui.senhaEdit_4.insert(senhaStr)

