import sys
import pandas as pd

from AnaliseDados.template6 import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import QtWidgets

class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Variável para receber os retornos do dataframe df das funções
        self.df = ""
        self.arq = ""
        self.analises = ""
        self.valor_barra = 0
        self.incremento_barra = 25

        # Botões
        self.btn_salvar.clicked.connect(self.salvar_arq)
        self.btn_abrir.clicked.connect(self.abrir_arq)
        self.btn_qtd_colunas.clicked.connect(self.qtd_colunas)
        self.btn_nome_colunas.clicked.connect(self.nome_colunas)
        self.btn_value_counts.clicked.connect(self.value_counts)
        self.btn_exibe_linha.clicked.connect(self.exibe_linha)
        self.btn_fechar.clicked.connect(self.fechar_programa)

        # setEnable
        self.btn_salvar.setEnabled(False)
        self.btn_qtd_colunas.setEnabled(False)
        self.btn_nome_colunas.setEnabled(False)
        self.btn_value_counts.setEnabled(False)
        self.btn_exibe_linha.setEnabled(False)

    def abrir_arq(self):
        try:

            if not self.radio_excel.isChecked() and not self.radio_csv.isChecked() and not self.radio_outros.isChecked():
                info = "É obrigatória a marcação de um tipo de arquivo"
                QMessageBox.about(janela, "Alerta", info)
            elif self.radio_outros.isChecked():
                info = "Somente conseguimos trabalhar com excel e csv"
                QMessageBox.about(janela, "Alerta", info)
            else:

                self.analises = ""
                self.valor_barra = 0
                self.progressBar.setValue(self.valor_barra)
                self.label_qtd.setText("")
                self.label_colunas.setText("")
                self.label_resultados.setText("")
                self.input_coluna.setText("")
                self.input_linha.setText("")

                # Abertura de arquivo do computador
                arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]

                with open(arquivo, 'r', encoding='utf-8') as self.arq:
                    if self.radio_excel.isChecked():
                        self.df = pd.read_excel(self.arq)
                    elif self.radio_csv.isChecked():
                        self.df = pd.read_csv(self.arq)

                self.label_nome_arq.setText(self.arq.name)

                self.btn_salvar.setEnabled(False)
                self.btn_qtd_colunas.setEnabled(True)
                self.btn_nome_colunas.setEnabled(True)
                self.btn_value_counts.setEnabled(True)
                self.btn_exibe_linha.setEnabled(True)

                return self.df, self.arq, self.valor_barra

        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def nome_colunas(self):
        try:
            nome_colunas = f"O nome das colunas são os seguintes: {self.df.columns}"

            self.label_colunas.setText(nome_colunas)

            self.analises += f"Arquivo: {self.arq.name}\n\n"
            self.analises += f"{nome_colunas}\n\n"

            self.valor_barra += self.incremento_barra
            self.progressBar.setValue(self.valor_barra)
            self.btn_salvar.setEnabled(True)

            return self.df

        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def qtd_colunas(self):
        try:
            shape = f"O arquivo importado possui {self.df.shape[0]} linhas e {self.df.shape[1]} colunas."
            self.label_qtd.setText(shape)
            self.analises += f"{shape}\n\n"

            self.valor_barra += self.incremento_barra
            self.progressBar.setValue(self.valor_barra)
            self.btn_salvar.setEnabled(True)

        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def value_counts(self):
        try:
            nome_coluna = self.input_coluna.text()
            resultado = self.df[nome_coluna].value_counts()
            resultado = str(resultado)
            self.label_resultados.setText(resultado)

            #plt.plot(self.df[nome_coluna].value_counts())
            #plt.savefig("grafico-value_counts.png")
            #im = plt.imread("grafico-value_counts.png")
            #res = resize(im, (5, 5))
            #plt.show()
            #plt.savefig("grafico-value_counts.png")

            #self.label_grafico.setPixmap(QtGui.QPixmap(r"C:\Users\vinic\Documents\Crud\AnaliseDados\grafico-value_counts.png"))

            self.analises += f"{resultado}\n\n"

            self.valor_barra += self.incremento_barra
            self.progressBar.setValue(self.valor_barra)
            self.btn_salvar.setEnabled(True)

        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def exibe_linha(self):
        try:
            indice_linha = self.input_linha.text()
            if indice_linha == "":
                self.input_linha.setText("0")
                indice_linha = 0

            indice_linha = int(indice_linha)
            resultado = self.df.loc[indice_linha]
            resultado = str(resultado)
            self.label_resultados.setText(resultado)

            self.analises += f"{resultado}\n\n"

            self.valor_barra += self.incremento_barra
            self.progressBar.setValue(self.valor_barra)
            self.btn_salvar.setEnabled(True)

        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def salvar_arq(self):
        try:
            arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
            print(arquivo)

            with open(arquivo + '.txt', 'w') as arq:
                arq.write(self.analises)
        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")

    def fechar_programa(self):
        try:
            sys.exit()
        except Exception as e:
            print(f"Erro capturado: {e}")
            QMessageBox.about(janela, "Erro", f"{e}")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    qt.exec()
