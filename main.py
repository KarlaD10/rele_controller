from ui_main import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.thread = False
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_rele1.clicked.connect(self.rele)

    def rele(self):
        print("Nombre del button"+self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()
