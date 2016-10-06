import sys
from PyQt4 import QtCore, QtGui
import sys 
sys.path.append("./..")
from citation_manager import Citation_Manager
from citation_manager_UI_edit import Ui_MainWindow 
import signal
import logging
import os 

class CitationManagerGUI(QtGui.QMainWindow):

    def __init__(self,cm,parent=None):

        QtGui.QMainWindow.__init__(self, parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.QMaiWindow = QtGui.QMainWindow(self) 
        self.main_widget = QtGui.QWidget(self)
        # now setup logging
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger()
        self.cm = cm 
        self.__connect()

    def __connect(self):

        self.timer = QtCore.QTimer()
        self.timer.start(5000)

        # self.cm.render_md()
        # QtCore.QObject.connect(self.ui.html_display, QtCore.SIGNAL("sourceChanged()"), self.render_html)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL('timeout()'), self.update_json)
        # QtCore.QObject.connect(self.ui.render_html, QtCore.SIGNAL('clicked()'),self.render_html)
        QtCore.QObject.connect(self.ui.citation_viewer, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), self.update_editor)
        QtCore.QObject.connect(self.ui.note_edit, QtCore.SIGNAL("textChanged()"), self.update_note)
        QtCore.QObject.connect(self.ui.actionGen_HTML, QtCore.SIGNAL("triggered()"), self.gen_html)
        QtCore.QObject.connect(self.ui.actionGen_JSON, QtCore.SIGNAL("triggered()"), self.gen_json)
        QtCore.QObject.connect(self.ui.actionSelect_JSON, QtCore.SIGNAL("triggered()"), self.select_json)
        QtCore.QObject.connect(self.ui.save_shortcut, QtCore.SIGNAL("activated()"), self.save)
        QtCore.QObject.connect(self.ui.open_shortcut, QtCore.SIGNAL("activated()"), self.select_json)
        
        for cit in self.cm:
            self.ui.citation_viewer.addItem(cit.title[0])

    def save(self):
        """
        Generate html files and save the current JSON configuration
        """
        self.gen_html()
        self.gen_json()

    def gen_html(self):
        """
        Save the current html file.
        """
        self.cm.render_md(save=True,css_loc="./../",js_loc="./../")

    def gen_json(self):
        """
        Save the current configuration to a JSON file
        """
        self.cm.create_json("citations.json")

    def select_json(self):
        """
        Select a JSON file to load. 
        """
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '~/',"JSON files (*.json)")
    
        self.cm.load_json_file(fname)
        self.ui.citation_viewer.clear()
        for cit in self.cm:
            self.ui.citation_viewer.addItem(cit.title[0])

    def render_html(self):
        """
        Render the current HTML file
        """
        md, html = self.cm.render_md(css_loc="./../",js_loc="./../")
        # self.ui.html_display.setSource(QtCore.QUrl("Citations.html"))
        self.ui.html_display.setHtml(html)
        # self.ui.html_display.load(QtCore.QUrl("www.google.com"))
        # self.ui.html_display.show()

    def update_json(self):
        """
        Update the JSON file
        """
        pass
        # self.logger.info("Creating new JSON file")
        # self.cm.create_json("citations.json")

    def update_editor(self):
        """
        Update the text inside the editor
        """
        selected_item = self.ui.citation_viewer.currentRow()
        self.ui.note_edit.setText(self.cm[selected_item].note[0])

    def update_note(self):
        """
        Update the note of the current citation
        """
        if (str(self.ui.note_edit.toPlainText()) == str()):
            pass
        else:
            selected_item = self.ui.citation_viewer.currentRow()
            self.cm[selected_item].note[0] = str(self.ui.note_edit.toPlainText())
            self.render_html()


def app_exit():
    cm = Citation_Manager(json_file="./../citations_keep.json")
    app = QtGui.QApplication(sys.argv)
    GUI = CitationManagerGUI(cm)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    GUI.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(app_exit())
