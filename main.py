import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.sip import setdeleted
from Model.Grid import Grid
from View.GridView import GridView
from Controller.Controle import Controle
from View.LevelMenuView import LevelMenuView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.__model = Grid()
        self.__controller = Controle(self.__model)
        self.__levelView=LevelMenuView(self.__model, self.__controller)
        self.__levelView.show() 

# Main
if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())