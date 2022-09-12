import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic

default_button_style = \
"""
    QToolButton {
        font: 10pt "MS UI Gothic";
        padding-left:10px;
    }

    QToolButton:hover {
        background-color: rgb(60, 60, 60);
    }	
"""

clicked_button_style = \
"""
    QToolButton {
        font: 10pt "MS UI Gothic";
        padding-left:10px;
        border : solid white;
        font-weight: bold;
        border-width : 0px 0px 0px 2px;
    }

    QToolButton:hover {
        background-color: rgb(60, 60, 60);
    }	
"""


class OutroApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(self.dir_path, 'outroapp.ui'), self)
        self.menu_open = False

        self.toolButton.clicked.connect(lambda: self.slide_menu())
        self.toolButton_2.clicked.connect(lambda: self.open_home())
        self.toolButton_3.clicked.connect(lambda: self.open_audio())
        self.toolButton_4.clicked.connect(lambda: self.open_image())
        # self.label = HoverButton(self.label)

    def close_menu(self):
        self.open_animation = QtCore.QPropertyAnimation(self.frame, b"maximumWidth")
        self.open_animation.setDuration(500)
        self.open_animation.setStartValue(150)
        self.open_animation.setEndValue(50)
        self.open_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.open_animation.start()
        self.close_animation = QtCore.QPropertyAnimation(self.frame, b"minimumWidth")
        self.close_animation.setDuration(500)
        self.close_animation.setStartValue(150)
        self.close_animation.setEndValue(50)
        self.close_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.close_animation.start()

        menu_icon = QtGui.QIcon(os.path.join(self.dir_path, 'media', 'icons', 'icons8-menu.svg'))
        self.toolButton.setIcon(menu_icon)
        self.menu_open = False

    def open_menu(self):
        self.open_animation = QtCore.QPropertyAnimation(self.frame, b"maximumWidth")
        self.open_animation.setDuration(500)
        self.open_animation.setStartValue(50)
        self.open_animation.setEndValue(150)
        self.open_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.open_animation.start()
        self.close_animation = QtCore.QPropertyAnimation(self.frame, b"minimumWidth")
        self.close_animation.setDuration(500)
        self.close_animation.setStartValue(50)
        self.close_animation.setEndValue(150)
        self.close_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.close_animation.start()

        close_icon = QtGui.QIcon(os.path.join(self.dir_path, 'media', 'icons', 'icons8-close.svg'))
        self.toolButton.setIcon(close_icon)
        self.menu_open = True

    def side_button_clicked(self, button):
        for child in self.frame.children():
            if child != button and child != self.toolButton:
                child.setStyleSheet(default_button_style)
        button.setStyleSheet(clicked_button_style)

    def slide_menu(self):
        if not self.menu_open:
            self.open_menu()
        else:
            self.close_menu()

    def open_home(self):
        self.side_button_clicked(self.sender())
        if self.menu_open:
            self.close_menu()

    def open_audio(self):
        self.side_button_clicked(self.sender())
        if self.menu_open:
            self.close_menu()

    def open_image(self):
        self.side_button_clicked(self.sender())
        if self.menu_open:
            self.close_menu()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = OutroApp()
    mainwindow.setWindowTitle("MyOutro")
    mainwindow.show()
    sys.exit(app.exec_())
