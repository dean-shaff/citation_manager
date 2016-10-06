# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './citation_manager_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        cit_width = 200
        cit_height = 530
        note_width = 440
        note_height = 530
        html_width = 440
        html_height = 530

        MainWindow.resize(cit_width+note_width+html_width+4*10, 550)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.citation_viewer = QtGui.QListWidget(self.centralwidget)
        self.citation_viewer.setGeometry(QtCore.QRect(10, 10, cit_width, cit_height))
        self.citation_viewer.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.citation_viewer.setObjectName(_fromUtf8("citation_viewer"))

        self.note_edit = QtGui.QTextEdit(self.centralwidget)
        self.note_edit.setGeometry(QtCore.QRect(2*10+cit_width, 10, note_width, note_height))
        self.note_edit.setObjectName(_fromUtf8("note_edit"))
        self.note_edit.setTabStopWidth(30)

        
        # self.html_display = QtWebKit.QWebView(self.centralwidget)
        self.html_display = QtGui.QTextBrowser(self.centralwidget)
        self.html_display.setGeometry(QtCore.QRect(3*10+cit_width+note_width, 10, html_width, html_height))
        self.html_display.setObjectName(_fromUtf8("html_display"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect_JSON = QtGui.QAction(MainWindow)
        self.actionSelect_JSON.setObjectName(_fromUtf8("actionSelect_JSON"))
        self.menuFile.addAction(self.actionSelect_JSON)

        self.actionGen_JSON = QtGui.QAction(MainWindow)
        self.actionGen_JSON.setObjectName(_fromUtf8("actionGen_JSON"))
        self.menuFile.addAction(self.actionGen_JSON)

        self.actionGen_HTML = QtGui.QAction(MainWindow)
        self.actionGen_HTML.setObjectName(_fromUtf8("actionGen_HTML"))
        self.menuFile.addAction(self.actionGen_HTML)

        self.menubar.addAction(self.menuFile.menuAction())

        self.save_shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_S), MainWindow)
        self.open_shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_O), MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSelect_JSON.setText(_translate("MainWindow", "Select JSON", None))
        self.actionGen_HTML.setText(_translate("MainWindow", "Generate HTML", None))
        self.actionGen_JSON.setText(_translate("MainWindow", "Generate JSON", None))
