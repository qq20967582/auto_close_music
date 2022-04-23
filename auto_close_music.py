# -*- encoding: utf-8 -*-

import os
import sys
import time
import threading
from auto_close_music_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory


class AutoCloseMusic(Ui_MainWindow):
    def __init__(self):
        super(AutoCloseMusic, self).__init__()
        self.close_music_thread()

    def setupUi(self, MainWindow):
        super(AutoCloseMusic, self).setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        super(AutoCloseMusic, self).retranslateUi(MainWindow)

    def close_music_thread(self):
        close_music_thread = threading.Thread(target=self.close_music, daemon=True)
        close_music_thread.start()

    def close_music(self):
        while True:
            now_time = time.strftime("%H", time.localtime())
            print(now_time)
            try:
                if now_time >= "22" or now_time <= "07":
                    # QQ音乐
                    os.system(r'taskkill /F /IM QQMusic.exe')
                    # 酷狗音乐
                    os.system(r'taskkill /F /IM KuGou.exe')
                    # 网易云音乐
                    os.system(r'taskkill /F /IM cloudmusic.exe')
            except Exception as e:
                print(e)
            time.sleep(5)


if __name__ == '__main__':
    # 设置表格样式为Fusion
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = AutoCloseMusic()
    ui.setupUi(mainWindow)
    mainWindow.show()
    mainWindow.setWindowTitle("自动关闭音乐播放器 Ver 1.0.1")
    sys.exit(app.exec_())
