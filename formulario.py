import csv
import os
import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget, QTableWidgetItem

BASE = Path(__file__).resolve().parent
DATOS = BASE / 'registros.txt'
CAMPOS = ('Nombre', 'Apellido', 'Matrícula', 'Teléfono')


class VentanaArchivos(QWidget):
    def __init__(self, volver):
        super().__init__()
        uic.loadUi(str(BASE / 'archivos.ui'), self)
        self.volver = volver
        self.tablaRegistros.setColumnCount(4)
        self.tablaRegistros.setHorizontalHeaderLabels(CAMPOS)
        self.tablaRegistros.horizontalHeader().setStretchLastSection(True)
        self.tablaRegistros.setSelectionBehavior(self.tablaRegistros.SelectionBehavior.SelectRows)
        self.btnVolver.clicked.connect(self.volver_al_formulario)
        self.btnRegistro.clicked.connect(self.volver_al_formulario)
        self.btnVerArchivos.clicked.connect(self.actualizar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.btnCarpetaRegistro.clicked.connect(self.actualizar)
        self.btnAbrirArchivo.clicked.connect(self.abrir_archivo)
        self.buscar.textChanged.connect(self.actualizar)

    def actualizar(self):
        self.tablaRegistros.setRowCount(0)
        if not DATOS.exists():
            return
        try:
            with DATOS.open('r', encoding='utf-8', newline='') as archivo:
                registros = list(csv.reader(archivo, delimiter='\t'))
            filtro = self.buscar.text().strip().casefold()
            for registro in registros:
                if len(registro) != 4 or (filtro and filtro not in ' '.join(registro).casefold()):
                    continue
                fila = self.tablaRegistros.rowCount()
                self.tablaRegistros.insertRow(fila)
                for columna, valor in enumerate(registro):
                    item = QTableWidgetItem(valor)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.tablaRegistros.setItem(fila, columna, item)
            self.tablaRegistros.resizeColumnsToContents()
        except OSError as error:
            QMessageBox.critical(self, 'Error al leer', str(error))

    def abrir_archivo(self):
        if not DATOS.exists():
            QMessageBox.information(self, 'Sin registros', 'Todavía no existe registros.txt. Guarda un estudiante primero.')
            return
        try:
            os.startfile(str(DATOS))  # Windows
        except (OSError, AttributeError) as error:
            QMessageBox.warning(self, 'No se pudo abrir', str(error))

    def volver_al_formulario(self):
        self.hide()
        self.volver.show()


class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(str(BASE / 'formulario.ui'), self)
        self.ventana_archivos = VentanaArchivos(self)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnVerArchivos.clicked.connect(self.ver_archivos)
        self.btnAccesoArchivos.clicked.connect(self.ver_archivos)
        self.btnRegistro.clicked.connect(lambda: None)

    def guardar(self):
        valores = [
            self.campo_nombre.text().strip(),
            self.campo_apellido.text().strip(),
            self.campo_matricula.text().strip(),
            self.campo_telefono.text().strip(),
        ]
        if not all(valores):
            QMessageBox.warning(self, 'Faltan datos', 'Completa los cuatro campos antes de guardar.')
            return
        if not valores[3].isdigit() or len(valores[3]) != 10:
            QMessageBox.warning(self, 'Teléfono incorrecto', 'Ingresa un teléfono de 10 dígitos.')
            return
        try:
            if DATOS.exists():
                with DATOS.open('r', encoding='utf-8', newline='') as archivo:
                    existentes = list(csv.reader(archivo, delimiter='\t'))
                if any(len(fila) == 4 and fila[2].casefold() == valores[2].casefold() for fila in existentes):
                    QMessageBox.warning(self, 'Matrícula duplicada', 'Ya hay un estudiante con esa matrícula.')
                    return
            # csv.writer con delimitador TAB conserva los campos incluso si tienen espacios.
            with DATOS.open('a', encoding='utf-8', newline='') as archivo:
                csv.writer(archivo, delimiter='\t').writerow(valores)
        except OSError as error:
            QMessageBox.critical(self, 'Error al guardar', str(error))
            return
        self.estado.setText('Registro guardado')
        QMessageBox.information(self, 'Guardado correctamente', 'Estudiante registrado en registros.txt.')
        self.limpiar()

    def limpiar(self):
        for campo in (self.campo_nombre, self.campo_apellido, self.campo_matricula, self.campo_telefono):
            campo.clear()
        self.campo_nombre.setFocus()

    def ver_archivos(self):
        self.ventana_archivos.actualizar()
        self.ventana_archivos.show()
        self.ventana_archivos.raise_()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Formulario()
    ventana.show()
    sys.exit(app.exec())
