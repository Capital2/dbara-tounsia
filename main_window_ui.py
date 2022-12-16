# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(698, 413)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("color: rgb(0, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alling = QtWidgets.QListWidget(self.centralwidget)
        self.alling.setStyleSheet("")
        self.alling.setFrameShape(QtWidgets.QFrame.Box)
        self.alling.setMovement(QtWidgets.QListView.Free)
        self.alling.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.alling.setViewMode(QtWidgets.QListView.IconMode)
        self.alling.setWordWrap(False)
        self.alling.setObjectName("alling")
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.alling.addItem(item)
        self.horizontalLayout.addWidget(self.alling)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.ing = QtWidgets.QListWidget(self.centralwidget)
        self.ing.setStyleSheet("")
        self.ing.setFrameShape(QtWidgets.QFrame.Box)
        self.ing.setSelectionRectVisible(False)
        self.ing.setObjectName("ing")
        self.gridLayout_2.addWidget(self.ing, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.ing.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.alling.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.ing.clear) # type: ignore
        self.pushButton.clicked.connect(MainWindow.addToIng) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.removeFromIng) # type: ignore
        self.pushButton_4.clicked.connect(MainWindow.suggest_recipe) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dbara Tounsia"))
        self.pushButton_4.setText(_translate("MainWindow", "kolli chnekel"))
        self.label.setText(_translate("MainWindow", "Q\'avez vous dans le réfrégirateur?"))
        self.alling.setSortingEnabled(True)
        __sortingEnabled = self.alling.isSortingEnabled()
        self.alling.setSortingEnabled(False)
        item = self.alling.item(0)
        item.setText(_translate("MainWindow", "citrouille"))
        item = self.alling.item(1)
        item.setText(_translate("MainWindow", "fromage"))
        item = self.alling.item(2)
        item.setText(_translate("MainWindow", "oeuf"))
        item = self.alling.item(3)
        item.setText(_translate("MainWindow", "oignon"))
        item = self.alling.item(4)
        item.setText(_translate("MainWindow", "patata"))
        item = self.alling.item(5)
        item.setText(_translate("MainWindow", "piment"))
        item = self.alling.item(6)
        item.setText(_translate("MainWindow", "poivron"))
        item = self.alling.item(7)
        item.setText(_translate("MainWindow", "thon"))
        item = self.alling.item(8)
        item.setText(_translate("MainWindow", "tomate"))
        item = self.alling.item(9)
        item.setText(_translate("MainWindow", "viande"))
        self.alling.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "retirer"))
        self.pushButton.setText(_translate("MainWindow", "ajouter"))
        self.pushButton_2.setText(_translate("MainWindow", "vider"))
