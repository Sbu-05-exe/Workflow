# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import controller
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

class Ui_Settings(object):
   
    def setupUi(self, Settings):
        # apps are the available apps the user has on their computer and
        # app list are the apps the user would run in the current workspace
        self.workspace = controller.TbWorkspace.get_active_workspace()
    
        self.apps = controller.TbWebApps.get_apps()
        self.app_lst = controller.TbWorkAppSite.get_apps(self.workspace.id)
        
        # Have to filter out the apps from the app_lst so that there are no duplicates
        # In combobox and the list Widget
        appnames = [record.name for record in self.app_lst]
        self.apps = [record for record in self.apps if not(record.name in appnames)]

        self.webs = controller.TbWorkAppSite.get_webs(self.workspace.id)

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
        self.btnBack = QtWidgets.QPushButton(self.header_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
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
        self.gridLayout_4.addWidget(self.btnFind, 2, 2, 1, 1, QtCore.Qt.AlignTop)
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
        self.gridLayout_4.addWidget(self.btnRemove_app, 3, 2, 1, 1, QtCore.Qt.AlignBottom)
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
        self.btn_frm = QtWidgets.QFrame(self.main_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_frm.sizePolicy().hasHeightForWidth())
        self.btn_frm.setSizePolicy(sizePolicy)
        self.btn_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frm.setObjectName("btnDelete")
        self.Hbox_btn_frm = QtWidgets.QHBoxLayout(self.btn_frm)
        self.Hbox_btn_frm.setObjectName("Hbox_btn_frm")
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.Hbox_btn_frm.addItem(spacerItem)
        self.btnDelete = QtWidgets.QPushButton(self.btn_frm)
        self.btnDelete.setObjectName('btnDelete')
        self.Hbox_btn_frm.addWidget(self.btnDelete, 0,QtCore.Qt.AlignLeft)
        self.btnHelp = QtWidgets.QPushButton(self.btn_frm)
        self.btnHelp.setObjectName("btnHelp")
        self.Hbox_btn_frm.addWidget(self.btnHelp,0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addWidget(self.btn_frm, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.main_frm, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        self.setupSignals()
        QtCore.QMetaObject.connectSlotsByName(Settings)

        return self.btnBack, self.btnDelete

    def get_Applications(self):
        return self.apps + self.app_lst, self.app_lst

    def get_Websites(self):
        return self.webs

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.btnBack.setText(_translate("Settings", "Back"))
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
        self.btnDelete.setText(_translate("Settings", "Delete"))

    def setupSignals(self):

        # setup the cmbx, lstWeb and lstApp
        self.cmbxApp.addItems([record.name for record in self.apps])
        self.lstApp.addItems([record.name for record in self.app_lst])
        self.lstWeb.addItems([record.name for record in self.webs])

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
        mssg.setText('Click on "Find" to look for executables applications and add them to the list of available applications')
        mssg.setIcon(QMessageBox.Information)
        mssg.setStandardButtons(QMessageBox.Ok)

        value = mssg.exec_() 

    def Add_url(self):
        # 1 Get the text from the edtUrl
        # 2 Clear both edt and the listWeb
        # 3 Check if url is not already in the database
        # 4 Insert the name of the url into lstWeb

        url = self.edtUrl.text()
        self.edtUrl.clear()
        self.lstWeb.clear()

        record = controller.TbWebApps.insert_web(url)
        controller.TbWorkAppSite.insert_rec(self.workspace.id, record.AppsiteID)
        self.webs = controller.TbWorkAppSite.get_webs(self.workspace.id)
        self.lstWeb.addItems([query.name for query in self.webs])

    def Add_app(self):

        if self.cmbxApp.count():
            
            app = self.cmbxApp.currentText()

            for record in self.apps:
                
                if record.name == app:
                    
                    controller.TbWorkAppSite.insert_rec(self.workspace.id, str(record.AppsiteID))
                    self.apps.remove(record)
                    self.cmbxApp.clear()
                    self.cmbxApp.addItems([record.name for record in self.apps])
                    self.app_lst = controller.TbWorkAppSite.get_apps(self.workspace.id)
                    self.lstApp.addItem(app)
    
    def remove_url(self):

        #  1) Get the selected url
        #  2) Get its query record in self.webs and obtain its primary key
        #  3) Use the primary key to delete it from the TbWorkAppsite
        #  4) Refresh lstWeb
        for i in range(self.lstWeb.count()):
            
            li = self.lstWeb.item(i)
            
            if li.isSelected():
                
                for query in self.webs:

                    if query.name == li.text():

                        controller.TbWorkAppSite.del_record(query.id)

                        self.webs = controller.TbWorkAppSite.get_webs(self.workspace.id)
                        self.lstWeb.clear()
                        self.lstWeb.addItems([query.name for query in self.webs])

    def remove_app(self):
        
        for i in range(self.lstApp.count()):
            
            li = self.lstApp.item(i)

            if li.isSelected():

                app = li.text()
                
                for query in self.app_lst:
                    
                    if query.name == app:

                        controller.TbWorkAppSite.del_record(str(query.id))
                        self.app_lst.remove(query)
                        self.apps.append(query.get_record())
                        self.cmbxApp.addItem(app)

        self.lstApp.clear()
        self.lstApp.addItems([query.name for query in self.app_lst])

    def find_apps(self):
        
        filename = QFileDialog.getOpenFileName(self.main_frm, 'Select executable File', '/', 'executables(*.exe)')[0]
        
        # Don't add exetubles that already exists between the two lists
        if not((filename in self.apps) or (filename in self.app_lst)):
            
            new_record = controller.TbWebApps.insert_app(filename)
            print(new_record.name)
            self.apps.append(new_record)
            self.cmbxApp.addItem(self.apps[-1].name)

        else:
            pass
            # A pop notification to say that the app is already available in the combox

class App_Form(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_Settings()
        self.btnBack, self.btnDelete = self.ui.setupUi(self)
        self.fn_pack = None
        self.record = controller.TbWorkspace.get_active_workspace()

    def set_fn_pack(self,fn_pack):
        
        self.fn_pack = fn_pack
        self.btnBack.clicked.connect(self.fn_pack.render_workspace)
        self.btnDelete.clicked.connect(self.delete_workspace)

    def delete_workspace(self):
        
        mssg = QMessageBox()
        mssg.setWindowTitle('Delete Workspace')
        mssg.setText('Are you sure you want delete this workspace. You cannot undo these changes')
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)

        value = mssg.exec_()

        if (value == QMessageBox.Yes):
            
            record = controller.TbWorkspace.get_active_workspace()
            controller.TbWorkspace.del_workspace(record.id)
            os.startfile(App.py)
            sys.exit()

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = App_Form()
    # settings.set_fn_pack()
    settings.show()
    sys.exit(app.exec_())