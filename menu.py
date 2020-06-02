import sys
import controller
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel, QInputDialog

# workspace = ['School','Coding','Blog','Project X']
class Record():
	def __init__(self, mylist):
		self.pk = mylist[0]
		self.name = mylist[1]

class Button(QPushButton):
	def __init__(self, text):
		super().__init__(text)
		self.text = text

class MenuWidget(QWidget):
	def __init__(self, parent_fn=None):
		super().__init__()
		
		self.workspace = controller.TbWorkspace.getTb()
		self.layout = self.initUI()
		self.prep_widgets = parent_fn

	def initUI(self):
		vbox = QVBoxLayout()

		for record in self.workspace:
			self.Add_Workspace(record.name, vbox)

		btn_add = self.create_btn_add()
		vbox.addWidget(btn_add)

		self.setLayout(vbox)
		self.setStyleSheet(open('app.css').read())

		return vbox

	def create_btn_add(self):
		add_btn = QPushButton('+')
		add_btn.setStyleSheet("""
			QPushButton {
				font: 20px black;
				border: 3px dashed black;
				padding: 20px;
			}
			""")

		add_btn.clicked.connect(self.addCategory)

		return add_btn


	def Add_Workspace(self, text, layout):
		btn = QPushButton(text)
		btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn.clicked.connect(self.buttonClicked)
		layout.addWidget(btn)

	def render_layout(self):
		for i in reversed(range(self.layout.count())):
			# Remove all widgets
			widget = self.layout.itemAt(i).widget()
			widget.setParent(None)

		for record in self.workspace:
			self.Add_Workspace(record.name, self.layout)

		btn_add = self.create_btn_add()
		self.layout.addWidget(btn_add)

	def buttonClicked(self):
		sender = self.sender()
		btn_text = sender.text()

		for record in self.workspace:
			if record.name == btn_text:
				if controller.TbWorkspace.set_active(record.id) == 'SUCCESSFUL':
					self.prep_widgets()	

	def addCategory(self):
		text, ok = QInputDialog.getText(self,'Entry','Enter name of workspace: ',)
		if (ok and text):

			# Update the database
			controller.TbWorkspace.insert_new_workspace(text)
			self.workspace = controller.TbWorkspace.getTb() 
			self.render_layout()

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Menu')

	win = MenuWidget()
	win.show()
	sys.exit(App.exec_())

if __name__ == '__main__':
	main()