#self.logoLabel.setPixmap(QtGui.QPixmap("images/g6_logo.png")) to get logo working
#note: pyuic5 –x "filename".ui –o "filename".py to convert .ui files to .py
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from page1and2test import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        #self.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.button1.clicked.connect(self.showPage1)
        self.ui.button2.clicked.connect(self.showPage2)

    def show(self):
        self.main_win.show()
    #on button1 click show page 1
    def showPage1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    #on button2 click show page 2
    def showPage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mainUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        #self.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.tasksPage)

        self.ui.tasksButton.clicked.connect(self.showTasksPage)
        self.ui.profilesButton.clicked.connect(self.showProfilesPage)
        self.ui.accountsButton.clicked.connect(self.showAccountsPage)
        self.ui.settingsButton.clicked.connect(self.showSettingsPage)

    def show(self):
        self.main_win.show()
    def showTasksPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.tasksPage)
    def showProfilesPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.profilesPage)
    def showAccountsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accountsPage)
    def showSettingsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settingsPage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())