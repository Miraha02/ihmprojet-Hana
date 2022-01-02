from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Model.Grid import Grid
from PyQt5.QtMultimedia import QSound
from os import walk

class Controle(QWidget):
    def __init__(self,model):
        super().__init__()
        self.__BattleTheme=QSound(".\Sound\BattleTheme.wav")
        self.__BoxFall = QSound(".\Sound\BoxFall.wav")
        self.__Win = QSound(".\Sound\Win.wav")
        self.__BlockMur = QSound(".\Sound\BlockMur.wav")
        self.__Grid=model
        self.__view=None

    def battleThemeSound(self):
        self.__BattleTheme.play()
    def battleThemeSoundStop(self):
        self.__BattleTheme.stop()
    def boxFallSound(self):
        self.__BoxFall.play()
    def winSound(self):
        self.__Win.play()
    def blockMurSound(self):
        self.__BlockMur.play()

    def setView(self,view):
        self.__view=view
    
    def chargeLevel(self):
        self.battleThemeSound()
        if self.__Grid.getLevel()[2] and self.__Grid.getLevelChoisi()==3:
            self.__Grid.generateMap3()
        elif self.__Grid.getLevel()[1] and self.__Grid.getLevelChoisi()==2:
            self.__Grid.generateMap2()
        elif self.__Grid.getLevel()[0] and self.__Grid.getLevelChoisi()==1:
            self.__Grid.generateMap1()
    

    def verifWin(self):
        for i in range (len(self.__Grid.getGrid())):
            for j in range (len(self.__Grid.getGrid()[i])): #parcours chaque case
                if (self.__Grid.getGrid()[i][j]==4):
                    self.boxFallSound()
                    return

        self.battleThemeSoundStop()
        self.__Grid.setWin(True)
        self.winSound()
        if self.__Grid.getLevelActu()==self.__Grid.getLevelChoisi():
            self.__Grid.prochainLevel()

    def deplacerCai(self,x,y):

        #Caisse
        #test que la caisse ne sorte pas de la map
        for i in range (len(self.__Grid.getGrid())):
            for j in range (len(self.__Grid.getGrid()[i])): #parcours chaque case
                if (self.__Grid.getGrid()[i][j]==2): #si c'est une caisse
                    if not (0<=i+x<self.__Grid.getNbLigne()) and ((i==self.__Grid.getPositionJ()[0])and (j==self.__Grid.getPositionJ()[1])):
                        return
                    elif not (0<=j+y<self.__Grid.getNbColonne())and ((j==self.__Grid.getPositionJ()[1])and (i==self.__Grid.getPositionJ()[0])):
                        return
                    elif (self.__Grid.getPositionJ()[0]==i and self.__Grid.getPositionJ()[1]==j): #test que la caisse est pousse par le joueur
                        if (self.__Grid.getGrid()[i+x][j+y]==4): #test de deplacement dans le trou
                            self.__Grid.getGrid()[i+x][j+y]=5  #la case prend l'etat 5 correspondant a une caisse dans un trou
                            self.verifWin()
                        else:
                            self.__Grid.getGrid()[i+x][j+y]=2 #la nouvelle case devient une caisse
        

    def deplacerJo(self,x,y):
        
        # Mur
        for i in range (len(self.__Grid.getGrid())):
            for j in range (len(self.__Grid.getGrid()[i])): 
                if (self.__Grid.getGrid()[i][j]==3 or self.__Grid.getGrid()[i][j]==4 or self.__Grid.getGrid()[i][j]==5): #pour chaque case check s'il s'agit d'un mur ou d'un trou (vide ou pas)
                    if (self.__Grid.getPositionJ()[0]+x == i) and (self.__Grid.getPositionJ()[1]==j):
                        self.blockMurSound()
                        return
                    if (self.__Grid.getPositionJ()[0] == i) and (self.__Grid.getPositionJ()[1]+y ==j):
                        self.blockMurSound()
                        return
        
        #Joueur
        for i in range (len(self.__Grid.getGrid())):
            for j in range (len(self.__Grid.getGrid()[i])): #parcours chaque case
                if (self.__Grid.getGrid()[i][j]==2): #si c'est une caisse
                    #test que qu'on n'essaye pas de faire sortir une caisse de la map
                    if ((i==0) and ((i==self.__Grid.getPositionJ()[0]+x)and(j==self.__Grid.getPositionJ()[1]))):
                        self.__Grid.setPositionJ0(1)
                        return 
                    elif ((i==self.__Grid.getNbLigne()-1) and ((i==self.__Grid.getPositionJ()[0]+x)and(j==self.__Grid.getPositionJ()[1]))):
                        self.__Grid.setPositionJ0(self.__Grid.getNbLigne()-2)
                        return
                    elif ((j==0) and ((j==self.__Grid.getPositionJ()[1]+y)and(i==self.__Grid.getPosition()[0]))):
                        self.__Grid.setPositionJ1(1)
                        return 
                    elif ((j==self.__Grid.getNbColonne()-1) and ((j==self.__Grid.getPositionJ()[1]+y)and(i==self.__Grid.getPositionJ()[0]))):
                        self.__Grid.setPositionJ1(self.__Grid.getNbColonne()-2)
                        return
                    #test si il y a une caisse puis un mur ou un trourempli  la ou le joueur se deplace
                    elif (((i==self.__Grid.getPositionJ()[0]+x)and(j==self.__Grid.getPositionJ()[1]+y)) and (self.__Grid.getGrid()[self.__Grid.getPositionJ()[0]+(2*x)][self.__Grid.getPositionJ()[1]+(2*y)]==3 or self.__Grid.getGrid()[self.__Grid.getPositionJ()[0]+(2*x)][self.__Grid.getPositionJ()[1]+(2*y)]==5 or self.__Grid.getGrid()[self.__Grid.getPositionJ()[0]+(2*x)][self.__Grid.getPositionJ()[1]+(2*y)]==2)):
                        self.blockMurSound()
                        return

        if not (0<=self.__Grid.getPositionJ()[0]+x<self.__Grid.getNbLigne()):
            return
        elif not (0<=self.__Grid.getPositionJ()[1]+y<self.__Grid.getNbColonne()):
            self.blockMurSound()
            return
        
        else:
            lgnavt=self.__Grid.getPositionJ()[0]
            colavt =self.__Grid.getPositionJ()[1]
            self.__Grid.setPositionJ0(self.__Grid.getPositionJ()[0]+x)
            self.__Grid.setPositionJ1(self.__Grid.getPositionJ()[1]+y)
            self.__Grid.ajoutPas()

        self.deplacerCai(x,y)
        lgnJ = self.__Grid.getPositionJ()[0] # ligne joueur
        colJ = self.__Grid.getPositionJ()[1] # colonne joueur
        self.__Grid.getGrid()[lgnJ][colJ]=1
        self.__Grid.getGrid()[lgnavt][colavt]=0
        self.__view.UpdateView()
    

    def reset(self):
        self.__Grid.setLevel2(False)
        self.__Grid.setLevel3(False)
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3],"w") #ouvre le ficher
        file.write("True\n"+"False\n"+"False\n") #reset le fichier mets tous les niveaux a false sauf le 1