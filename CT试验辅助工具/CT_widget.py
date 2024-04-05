# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CT_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(902, 763)
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        font.setHintingPreference(QFont.PreferFullHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 260, 671, 71))
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setMidLineWidth(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 337, 260))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit_I1e = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_I1e.setObjectName(u"lineEdit_I1e")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_I1e.sizePolicy().hasHeightForWidth())
        self.lineEdit_I1e.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_I1e, 1, 1, 1, 1)

        self.lineEdit_I2e = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_I2e.setObjectName(u"lineEdit_I2e")
        sizePolicy.setHeightForWidth(self.lineEdit_I2e.sizePolicy().hasHeightForWidth())
        self.lineEdit_I2e.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_I2e, 2, 1, 1, 1)

        self.lineEdit_Imax = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Imax.setObjectName(u"lineEdit_Imax")
        sizePolicy.setHeightForWidth(self.lineEdit_Imax.sizePolicy().hasHeightForWidth())
        self.lineEdit_Imax.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_Imax, 0, 1, 1, 1)

        self.lineEdit_U2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_U2.setObjectName(u"lineEdit_U2")
        sizePolicy.setHeightForWidth(self.lineEdit_U2.sizePolicy().hasHeightForWidth())
        self.lineEdit_U2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_U2, 3, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.lineEdit_L_R2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_L_R2.setObjectName(u"lineEdit_L_R2")
        sizePolicy.setHeightForWidth(self.lineEdit_L_R2.sizePolicy().hasHeightForWidth())
        self.lineEdit_L_R2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_L_R2, 4, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_2.addWidget(self.label_19, 5, 0, 1, 1)

        self.lineEdit_Zreal = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Zreal.setObjectName(u"lineEdit_Zreal")
        sizePolicy.setHeightForWidth(self.lineEdit_Zreal.sizePolicy().hasHeightForWidth())
        self.lineEdit_Zreal.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_Zreal, 5, 1, 1, 1)

        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(350, 0, 341, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)

        self.lineEdit_K = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_K.setObjectName(u"lineEdit_K")
        sizePolicy.setHeightForWidth(self.lineEdit_K.sizePolicy().hasHeightForWidth())
        self.lineEdit_K.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_K, 0, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_K1 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_K1.setObjectName(u"lineEdit_K1")
        sizePolicy.setHeightForWidth(self.lineEdit_K1.sizePolicy().hasHeightForWidth())
        self.lineEdit_K1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_K1, 1, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_K2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_K2.setObjectName(u"lineEdit_K2")
        sizePolicy.setHeightForWidth(self.lineEdit_K2.sizePolicy().hasHeightForWidth())
        self.lineEdit_K2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_K2, 2, 1, 1, 1)

        self.btn_culc = QPushButton(Form)
        self.btn_culc.setObjectName(u"btn_culc")
        self.btn_culc.setGeometry(QRect(360, 190, 141, 23))
        self.btn_save2doc = QPushButton(Form)
        self.btn_save2doc.setObjectName(u"btn_save2doc")
        self.btn_save2doc.setGeometry(QRect(360, 220, 141, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CT\u8bd5\u9a8c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u4e8c\u6b21\u7ed5\u7ec4\u6f0f\u6297 Z2", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u7535\u6d41\u500d\u6570    m", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u52b1\u78c1\u7535\u6d41 Io", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u52b1\u78c1\u7535\u52a8\u52bf E", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Z\u5141(\u03a9)", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u5408\u683c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"0", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("Form", u"\u62d0\u70b9\u7535\u538bU2 \uff08\u586b\u5199\uff09\n"
"", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u77ed\u8def\u7535\u6d41Imax(Izd)\uff08\u586b\u5199\uff09\n"
"", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4e8c\u6b21\u4fa7\u989d\u5b9a\u7535\u6d41I2e\uff08\u586b\u5199\uff09\n"
"", None))
        self.lineEdit_I1e.setText("")
        self.lineEdit_I2e.setText("")
        self.lineEdit_Imax.setText("")
        self.lineEdit_U2.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4e00\u6b21\u7535\u6d41I1e  \uff08\u586b\u5199\uff09\n"
"", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u76f4\u6d41\u7535\u963bR2(\u03a9)\uff08\u586b\u5199\uff09\n"
"", None))
        self.lineEdit_L_R2.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"\u5b9e\u9645\u4e8c\u6b21\u8d1f\u62c5Z\u5b9e(\u03a9)\uff08\u586b\u5199\uff09\n"
"", None))
        self.lineEdit_Zreal.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"\u53ef\u9760\u7cfb\u6570k\uff08\u586b\u5199\uff09", None))
        self.lineEdit_K.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"\u7cfb\u6570K1\uff08\u586b\u5199\uff09", None))
        self.lineEdit_K1.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7cfb\u6570K2\uff08\u586b\u5199\uff09", None))
        self.lineEdit_K2.setText("")
        self.btn_culc.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.btn_save2doc.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi

