import PyQt5, sys, os # Python files
import menu, settings, workstation, controller# App Files
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

'''
====================================================================================
							Utility Functions and classes
====================================================================================
'''

class function_pack():
	# I dont really need this class anymore but it does make my code more self_explanatory
	# when reading other modules so I'll keep it 
	def __init__(self, function):
		'''
		 A class built to store functions passed down to widgets/forms 
		 so they can navigate their way back to this central form
		'''
		self.function = function
		self.render_menu = lambda: self.function(0)
		self.render_workspace =  lambda: self.function(1)
		self.render_settings = lambda: self.function(2)

'''
=================================================================================
									The Actual File
=================================================================================
'''

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window,self).__init__(*args, **kwargs)
		self.Stack = QStackedWidget()

		self.menu_frm = menu.MenuWidget(self.prep_widgets)
		self.workspace = None
		self.settings = None

		self.Stack.addWidget(self.menu_frm)

		self.setCentralWidget(self.Stack)
		self.render()
		self.showMaximized()

		self.setStyleSheet(open('app.css').read())	

	def prep_widgets(self):

		self.workspace = workstation.App_Form()
		self.settings = settings.App_Form()
		self.Stack.addWidget(self.workspace)
		self.Stack.addWidget(self.settings)

		fn_pack = function_pack(self.render) 

		self.workspace.set_fn_pack(fn_pack)
		self.settings.set_fn_pack(fn_pack)

		fn_pack.render_workspace()

	def render(self, i=0):

		self.Stack.setCurrentIndex(i)

		# if you switch to the workspace
		# refresh the workspace widget
		if i == 1:
			self.workspace.display()
		# if you switch back to the meny 
		# refresh the menu widget
		if i == 0:
			# Except I don't know how to refresh the menu widget without taking it of the stack widget
			controller.TbWorkspace.log_off()
			# Need to refresh the workspaces, and settings
			if (self.workspace or self.settings):
				self.workspace.setParent(None)
				self.settings.setParent(None)

	def set_workspace(self, widget):	
		self.workspace = widget

	def set_settings(self, widget):
		self.settings = widget

def main():
	myApp = QApplication(sys.argv)
	myApp.setApplicationName('Workflow')

	win = Window()
	win.show()
	sys.exit(myApp.exec_())

if __name__ == '__main__':
	main()