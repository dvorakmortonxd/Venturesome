import sys
import os
from typing import Container
from PyQt5 import *
from PyQt5.QtPrintSupport import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
urladdress = 'http://duckduckgo.com'

class MainWindow(QMainWindow):
    def GoHome(self):
        self.browser.setUrl(QUrl('http://duckduckgo.com'))
    def URL(self):
        urladdress = self.SearchBar.text()
        if "." in urladdress:
            if "http://" in urladdress:
                self.browser.setUrl(QUrl(urladdress))
            elif "https://" in urladdress:
                self.browser.setUrl(QUrl(urladdress))
            else:
                self.browser.setUrl(QUrl("http://" + urladdress))
        else:
            self.browser.setUrl(QUrl("https://duckduckgo.com/?q=" + urladdress))
    def UpdateUrl(self, q):
        with open("C:\Windows\Temp\Venturesome_History.browserhistory", "a") as f:
            f.write(q.toString() + "\n")
            f.close()
        print(os.path.isfile('C:\Windows\Temp\Venturesome'))
        self.SearchBar.setText(q.toString())
    def __init__(self, *args, **kwargs):
    #main
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
#Tabs   
    #BrowserBar
        BrowserBar = QToolBar("navigation")
        self.addToolBar(BrowserBar)
    #Buttons
        #HeightButton
        HeightButton = QAction('|\n|', self)
        #BackButton
        BackButton = QAction('<', self)
        BackButton.triggered.connect(self.browser.back)
        #ForwardButton
        ForwardButton = QAction('>', self)
        ForwardButton.triggered.connect(self.browser.forward)
        #ReloadButton
        ReloadButton = QAction('🔄', self)
        ReloadButton.triggered.connect(self.browser.reload)
        #HomeButton
        HomeButton = QAction('🏠', self)
        HomeButton.triggered.connect(self.GoHome)
        #SearchBar
        self.SearchBar = QLineEdit()
        self.SearchBar.returnPressed.connect(self.URL)
        self.browser.urlChanged.connect(self.UpdateUrl)
        #AddButtons
        BrowserBar.addAction(BackButton)
        BrowserBar.addAction(ForwardButton)
        BrowserBar.addAction(ReloadButton)
        BrowserBar.addAction(HomeButton)
        BrowserBar.addWidget(self.SearchBar)

        #needs to be last or weird
        BrowserBar.addAction(HeightButton)


os.environ[
        "QTWEBENGINE_CHROMIUM_FLAGS"
    ] = "--blink-settings=darkMode=4,darkModeImagePolicy=2"
QApplication.setApplicationName("Venturesome")
QApplication.setApplicationVersion("1.0")
app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
#save.emojis=◀▶
#save.mojis=🔁◀️▶️➰🏠
