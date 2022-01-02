from os import close
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget


class FinLevelView(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()

        FinLevelWidget=QWidget()
        self.setCentralWidget(FinLevelWidget)
        FinLevelWidget.setLayout(QVBoxLayout())
        FinLevelWidget.setFixedSize(450,450)
        FinLevelWidget.setStyleSheet("background-image: url(block/YouWin.jpg)")
        

        #button Leave
        self.__leave=QPushButton("Leave")
        self.__leave.clicked.connect(self.close)
        self.__leave.setStyleSheet("background-image: url(block/end_stone.png)")
        self.statusBar().layout().addWidget(self.__leave)

    def setLevelMenuView(self, lmv):
        self.__LevelMenuView=lmv
    
    def setGridView(self, gridView):
        self.__GridView=gridView
