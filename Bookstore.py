# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

OrderList = []

class Ui_MainWindow(object):




        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1130, 635)
                MainWindow.setMinimumSize(QtCore.QSize(1130, 635))
                MainWindow.setMaximumSize(QtCore.QSize(1130, 635))
                MainWindow.setStyleSheet("background-image: url(:/BG/bg.png);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(320, 40, 491, 51))
                self.textBrowser.setMinimumSize(QtCore.QSize(491, 51))
                self.textBrowser.setMaximumSize(QtCore.QSize(491, 51))
                self.textBrowser.setStyleSheet("background-image: url(:/BG/W.png);")
                self.textBrowser.setObjectName("textBrowser")
                self.bookstorebutton = QtWidgets.QPushButton(self.centralwidget)
                self.bookstorebutton.setGeometry(QtCore.QRect(60, 200, 201, 61))
                self.bookstorebutton.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 16pt \"Nirmala UI\";")
                self.bookstorebutton.setObjectName("bookstorebutton")
                self.orderButton = QtWidgets.QPushButton(self.centralwidget)
                self.orderButton.setGeometry(QtCore.QRect(60, 280, 201, 61))
                self.orderButton.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 16pt \"Nirmala UI\";")
                self.orderButton.setObjectName("orderButton")


                self.orderButton.clicked.connect(self.showOrder)
                self.abouusButton = QtWidgets.QPushButton(self.centralwidget)
                self.abouusButton.setGeometry(QtCore.QRect(60, 360, 201, 61))
                self.abouusButton.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "\n"
        "font: 75 16pt \"Nirmala UI\";")
                self.abouusButton.setObjectName("abouusButton")
                self.bookstorebutton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.bookstorebutton_2.setGeometry(QtCore.QRect(60, 120, 201, 61))
                self.bookstorebutton_2.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 16pt \"Nirmala UI\";")
                self.bookstorebutton_2.setObjectName("bookstorebutton_2")
                self.frameBookstore = QtWidgets.QFrame(self.centralwidget)
                self.frameBookstore.setGeometry(QtCore.QRect(280, 110, 811, 423))
                self.frameBookstore.setMinimumSize(QtCore.QSize(811, 421))
                self.frameBookstore.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frameBookstore.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frameBookstore.setObjectName("frameBookstore")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameBookstore)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.widget = QtWidgets.QWidget(self.frameBookstore)
                self.widget.setMinimumSize(QtCore.QSize(297, 401))
                self.widget.setMaximumSize(QtCore.QSize(297, 401))
                self.widget.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget.setObjectName("widget")
                self.comboBox = QtWidgets.QComboBox(self.widget)
                self.comboBox.setGeometry(QtCore.QRect(10, 70, 281, 29))
                self.comboBox.setStyleSheet("font: 12pt \"Nirmala UI\";")



                
                self.comboBox.setObjectName("comboBox")
                self.ShowNameBook()
                self.comboBox.currentIndexChanged.connect(self.ShowDetail)
                

                self.label_6 = QtWidgets.QLabel(self.widget)
                self.label_6.setGeometry(QtCore.QRect(10, 20, 277, 32))
                self.label_6.setMinimumSize(QtCore.QSize(277, 30))
                self.label_6.setStyleSheet("font: 16pt \"Nirmala UI\";")
                self.label_6.setObjectName("label_6")
                self.horizontalLayout.addWidget(self.widget)
                self.widget_2 = QtWidgets.QWidget(self.frameBookstore)
                self.widget_2.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget_2.setObjectName("widget_2")
                self.label_7 = QtWidgets.QLabel(self.widget_2)
                self.label_7.setGeometry(QtCore.QRect(140, 10, 211, 30))
                self.label_7.setStyleSheet("font: 16pt \"Nirmala UI\";")
                self.label_7.setObjectName("label_7")
                self.bookstorebutton_3 = QtWidgets.QPushButton(self.widget_2)
                self.bookstorebutton_3.setGeometry(QtCore.QRect(170, 360, 151, 31))
                self.bookstorebutton_3.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 12pt \"Nirmala UI\";")
                self.bookstorebutton_3.setObjectName("bookstorebutton_3")


                self.bookstorebutton_3.clicked.connect(self.addOrder)



                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
                self.plainTextEdit.setGeometry(QtCore.QRect(40, 50, 421, 231))
                self.plainTextEdit.setObjectName("plainTextEdit")

                self.horizontalLayout.addWidget(self.widget_2)
                self.frameBookstore_2 = QtWidgets.QFrame(self.centralwidget)
                self.frameBookstore_2.setGeometry(QtCore.QRect(280, 110, 811, 423))
                self.frameBookstore_2.setMinimumSize(QtCore.QSize(811, 421))
                self.frameBookstore_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frameBookstore_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frameBookstore_2.setObjectName("frameBookstore_2")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameBookstore_2)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.widget_5 = QtWidgets.QWidget(self.frameBookstore_2)
                self.widget_5.setMinimumSize(QtCore.QSize(297, 401))
                self.widget_5.setMaximumSize(QtCore.QSize(297, 401))
                self.widget_5.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget_5.setObjectName("widget_5")
                self.label = QtWidgets.QLabel(self.widget_5)
                self.label.setGeometry(QtCore.QRect(60, 300, 201, 61))
                self.label.setText("")
                self.label.setObjectName("label")
                self.widget_7 = QtWidgets.QWidget(self.widget_5)
                self.widget_7.setGeometry(QtCore.QRect(30, 20, 250, 250))
                self.widget_7.setMinimumSize(QtCore.QSize(250, 250))
                self.widget_7.setMaximumSize(QtCore.QSize(250, 250))
                self.widget_7.setStyleSheet("\n"
        "background-image: url(:/logo/pream.png);")
                self.widget_7.setObjectName("widget_7")
                self.horizontalLayout_3.addWidget(self.widget_5)
                self.widget_6 = QtWidgets.QWidget(self.frameBookstore_2)
                self.widget_6.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget_6.setObjectName("widget_6")
                self.horizontalLayout_3.addWidget(self.widget_6)
                self.frameBookstore_3 = QtWidgets.QFrame(self.centralwidget)
                self.frameBookstore_3.setGeometry(QtCore.QRect(280, 110, 811, 423))
                self.frameBookstore_3.setMinimumSize(QtCore.QSize(811, 421))
                self.frameBookstore_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frameBookstore_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frameBookstore_3.setObjectName("frameBookstore_3")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameBookstore_3)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.widget_4 = QtWidgets.QWidget(self.frameBookstore_3)
                self.widget_4.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget_4.setObjectName("widget_4")
                self.label_9 = QtWidgets.QLabel(self.widget_4)
                self.label_9.setGeometry(QtCore.QRect(290, 20, 201, 61))
                self.label_9.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.widget_4)
                self.label_10.setGeometry(QtCore.QRect(80, 120, 641, 61))
                self.label_10.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.widget_4)
                self.label_11.setGeometry(QtCore.QRect(50, 180, 721, 61))
                self.label_11.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(self.widget_4)
                self.label_12.setGeometry(QtCore.QRect(300, 250, 191, 61))
                self.label_12.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
                self.label_12.setObjectName("label_12")
                self.horizontalLayout_2.addWidget(self.widget_4)
                self.frameOrder = QtWidgets.QFrame(self.centralwidget)
                self.frameOrder.setGeometry(QtCore.QRect(280, 110, 811, 423))
                self.frameOrder.setMinimumSize(QtCore.QSize(811, 421))
                self.frameOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frameOrder.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frameOrder.setObjectName("frameOrder")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameOrder)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.widget_10 = QtWidgets.QWidget(self.frameOrder)
                self.widget_10.setStyleSheet("background-image: url(:/BG/W.png);")
                self.widget_10.setObjectName("widget_10")
                self.label_2 = QtWidgets.QLabel(self.widget_10)
                self.label_2.setGeometry(QtCore.QRect(600, 40, 111, 41))
                self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
        "background-image: url(:/BG/W.png);")
                self.label_2.setObjectName("label_2")
                self.bookstorebutton_4 = QtWidgets.QPushButton(self.widget_10)
                self.bookstorebutton_4.setGeometry(QtCore.QRect(560, 220, 191, 40))
                self.bookstorebutton_4.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 16pt \"Nirmala UI\";")
                self.bookstorebutton_4.setObjectName("bookstorebutton_4")
                self.bookstorebutton_4.clicked.connect(self.buy)

                self.label_3 = QtWidgets.QLabel(self.widget_10)
                self.label_3.setGeometry(QtCore.QRect(180, 20, 191, 41))
                self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
        "")
                self.label_3.setObjectName("label_3")
                self.widget_3 = QtWidgets.QWidget(self.widget_10)
                self.widget_3.setGeometry(QtCore.QRect(370, 210, 120, 80))
                self.widget_3.setObjectName("widget_3")
                self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget_10)
                self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 70, 491, 311))
                self.plainTextEdit_2.setObjectName("plainTextEdit_2")


                self.label_price = QtWidgets.QLabel(self.widget_10)
                self.label_price.setGeometry(QtCore.QRect(650, 80, 51, 41))
                self.label_price.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
        "background-image: url(:/BG/W.png);")
                self.label_price.setObjectName("label_price")


                self.label_8 = QtWidgets.QLabel(self.widget_10)
                self.label_8.setGeometry(QtCore.QRect(700, 80, 51, 41))
                self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
        "background-image: url(:/BG/W.png);")
                self.label_8.setObjectName("label_8")





                self.bookstorebutton_5 = QtWidgets.QPushButton(self.widget_10)
                self.bookstorebutton_5.setGeometry(QtCore.QRect(560, 270, 191, 40))
                self.bookstorebutton_5.setStyleSheet("background-image: url(:/BG/W.png);\n"
        "font: 16pt \"Nirmala UI\";")
                self.bookstorebutton_5.setObjectName("bookstorebutton_5")
                self.bookstorebutton_5.clicked.connect(self.clear)


                self.horizontalLayout_4.addWidget(self.widget_10)
                self.frameBookstore_3.raise_()
                self.frameBookstore_2.raise_()
                self.frameOrder.raise_()
                self.frameBookstore.raise_()
                self.textBrowser.raise_()
                self.bookstorebutton.raise_()
                self.orderButton.raise_()
                self.abouusButton.raise_()
                self.bookstorebutton_2.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 25))
                self.menubar.setObjectName("menubar")
                self.menuHome = QtWidgets.QMenu(self.menubar)
                self.menuHome.setObjectName("menuHome")
                self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
                self.menuAbout_Us.setObjectName("menuAbout_Us")
                self.menuBookstore = QtWidgets.QMenu(self.menubar)
                self.menuBookstore.setObjectName("menuBookstore")
                self.menuORDER = QtWidgets.QMenu(self.menubar)
                self.menuORDER.setObjectName("menuORDER")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.action = QtWidgets.QAction(MainWindow)
                self.action.setObjectName("action")
                self.action_3 = QtWidgets.QAction(MainWindow)
                self.action_3.setObjectName("action_3")
                self.menubar.addAction(self.menuHome.menuAction())
                self.menubar.addAction(self.menuBookstore.menuAction())
                self.menubar.addAction(self.menuORDER.menuAction())
                self.menubar.addAction(self.menuAbout_Us.menuAction())

                self.retranslateUi(MainWindow)
                self.bookstorebutton.clicked.connect(self.frameBookstore.show) # type: ignore
                self.bookstorebutton_2.clicked.connect(self.frameBookstore_2.show) # type: ignore
                self.abouusButton.clicked.connect(self.frameBookstore_3.show) # type: ignore
                self.bookstorebutton_2.clicked.connect(self.frameBookstore.close) # type: ignore
                self.bookstorebutton_2.clicked.connect(self.frameBookstore_3.close) # type: ignore
                self.bookstorebutton.clicked.connect(self.frameBookstore_3.close) # type: ignore
                self.bookstorebutton.clicked.connect(self.frameBookstore_2.close) # type: ignore
                self.abouusButton.clicked.connect(self.frameBookstore.close) # type: ignore
                self.abouusButton.clicked.connect(self.frameBookstore_2.close) # type: ignore
                self.orderButton.clicked.connect(self.frameOrder.show) # type: ignore
                self.abouusButton.clicked.connect(self.frameOrder.close) # type: ignore
                self.bookstorebutton.clicked.connect(self.frameOrder.close) # type: ignore
                self.bookstorebutton_2.clicked.connect(self.frameOrder.close) # type: ignore
                self.orderButton.clicked.connect(self.frameBookstore_2.close) # type: ignore
                self.orderButton.clicked.connect(self.frameBookstore_3.close) # type: ignore
                self.orderButton.clicked.connect(self.frameBookstore.close) # type: ignore
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "โปรแกรมซื้อหนังสือ"))
                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.85455pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">PHOENIX DREAM BOOK</span></p></body></html>"))
                self.bookstorebutton.setText(_translate("MainWindow", "BOOKSTORE"))
                self.orderButton.setText(_translate("MainWindow", "ORDER"))
                self.abouusButton.setText(_translate("MainWindow", "ABout Us"))
                self.bookstorebutton_2.setText(_translate("MainWindow", "HOME"))
                self.label_6.setText(_translate("MainWindow", "          รายการหนังสือ"))
                self.label_7.setText(_translate("MainWindow", " รายละเอียดหนังสือ"))
                self.bookstorebutton_3.setText(_translate("MainWindow", "Add To Order"))

                self.label_9.setText(_translate("MainWindow", "    ผู้จัดทำ"))
                self.label_10.setText(_translate("MainWindow", " นายภัทรพล สมสกุล 116310400294-9"))
                self.label_11.setText(_translate("MainWindow", " นายกรกฤตย ก๋ำนารายณ์ 116310462007-0"))
                self.label_12.setText(_translate("MainWindow", "63146CPE2"))
                self.label_2.setText(_translate("MainWindow", "  Total Price"))
                self.bookstorebutton_4.setText(_translate("MainWindow", "Buy"))
                self.label_3.setText(_translate("MainWindow", "     Order List"))
                self.label_8.setText(_translate("MainWindow", " Bath"))
                self.label_price.setText(_translate("MainWindow", "0"))

                self.bookstorebutton_5.setText(_translate("MainWindow", "clear order"))
                self.menuHome.setTitle(_translate("MainWindow", "HOME"))
                self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))
                self.menuBookstore.setTitle(_translate("MainWindow", "BOOKSTORE"))
                self.menuORDER.setTitle(_translate("MainWindow", "ORDER"))
                self.action.setText(_translate("MainWindow", "รายการหนังสือ"))
                self.action_3.setText(_translate("MainWindow", "รายการสั่งซื้อ"))


        def ShowDetail(self) :
                        self.db = pymysql.connect(host="127.0.0.1", database="bookstore", user="root", password="1234", charset="utf8")
                        self.cur = self.db.cursor()
                        data = self.comboBox.currentText()
                        self.cur.execute(f'SELECT * FROM book WHERE name_book = "{data}";')
                        data = self.cur.fetchall()
                        self.plainTextEdit.clear()
                        for i in data:
                                self.plainTextEdit.insertPlainText(i[1])  
                
        def ShowNameBook(self) :
                        self.db = pymysql.connect(host="127.0.0.1", database="bookstore", user="root", password="1234", charset="utf8")
                        self.cur = self.db.cursor()
                        self.cur.execute('SELECT * FROM book;')
                        data = self.cur.fetchall()
                        
                        for i in data:
                                self.comboBox.addItem(i[0])


        def addOrder (self):
                self.db = pymysql.connect(host="127.0.0.1", database="bookstore", user="root", password="1234", charset="utf8")
                self.cur = self.db.cursor()
                data = self.comboBox.currentText()
                self.cur.execute(f'SELECT * FROM book WHERE name_book = "{data}";')
                data = self.cur.fetchall()
                
                for i in data:
                        OrderList.append(i)

        def showOrder (self):
                price = 0
                self.plainTextEdit_2.clear()
               
                self.db = pymysql.connect(host="127.0.0.1", database="bookstore", user="root", password="1234", charset="utf8")
                self.cur = self.db.cursor()
                
                self.plainTextEdit_2.insertPlainText(f"name :                                                        price :\n")
                for i in OrderList:
                        self.plainTextEdit_2.insertPlainText(f"{i[0]}                                                     {i[2]}\n")
                        price = price + i[2]
                self.label_price.setText(f'{price}')
  
        def clear(self):
                OrderList.clear()
                self.showOrder


        def buy(self):
                print('test')

        import Image_rc

       

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
