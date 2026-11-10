import sys
import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox
)

from principal2 import Ui_LoginWindow


class Window(QMainWindow, Ui_LoginWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)


        self.btnLogin.clicked.connect(self.abrir_archivo)

        # Acciones del menú y toolbar
        self.connectSignalsSlots()
    # --------------------------
    # ABRIR ARCHIVO
    # --------------------------
    def abrir_archivo(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            "",
            "Archivos de texto (*.ism);;Todos (*.*)"
        )

        if archivo:

            with open(
                archivo,
                "r",
                encoding="utf-8"
            ) as f:

                contenido = f.read()

            self.cajaTexto.setPlainText(
                contenido
            )

            self.statusbar.showMessage(
                f"Archivo abierto: {archivo}",
                5000
            )


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())