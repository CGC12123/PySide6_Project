# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(852, 563)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.gridLayout_3 = QGridLayout(self.Page1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.FramePage1 = QFrame(self.Page1)
        self.FramePage1.setObjectName(u"FramePage1")
        self.FramePage1.setFrameShape(QFrame.StyledPanel)
        self.FramePage1.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.FramePage1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 208, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.P1_lb_showNum = QLabel(self.FramePage1)
        self.P1_lb_showNum.setObjectName(u"P1_lb_showNum")
        self.P1_lb_showNum.setLayoutDirection(Qt.LeftToRight)
        self.P1_lb_showNum.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.P1_lb_showNum, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(349, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.P1_bt_addNum = QPushButton(self.FramePage1)
        self.P1_bt_addNum.setObjectName(u"P1_bt_addNum")

        self.gridLayout_5.addWidget(self.P1_bt_addNum, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.FramePage1, 0, 1, 1, 1)

        self.tabWidget.addTab(self.Page1, "")
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.gridLayout_2 = QGridLayout(self.Page2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FramePage2 = QFrame(self.Page2)
        self.FramePage2.setObjectName(u"FramePage2")
        self.FramePage2.setFrameShape(QFrame.StyledPanel)
        self.FramePage2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.FramePage2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 208, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.P2_lb_showNum = QLabel(self.FramePage2)
        self.P2_lb_showNum.setObjectName(u"P2_lb_showNum")
        self.P2_lb_showNum.setLayoutDirection(Qt.LeftToRight)
        self.P2_lb_showNum.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.P2_lb_showNum, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(349, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.P2_bt_addNum = QPushButton(self.FramePage2)
        self.P2_bt_addNum.setObjectName(u"P2_bt_addNum")

        self.gridLayout_6.addWidget(self.P2_bt_addNum, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.FramePage2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Page2, "")
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.gridLayout_4 = QGridLayout(self.Page3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.FramePage3 = QFrame(self.Page3)
        self.FramePage3.setObjectName(u"FramePage3")
        self.FramePage3.setFrameShape(QFrame.StyledPanel)
        self.FramePage3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.FramePage3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_6 = QSpacerItem(20, 208, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.P3_lb_showNum = QLabel(self.FramePage3)
        self.P3_lb_showNum.setObjectName(u"P3_lb_showNum")
        self.P3_lb_showNum.setLayoutDirection(Qt.LeftToRight)
        self.P3_lb_showNum.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.P3_lb_showNum, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(349, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.P3_bt_addNum = QPushButton(self.FramePage3)
        self.P3_bt_addNum.setObjectName(u"P3_bt_addNum")

        self.gridLayout_7.addWidget(self.P3_bt_addNum, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.FramePage3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Page3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.P1_lb_showNum.setText(QCoreApplication.translate("main", u"1", None))
        self.P1_bt_addNum.setText(QCoreApplication.translate("main", u"Page1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page1), QCoreApplication.translate("main", u"Page1", None))
        self.P2_lb_showNum.setText(QCoreApplication.translate("main", u"2", None))
        self.P2_bt_addNum.setText(QCoreApplication.translate("main", u"Page2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page2), QCoreApplication.translate("main", u"Page2", None))
        self.P3_lb_showNum.setText(QCoreApplication.translate("main", u"3", None))
        self.P3_bt_addNum.setText(QCoreApplication.translate("main", u"Page3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page3), QCoreApplication.translate("main", u"Page3", None))
    # retranslateUi

