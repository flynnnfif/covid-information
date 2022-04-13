#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,QComboBox
import utils


app = QApplication(sys.argv)
dlg = QDialog()
dlg.setWindowTitle('covid')
dlg.resize(500, 500)

btn = QPushButton(dlg)
btn.resize(200, 50)
btn.setText('click it!')
btn.move(100, 100)
f = open("prov.txt", "r",encoding="utf-8")
combo = QComboBox(dlg)

for line in f.readlines():
    line=line.strip()
    combo.addItem(line)
f.close()


dlg.show()
sys.exit(app.exec())

