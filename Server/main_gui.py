# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.take_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.take_off_button.setGeometry(QtCore.QRect(760, 70, 100, 40))
        self.take_off_button.setObjectName("take_off_button")
        self.land_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_all_button.setGeometry(QtCore.QRect(890, 70, 91, 40))
        self.land_all_button.setObjectName("land_all_button")
        self.disarm_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_all_button.setGeometry(QtCore.QRect(1010, 70, 101, 40))
        self.disarm_all_button.setStyleSheet("background-color: red\n"
"")
        self.disarm_all_button.setObjectName("disarm_all_button")
        self.take_off_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.take_off_n_button.setGeometry(QtCore.QRect(760, 150, 100, 40))
        self.take_off_n_button.setObjectName("take_off_n_button")
        self.land_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_n_button.setGeometry(QtCore.QRect(890, 150, 91, 40))
        self.land_n_button.setStyleSheet("")
        self.land_n_button.setObjectName("land_n_button")
        self.disarm_n_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_n_button.setGeometry(QtCore.QRect(1010, 150, 101, 40))
        self.disarm_n_button.setStyleSheet("background-color: red\n"
"")
        self.disarm_n_button.setObjectName("disarm_n_button")
        self.take_off_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.take_off_spinBox.setGeometry(QtCore.QRect(790, 120, 50, 22))
        self.take_off_spinBox.setObjectName("take_off_spinBox")
        self.land_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.land_spinBox.setGeometry(QtCore.QRect(910, 120, 50, 22))
        self.land_spinBox.setObjectName("land_spinBox")
        self.disarm_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.disarm_spinBox.setGeometry(QtCore.QRect(1040, 120, 50, 22))
        self.disarm_spinBox.setObjectName("disarm_spinBox")
        self.control_console_label = QtWidgets.QLabel(self.centralwidget)
        self.control_console_label.setGeometry(QtCore.QRect(840, 20, 200, 20))
        self.control_console_label.setAlignment(QtCore.Qt.AlignCenter)
        self.control_console_label.setObjectName("control_console_label")
        self.turn_on_led_button = QtWidgets.QPushButton(self.centralwidget)
        self.turn_on_led_button.setGeometry(QtCore.QRect(1140, 60, 100, 61))
        self.turn_on_led_button.setStyleSheet("")
        self.turn_on_led_button.setObjectName("turn_on_led_button")
        self.turn_off_led_button = QtWidgets.QPushButton(self.centralwidget)
        self.turn_off_led_button.setGeometry(QtCore.QRect(1140, 140, 100, 61))
        self.turn_off_led_button.setObjectName("turn_off_led_button")
        self.stop_swarm_but = QtWidgets.QPushButton(self.centralwidget)
        self.stop_swarm_but.setGeometry(QtCore.QRect(220, 510, 141, 51))
        self.stop_swarm_but.setStyleSheet("")
        self.stop_swarm_but.setObjectName("stop_swarm_but")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(620, 60, 111, 40))
        self.connect_button.setStyleSheet("")
        self.connect_button.setObjectName("connect_button")
        self.swarm_size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.swarm_size_spinBox.setGeometry(QtCore.QRect(260, 80, 50, 20))
        self.swarm_size_spinBox.setObjectName("swarm_size_spinBox")
        self.swarm_size_label = QtWidgets.QLabel(self.centralwidget)
        self.swarm_size_label.setGeometry(QtCore.QRect(240, 50, 100, 20))
        self.swarm_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.swarm_size_label.setObjectName("swarm_size_label")
        self.send_command_label = QtWidgets.QLabel(self.centralwidget)
        self.send_command_label.setGeometry(QtCore.QRect(840, 260, 200, 20))
        self.send_command_label.setAlignment(QtCore.Qt.AlignCenter)
        self.send_command_label.setObjectName("send_command_label")
        self.console_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.console_textEdit.setGeometry(QtCore.QRect(640, 290, 591, 271))
        self.console_textEdit.setStyleSheet("background-color: rgb(1, 36, 86)")
        self.console_textEdit.setObjectName("console_textEdit")
        self.show_3d_scene_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_3d_scene_button.setGeometry(QtCore.QRect(220, 300, 141, 51))
        self.show_3d_scene_button.setStyleSheet("")
        self.show_3d_scene_button.setObjectName("show_3d_scene_button")
        self.upload_animation_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_animation_button.setGeometry(QtCore.QRect(220, 370, 141, 51))
        self.upload_animation_button.setStyleSheet("")
        self.upload_animation_button.setObjectName("upload_animation_button")
        self.state_label = QtWidgets.QLabel(self.centralwidget)
        self.state_label.setGeometry(QtCore.QRect(220, 160, 131, 41))
        self.state_label.setStyleSheet("color: red\n"
"\n"
"")
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.statement_swarm_label = QtWidgets.QLabel(self.centralwidget)
        self.statement_swarm_label.setGeometry(QtCore.QRect(230, 140, 111, 20))
        self.statement_swarm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.statement_swarm_label.setObjectName("statement_swarm_label")
        self.start_animation_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_animation_button.setGeometry(QtCore.QRect(220, 440, 141, 51))
        self.start_animation_button.setStyleSheet("")
        self.start_animation_button.setObjectName("start_animation_button")
        self.back_label = QtWidgets.QLabel(self.centralwidget)
        self.back_label.setGeometry(QtCore.QRect(0, -1, 1280, 701))
        self.back_label.setObjectName("back_label")
        self.safty_button = QtWidgets.QPushButton(self.centralwidget)
        self.safty_button.setGeometry(QtCore.QRect(620, 110, 111, 40))
        self.safty_button.setStyleSheet("")
        self.safty_button.setObjectName("safty_button")
        self.synch_button = QtWidgets.QPushButton(self.centralwidget)
        self.synch_button.setGeometry(QtCore.QRect(620, 160, 111, 40))
        self.synch_button.setStyleSheet("")
        self.synch_button.setObjectName("synch_button")
        self.time_to_start_label = QtWidgets.QLabel(self.centralwidget)
        self.time_to_start_label.setGeometry(QtCore.QRect(220, 200, 141, 51))
        self.time_to_start_label.setStyleSheet("color:rgb(30, 30, 30)")
        self.time_to_start_label.setObjectName("time_to_start_label")
        self.back_label.raise_()
        self.take_off_button.raise_()
        self.land_all_button.raise_()
        self.disarm_all_button.raise_()
        self.take_off_n_button.raise_()
        self.land_n_button.raise_()
        self.disarm_n_button.raise_()
        self.take_off_spinBox.raise_()
        self.land_spinBox.raise_()
        self.disarm_spinBox.raise_()
        self.control_console_label.raise_()
        self.turn_on_led_button.raise_()
        self.turn_off_led_button.raise_()
        self.stop_swarm_but.raise_()
        self.connect_button.raise_()
        self.swarm_size_spinBox.raise_()
        self.swarm_size_label.raise_()
        self.send_command_label.raise_()
        self.console_textEdit.raise_()
        self.show_3d_scene_button.raise_()
        self.upload_animation_button.raise_()
        self.state_label.raise_()
        self.statement_swarm_label.raise_()
        self.start_animation_button.raise_()
        self.safty_button.raise_()
        self.synch_button.raise_()
        self.time_to_start_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drone Swarm"))
        self.take_off_button.setText(_translate("MainWindow", "Take off all"))
        self.land_all_button.setText(_translate("MainWindow", "Land all"))
        self.disarm_all_button.setText(_translate("MainWindow", "Disarm all"))
        self.take_off_n_button.setText(_translate("MainWindow", "Take off n"))
        self.land_n_button.setText(_translate("MainWindow", "Land n"))
        self.disarm_n_button.setText(_translate("MainWindow", "Disarm n"))
        self.control_console_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Control console</span></p></body></html>"))
        self.turn_on_led_button.setText(_translate("MainWindow", "Turn on Leds"))
        self.turn_off_led_button.setText(_translate("MainWindow", "Turn off Leds"))
        self.stop_swarm_but.setText(_translate("MainWindow", "Stop swarm"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.swarm_size_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Swarm Size</span></p></body></html>"))
        self.send_command_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Send command</span></p></body></html>"))
        self.console_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; color:#ffffff;\">...</span></p></body></html>"))
        self.show_3d_scene_button.setText(_translate("MainWindow", "Show 3d scene"))
        self.upload_animation_button.setText(_translate("MainWindow", "Upload animation"))
        self.state_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Disconnect</span></p></body></html>"))
        self.statement_swarm_label.setText(_translate("MainWindow", "Statement swarm"))
        self.start_animation_button.setText(_translate("MainWindow", "Start animation"))
        self.back_label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/back/back.png\"/></p></body></html>"))
        self.safty_button.setText(_translate("MainWindow", "Safty check"))
        self.synch_button.setText(_translate("MainWindow", "Synchronize"))
        self.time_to_start_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\"/></p></body></html>"))

import back_1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

