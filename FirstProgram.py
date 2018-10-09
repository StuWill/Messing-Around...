import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp, QMenu, QTextEdit, QLabel
from PyQt5.QtGui import QIcon, QFont


class Program(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        labl1 = QLabel('My first Program', self)
        labl1.move(200, 200)

        #self.setGeometry(500, 500, 600, 300)
        self.resize(600, 300)
        self.center()
        self.setWindowTitle('Top Secret')
        self.setWindowIcon(QIcon('web.ico'))

# Menu Bar
        menubar = self.menuBar()

    # File Menu
        fileMenu = menubar.addMenu('&File') # menuBar.(something) adds various menus to menu bar, in this case 'File'.

        newAct = QAction('New', self)
        newAct.setStatusTip('New')
        fileMenu.addAction(newAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import Mail', self)#
        impAct.setStatusTip('Import mail')
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)

        exitAct = QAction(QIcon('close.ico'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application') # displays message on status bar when item is hovered over.
        exitAct.triggered.connect(qApp.quit) # assigns action if item triggered, in this case to quit.
        fileMenu.addAction(exitAct)

    # View Menu
        viewMenu = menubar.addMenu('&View')

        viewStatAct = QAction('View Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

# Tool Bar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

# Status Bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

# Text Edit
        #textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

# Tooltips & Buttons
        QToolTip.setFont(QFont('Arial', 10))

        self.setToolTip('this is a widgety thing!')

        btn = QPushButton('Push Me', self)
        btn.setToolTip('This is a <b>button tooltip</b> widget thingy')
        btn.resize(btn.sizeHint())
        btn.move(50, 100)

        qbtn = QPushButton('Exit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.setToolTip('Press me to <b>quit</b>!')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 100)

        self.show()

# Center Window
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# Context Menu
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

# Toggles
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

# Close Window Check
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you positive you want to <i>quit</i>?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Pro = Program()
    sys.exit(app.exec_())


