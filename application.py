#!python
# -*- coding: utf-8 -*-

import sys
from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtWidgets import (QWidget, QLabel, QLineEdit,
                       QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, 
                       QFrame, QSizePolicy, QDialog, QFileDialog, 
                       QTabWidget, QTableWidget, QTableWidgetItem, 
                       QComboBox, QApplication)
from qtpy.QtGui import (QPixmap)

class AnswerWindow:
    def __init__(self, parent=None, numTab=5):
        self.w = QDialog()
        self.parent = parent
        self.tables = [] 
        self.numTab = numTab
        self.initUI()
        
    def closeWindow(self):
         self.w.close()

    def show(self):
        self.setData()
        self.w.exec_()

    def setData(self, data=None):
        horHeaders = [ u'条件', u'値']
        condNames = [u'線材種', u'回転方向', u'回転速度', u'送り速度',
                     u'切り込み量', u'突き出し量', u'乗せ率', u'パス回数', u'摩耗量']
        for i in range(self.numTab):
            table = self.tables[i]
            table.setHorizontalHeaderLabels(horHeaders)
            for m in condNames:
                item = QTableWidgetItem(m)
                table.setItem(condNames.index(m), 0, item)

    def initUI(self):
        self.w.setWindowTitle(u'回答結果')
        vbox = QVBoxLayout()
        ansBtn = QPushButton(u"閉じる")
        ansBtn.clicked.connect(self.closeWindow)
        
        self.tabs = QTabWidget()

        for i in range(self.numTab):
            tab = QTableWidget()
            tab.setRowCount(9) # あとで9のところは変更してください。
            tab.setColumnCount(2)
            self.tabs.addTab(tab, "第" + str(i + 1) + "候補")
            self.tables.append(tab)

        vbox.addWidget(self.tabs)
        vbox.addWidget(ansBtn)
        self.w.setLayout(vbox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def closeWindow(self):
        self.close()
    
    def showResult(self):
        ans = AnswerWindow(self)
        ans.show()
    
    def initUI(self):
        labelMName = QLabel(u'被削材種')
        labelTN1 = QLabel(u'上面ダレ量（1箇所目）')
        labelTN2 = QLabel(u'上面ダレ量（2箇所目）')
        labelSN1 = QLabel(u'側面ダレ量（1箇所目）')
        labelSN2 = QLabel(u'側面ダレ量（2箇所目）')
        labelN1S = QLabel(u'側面ダレ面積（1箇所目）')
        labelN2S = QLabel(u'側面ダレ面積（2箇所目）')
        labelImg = QLabel(u'ダレ形状画像')
        self.image    = QLabel();
        self.image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image.setFixedSize(200, 200)
        sel_img_btn = QPushButton(u'ファイル選択')
        
        comboMName = QComboBox(self)
        comboMName.addItem(u'材料A')
        comboMName.addItem(u'材料B')

        editTN1 = QLineEdit()
        editTN2 = QLineEdit()
        editSN1 = QLineEdit()
        editSN2 = QLineEdit()
        editN1S = QLineEdit()
        editN2S = QLineEdit()
        
        grid= QGridLayout()
        grid.setSpacing(10)
        
        # ラベルと入力フォームの作成
        grid.addWidget(labelMName, 1, 0)
        grid.addWidget(comboMName, 1, 1)

        grid.addWidget(labelTN1,2, 0)
        grid.addWidget(editTN1, 2, 1)

        grid.addWidget(labelTN2,3, 0)
        grid.addWidget(editTN2, 3, 1)

        grid.addWidget(labelSN1,4, 0)
        grid.addWidget(editSN1, 4, 1)

        grid.addWidget(labelSN2,5, 0)
        grid.addWidget(editSN2, 5, 1)

        grid.addWidget(labelN1S,6, 0)
        grid.addWidget(editN1S, 6, 1)
        
        grid.addWidget(labelN2S,7, 0)
        grid.addWidget(editN2S, 7, 1)
        
        # 画像ファイルの入力・閲覧
        hbox_img = QHBoxLayout()
        hbox_img.addWidget(labelImg)
        hbox_img.addWidget(self.image)
        hbox_img.addWidget(sel_img_btn)
        sel_img_btn.clicked.connect(self.showFileDialog)
        
        recomBtn = QPushButton(u"条件回答")
        recomBtn.clicked.connect(self.showResult)
        exitBtn  = QPushButton(u"終了")
        exitBtn.clicked.connect(self.closeWindow)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(recomBtn)
        hbox.addWidget(exitBtn)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox_img)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.resize(400, 150)
        self.setWindowTitle(u'Xebec Recommendation System')
        self.show()
        
    def showFileDialog(self):
        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        fname = QFileDialog.getOpenFileName(self, u'画像ファイル選択', "C:/")
        pixmap =  QPixmap(fname[0])
        self.image.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())