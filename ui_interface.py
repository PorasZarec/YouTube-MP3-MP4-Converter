# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacecUQHqV.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 444)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(767, 593))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.frame_5)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.top_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(620, 340))
        self.label_3.setPixmap(QPixmap(u":/icons/assets/5296522_youtube_youtube logo_icon.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.middle_frame = QFrame(self.frame_5)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.middle_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.middle_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setPixmap(QPixmap(u":/icons/assets/8665779_link_connection_icon.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.middle_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_link_input = QLineEdit(self.middle_frame)
        self.lineEdit_link_input.setObjectName(u"lineEdit_link_input")

        self.horizontalLayout_2.addWidget(self.lineEdit_link_input)

        self.cmbox_type = QComboBox(self.middle_frame)
        self.cmbox_type.addItem("")
        self.cmbox_type.addItem("")
        self.cmbox_type.setObjectName(u"cmbox_type")
        self.cmbox_type.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setBold(True)
        font1.setKerning(True)
        self.cmbox_type.setFont(font1)
        self.cmbox_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmbox_type.setLayoutDirection(Qt.LeftToRight)
        self.cmbox_type.setEditable(False)
        self.cmbox_type.setMaxVisibleItems(2)

        self.horizontalLayout_2.addWidget(self.cmbox_type)


        self.verticalLayout_2.addWidget(self.middle_frame)

        self.bottom_frame = QFrame(self.frame_5)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_download = QPushButton(self.bottom_frame)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setMinimumSize(QSize(200, 0))
        self.btn_download.setMaximumSize(QSize(16777215, 16777215))
        self.btn_download.setFont(font)
        self.btn_download.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/assets/4102578_applications_media_social_youtube_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_download)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.bottom_frame, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font2 = QFont()
        font2.setBold(False)
        self.statusbar.setFont(font2)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.cmbox_type.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter YouTube Link:", None))
        self.cmbox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.cmbox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4", None))

        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

