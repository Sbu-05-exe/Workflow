import PyQt5, sys, settings, workstation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

workspace = ['School','Writing','Coding']


def setup_external_UIs():

	station_widget = QWidget()
	ui = workstation.Ui_Workstation()
	ui.setupUi(station_widget)

	settings_widget = QWidget()
	ui = settings.Ui_Settings('Workstation')
	ui.setupUi(settings_widget)

	return station_widget,  settings_widget

class Button(QPushButton):
	def __init__(self, text, parent):
		super(Button,self).__init__(text)
		self.text = text

		# Loophole of the century
		self.clicked.connect(lambda: parent.switch(self.text,'workstation'))

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Window,self).__init__(*args, **kwargs)

		self.work_frm, self.set_frm = setup_external_UIs()

		menu_frm = self.setMenu()
		menu_frm.setStyleSheet(open('app.css').read())

		self.menu_frm = menu_frm

		self.main_frm = menu_frm
		self.setCentralWidget(self.main_frm)
		self.show()
		self.frames = {
			'menu': self.menu_frm,
			'workstation': self.work_frm,
			'settings': self.set_frm
		}

	def change_frames(self, widget):
		self.setCentralWidget(main_frm)

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
		add_btn.clicked.connect(lambda: self.check('it works'))
		vbox.addWidget(add_btn)
		frame.setLayout(vbox)

		return frame

	def switch(self, text, frame):
		my_widget = self.frames[frame]
		print(self.frames[frame])
		
		self.main_frm = my_widget
		self.setWindowTitle(text)
		self.setCentralWidget(self.main_frm)

	def create_frms(frame):
		form_settings = UiForm()
		form_settings.setupUi(Form)


def main():
	myApp = QApplication(sys.argv)
	myApp.setApplicationName('Workflow')

	win = Window()
	win.show()
	
	sys.exit(myApp.exec_())

if __name__ == '__main__':
	main()