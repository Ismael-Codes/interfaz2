import sys
import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox
)

from principal import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Habilitar toolbar
        self.toolBar.setEnabled(True)

        # Botones
        self.botonAbrir.clicked.connect(self.abrir_archivo)
        self.botonComando.clicked.connect(self.ejecutarComando)

        # Acciones del menú y toolbar
        self.connectSignalsSlots()

    def connectSignalsSlots(self):

        self.action_Crear.triggered.connect(
            self.crearArchivo
        )

        self.action_Copiar.triggered.connect(
            self.cajaTexto.copy
        )

        self.action_Cortar.triggered.connect(
            self.cajaTexto.cut
        )

        self.action_Pegar.triggered.connect(
            self.cajaTexto.paste
        )

        self.action_Acerca_de.triggered.connect(
            self.acercaDe
        )

    # --------------------------
    # NUEVO ARCHIVO
    # --------------------------
    def crearArchivo(self):

        self.cajaTexto.clear()

        self.cajaTexto.setFocus()

        self.statusbar.showMessage(
            "Nuevo archivo",
            3000
        )

    # --------------------------
    # ACERCA DE
    # --------------------------
    def acercaDe(self):

        QMessageBox.about(
            self,
            "Acerca de",
            "Editor de texto\nPyQt6"
        )

    # --------------------------
    # COMANDO DEL SISTEMA
    # --------------------------
    def ejecutarComando(self):

        resultado = subprocess.run(
            ["ls"],
            capture_output=True,
            text=True
        )

        self.salidaConsola.setPlainText(
            resultado.stdout
        )

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