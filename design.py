# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 395)
        MainWindow.setMinimumSize(QtCore.QSize(640, 395))
        MainWindow.setMaximumSize(QtCore.QSize(640, 395))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(219, 255, 208)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.V0_label = QtWidgets.QLabel(self.centralwidget)
        self.V0_label.setGeometry(QtCore.QRect(20, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.V0_label.setFont(font)
        self.V0_label.setObjectName("V0_label")
        self.A_label = QtWidgets.QLabel(self.centralwidget)
        self.A_label.setGeometry(QtCore.QRect(20, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.A_label.setFont(font)
        self.A_label.setObjectName("A_label")
        self.S_label = QtWidgets.QLabel(self.centralwidget)
        self.S_label.setGeometry(QtCore.QRect(20, 120, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.S_label.setFont(font)
        self.S_label.setObjectName("S_label")
        self.H_label = QtWidgets.QLabel(self.centralwidget)
        self.H_label.setGeometry(QtCore.QRect(20, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.H_label.setFont(font)
        self.H_label.setObjectName("H_label")
        self.V0_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.V0_lineEdit.setGeometry(QtCore.QRect(50, 20, 120, 20))
        self.V0_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.V0_lineEdit.setMaxLength(3)
        self.V0_lineEdit.setObjectName("V0_lineEdit")
        self.A_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.A_lineEdit.setGeometry(QtCore.QRect(50, 70, 120, 21))
        self.A_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.A_lineEdit.setMaxLength(2)
        self.A_lineEdit.setObjectName("A_lineEdit")
        self.S_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.S_lineEdit.setGeometry(QtCore.QRect(50, 120, 120, 20))
        self.S_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.S_lineEdit.setMaxLength(10)
        self.S_lineEdit.setObjectName("S_lineEdit")
        self.H_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.H_lineEdit.setGeometry(QtCore.QRect(50, 170, 120, 20))
        self.H_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.H_lineEdit.setText("")
        self.H_lineEdit.setMaxLength(2)
        self.H_lineEdit.setObjectName("H_lineEdit")
        self.L_label = QtWidgets.QLabel(self.centralwidget)
        self.L_label.setGeometry(QtCore.QRect(20, 250, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_label.setFont(font)
        self.L_label.setObjectName("L_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 220, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 10, 401, 321))
        self.graphicsView.setStyleSheet("background-color:rgb(230, 212, 255)")
        self.graphicsView.setObjectName("graphicsView")
        self.V0_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.V0_unit_label.setGeometry(QtCore.QRect(180, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.V0_unit_label.setFont(font)
        self.V0_unit_label.setObjectName("V0_unit_label")
        self.A_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.A_unit_label.setGeometry(QtCore.QRect(180, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.A_unit_label.setFont(font)
        self.A_unit_label.setObjectName("A_unit_label")
        self.S_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.S_unit_label.setGeometry(QtCore.QRect(180, 120, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.S_unit_label.setFont(font)
        self.S_unit_label.setObjectName("S_unit_label")
        self.H_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.H_unit_label.setGeometry(QtCore.QRect(180, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.H_unit_label.setFont(font)
        self.H_unit_label.setObjectName("H_unit_label")
        self.L_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.L_unit_label.setGeometry(QtCore.QRect(180, 250, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_unit_label.setFont(font)
        self.L_unit_label.setObjectName("L_unit_label")
        self.L_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.L_lineEdit.setGeometry(QtCore.QRect(50, 250, 120, 20))
        self.L_lineEdit.setStyleSheet("background-color: rgb(221, 252, 255);")
        self.L_lineEdit.setReadOnly(True)
        self.L_lineEdit.setObjectName("L_lineEdit")
        self.result_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.result_lineEdit.setGeometry(QtCore.QRect(20, 290, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.result_lineEdit.setFont(font)
        self.result_lineEdit.setAutoFillBackground(False)
        self.result_lineEdit.setStyleSheet("background-color: rgb(221, 252, 255);")
        self.result_lineEdit.setText("")
        self.result_lineEdit.setReadOnly(True)
        self.result_lineEdit.setObjectName("result_lineEdit")
        self.calculate_Button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_Button.setGeometry(QtCore.QRect(10, 340, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.calculate_Button.setFont(font)
        self.calculate_Button.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.calculate_Button.setObjectName("calculate_Button")
        self.visualize_Button = QtWidgets.QPushButton(self.centralwidget)
        self.visualize_Button.setGeometry(QtCore.QRect(329, 340, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.visualize_Button.setFont(font)
        self.visualize_Button.setStyleSheet("background-color: rgb(255, 254, 217);")
        self.visualize_Button.setObjectName("visualize_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(200, 230, 208)")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.graphicsView.setMouseEnabled(x=False, y=False)  # Запрещаем перемещать график
        self.graphicsView.setMenuEnabled(enableMenu=False, enableViewBoxMenu='same')  # Отключаем меню

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ball Fling"))
        self.V0_label.setText(_translate("MainWindow", "V0"))
        self.A_label.setText(_translate("MainWindow", "A "))
        self.S_label.setText(_translate("MainWindow", "S"))
        self.H_label.setText(_translate("MainWindow", "H"))
        self.L_label.setText(_translate("MainWindow", "L"))
        self.V0_unit_label.setText(_translate("MainWindow", "м/с"))
        self.A_unit_label.setText(_translate("MainWindow", "град"))
        self.S_unit_label.setText(_translate("MainWindow", "м"))
        self.H_unit_label.setText(_translate("MainWindow", "м"))
        self.L_unit_label.setText(_translate("MainWindow", "м"))
        self.calculate_Button.setText(_translate("MainWindow", "Посчитать"))
        self.visualize_Button.setText(_translate("MainWindow", "Отобразить"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
