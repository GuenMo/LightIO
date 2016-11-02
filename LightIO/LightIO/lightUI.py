# coding:utf-8

from PySide import QtGui, QtCore
import os.path
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance

import lightUtils
reload(lightUtils)

def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtGui.QMainWindow)


class LightUI(QtGui.QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(LightUI, self).__init__(parent)
    
        # Window
        self.setWindowTitle('Light IO')
        self.setFixedWidth(200) 
        self.setFixedHeight(60)
        
        # Layout
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setContentsMargins(5,5,5,5)
        mainLayout.setSpacing(5)
        mainLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.saveBttn = QtGui.QPushButton('Save Render Global')
        self.loadBttn = QtGui.QPushButton('Load Render Global')
        mainLayout.addWidget(self.saveBttn)
        mainLayout.addWidget(self.loadBttn)
        
        self.setLayout(mainLayout)
        
        # 
        self.saveBttn.clicked.connect(self.saveRenderGlobal)
        self.loadBttn.clicked.connect(self.loadRenderGlobal)
    
    def saveRenderGlobal(self):
        lightUtils.saveRenderGlobal()
        
    def loadRenderGlobal(self):
        lightUtils.loadeRenderGlobal()
        
    def warningMessage(self, message):
        warningMessage = QtGui.QMessageBox(self)
        warningMessage.setText(message)
        warningMessage.setIcon(QtGui.QMessageBox.Critical)
        warningMessage.exec_()
        
def main():
    global win
    try:
        win.close()
        win.deleteLater()
    except: 
        pass
    win = LightUI()
    win.show()


