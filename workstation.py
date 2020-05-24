# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workstation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Workstation(object):
    def setupUi(self, Workstation,text):
        Workstation.setObjectName("Workstation")
        Workstation.resize(784, 564)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        Workstation.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Workstation)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QFrame(Workstation)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_settings = QtWidgets.QPushButton(self.main_frame)
        self.lbl_settings.setObjectName("lbl_settings")
        self.gridLayout_3.addWidget(self.lbl_settings, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.btn_back = QtWidgets.QPushButton(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_3.addWidget(self.btn_back, 0, 0, 1, 1)
        self.Auto_frm = QtWidgets.QFrame(self.main_frame)
        self.Auto_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Auto_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Auto_frm.setObjectName("Auto_frm")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Auto_frm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Program_frm = QtWidgets.QFrame(self.Auto_frm)
        self.Program_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Program_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Program_frm.setObjectName("Program_frm")
        self.gridLayout = QtWidgets.QGridLayout(self.Program_frm)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_go_app = QtWidgets.QPushButton(self.Program_frm)
        self.btn_go_app.setObjectName("btn_go_app")
        self.gridLayout.addWidget(self.btn_go_app, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_app = QtWidgets.QLabel(self.Program_frm)
        self.lbl_app.setObjectName("lbl_app")
        self.gridLayout.addWidget(self.lbl_app, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.lst_app = QtWidgets.QListWidget(self.Program_frm)
        self.lst_app.setObjectName("lst_app")
        self.gridLayout.addWidget(self.lst_app, 3, 1, 2, 2)
        self.horizontalLayout_2.addWidget(self.Program_frm)
        self.Website_frm = QtWidgets.QFrame(self.Auto_frm)
        self.Website_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Website_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Website_frm.setObjectName("Website_frm")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Website_frm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_web = QtWidgets.QLabel(self.Website_frm)
        self.lbl_web.setObjectName("lbl_web")
        self.gridLayout_2.addWidget(self.lbl_web, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.btn_go_web = QtWidgets.QPushButton(self.Website_frm)
        self.btn_go_web.setObjectName("btn_go_web")
        self.gridLayout_2.addWidget(self.btn_go_web, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.lst_web = QtWidgets.QListWidget(self.Website_frm)
        self.lst_web.setObjectName("lst_web")
        self.gridLayout_2.addWidget(self.lst_web, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.Website_frm)
        self.gridLayout_3.addWidget(self.Auto_frm, 1, 0, 1, 3)
        self.lbl_head = QtWidgets.QLabel(self.main_frame)
        self.lbl_head.setObjectName("lbl_head")
        self.gridLayout_3.addWidget(self.lbl_head, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.main_frame)

        self.retranslateUi(Workstation,text)
        QtCore.QMetaObject.connectSlotsByName(Workstation)

    def retranslateUi(self, Workstation,text):
        _translate = QtCore.QCoreApplication.translate
        Workstation.setWindowTitle(_translate("Workstation", "Form"))
        self.lbl_settings.setText(_translate("Workstation", "Settings"))
        self.btn_back.setText(_translate("Workstation", "Back"))
        self.btn_go_app.setText(_translate("Workstation", "Go"))
        self.lbl_app.setText(_translate("Workstation", "Applications"))
        self.lbl_web.setText(_translate("Workstation", "Websites"))
        self.btn_go_web.setText(_translate("Workstation", "Go"))
        self.lbl_head.setText(_translate("Workstation", text))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Workstation = QtWidgets.QWidget()
    ui = Ui_Workstation()
    ui.setupUi(Workstation)
    Workstation.show()
    sys.exit(app.exec_())
