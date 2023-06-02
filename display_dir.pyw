from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from directoryGui import Ui_MainWindow
import re, os, sys, pickle, traceback, json



class myApp(QtWidgets.QMainWindow):

	def __init__(self):
		super(myApp, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.centralwidget = QtWidgets.QWidget()
		
		self.ui.loadButton.clicked.connect(self.load_dir_list)
		self.ui.refreshDir.clicked.connect(self.check_adrbar)
		self.ui.backButton.clicked.connect(self.move_back)
		self.ui.forwardButton.clicked.connect(self.move_forward)

		self.ui.forwardButton.setEnabled(False)
		self.forward = list()
		self.cwd = str()
		self.platform = str()
		with open("extensions.json") as extensions:
			self.extension_logos = json.load(extensions)
		self.known_types = self.extension_logos.keys()
	

		
		
	def load_dir_list(self):
		path, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a pickle file.")
		#exceptions
		try:
			with open(path, "rb") as f:
				self.dir_list = pickle.load(f)
				
				if self.dir_list[0][0] == "c:\\":
					self.platform = "win32"
				else:
					self.platform = "unix"

			self.update_directory(self.dir_list[0][0])
		except:
			traceback.print_exc()

	def update_directory(self, new_dir):

		if new_dir == self.dir_list[0][0]: # when we at Home directory.
			self.ui.backButton.setEnabled(False)
		
		if new_dir == "c:":
			new_dir = "c:\\"
		if new_dir[0:4] == r"c:\\":
			new_dir = f"c:\\" + new_dir[4:]


		dirs, files = self.get_directory(new_dir)
		if dirs != None and files != None:
			self.cwd = new_dir
			self.ui.addressBar.setText(self.cwd)
			#print(dirs, files)
			self.generate_symbol(dirs, files)
		else:
			print("No such folder.")
			self.ui.addressBar.setText(self.cwd)

	def get_directory(self, inq_dir):
		for dir in self.dir_list:
			path, dirs, files = list(dir)
			if inq_dir == path:
				return dirs, files
		return None, None

	
	
	def move_back(self):
		self.forward.append(self.cwd)
		self.ui.forwardButton.setEnabled(True)
		if self.platform == "unix":
			slash = "/"
		elif self.platform == "win32":
			slash = '\\'
		back_dir = slash.join(self.cwd.split(slash)[:-1])
		self.update_directory(back_dir)

	
	
	def move_forward(self):
		for i in range(len(self.forward) -1, -1, -1):
			print(i)
			self.update_directory(self.forward[i])
			self.forward.remove(self.forward[i])
			if len(self.forward) == 0:
				self.ui.forwardButton.setEnabled(False)
			return

			
		#pass

	def chdir(self, name):
		self.ui.forwardButton.setEnabled(False)
		self.ui.backButton.setEnabled(True)
		self.forward = list()
		
		if self.platform == "unix":
			slash = "/"
		elif self.platform == "win32":
			slash = '\\'
		
		print(self.cwd + slash + name)
		self.update_directory(self.cwd + slash + name)
		
	
	def generate_symbol(self,dirs, files):
		
		def deleteItemsOfLayout(layout):
			if layout is not None:
				while layout.count():
					item = layout.takeAt(0)
					widget = item.widget()
					if widget is not None:
						widget.setParent(None)
					else:
						deleteItemsOfLayout(item.layout())

				 
				 
		len_widgets = self.ui.contents.count()
		#self.ui.contents.clear()
		while(len_widgets >= 0):
			my_widget = self.ui.contents.itemAt(len_widgets)
			if my_widget != None:
				if my_widget.layout() != None:
					#remove_widgets(my_widget)
					#self.ui.contents.removeItem(my_widget.layout())
					deleteItemsOfLayout(my_widget)
				elif my_widget.widget() != None:
					my_widget.widget().setParent(None)

			len_widgets -= 1
				
		self.symbol_coordinates = {}

		def template(name, type_, order):
			row = int(order / 5)
			column = order % 5
			column_space = 21
			row_space = 57
			
			
			_translate = QtCore.QCoreApplication.translate
			self.ui.verticalLayout_12 = QtWidgets.QVBoxLayout()
			#self.ui.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
			self.ui.verticalLayout_12.setContentsMargins(5, 5, 0, 0)
			self.ui.verticalLayout_12.setSpacing(5)
			self.ui.verticalLayout_12.setObjectName(f"verticalLayout_{name}")
			self.ui.folder = QtWidgets.QLabel(self.ui.centralwidget)
			self.ui.folder.setMaximumSize(QtCore.QSize(100, 33))
			#self.ui.folder.setMinimumSize(QtCore.QSize(100, 33))
			font = QtGui.QFont()
			font.setFamily("Sans Serif")
			font.setPointSize(8)
			font.setBold(False)
			font.setItalic(False)
			font.setWeight(50)

			self.ui.button = QtWidgets.QPushButton("", self)#🗀
			self.ui.verticalLayout_12.addWidget(self.ui.button)
			self.ui.button.setAccessibleName(name)
			self.ui.button.setStyleSheet("background-color : transparent")
			self.ui.button.setIconSize(QtCore.QSize(64, 64))
			self.ui.button.setToolTip(name)
			if type_ == "dir":
				logo_extension = "dir"
				self.ui.button.clicked.connect(lambda ch, name=name: self.chdir(name))
			else:
				file_extension = name.split(".")[-1]
				if file_extension in self.known_types:
					logo_extension = self.extension_logos[file_extension]
				else:
					logo_extension = "unknown"
			self.ui.button.setIcon(QtGui.QIcon(f"logos/{logo_extension}.png"))
				
				

			self.ui.folder.setFont(font)
			self.ui.folder.setLayoutDirection(QtCore.Qt.LeftToRight)
			self.ui.folder.setAlignment(QtCore.Qt.AlignCenter)
			self.ui.folder.setObjectName(f"label_{name}")
			self.ui.verticalLayout_12.addWidget(self.ui.folder)
			spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
			self.ui.verticalLayout_12.addItem(spacerItem)
			self.ui.contents.addLayout(self.ui.verticalLayout_12, row, column, 1, 1)
			self.ui.folder.setText(_translate("Dialog", name))
			#self.ui.folder.adjustSize()



			
			if type_ not in self.known_types:
				type_ = "unknown"
				
			self.pixmap = QPixmap(f"logos/{type_}.png")

		count = 0
		
		for dir in dirs:
			template(dir, "dir", count)
			count += 1
		for file in files:
			template(file, file.split(".")[-1], count)
			count += 1


	def check_adrbar(self):
		self.update_directory(self.ui.addressBar.text())


def app():
	app = QtWidgets.QApplication(sys.argv)
	win = myApp()
	win.show()
	sys.exit(app.exec_())

app()

