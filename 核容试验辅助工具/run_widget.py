# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(902, 763)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 281, 295))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_2.addWidget(self.dateEdit, 6, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 10, 0, 1, 1)

        self.btn_run = QPushButton(self.gridLayoutWidget_2)
        self.btn_run.setObjectName(u"btn_run")

        self.gridLayout_2.addWidget(self.btn_run, 11, 0, 1, 2)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 9, 0, 1, 1)

        self.radioButton_remain = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_remain.setObjectName(u"radioButton_remain")
        self.radioButton_remain.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_remain, 8, 0, 1, 1)

        self.lineEdit_random_value = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_random_value.setObjectName(u"lineEdit_random_value")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_random_value.sizePolicy().hasHeightForWidth())
        self.lineEdit_random_value.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_random_value, 10, 1, 1, 1)

        self.timeEdit = QTimeEdit(self.gridLayoutWidget_2)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout_2.addWidget(self.timeEdit, 7, 1, 1, 1)

        self.radioButton_submit = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_submit.setObjectName(u"radioButton_submit")

        self.gridLayout_2.addWidget(self.radioButton_submit, 8, 1, 1, 1)

        self.lineEdit_battery_capacity = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_battery_capacity.setObjectName(u"lineEdit_battery_capacity")
        sizePolicy.setHeightForWidth(self.lineEdit_battery_capacity.sizePolicy().hasHeightForWidth())
        self.lineEdit_battery_capacity.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_battery_capacity, 4, 1, 1, 1)

        self.comboBox_voltage = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_voltage.addItem("")
        self.comboBox_voltage.addItem("")
        self.comboBox_voltage.setObjectName(u"comboBox_voltage")

        self.gridLayout_2.addWidget(self.comboBox_voltage, 3, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        sizePolicy.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_name, 1, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.comboBox_choose = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_choose.addItem("")
        self.comboBox_choose.addItem("")
        self.comboBox_choose.setObjectName(u"comboBox_choose")

        self.gridLayout_2.addWidget(self.comboBox_choose, 2, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.btn_openfile = QPushButton(self.gridLayoutWidget_2)
        self.btn_openfile.setObjectName(u"btn_openfile")

        self.gridLayout_2.addWidget(self.btn_openfile, 9, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)

        self.lineEdit_person = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_person.setObjectName(u"lineEdit_person")
        sizePolicy.setHeightForWidth(self.lineEdit_person.sizePolicy().hasHeightForWidth())
        self.lineEdit_person.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit_person, 5, 1, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(300, 10, 351, 111))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CT\u8bd5\u9a8c", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u53d8\u7535\u7ad9\u540d\u79f0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u53d8\u5316\u5e45\u5ea6", None))
        self.btn_run.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u65e5\u671f/\u65f6\u95f4", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u6863", None))
        self.radioButton_remain.setText(QCoreApplication.translate("Form", u"\u81ea\u5df1\u7559\u5b58", None))
        self.lineEdit_random_value.setText(QCoreApplication.translate("Form", u"0.005", None))
        self.radioButton_submit.setText(QCoreApplication.translate("Form", u"\u76d1\u7406\u6587\u6863", None))
        self.lineEdit_battery_capacity.setText(QCoreApplication.translate("Form", u"300", None))
        self.comboBox_voltage.setItemText(0, QCoreApplication.translate("Form", u"220kV", None))
        self.comboBox_voltage.setItemText(1, QCoreApplication.translate("Form", u"66kV", None))

        self.label_14.setText(QCoreApplication.translate("Form", u"\u7535\u538b\u7b49\u7ea7", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u84c4\u7535\u6c60\u7ec4", None))
        self.lineEdit_name.setText(QCoreApplication.translate("Form", u"\u5929\u534e", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8bd5\u9a8c\u5f00\u59cb\u65f6\u95f4", None))
        self.comboBox_choose.setItemText(0, QCoreApplication.translate("Form", u"\u7b2c\u4e00\u7ec4", None))
        self.comboBox_choose.setItemText(1, QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u7ec4", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"\u84c4\u7535\u6c60\u7ec4\u5bb9\u91cf", None))
        self.btn_openfile.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6a21\u7248\u6587\u6863", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u8bd5\u9a8c\u4eba", None))
        self.lineEdit_person.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bf4\u660e\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u76f4\u63a5\u4fdd\u5b58\u5230\u684c\u9762</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">66kV\u7559\u5b58\u6587\u4ef6\u91cc\u53ea\u6709\u7b2c\u4e00\u5957\u84c4\u7535"
                        "\u6c60\u7ec4\uff0c\u4e0d\u9002\u7528\u4e8e\u548c\u5e73I II\u5957</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9ed8\u8ba4104\u5757\uff0c\u4e0d\u652f\u6301\u7279\u6b8a\u60c5\u51b5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6a21\u7248\u6587\u4ef6\u5df2\u5185\u7f6e\uff0c\u53ef\u4e0d\u9009</p></body></html>", None))
    # retranslateUi

