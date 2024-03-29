from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("File Explorer")
        MainWindow.resize(600, 750)
        MainWindow.setMinimumSize(QtCore.QSize(600, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.contents = QtWidgets.QGridLayout()
        self.contents.setObjectName("contents")
        #self.gridLayout.addLayout(self.contents, 3, 0, 1, 1)
        
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.contents)


        self.scroll_contents = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_contents.setWidgetResizable(True)
        self.scroll_contents.setObjectName("scroll_contents")
        self.scroll_contents.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 434, 353))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scroll_contents.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll_contents, 2, 0, 1, 1)
        self.scroll_contents.setWidgetResizable(True)
        self.scroll_contents.setWidget(self.widget)
        #self.scroll_contents.addScrollBarWidget()
        self.scroll_contents.verticalScrollBar()



        self.navBar = QtWidgets.QHBoxLayout()
        self.navBar.setObjectName("navBar")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMaximumSize(QtCore.QSize(50, 33))
        self.backButton.setObjectName("backButton")
        self.navBar.addWidget(self.backButton)
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setEnabled(True)
        self.forwardButton.setMaximumSize(QtCore.QSize(50, 33))
        self.forwardButton.setObjectName("forwardButton")
        self.navBar.addWidget(self.forwardButton)
        self.refreshDir = QtWidgets.QPushButton(self.centralwidget)
        self.refreshDir.setMaximumSize(QtCore.QSize(25, 33))
        self.refreshDir.setObjectName("refreshDir")
        self.navBar.addWidget(self.refreshDir)
        self.addressBar = QtWidgets.QLineEdit(self.centralwidget)
        self.addressBar.setObjectName("addressBar")
        self.navBar.addWidget(self.addressBar)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setMaximumSize(QtCore.QSize(50, 33))
        self.loadButton.setObjectName("loadButton")
        self.navBar.addWidget(self.loadButton)
        self.gridLayout.addLayout(self.navBar, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.contentGrid = QtWidgets.QGridLayout()
        self.contentGrid.setObjectName("contentGrid")
        self.gridLayout_2.addLayout(self.contentGrid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("File Explorer", "File Explorer"))
        self.backButton.setText(_translate("MainWindow", "←"))
        self.forwardButton.setText(_translate("MainWindow", "→"))
        self.refreshDir.setText(_translate("MainWindow", "⟳"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
#import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
