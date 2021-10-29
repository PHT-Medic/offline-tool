# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dynamic_ModelPage_new2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
#
#from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from visualisation.label_dictionary import Model_Page_labels


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        MainWindow.setMinimumSize(QtCore.QSize(552, 515))
        self.setStyleSheet("background-color: #e6e6e6;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(40, 30, 40, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(25, -1, 25, 20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 24))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 2, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(280, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setContentsMargins(40, 25, 40, 15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem1, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 283, 123))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_5.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(40, 30, 40, 30)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 2, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label.setStyleSheet("font: 14px Arial")
        self.label_2.setStyleSheet("font: 14px Arial")
        self.label_3.setStyleSheet("font: 14px Arial")
        self.label_4.setStyleSheet("font: 16px Arial")
        self.label_5.setStyleSheet("font: 14px Arial; border 0px;")
        self.label_6.setStyleSheet("font: 14px Arial")
        self.pushButton.setStyleSheet("font: 14px Arial")
        self.pushButton_2.setStyleSheet("font: 14px Arial")
        self.pushButton_3.setStyleSheet("font: 14px Arial")
        self.pushButton_4.setStyleSheet("font: 14px Arial")
        self.pushButton_5.setStyleSheet("font: 14px Arial")
        self.pushButton_6.setStyleSheet("font: 14px Arial")
        self.pushButton_7.setStyleSheet("font: 14px Arial")

        # self.scrollAreaWidgetContents.setStyleSheet("background-color: #f2f2f2; border:1.5px solid #b3b3b3;")
        # self.label_5.setStyleSheet("background-color:white; border:1.5px solid #b3b3b3; font: 14px Arial;")
        self.listWidget.setStyleSheet("""QListWidget{background: #f2f2f2;  border:1.5px solid #b3b3b3;}""")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PHT offline tool"))
        self.pushButton.setText(_translate("MainWindow", "Select model files directory"))
        self.label.setText(_translate("MainWindow", "No directory chosen yet"))
        self.pushButton_7.setText(_translate("MainWindow", "Secure Addition Page"))
        self.label_6.setText(_translate("MainWindow", "Select the model directory first"))
        self.label_4.setText(_translate("MainWindow", "List of Modelfiles"))
        self.label_5.setText(_translate("MainWindow", "No models selected yet"))
        self.pushButton_4.setText(_translate("MainWindow", "Decrypt selected models"))
        self.pushButton_6.setText(_translate("MainWindow", "Show decrypted files"))
        self.pushButton_5.setText(_translate("MainWindow", "Return "))
        self.label_2.setText(_translate("MainWindow", "No train config selected"))
        self.pushButton_3.setText(_translate("MainWindow", "Pick and load private key"))
        self.pushButton_2.setText(_translate("MainWindow", "Select train_config.json"))
        self.label_3.setText(_translate("MainWindow", "No private key selected yet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
