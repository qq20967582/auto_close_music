# -*- encoding: utf-8 -*-

import os
import sys
import time
import psutil
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

    def judgeprocess(self, processname):
        pl = psutil.pids()
        for pid in pl:
            if psutil.Process(pid).name() == processname:
                print(pid)
                return True

    def close_music_thread(self):
        close_music_thread = threading.Thread(target=self.close_music, daemon=True)
        close_music_thread.start()

    def close_music(self):
        while True:
            now_time = time.strftime("%H", time.localtime())
            try:
                if int(now_time) >= 22 and self.judgeprocess("QQMusic.exe") or int(now_time) <= 7 and self.judgeprocess("QQMusic.exe"):
                    # QQ音乐
                    os.system(r'taskkill /F /IM QQMusic.exe')
                elif int(now_time) >= 22 and self.judgeprocess("KuGou.exe") or int(now_time) <= 7 and self.judgeprocess("KuGou.exe"):
                    # 酷狗音乐
                    os.system(r'taskkill /F /IM KuGou.exe')
                elif int(now_time) >= 22 and self.judgeprocess("cloudmusic.exe") or int(now_time) <= 7 and self.judgeprocess("cloudmusic.exe"):
                    # 网易云音乐
                    os.system(r'taskkill /F /IM cloudmusic.exe')
            except Exception as e:
                print(e)
            time.sleep(10)


if __name__ == '__main__':
    # 设置表格样式为Fusion
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = AutoCloseMusic()
    ui.setupUi(mainWindow)
    mainWindow.show()
    mainWindow.setWindowTitle("定时自动关闭音乐 Ver 1.0.1")
    sys.exit(app.exec_())
