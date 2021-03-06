#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,QComboBox,QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap,QIcon
from datetime import datetime
import time
from utils import covid_info,covid_table
import matplotlib.pyplot as plt

#information
covid_result=covid_info(0,0)
pic_table = covid_table()
#button
btn_x = 200
class button(QPushButton):
    def __init__(self,f,t,y):
        QPushButton.__init__(self,f)
        self.resize(200,50)
        self.setText(t)
        self.move(btn_x,y)
#time
mytime = time.localtime()
if mytime.tm_hour < 12:
    str_hello='早上好！'
elif mytime.tm_hour<18:
    str_hello='下午好！'
else:
    str_hello='晚上好！'
#UI
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
        self.resize(600,600)

        hello = QLabel(self)
        hello.setText(str_hello)
        hello.resize(200,30)
        moji_x=130
        moji_y=35
        hello.move(moji_x,moji_y)

        date_time = QLabel(self)
        dt=str(datetime.now())
        date_time.setText(dt)
        date_time.resize(500,30)
        date_time.move(moji_x,moji_y+20)

        moji_coun = QLabel(self)
        country_number=covid_result.country()
        moji_coun.setText(country_number)
        moji_coun.resize(600,220)
        moji_coun.move(10,100)

class CTlab(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('疫情信息助手')
        self.resize(700,700)
        self.setWordWrap(True)
    def showlab(self,t):
        self.setText(t)
        self.show()

class area_tab(tuple):
    def pro_area(self):
        re_area = ' '
        for i in self:
            re_area += i+"\n"
        re_area = re_area[10:]
        return(re_area)

app = QApplication(sys.argv)
ex = covid_info_ui()
lab_city=CTlab()
#combobox
btn_y = 340
f = open("prov.txt", "r",encoding="utf-8")
combo = QComboBox(ex)
combo.resize(120,50)
combo.move(50,btn_y)
for line in f.readlines():
    line=line.strip()
    combo.addItem(line)
f.close()
#button
btn_1 = button(ex,'省市简报',btn_y)
btn_2 = button(ex,'省市中高风险区',btn_y+50)
btn_3 = button(ex,'新增确诊趋势图',btn_y+100)
btn_4 = button(ex,'新增无症状趋势图',btn_y+150)
btn_1.clicked.connect(lambda:lab_city.showlab(covid_result.city(combo.currentText())))
btn_2.clicked.connect(lambda:lab_city.showlab(area_tab.pro_area(covid_result.area(combo.currentText()))))
def win_plt():
    plt.plot(pic_table.date,pic_table.numc_list)
    plt.show()
btn_3.clicked.connect(lambda:win_plt())
def no_plt():
    plt.plot(pic_table.date,pic_table.numl_list)
    plt.show()
btn_4.clicked.connect(lambda:no_plt())
#warningUI
dlg = QDialog()
def understand():
    ex.show()
    dlg.done(1)
dlg.setWindowTitle('警告！')
dlg.resize(1000, 200)
warn_icon = QIcon()
warn_icon.addPixmap(QPixmap('noun-warning-1559852.png'))
dlg.setWindowIcon(warn_icon)
lab_warning = QLabel(dlg)
lab_warning.setText('本软件仅提供数据汇总，数据来源均为国家卫健委。\n继续使用意味着您理解：本软件不对数据真实性负任何责任，不可以作为任何医疗建议！\n感谢您的使用！')
lab_warning.move(10,10)
btn_warn=button(dlg,'我理解以上声明',100)
btn_warn.move(370,120)
btn_warn.clicked.connect(lambda:understand())

dlg.show()
sys.exit(app.exec())