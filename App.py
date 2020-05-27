import PyQt5, sys, os # Python files
import menu, settings, workstation # App Files
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel, QStackedWidget
from PyQt5.QtCore import Qt

# File Handling functions that are used amongs all modules!

# Returns a list delimeted by a ',' in a file
def check_file(file_name):
	if os.path.isfile(file_name):
		with open(file_name,'r') as f:
			result = f.read().split(',')
			# making sure to not return an empty string
			return [item for item in result if item]

	else:
		return []

# Saving contents of an list to a file 
def save_file(file_name, lst):
	s = ','.join(lst)
	with open(file_name, 'w') as f:
		f.write(s)


# I dont really need this class anymore but it does make my code more self_explanatory
# when reading other modules so I'll keep it 

class function_pack():
	def __init__(self, function):
		'''
		 A class built to store functions passed down to widgets/forms 
		 so they can navigate their way back to this central form
		'''
		self.function = function
		self.render_menu = lambda: self.function(0)
		self.render_workspace =  lambda: self.function(1)
		self.render_settings = lambda: self.function(2)

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window,self).__init__(*args, **kwargs)
		self.Stack = QStackedWidget()

		menu_frm = menu.MenuWidget(self.prep_widgets)

		self.menu_frm = menu_frm
		self.workstation = None
		self.settings = None

		self.Stack.addWidget(menu_frm)

		self.setCentralWidget(self.Stack)
		self.render()
		self.showMaximized()

	def prep_widgets(self, text):
		workspace_widget = workstation.App_Form(text)
		settings_widget = settings.App_Form(text)

		self.Stack.addWidget(workspace_widget)
		self.Stack.addWidget(settings_widget)

		fn_pack = function_pack(self.render) 

		workspace_widget.set_fn_pack(fn_pack)
		settings_widget.set_fn_pack(fn_pack)

		fn_pack.render_workspace()

	def render(self, i=0):
		self.Stack.setCurrentIndex(i)

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