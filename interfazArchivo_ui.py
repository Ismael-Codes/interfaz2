# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazArchivo.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(self.centralwidget)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNombre)

        self.lineEditNombre = QLineEdit(self.centralwidget)
        self.lineEditNombre.setObjectName(u"lineEditNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEditNombre)

        self.labelApellido = QLabel(self.centralwidget)
        self.labelApellido.setObjectName(u"labelApellido")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelApellido)

        self.lineEditApellido = QLineEdit(self.centralwidget)
        self.lineEditApellido.setObjectName(u"lineEditApellido")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEditApellido)

        self.labelMatricula = QLabel(self.centralwidget)
        self.labelMatricula.setObjectName(u"labelMatricula")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelMatricula)

        self.lineEditMatricula = QLineEdit(self.centralwidget)
        self.lineEditMatricula.setObjectName(u"lineEditMatricula")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEditMatricula)

        self.labelTelefono = QLabel(self.centralwidget)
        self.labelTelefono.setObjectName(u"labelTelefono")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelTelefono)

        self.lineEditTelefono = QLineEdit(self.centralwidget)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEditTelefono)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.horizontalLayout.addWidget(self.btnGuardar)

        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.horizontalLayout.addWidget(self.btnLimpiar)

        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")

        self.horizontalLayout.addWidget(self.btnSalir)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro de Estudiantes", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.labelApellido.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.labelMatricula.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.labelTelefono.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"&Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"&Limpiar", None))
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"&Salir", None))
    # retranslateUi

