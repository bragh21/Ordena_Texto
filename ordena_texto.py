# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, 
                             QPushButton, QGroupBox, QTextEdit, QRadioButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect 
# import subprocess  Para função copiar

class TelaPrincipal:
    def __init__(self) -> None:
        self.janela = QMainWindow()
        self.widget_principal = QWidget(self.janela)

        self.gb_opc_ordenacao = QGroupBox(self.widget_principal)
        self.rb_ord_crescente = QRadioButton(self.gb_opc_ordenacao)
        self.rb_ord_decrescente = QRadioButton(self.gb_opc_ordenacao)

        self.gb_entrada = QGroupBox(self.widget_principal)
        self.texto_desordenado = QTextEdit(self.gb_entrada)
        self.btn_ordenar = QPushButton(self.gb_entrada)
        self.btn_limpar = QPushButton(self.gb_entrada)

        self.gp_saida = QGroupBox(self.widget_principal)
        self.btn_copiar_texto = QPushButton(self.gp_saida)
        self.texto_ordenado = QTextEdit(self.gp_saida)
        
        self.setupUi()
        self.mostra_tela()

    def setupUi(self):
        self.janela.setWindowIcon(QIcon(u'D:\Repositorios_Separados_GITHUB\Ordena_Texto\icone_app.png'))
        self.janela.setWindowTitle("Ordenador de Texto")
        self.janela.setFixedSize(387, 665)
        self.janela.statusBar().showMessage("By Anderson Bragherolli, 2021") 

        # GroupBox Tipo de Ordenação
        self.gb_opc_ordenacao.setGeometry(QRect(20, 10, 341, 51))
        self.gb_opc_ordenacao.setTitle("Ordenação:")
        self.rb_ord_crescente.setGeometry(QRect(20, 20, 89, 20))
        self.rb_ord_crescente.setText("Crescente")
        self.rb_ord_crescente.setChecked(True)
        self.rb_ord_decrescente.setGeometry(QRect(190, 20, 89, 20))
        self.rb_ord_decrescente.setText("Decrescente")

        # GroupBox Entrada de Dados
        self.gb_entrada.setGeometry(QRect(20, 70, 341, 271))
        self.gb_entrada.setTitle("Entre com o texto a ser ordenado:")
        self.texto_desordenado.setGeometry(QRect(13, 20, 311, 201))
        self.btn_ordenar.setGeometry(QRect(230, 230, 91, 24))
        self.btn_ordenar.setText("Ordenar")
        self.btn_ordenar.clicked.connect(self.ordena_texto) # Link to EventHandler
        self.btn_limpar.setGeometry(QRect(10, 230, 91, 24))
        self.btn_limpar.setText("Limpar")
        self.btn_limpar.clicked.connect(self.limpar) # Link to EventHandler
        
        # GroupBox Saida
        self.gp_saida.setGeometry(QRect(20, 360, 341, 281))
        self.gp_saida.setTitle("Resultado:")
        self.btn_copiar_texto.setDisabled(True)
        self.btn_copiar_texto.setGeometry(QRect(230, 30, 91, 24))
        self.btn_copiar_texto.setText("Copiar")
        self.btn_copiar_texto.clicked.connect(self.copiar_texto) # Link to EventHandler
        self.texto_ordenado.setGeometry(QRect(10, 60, 311, 211))
        self.texto_ordenado.setReadOnly(True)

        self.janela.setCentralWidget(self.widget_principal)
        
    def mostra_tela(self):
        self.janela.show()

    def ordena_texto(self):
        
        if self.rb_ord_crescente.isChecked():
            texto_desord = str(self.texto_desordenado.toPlainText()).strip()
            texto_desord = texto_desord.split(u'\n')
            texto_desord.sort()

            self.texto_ordenado.setText(u"\n".join(texto_desord))
        elif self.rb_ord_decrescente.isChecked():
            texto_desord = str(self.texto_desordenado.toPlainText()).strip()
            texto_desord = texto_desord.split(u'\n')
            texto_desord.sort(reverse=True)
            self.texto_ordenado.setText(u"\n".join(texto_desord))

    def copiar_texto(self):
        # txt = str(self.texto_ordenado.toPlainText())
        # cmd = f'echo "{txt.strip()}"|clip'
        # print(cmd)
        # subprocess.call(cmd, shell=True)
        pass

    def limpar(self):
        self.texto_desordenado.setText("")
        self.texto_ordenado.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = TelaPrincipal()
    sys.exit(app.exec_())
