from PySide6.QtWidgets import QMainWindow, QMessageBox

from interfazArchivo_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.btnGuardar.clicked.connect(self.guardarDatos)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnSalir.clicked.connect(self.close)

    def guardarDatos(self):
        nombre = self.lineEditNombre.text().strip()
        apellido = self.lineEditApellido.text().strip()
        matricula = self.lineEditMatricula.text().strip()
        telefono = self.lineEditTelefono.text().strip()

        # Validar que no haya campos vacíos
        if nombre == "" or apellido == "" or matricula == "" or telefono == "":
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Por favor, llena todos los campos.",
            )
            return

        # Guardar en el archivo de texto (modo "a" = agrega al final)
        with open("datos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"Nombre: {nombre} | Apellido: {apellido} | "
                f"Matricula: {matricula} | Telefono: {telefono}\n"
            )

        QMessageBox.information(
            self,
            "Guardado",
            "Los datos se guardaron correctamente.",
        )
        self.statusbar.showMessage("Datos guardados en datos.txt", 3000)
        self.limpiarCampos()

    def limpiarCampos(self):
        self.lineEditNombre.clear()
        self.lineEditApellido.clear()
        self.lineEditMatricula.clear()
        self.lineEditTelefono.clear()
        self.lineEditNombre.setFocus()