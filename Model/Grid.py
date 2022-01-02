from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from os import walk

class Grid():

    def __init__(self):
        self.__fichier=None
        self.__Taille=64
        self.__NbLigne=12
        self.__NbColone=12
        self.__grid=[]
        self.__view=None
        self.__controle=None
        #joueur
        self.__xJ=None
        self.__yJ=None
        self.__positionJ=None

        #victoire
        self.__win=False

        #level
        self.__levelActu=1
        self.__levelChoisi=1
        self.__level1=True
        self.__level2=False
        self.__level3=False
        self.choixLevel()

        #nombre de pas
        self.__nbPas=0
    
    def getWin(self):
        return self.__win
    
    def setWin(self, bool):
        self.__win=bool

    def getLevel(self):
        return [self.__level1, self.__level2, self.__level3]

    def setLevel1(self,bool):
        self.__level1=bool
    
    def setLevel2(self,bool):
        self.__level2=bool
    
    def setLevel3(self,bool):
        self.__level3=bool

    def getNbLigne(self):
        return self.__NbLigne

    def getNbColonne(self):
        return self.__NbColone

    def setView(self,view):
        self.__view=view

    def getGrid(self):
        return self.__grid
    
    def getNbPas(self):
        return self.__nbPas

    def ajoutPas(self):
        self.__nbPas+=1

    def generateGrid(self):
        self.__grid=[]
        for i in range (self.__NbLigne):
            self.__grid.append([])
            for j in range (self.__NbColone):
                self.__grid[i].append(0)
    
    def resetPas(self):
        self.__nbPas=0

    def getLevelActu(self):
        return self.__levelActu
    
    def getLevelChoisi(self):
        return self.__levelChoisi
    
    def setLevelChoisi(self, numLevel):
        self.__levelChoisi=numLevel
    

    def getTaille(self):
        return self.__Taille

    def setControle(self,controle):
        self.__controle=controle
    
    def getPositionJ(self):
        return self.__positionJ
    
    def setPositionJ0(self,x):
        self.__positionJ[0]=x

    def setPositionJ1(self,y):
        self.__positionJ[1]=y

    def setView(self,view):
        self.__view=view

    def generateMap1(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][0], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n") #retire le \n
                line=line[0].split(",") #transform la chaine en tableau de charatere
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1: #si il s'agit d'un joueur
                    self.__xJ=i #initialise les coo du joueurs
                    self.__yJ=j
                    self.__positionJ=[self.__xJ,self.__yJ]
            

        
    def generateMap2(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][1], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n")
                line=line[0].split(",")
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1:
                    self.__xJ=i
                    self.__yJ=j
                    self.__positionJ=[self.__xJ,self.__yJ]
    
    def generateMap3(self):
        self.generateGrid()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][2], "r") as file: #ouvre le ficher et le ferme a la sortie
            for i in range (self.__NbLigne):
                line=file.readline()
                line=line.split("\n")
                line=line[0].split(",")
                self.__grid[i]=line
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                self.__grid[i][j]=int(self.__grid[i][j]) #transformation des string en int
                if self.__grid[i][j]==1:
                    self.__xJ=i
                    self.__yJ=j
                    self.__positionJ=[self.__xJ,self.__yJ]
    
    def choixLevel(self): #fonction permettant de savoir quels levels sont accessible
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        with open("Level/"+fileLevel[2][3], "r") as file: #ouvre le ficher et le ferme a la sortie
            line=file.readline() #lie une ligne
            ligne=0
            while line!="": #tant qu'il ya a des lignes
                if line=='True\n':
                    if ligne==0:
                        self.__level1=True
                        self.__levelActu=1
                    elif ligne==1:
                        self.__level2=True
                        self.__levelActu=2
                    elif ligne==2:
                        self.__level3=True
                        self.__levelActu=3
                line=file.readline()
                ligne+=1

    def prochainLevel(self):
        self.__levelActu+=1
        if self.__levelActu==2:
            self.__level2=True
        elif self.__levelActu==3:
            self.__level3=True
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3],"w") #ouvre le ficher
        if self.__level1:
            file.write("True\n") #rentre true pour le level1 (celui ci doit tjr etre a True)
        file.close()
        fileLevel=next(walk("Level")) #parcours les fichiers d'un repertoire
        file=open("Level/"+fileLevel[2][3], "a") #ouvre le ficher
        if  self.__level2: #si on peut passer au level 2
            file.write("True\n") #le level 2 est accessible
        if  self.__level3: #si on peut passer au level 3
            file.write("True\n") #le level 3 est accessible
        file.close() #ferme le fichier (economie)
    
    

