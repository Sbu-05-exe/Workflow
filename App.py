import PyQt5, sys, settings, workstation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

workspace = ['School','Writing','Coding']

class render_funcs():
	def __init__(self, function):
		'''
		 A class built to store functions passed down to widgets/forms 
		 so they can navigate their way back to this central form
		'''
		self.function = function 
		self.render_menu = None
		self.render_workspace =  None
		self.render_settings = None

	def set_menu_func(self, widget):
		self.render_menu = lambda: self.function(widget)

	def set_workspace_func(self,widget):
		self.render_workspace = lambda: self.function(widget)
		# self.render_workspace()

	def set_settings_func(self, widget):
		self.render_settings = lambda: self.function(widget)

class Button(QPushButton):
	def __init__(self, text, parent):
		super(Button,self).__init__(text)
		self.text = text
		self.clicked.connect(lambda: self.prep_widget(parent))

	def prep_widget(self, parent):
		# setup the forms
		station_widget = workstation.App_Form(self.text)
		settings_widget = settings.App_Form(self.text)

		# setup the setcentralwidget function for each widget 
		function_pack = render_funcs(parent.render)
		function_pack.set_menu_func(parent.main_frm)
		function_pack.set_workspace_func(station_widget)
		function_pack.set_settings_func(settings_widget)

		station_widget.set_function_pack(function_pack)
		settings_widget.set_function_pack(function_pack)

		parent.setWindowTitle('Workspace - ' + self.text)

		return function_pack.render_workspace()

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window,self).__init__(*args, **kwargs)

		menu_frm = self.setMenu()
		menu_frm.setStyleSheet(open('app.css').read())

		self.menu_frm = menu_frm
		self.workstation = None
		self.settings = None

		self.main_frm = self.menu_frm
		self.render(self.main_frm)
		self.showMaximized()

	def setMenu(self):
		frame = QWidget()
		vbox = QVBoxLayout()

		for work in workspace:
			btn = Button(work, self)
			btn.setSizePolicy(True,True)
			vbox.addWidget(btn)

		add_btn = QPushButton('+')
		add_btn.setStyleSheet("""
			QPushButton {
				font: 20px black;
				border: 3px dashed black;
				padding: 20px;
			}
			""")
		add_btn.clicked.connect(lambda: self.nothing('it works'))
		vbox.addWidget(add_btn)
		frame.setLayout(vbox)

		return frame

	def render(self, widget):
		self.main_frm = widget
		self.setCentralWidget(self.main_frm)

	def set_workspace(widget):
		self.workstation = widget

	def set_settings(widget):
		self.settings = settings

def main():
	myApp = QApplication(sys.argv)
	myApp.setApplicationName('Workflow')

	win = Window()
	win.show()	
	sys.exit(myApp.exec_())

if __name__ == '__main__':
	main()