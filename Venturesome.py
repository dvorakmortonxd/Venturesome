import sys
import os
import qdarkstyle
from PyQt5 import QtGui
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
urladdress = "http://search.brave.com"

duckduckgo = "http://duckduckgo.com/?q="
searxng = "http://searx.be/?q="
brave = "https://search.brave.com/search?q="

pick = 2

search = brave

def changetoddg():
    search = duckduckgo
    pick = 1

def changetobrave():
    search = brave
    pick = 2

def changetosearx():
    search = searxng
    pick = 3

class MainWindow(QMainWindow):
    def GoHome(self):
        self.browser.setUrl(QUrl("http://search.brave.com"))
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
            if pick == 1:
                self.browser.setUrl(QUrl(duckduckgo + urladdress))
            elif pick == 2:
                self.browser.setUrl(QUrl(brave + urladdress))
            else:
                self.browser.setUrl(QUrl(searxng + urladdress))
    def UpdateUrl(self, q):
        with open("Web_Browser_History.venturesome_history", "a") as f:
            f.write(q.toString() + "\n")
            f.close()
        self.SearchBar.setText(q.toString())
    def __init__(self, *args, **kwargs):
    #main
        super(MainWindow, self).__init__(*args, **kwargs)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowTitle("Venturesome")
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'logo.png'))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://search.brave.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
#Tabs
    #BrowserBar
        BrowserBar = QToolBar("navigation")
        self.addToolBar(BrowserBar)
        
    #Buttons
        ##HeightButton
        #HeightButton = QAction('...', self)
        #BackButton
        BackButton = QAction('◀️', self)
        BackButton.triggered.connect(self.browser.back)
        #ForwardButton
        ForwardButton = QAction('▶️', self)
        ForwardButton.triggered.connect(self.browser.forward)
        #ReloadButton
        ReloadButton = QAction('🔃', self)
        ReloadButton.triggered.connect(self.browser.reload)
        #SearchBar
        self.SearchBar = QLineEdit()
        self.SearchBar.returnPressed.connect(self.URL)
        self.browser.urlChanged.connect(self.UpdateUrl)
        #HomeButton
        HomeButton = QAction('🏠', self)
        HomeButton.triggered.connect(self.GoHome)
        #AddButtons
        BrowserBar.addAction(BackButton)
        BrowserBar.addAction(ForwardButton)
        BrowserBar.addAction(ReloadButton)
        BrowserBar.addWidget(self.SearchBar)
        BrowserBar.addAction(HomeButton)

        #needs to be last or weird
        #BrowserBar.addAction(HeightButton)


os.environ[
        "QTWEBENGINE_CHROMIUM_FLAGS"
    ] = "--blink-settings=darkMode=4,darkModeImagePolicy=2"
QApplication.setApplicationName("Venturesome")
QApplication.setApplicationVersion("1.0")
app = QApplication(sys.argv)
window = MainWindow()
#app.setStyleSheet(qdarktheme.load_stylesheet())
app.exec()
#save.emojis=◀▶
#save.mojis=🔁◀️▶️➰🏠
