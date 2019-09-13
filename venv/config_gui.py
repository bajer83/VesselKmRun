# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 169))
        Dialog.setMaximumSize(QtCore.QSize(400, 169))
        Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tCPListeningPortLabel = QtWidgets.QLabel(Dialog)
        self.tCPListeningPortLabel.setObjectName("tCPListeningPortLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tCPListeningPortLabel)
        self.tCPListeningPortSpinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tCPListeningPortSpinBox.sizePolicy().hasHeightForWidth())
        self.tCPListeningPortSpinBox.setSizePolicy(sizePolicy)
        self.tCPListeningPortSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tCPListeningPortSpinBox.setMinimum(2000)
        self.tCPListeningPortSpinBox.setMaximum(65000)
        self.tCPListeningPortSpinBox.setProperty("value", 3003)
        self.tCPListeningPortSpinBox.setObjectName("tCPListeningPortSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tCPListeningPortSpinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_server_btn = QtWidgets.QPushButton(Dialog)
        self.start_server_btn.setObjectName("start_server_btn")
        self.horizontalLayout_3.addWidget(self.start_server_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configuration"))
        self.label.setText(_translate("Dialog", "Settings:"))
        self.tCPListeningPortLabel.setText(_translate("Dialog", "TCP listening port:"))
        self.start_server_btn.setText(_translate("Dialog", "Connect to UDP"))
        self.close_btn.setText(_translate("Dialog", "Close"))
