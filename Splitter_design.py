# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:55:18 2022

@author: mattjin
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,QSplitter, QMainWindow,
                             QApplication, QTextEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

# Left Part        
        topleft_buttons = QFrame(self)
        topleft_buttons.setFrameShape(QFrame.StyledPanel)

        topleft_perturbation = QFrame(self)
        topleft_perturbation.setFrameShape(QFrame.StyledPanel)
        
        topleft_images = QFrame(self)
        topleft_images.setFrameShape(QFrame.StyledPanel)

        topleft_tree = QFrame(self)
        topleft_tree.setFrameShape(QFrame.StyledPanel)

# Right Part
        bottom_information = QFrame(self)
        bottom_information.setFrameShape(QFrame.StyledPanel)
        
        bottom_dotmap = QFrame(self)
        bottom_dotmap.setFrameShape(QFrame.StyledPanel)
        
        bottom_animation = QFrame(self)
        bottom_animation.setFrameShape(QFrame.StyledPanel)

        bottom_matrix = QFrame(self)
        bottom_matrix.setFrameShape(QFrame.StyledPanel)
        
        bottom_parallel = QFrame(self)
        bottom_parallel.setFrameShape(QFrame.StyledPanel)
        
# Combine together
        splitter_left = QSplitter(Qt.Vertical)
        splitter_left.addWidget(topleft_buttons)
        splitter_left.addWidget(topleft_perturbation)
        splitter_left.addWidget(topleft_images)
        splitter_left.addWidget(topleft_tree)

        splitter_right = QSplitter(Qt.Vertical)
        splitter_right_1 = QSplitter(Qt.Horizontal)
        splitter_right_2 = QSplitter(Qt.Horizontal)
        
        splitter_right_1.addWidget(bottom_information)
        splitter_right_1.addWidget(bottom_dotmap)   
        splitter_right_2.addWidget(bottom_animation)
        splitter_right_2.addWidget(bottom_matrix)
        
        splitter_right.addWidget(splitter_right_1)
        splitter_right.addWidget(splitter_right_2)
        splitter_right.addWidget(bottom_parallel)       

        splitter_all = QSplitter(Qt.Horizontal)
        splitter_all.addWidget(splitter_left)
        splitter_all.addWidget(splitter_right)
        
        hbox.addWidget(splitter_all)
        self.setLayout(hbox)
        
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(Example())
        self.setWindowTitle('AA-ML-Testing Demo')
        self.resize(1280, 760)
        self.statusBar().showMessage('Status is here')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    result = Main()
    result.show()
    sys.exit(app.exec_())
