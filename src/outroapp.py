import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic

class OutroApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(self.dir_path, 'outroapp.ui'), self)
        self.menu_open = False

        self.toolButton.clicked.connect(lambda: self.slide_menu())

    def slide_menu(self):
        if not self.menu_open:
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

        else:
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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = OutroApp()
    mainwindow.show()
    sys.exit(app.exec_())
