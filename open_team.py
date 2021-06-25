# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_team.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect('fantasy.db')
cur = conn.cursor()


class Ui_OpenTeam(object):

    def openteam(self):
        cur.execute("select distinct name from teams;")
        result = cur.fetchall()
        for t in result:
            self.comboOpenTeam.addItem(t[0].replace("!", "'"))

    def setupUi(self, OpenTeam):
        OpenTeam.setObjectName("OpenTeam")
        OpenTeam.resize(320, 240)
        OpenTeam.setStyleSheet("QDialog{\n"
                               "background-color:rgb(180, 180, 180)\n"
                               "}\n"
                               "QComboBox{\n"
                               "background-color:rgb(255, 255, 255)\n"
                               "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(OpenTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboOpenTeam = QtWidgets.QComboBox(OpenTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboOpenTeam.setFont(font)
        self.comboOpenTeam.setObjectName("comboOpenTeam")
        self.comboOpenTeam.addItem("")
        self.verticalLayout.addWidget(self.comboOpenTeam)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.btnOpenTeam = QtWidgets.QPushButton(OpenTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnOpenTeam.setFont(font)
        self.btnOpenTeam.setObjectName("btnOpenTeam")
        self.verticalLayout.addWidget(self.btnOpenTeam)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(OpenTeam)
        QtCore.QMetaObject.connectSlotsByName(OpenTeam)

    def retranslateUi(self, OpenTeam):
        _translate = QtCore.QCoreApplication.translate
        OpenTeam.setWindowTitle(_translate("OpenTeam", "Open Team"))
        self.label.setText(_translate("OpenTeam", "Select Team to Open"))
        self.comboOpenTeam.setItemText(
            0, _translate("OpenTeam", "Select Team"))
        self.btnOpenTeam.setText(_translate("OpenTeam", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenTeam = QtWidgets.QDialog()
    ui = Ui_OpenTeam()
    ui.setupUi(OpenTeam)
    OpenTeam.show()
    sys.exit(app.exec_())
