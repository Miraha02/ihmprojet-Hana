from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QPushButton, QMainWindow, QLabel, QHBoxLayout

class ResetMessage(QMainWindow):
    def __init__(self,controller, View):
        super().__init__()
        self.__controller=controller
        self.__LevelMenuView=View
        messageLayout=QWidget()
        self.setCentralWidget(messageLayout)
        messageLayout.setFixedSize(300,300)

        messageLabel=QLabel("oscour")
        messageLayout.setLayout(QHBoxLayout(messageLabel))

        self.yes=QPushButton("yes")
        self.no=QPushButton("no")

        messageLayout.layout().addWidget(self.yes)
        messageLayout.layout().addWidget(self.no)
        self.yes.clicked.connect(self.yesButton)
        self.no.clicked.connect(self.noButton)
        
    
    def yesButton(self):
        self.__controller.reset()
        self.__LevelMenuView.update()
        self.close()

    def noButton(self):
        self.close()
