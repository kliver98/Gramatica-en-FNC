# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pasos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        self.tfPaso1 = QtWidgets.QTextEdit(Dialog)
        self.tfPaso1.setGeometry(QtCore.QRect(10, 10, 441, 281))
        self.tfPaso1.setObjectName("tfPaso1")
        self.tfPaso2 = QtWidgets.QTextEdit(Dialog)
        self.tfPaso2.setGeometry(QtCore.QRect(450, 10, 441, 281))
        self.tfPaso2.setObjectName("tfPaso2")
        self.tfPaso3 = QtWidgets.QTextEdit(Dialog)
        self.tfPaso3.setGeometry(QtCore.QRect(10, 290, 441, 281))
        self.tfPaso3.setObjectName("tfPaso3")
        self.tfPaso4 = QtWidgets.QTextEdit(Dialog)
        self.tfPaso4.setGeometry(QtCore.QRect(450, 290, 441, 281))
        self.tfPaso4.setObjectName("tfPaso4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(301, 263, 150, 28))
        self.pushButton.setStyleSheet("")
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(741, 263, 150, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(301, 543, 150, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(741, 543, 150, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pasos seguidos para generar gramática en FNC"))
        self.pushButton.setText(_translate("Dialog", "Paso 1 - Terminales"))
        self.pushButton_2.setText(_translate("Dialog", "Paso 2 - No alcanzables"))
        self.pushButton_3.setText(_translate("Dialog", "Paso 3 - Prod. Lamba"))
        self.pushButton_4.setText(_translate("Dialog", "Paso 4 - Unitarias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
