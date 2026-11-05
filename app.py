import sys

import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog
)
#deivid fork
from principal import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.botonAbrir.clicked.connect(self.abrir_archivo)
        self.botonComando.clicked.connect(self.ejecutarComando)

    def ejecutarComando(self):

        resultado = subprocess.run(["ls"], capture_output=True, text=True, shell=True)

        print(resultado.stdout)
        self.salidaConsola.setPlainText(resultado.stdout)

    def abrir_archivo(self):

        archivo, _ = QFileDialog.getOpenFileName(            self,
            "Abrir archivo",
            "",
            "Archivos de texto (*.ism)"
        )

        if archivo:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()

            self.cajaTexto.setPlainText(contenido)
            self.statusbar.showMessage(f"Archivo abierto: {archivo}")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())