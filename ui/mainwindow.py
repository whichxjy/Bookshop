# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.back_frame = QtWidgets.QFrame(self.centralwidget)
        self.back_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.back_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.back_frame.setObjectName("back_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.back_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.title_frame = QtWidgets.QFrame(self.back_frame)
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.title_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.title_frame)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.title_frame, 0, 0, 1, 1)
        self.btn_back_frame = QtWidgets.QFrame(self.back_frame)
        self.btn_back_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_back_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_back_frame.setObjectName("btn_back_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.btn_back_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.show_stock_Btn = QtWidgets.QPushButton(self.btn_back_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.show_stock_Btn.setFont(font)
        self.show_stock_Btn.setObjectName("show_stock_Btn")
        self.gridLayout_3.addWidget(self.show_stock_Btn, 1, 1, 1, 1)
        self.sale_Btn = QtWidgets.QPushButton(self.btn_back_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.sale_Btn.setFont(font)
        self.sale_Btn.setObjectName("sale_Btn")
        self.gridLayout_3.addWidget(self.sale_Btn, 0, 1, 1, 1)
        self.return_Btn = QtWidgets.QPushButton(self.btn_back_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.return_Btn.setFont(font)
        self.return_Btn.setObjectName("return_Btn")
        self.gridLayout_3.addWidget(self.return_Btn, 3, 1, 1, 1)
        self.statistics_Btn = QtWidgets.QPushButton(self.btn_back_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.statistics_Btn.setFont(font)
        self.statistics_Btn.setObjectName("statistics_Btn")
        self.gridLayout_3.addWidget(self.statistics_Btn, 4, 1, 1, 1)
        self.purchase_Btn = QtWidgets.QPushButton(self.btn_back_frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.purchase_Btn.setFont(font)
        self.purchase_Btn.setObjectName("purchase_Btn")
        self.gridLayout_3.addWidget(self.purchase_Btn, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.btn_back_frame, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.back_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Book Management System", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Bookshop Management System", None, -1))
        self.show_stock_Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Show Stock", None, -1))
        self.sale_Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Sale", None, -1))
        self.return_Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Return", None, -1))
        self.statistics_Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Statistics", None, -1))
        self.purchase_Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Purchase", None, -1))
