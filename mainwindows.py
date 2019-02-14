#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic

#
#открыть окно mainwindow.ui
#код рабочий!!!
#
class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.resize(640, 480) # размер окна
    window.setWindowTitle(" тестовое окно ")  # заголовок



    sys.exit(app.exec_())