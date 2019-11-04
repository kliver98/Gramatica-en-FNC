# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Root(object):
    def setupUi(self, Root):
        Root.setObjectName("Root")
        Root.resize(1000, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Root)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 510, 961, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAyuda = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAyuda.setMinimumSize(QtCore.QSize(0, 40))
        self.btnAyuda.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAyuda.setFont(font)
        self.btnAyuda.setObjectName("btnAyuda")
        self.horizontalLayout.addWidget(self.btnAyuda)
        self.btnCargarDatos = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCargarDatos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCargarDatos.setFont(font)
        self.btnCargarDatos.setObjectName("btnCargarDatos")
        self.horizontalLayout.addWidget(self.btnCargarDatos)
        self.btnLimpiar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLimpiar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.horizontalLayout.addWidget(self.btnLimpiar)
        self.btnResolver = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnResolver.setMinimumSize(QtCore.QSize(0, 40))
        self.btnResolver.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnResolver.setFont(font)
        self.btnResolver.setObjectName("btnResolver")
        self.horizontalLayout.addWidget(self.btnResolver)
        self.btnPasos = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPasos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnPasos.setFont(font)
        self.btnPasos.setObjectName("btnPasos")
        self.horizontalLayout.addWidget(self.btnPasos)
        self.tfGramatica = QtWidgets.QTextEdit(Root)
        self.tfGramatica.setGeometry(QtCore.QRect(20, 60, 441, 431))
        self.tfGramatica.setObjectName("tfGramatica")
        self.label = QtWidgets.QLabel(Root)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tfFNC = QtWidgets.QTextEdit(Root)
        self.tfFNC.setEnabled(True)
        self.tfFNC.setGeometry(QtCore.QRect(470, 60, 511, 431))
        self.tfFNC.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tfFNC.setReadOnly(True)
        self.tfFNC.setObjectName("tfFNC")
        self.pushButton = QtWidgets.QPushButton(Root)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(782, 29, 200, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Root)
        QtCore.QMetaObject.connectSlotsByName(Root)

    def retranslateUi(self, Root):
        _translate = QtCore.QCoreApplication.translate
        Root.setWindowTitle(_translate("Root", "Generar gramática en FNC a partir de una GIC G - Por Joe & Kliver"))
        self.btnAyuda.setText(_translate("Root", "Ayuda"))
        self.btnCargarDatos.setText(_translate("Root", "Cargar datos de archivo"))
        self.btnLimpiar.setText(_translate("Root", "Limpiar datos introducidos"))
        self.btnResolver.setText(_translate("Root", "Resolver"))
        self.btnPasos.setText(_translate("Root", "Mostrar pasos"))
        self.label.setText(_translate("Root", "Inserte la gramática en el recuadro de abajo"))
        self.tfFNC.setHtml(_translate("Root", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Root", "Forma Normal de Chomsky"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Root = QtWidgets.QDialog()
    ui = Ui_Root()
    ui.setupUi(Root)
    Root.show()
    sys.exit(app.exec_())
