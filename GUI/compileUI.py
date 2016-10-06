import PyQt4.uic as uic

fpy = open("./citation_manager_UI.py",'w')
uic.compileUi("./citation_manager_UI.ui", fpy)
fpy.close()
