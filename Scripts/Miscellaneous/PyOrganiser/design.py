# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.todoView = QtWidgets.QListView(self.centralwidget)
        self.todoView.setGeometry(QtCore.QRect(10, 70, 631, 311))
        self.todoView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.todoView.setObjectName("todoView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 356, 184, 45))
        self.widget.setObjectName("widget")
        self.todoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.todoEdit.setGeometry(QtCore.QRect(10, 400, 521, 31))
        self.todoEdit.setObjectName("todoEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(540, 400, 101, 27))
        self.addButton.setObjectName("addButton")
        self.completeButton = QtWidgets.QPushButton(self.centralwidget)
        self.completeButton.setGeometry(QtCore.QRect(439, 440, 91, 27))
        self.completeButton.setObjectName("completeButton")
        self.inCompleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.inCompleteButton.setGeometry(QtCore.QRect(9, 440, 91, 27))
        self.inCompleteButton.setObjectName("inCompleteButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 440, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(540, 440, 101, 27))
        self.deleteButton.setObjectName("deleteButton")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(540, 10, 110, 28))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 5, 18), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Organizer"))
        self.addButton.setText(_translate("MainWindow", "Add Todo"))
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.inCompleteButton.setText(_translate("MainWindow", "Incomplete"))
        self.label.setText(_translate("MainWindow", "Day Scheduler"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
