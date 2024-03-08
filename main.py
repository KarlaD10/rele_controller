from ui_main import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.thread = False
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()
