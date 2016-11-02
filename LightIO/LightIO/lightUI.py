# coding:utf-8

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from shiboken import wrapInstance
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance

import os.path
import maya.OpenMayaUI as OpenMayaUI

import lightUtils
reload(lightUtils)

def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QMainWindow)


class LightUI(QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(LightUI, self).__init__(parent)
    
        # Window
        self.setWindowTitle('Light IO')
        self.setFixedWidth(200) 
        self.setFixedHeight(60)
        
        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(5,5,5,5)
        mainLayout.setSpacing(5)
        mainLayout.setAlignment(Qt.AlignTop)
        
        self.saveBttn = QPushButton('Save Render Global')
        self.loadBttn = QPushButton('Load Render Global')
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
        warningMessage = QMessageBox(self)
        warningMessage.setText(message)
        warningMessage.setIcon(QMessageBox.Critical)
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


