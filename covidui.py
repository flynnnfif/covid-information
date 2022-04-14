#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,QComboBox,QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QPixmap,QIcon
from datetime import datetime
import time

#button
btn_x = 200
class button(QPushButton):
    def __init__(self,f,t,y):
        QPushButton.__init__(self,f)
        self.resize(200,50)
        self.setText(t)
        self.move(btn_x,y)

mytime = time.localtime()
if mytime.tm_hour < 12:
    str_hello='早上好！'
elif mytime.tm_hour<18:
    str_hello='下午好！'
else:
    str_hello='晚上好！'
class covid_info_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("疫情信息助手")
        icon = QIcon()
        icon.addPixmap(QPixmap('noun-coronavirus-3377862.png'))
        self.setWindowIcon(icon)

        label = QLabel(self)
        pixmap = QPixmap('noun-man-4325221.png').scaledToHeight(100)
        label.resize(100,100)
        label.setPixmap(pixmap)
        label.move(0,0)
        self.resize(500,500)
        hello = QLabel(self)
        hello.setText(str_hello)
        hello.resize(200,30)
        hello.move(100,0)
        date_time = QLabel(self)
        dt=str(datetime.now())
        date_time.setText(dt)
        date_time.resize(500,30)
        date_time.move(100,30)
        
        

app = QApplication(sys.argv)
ex = covid_info_ui()

btn_y = 110
btn_1 = button(ex,'城市数据',btn_y)
btn_2 = button(ex,'城市中高风险区',btn_y+50)
btn_3 = button(ex,'详细疫情数据',btn_y+100)



dlg = QDialog()
dlg.setWindowTitle('疫情信息助手')
dlg.resize(500, 500)



#combobox
f = open("prov.txt", "r",encoding="utf-8")
combo = QComboBox(ex)
combo.resize(120,50)
combo.move(50,btn_y)
for line in f.readlines():
    line=line.strip()
    combo.addItem(line)
f.close()
btn_1.clicked.connect(lambda:print(combo.currentText()))




ex.show()
sys.exit(app.exec())

