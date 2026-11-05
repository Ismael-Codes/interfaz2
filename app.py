import sys

from PySide6.QtWidgets import (
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
        self.setWindowTitle("Editor de archivos")
        self.archivo_actual = None

        self.action_New.triggered.connect(self.nuevo_archivo)
        self.actionOpen.triggered.connect(self.abrir_archivo)
        self.actionSave.triggered.connect(self.guardar_archivo)
        self.actionExit.triggered.connect(self.close)
        self.actionCopy.triggered.connect(self.plainTextEdit.copy)
        self.actionPaste.triggered.connect(self.plainTextEdit.paste)
        self.actionCut.triggered.connect(self.plainTextEdit.cut)
        self.actionAbout.triggered.connect(self.acerca_de)

    def nuevo_archivo(self):
        self.plainTextEdit.clear()
        self.archivo_actual = None
        self.statusbar.showMessage("Archivo nuevo")

    def abrir_archivo(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            "",
            "Archivos de texto (*.ism)"
        )

        if archivo:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()

            self.plainTextEdit.setPlainText(contenido)
            self.archivo_actual = archivo
            self.statusbar.showMessage(f"Archivo abierto: {archivo}")

    def guardar_archivo(self):

        archivo = self.archivo_actual
        if not archivo:
            archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo",
                "",
                "Archivos de texto (*.ism)"
            )

        if archivo:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(self.plainTextEdit.toPlainText())

            self.archivo_actual = archivo
            self.statusbar.showMessage(f"Archivo guardado: {archivo}")

    def acerca_de(self):
        QMessageBox.about(self, "Acerca de", "Editor de archivos")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
