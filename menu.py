import sys
from controller import get_workspaces, insert_new_workspace
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel, QInputDialog

# workspace = ['School','Coding','Blog','Project X']

class Button(QPushButton):
	def __init__(self, text):
		super().__init__(text)
		self.text = text

class MenuWidget(QWidget):
	def __init__(self, parent_function=None):
		super().__init__()
		self.workspace = get_workspaces()
		self.layout = self.initUI()
		self.render_workstation = parent_function

	def initUI(self):
		vbox = QVBoxLayout()

		for work in self.workspace:
			self.Add_Workspace(work, vbox)

		add_btn = QPushButton('+')
		add_btn.setStyleSheet("""
			QPushButton {
				font: 20px black;
				border: 3px dashed black;
				padding: 20px;
			}
			""")

		add_btn.clicked.connect(self.addCategory)
		vbox.addWidget(add_btn)

		self.setLayout(vbox)
		self.setStyleSheet(open('app.css').read())

		return vbox

	def Add_Workspace(self, text, layout):
		btn = QPushButton(text)
		btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn.clicked.connect(self.buttonClicked)
		layout.addWidget(btn)

	def render_layout(self):
		# Remove btn_Add
		i = self.layout.count()
		btn_add = self.layout.itemAt(i-1).widget()
		btn_add.setParent(None)

		# Add an additional workspace button
		self.Add_Workspace(self.workspace[-1], self.layout)

		# Readd btn_ad
		self.layout.addWidget(btn_add)

	def buttonClicked(self):
		sender = self.sender()
		btn_text = sender.text()
		self.render_workstation(btn_text)	

	def addCategory(self):
		text, ok = QInputDialog.getText(self,'Entry','Enter name of workspace: ',)
		if (ok and text):
			self.workspace.append(text)
			# Update the database
			insert_new_workspace(text)
			self.render_layout()

def main():
	App = QApplication(sys.argv)
	App.setApplicationName('Menu')

	win = MenuWidget()
	win.show()
	sys.exit(App.exec_())

if __name__ == '__main__':
	main()