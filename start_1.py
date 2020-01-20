import main

import os
import pygame
from PyQt5.QtCore import QThread, QSize

from PyQt5.QtGui import QPixmap, QMovie, QPalette, QBrush, QImage
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class StartDialog():

    def __init__(self):
        super().__init__()

        self.__cat_index = -1
        self.__musicTread = MusicPlay()
        self.__musicTread.start()


    @property
    def cat_index(self):
        return self.__cat_index

    @cat_index.setter
    def cat_index(self, index):
        self.__cat_index = index


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setGeometry(600, 300, 640, 480)
        Dialog.setStyleSheet("QWidget {background-color: white;}")

        # 냥이 선택 창
        self.select_cat("next", Dialog)

        # 로고
        self.logo_img = QPixmap()
        self.cat_imgs.load("logo5.png")
        self.logo_img = self.cat_imgs.scaled(QSize(330, 150))
        self.logo_label = QLabel(Dialog)
        self.logo_label.setPixmap(self.logo_img)
        self.logo_label.show()
        self.logo_label.setGeometry(170, 0, 330, 150)


        self.title = QLabel(Dialog)
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("Dialog", "가장 마음에 드는 냥이를 선택하세요"))
        self.title.setStyleSheet(" { font-family: 'Malgun Gothic';}")

        self.title.setGeometry(170, 100, 300, 50)
        # self.title.setReadOnly(True)



        # self.title = QTextEdit(Dialog)
        # self.title.setText("앱 이름")
        # self.title.setStyleSheet("QTextEdit { border-radius: 10px; padding: 10px;}")
        # self.title.setGeometry(QtCore.QRect(200, 20, 200, 100))
        # self.title.setObjectName("title")
        # self.title.setReadOnly(True)

        # previous 버튼
        self.previous_btn = QPushButton(Dialog)
        self.previous_btn.setGeometry(QtCore.QRect(50, 180, 80, 80))
        previous_icon = QtGui.QIcon('previous.png')
        self.previous_btn.setIcon(previous_icon)
        self.previous_btn.setIconSize(QtCore.QSize(80, 80))
        self.previous_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        # next 버튼
        self.next_btn = QPushButton(Dialog)
        self.next_btn.setGeometry(QtCore.QRect(500, 180, 80, 80))
        next_icon = QtGui.QIcon('next.png')
        self.next_btn.setIcon(next_icon)
        self.next_btn.setIconSize(QtCore.QSize(80, 80))
        self.next_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        # # 실행 버튼
        # self.onoff = QDialogButtonBox(Dialog)
        # self.onoff.setGeometry(QtCore.QRect(450, 440, 156, 23))
        # self.onoff.setOrientation(QtCore.Qt.Horizontal)
        # self.onoff.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        # self.onoff.setObjectName("onoff")
        # # self.onoff.accepted.connect(Dialog.accept)
        # # self.onoff.accepted.setIcon( QtGui.QIcon('next.png'))
        # self.onoff.rejected.connect(Dialog.reject)


        # 시작 버튼
        self.select_btn = QPushButton(Dialog)
        self.select_btn.setGeometry(QtCore.QRect(450, 440, 60, 30))
        # select_icon = QtGui.QIcon('next.png')
        # self.select_btn.setIcon(select_icon)
        # self.select_btn.setIconSize(QtCore.QSize(80, 80))
        # self.select_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.select_btn.setText("시작")
        self.select_btn.show()

        # 종료 버튼
        self.exit_btn = QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(550, 440, 60, 30))
        # exit_icon = QtGui.QIcon('next.png')
        # self.exit_btn.setIcon(exit_icon)
        # self.exit_btn.setIconSize(QtCore.QSize(80, 80))
        # self.exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.exit_btn.setText("종료")
        self.exit_btn.show()

        # btn click slot
        self.next_btn.clicked.connect(lambda: self.select_cat("next", Dialog))
        self.previous_btn.clicked.connect(lambda: self.select_cat("previous", Dialog))
        self.exit_btn.clicked.connect(Dialog.reject)
        self.select_btn.clicked.connect(lambda: self.startMainwindow(Dialog))

        # self.select_btn.clicked.connect(self.actionCustomFactors, SIGNAL("triggered()"), self.OnCustomFactorsTriggered)


    # def OnCustomFactorsTriggered(self):
    #     self.customWin = main.mainWindow()
    #     self.customWin.show()
    #     self.connect(self.customWin, SIGNAL("closed()"), self.OnCustomWinClosed)

    def startMainwindow(self, Dialog):
        Dialog.reject()
        print("Hi 1")
        window = main.mainWindow()
        print("Hi 2")
        window.init_window()
        print("Hi 3")
        window.tab1.add_init_box(self.img_path)
        print("Hi 4")
        window.tab1.add_answer_box()
        print("Hi 5")
        window.tab1.add_suggestion_box()
        print("Hi 6")

    # 냥이 사진 select
    def select_cat(self, part, Dialog):
        # 사진 path
        img_path = "./images"
        cat_list = os.listdir(img_path)

        # index 계산
        if part == "previous":
            if self.__cat_index == 0:   # 맨 첫번째인데 previous
                self.__cat_index = len(cat_list)-1
            else:
                self.__cat_index -= 1

        elif part == "next":
            if self.__cat_index == (len(cat_list)-1):   # 맨 마지막인데 next
                self.__cat_index = 0
            else:
                self.__cat_index += 1

        img_path = img_path+"/"+cat_list[self.__cat_index]
        self.img_path = img_path
        print("인덱스" + str(self.__cat_index))
        print(img_path)

        # 캐릭터 보여주기
        self.cat_imgs = QPixmap()
        self.cat_imgs.load(img_path)
        # self.cat_imgs = QImage.fromData(open(img_path, "rb").read(), 'jpg')
        self.cat_imgs = self.cat_imgs.scaled(250, 250)

        self.cat_label = QLabel(Dialog)
        # self.cat_label.setImage(self.cat_imgs)
        self.cat_label.setPixmap(self.cat_imgs)
        self.cat_label.show()
        self.cat_label.setGeometry(180, 140, 250, 250)

class MusicPlay(QThread):
    def __init__(self, parent=None):
        super(MusicPlay, self).__init__(parent)

    def run(self):
        music_file = "./test1.mid"

        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 1024  # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(1)

        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print(" %s 로드" % music_file)
        except pygame.error:
            print(" %s 에러 (%s)" % (music_file, pygame.get_error()))

        pygame.mixer.music.play(-1)

        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#
#     ui = StartDialog()
#     Dialog = QDialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#
#     # sys.exit(app.exec_())
#
