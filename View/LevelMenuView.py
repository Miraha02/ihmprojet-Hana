from View.ResetMessage import ResetMessage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Model.Grid import Grid
from View.GridView import GridView

"""
Cette view correspond au menu de selection de niveau
il est possible de cliquer sur n'importe quel niveau mais le jeu ne se lancera pas si le niveau précédent n'a pas déjà été clear
le bouton reset devra afficher une nouvelle fenetre avec un message d'alerte stipulant que toute la progression du joueur sera perdu
"""

class LevelMenuView(QMainWindow):
    def __init__(self, Model, Controller):
        super().__init__()
        self.__Grid=Model
        self.__view=None
        self.__Controller=Controller

        levelWidget=QWidget()
        self.setCentralWidget(levelWidget)
        levelWidget.setLayout(QVBoxLayout())
        levelWidget.setFixedSize(500,500)

        #button1
        self.__button1=QPushButton("level 1")
        self.__button1.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button1.clicked.connect(lambda x:self.choixLevel(1))
        levelWidget.layout().addWidget(self.__button1)
        #button2
        self.__button2=QPushButton("level 2")
        self.__button2.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button2.clicked.connect(lambda x:self.choixLevel(2))
        levelWidget.layout().addWidget(self.__button2)
        #button3
        self.__button3=QPushButton("level 3")
        self.__button3.setStyleSheet("background-image: url(block/end_stone.png)")
        self.__button3.clicked.connect(lambda x:self.choixLevel(3))
        levelWidget.layout().addWidget(self.__button3)

        #button reset
        self.__buttonReset=QPushButton("Reset")
        self.__buttonReset.setStyleSheet("background-image: url(block/mycelium_top.png)")
        self.__buttonReset.clicked.connect(self.resetMessage)
        levelWidget.layout().addWidget(self.__buttonReset)

    def resetMessage(self):
        self.rMess=ResetMessage(self.__Controller, self)
        self.rMess.show()

    def affichage(self):
        self.__view = GridView(self.__Grid, self.__Controller)
        self.__Controller.setView(self.__view)
        self.__Grid.setView(self.__view)
        self.__view.setWindowTitle("Sokoban")
        self.__view.show()
        self.close()

    def choixLevel(self,numLevel):
        if numLevel==1:
            if self.__Grid.getLevel()[0]:
                self.__Grid.setLevelChoisi(1)
                self.__Controller.chargeLevel()
                self.affichage()
        elif numLevel==2:
            if self.__Grid.getLevel()[1]:
                self.__Grid.setLevelChoisi(2)
                self.__Controller.chargeLevel()
                self.affichage()
        elif numLevel==3:
            if self.__Grid.getLevel()[2]:
                self.__Grid.setLevelChoisi(3)
                self.__Controller.chargeLevel()
                self.affichage()
        
        
        
    


