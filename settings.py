# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import App
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon 

class Ui_Settings(object):
    def setupUi(self, Settings):
        # apps are the available apps the user has on their computer and
        # app list are the apps the user would run in the current workspace
        self.apps = App.check_file('exe.txt')
        self.app_lst = App.check_file('apps.txt')

        self.apps = [app for app in self.apps if not(app in self.app_lst)]
        self.webs = App.check_file('websites.txt')

        Settings.setObjectName("Settings")
        Settings.resize(798, 648)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(16)
        Settings.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frm = QtWidgets.QFrame(Settings)
        self.main_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frm.setObjectName("main_frm")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.main_frm)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.header_frm = QtWidgets.QFrame(self.main_frm)
        self.header_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frm.setObjectName("header_frm")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(self.header_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.lblHead = QtWidgets.QLabel(self.header_frm)
        self.lblHead.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHead.setObjectName("lblHead")
        self.horizontalLayout.addWidget(self.lblHead, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.header_frm, 0,0,1,3)
        self.web_frm = QtWidgets.QFrame(self.main_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_frm.sizePolicy().hasHeightForWidth())
        self.web_frm.setSizePolicy(sizePolicy)
        self.web_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.web_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.web_frm.setObjectName("web_frm")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.web_frm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.web_frm)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.btnAdd_url = QtWidgets.QPushButton(self.web_frm)
        self.btnAdd_url.setObjectName("btnAdd_url")
        self.gridLayout_2.addWidget(self.btnAdd_url, 4, 3, 1, 1)
        self.lblWeb = QtWidgets.QLabel(self.web_frm)
        self.lblWeb.setObjectName("lblWeb")
        self.gridLayout_2.addWidget(self.lblWeb, 0, 0, 2, 3, QtCore.Qt.AlignHCenter)
        self.lstWeb = QtWidgets.QListWidget(self.web_frm)
        self.lstWeb.setObjectName("lstWeb")
        self.gridLayout_2.addWidget(self.lstWeb, 5, 0, 1, 3)
        self.edtUrl = QtWidgets.QLineEdit(self.web_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtUrl.sizePolicy().hasHeightForWidth())
        self.edtUrl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(13)
        self.edtUrl.setFont(font)
        self.edtUrl.setObjectName("edtUrl")
        self.gridLayout_2.addWidget(self.edtUrl, 4, 1, 1, 1)
        self.btnRemove_web = QtWidgets.QPushButton(self.web_frm)
        self.btnRemove_web.setObjectName("btnRemove_web")
        self.gridLayout_2.addWidget(self.btnRemove_web, 5, 3, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_5.addWidget(self.web_frm, 1, 1, 1, 1)
        self.app_frm = QtWidgets.QFrame(self.main_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_frm.sizePolicy().hasHeightForWidth())
        self.app_frm.setSizePolicy(sizePolicy)
        self.app_frm.setMinimumSize(QtCore.QSize(363, 0))
        self.app_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_frm.setObjectName("app_frm")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.app_frm)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnFind = QtWidgets.QPushButton(self.app_frm)
        self.btnFind.setObjectName("btnFind")
        self.gridLayout_4.addWidget(self.btnFind, 3, 2, 1, 1, QtCore.Qt.AlignBottom)
        self.btnAdd_app = QtWidgets.QPushButton(self.app_frm)
        self.btnAdd_app.setObjectName("btnAdd_app")
        self.gridLayout_4.addWidget(self.btnAdd_app, 1, 2, 1, 1)
        self.lstApp = QtWidgets.QListWidget(self.app_frm)
        self.lstApp.setObjectName("lstApp")
        self.gridLayout_4.addWidget(self.lstApp, 2, 0, 2, 2)
        self.lblApp = QtWidgets.QLabel(self.app_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApp.sizePolicy().hasHeightForWidth())
        self.lblApp.setSizePolicy(sizePolicy)
        self.lblApp.setObjectName("lblApp")
        self.gridLayout_4.addWidget(self.lblApp, 1, 0, 1, 1)
        self.btnRemove_app = QtWidgets.QPushButton(self.app_frm)
        self.btnRemove_app.setObjectName("btnRemove_app")
        self.gridLayout_4.addWidget(self.btnRemove_app, 2, 2, 1, 1, QtCore.Qt.AlignTop)
        self.lbl_app = QtWidgets.QLabel(self.app_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_app.sizePolicy().hasHeightForWidth())
        self.lbl_app.setSizePolicy(sizePolicy)
        self.lbl_app.setObjectName("lbl_app")
        self.gridLayout_4.addWidget(self.lbl_app, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.cmbxApp = QtWidgets.QComboBox(self.app_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbxApp.sizePolicy().hasHeightForWidth())
        self.cmbxApp.setSizePolicy(sizePolicy)
        self.cmbxApp.setObjectName("cmbxApp")
        self.gridLayout_4.addWidget(self.cmbxApp, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.app_frm, 1, 2, 1, 1)
        self.btnOptions = QtWidgets.QFrame(self.main_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOptions.sizePolicy().hasHeightForWidth())
        self.btnOptions.setSizePolicy(sizePolicy)
        self.btnOptions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnOptions.setObjectName("btnOptions")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.btnOptions)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnHelp = QtWidgets.QPushButton(self.btnOptions)
        self.btnHelp.setObjectName("btnHelp")
        self.gridLayout_6.addWidget(self.btnHelp, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.gridLayout_5.addWidget(self.btnOptions, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.main_frm, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        self.setupSignals()
        QtCore.QMetaObject.connectSlotsByName(Settings)

        return self.btn_back

    def get_Applications(self):
        return self.apps + self.app_lst, self.app_lst

    def get_Websites(self):
        return self.webs

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.btn_back.setText(_translate("Settings", "Back"))
        self.lblHead.setText(_translate("Settings", "Settings"))
        self.label.setText(_translate("Settings", "url:"))
        self.btnAdd_url.setText(_translate("Settings", "Add"))
        self.lblWeb.setText(_translate("Settings", "Website"))
        self.edtUrl.setPlaceholderText(_translate("Settings", "http://google.com"))
        self.btnRemove_web.setText(_translate("Settings", "Remove"))
        self.btnFind.setText(_translate("Settings", "Find"))
        self.btnAdd_app.setText(_translate("Settings", "Add"))
        self.lblApp.setText(_translate("Settings", "App:"))
        self.btnRemove_app.setText(_translate("Settings", "Remove"))
        self.lbl_app.setText(_translate("Settings", "Programs"))
        self.btnHelp.setText(_translate("Settings", "Help"))
    
    def setupSignals(self):
        # setup the cmbx, lstWeb and lstApp
        self.cmbxApp.addItems(self.apps)
        self.lstApp.addItems(self.app_lst)
        self.lstWeb.addItems(self.webs)

        # Disable remove buttons as they nothing is selected
        self.btnRemove_app.setEnabled(False)
        self.btnRemove_web.setEnabled(False)

        # Enabled buttons when they are 
        self.lstWeb.itemActivated.connect(lambda: self.btnRemove_web.setEnabled(True))
        self.lstApp.itemActivated.connect(lambda: self.btnRemove_app.setEnabled(True))

        # setup btn removal of application/websites
        self.btnRemove_web.clicked.connect(self.remove_url)
        self.btnRemove_app.clicked.connect(self.remove_app)

        # setup addition of application/websites 
        self.btnAdd_url.clicked.connect(self.Add_url)
        self.btnAdd_app.clicked.connect(self.Add_app)

        # display help
        self.btnHelp.clicked.connect(self.show_help)

        # look for more applications on system
        self.btnFind.clicked.connect(self.find_apps)

    def show_help(self):
        mssg = QMessageBox()
        mssg.setWindowTitle('How to add Applicatons')
        mssg.setText('Click on find to look for applications in your systems to add to list of available application option')
        mssg.setIcon(QMessageBox.Information)
        mssg.setStandardButtons(QMessageBox.Ok)

        value = mssg.exec_() 

    def Add_url(self):
        url = self.edtUrl.text()
        self.edtUrl.clear()
        self.lstWeb.clear()
        self.webs.append(url)
        self.lstWeb.addItems(self.webs)

    def Add_app(self):
        if self.cmbxApp.count():
            app = self.cmbxApp.currentText()
            self.apps.remove(app)
            self.cmbxApp.clear()
            self.cmbxApp.addItems(self.apps)

            self.app_lst.append(app)
            self.lstApp.addItem(app)
    
    def remove_url(self):
        self.webs = []
        for i in range(self.lstWeb.count()):
            li = self.lstWeb.item(i)
            if not(li.isSelected()):
                self.webs.append(li.text())

        self.lstWeb.clear()
        self.lstWeb.addItems(self.webs)

    def remove_app(self):
        for i in range(self.lstApp.count()):
            li = self.lstApp.item(i)

            if li.isSelected():
                app = li.text()
                self.cmbxApp.addItem(app)
                self.apps.append(app)
                self.app_lst.remove(app)

        self.lstApp.clear()
        self.lstApp.addItems(self.app_lst)

    def find_apps(self):
        filename = QFileDialog.getOpenFileName(self.main_frm, 'Select executable File', '/', 'executables(*.exe)')[0]
        
        # Don't add exetubles that already exists between the two lists
        if not(app in self.apps or app in self.app_lst):
            self.apps.append(filename)
            self.cmbxApp.addItems(self.apps) 
            App.save_file('exe.txt', self.apps)

        else:
            pass
            # A pop notification to say that the app is already available in the combox


class App_Form(QWidget):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_Settings()
        self.btn_back = self.ui.setupUi(self)
        self.fn_pack = []

    def set_fn_pack(self,fn_pack):
        self.fn_pack = fn_pack
        self.btn_back.clicked.connect(self.closeEvent)

    def closeEvent(self, event):

        self.save_and_exit()

        if event:
            event.accept()
        else:
            self.fn_pack.render_workspace()

    def save_and_exit(self):
        # all the save code
        apps, app_lst = self.ui.get_Applications()
        webs = self.ui.get_Websites()

        App.save_file('exe.txt', apps)
        App.save_file('apps.txt', app_lst)
        App.save_file('websites.txt', webs)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = App_Form('Todo. Implement settings for multiple workspaces')
    settings.set_fn_pack('psych')
    settings.show()
    sys.exit(app.exec_())