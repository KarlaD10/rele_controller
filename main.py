from ui_main import *
from functools import partial
from PyQt5.Qt import *
import RPi.GPIO as GPIO
cont = 0;
pinControlRelay = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# Configura el pin del LED
led_pin = 18  # Cambia este número al pin que estés utilizando

# Inicializar la configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinControlRelay, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

# Configura el pin GPIO para generar una señal PWM
pwm_freq = 1000  # Frecuencia PWM en Hz (puedes ajustarla)
pwm = GPIO.PWM(led_pin, pwm_freq)

# Inicia la señal PWM con un ciclo de trabajo del 100% (LED encendido)
pwm.start(100)


class MainWindow(QtWidgets.QMainWindow):
    # Definir los pines GPIO utilizados para controlar los relés
    def __init__(self):
        self.thread = False
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_rele1.stateChanged.connect(self.debug)
        self.ui.btn_rele2.stateChanged.connect(self.btn2)
        self.ui.pushButton_17.clicked.connect(partial(self.variador, "menos"))
        self.ui.btn_aunmentar.clicked.connect(partial(self.variador, "mas"))

    def debug(self):
        if self.ui.btn_rele1.isChecked():
            GPIO.output(pinControlRelay[2], GPIO.LOW)
        else:
            GPIO.output(pinControlRelay[2], GPIO.LOW)

    def btn2(self):
        if self.ui.btn_rele1.isChecked():
            GPIO.output(pinControlRelay[3], GPIO.HIGH)
        else:
            GPIO.output(pinControlRelay[3], GPIO.HIGH)


    def variador(self, nombre):
        global cont

        if nombre=="mas":
            cont=cont+1;
            self.ui.label_19.setText(str(cont))
            pwm.ChangeDutyCycle(cont)
        else:
            numero = int(self.ui.label_19.text())
            n = numero-1
            self.ui.label_19.setText(str(n))
            pwm.ChangeDutyCycle(n)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()
