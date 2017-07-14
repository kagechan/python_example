# -*- coding: utf-8 -*-

import sys
from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtWidgets import (QWidget, QLabel, QLineEdit,
                       QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, 
                       QFrame, QSizePolicy, QDialog, QFileDialog, 
                       QTabWidget, QTableWidget, QTableWidgetItem, QApplication)
from qtpy.QtGui import (QPixmap)

class AnswerWindow:
    def __init__(self, parent=None):
        self.w = QDialog()
        self.parent = parent
        self.tables = [] 
        self.initUI()
        
    def closeWindow(self):
         self.w.close()

    def show(self):
        self.w.exec_()

    def initUI(self):
        self.w.setWindowTitle(u'回答結果')
        vbox = QVBoxLayout()
        ansBtn = QPushButton(u"閉じる")
        ansBtn.clicked.connect(self.closeWindow)
        
        self.tabs = QTabWidget()

        for i in [0, 1, 2, 3, 4]:
            tab = QTableWidget()
            tab.setRowCount(10) # あとで10のところは変更してください。
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
        labelN1 = QLabel(u'ダレ量N1長さ')
        labelN2 = QLabel(u'ダレ量N2長さ')
        labelN1S = QLabel(u'ダレ量N1面積')
        labelN2S = QLabel(u'ダレ量N2面積')
        labelImg = QLabel(u'ダレ形状画像')
        self.image    = QLabel();
        self.image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image.setFixedSize(200, 200)
        sel_img_btn = QPushButton(u'ファイル選択')
        
        editN1  = QLineEdit()
        editN2  = QLineEdit()
        editN1S = QLineEdit()
        editN2S = QLineEdit()
        
        grid= QGridLayout()
        grid.setSpacing(10)
        
        # ラベルと入力フォームの作成
        grid.addWidget(labelN1, 1, 0)
        grid.addWidget(editN1,  1, 1)
        grid.addWidget(labelN1S,2, 0)
        grid.addWidget(editN1S, 2, 1)
        
        grid.addWidget(labelN2, 3, 0)
        grid.addWidget(editN2,  3, 1)
        grid.addWidget(labelN2S,4, 0)
        grid.addWidget(editN2S, 4, 1)
        
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