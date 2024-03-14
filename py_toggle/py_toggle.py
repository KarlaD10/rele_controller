from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

class PyToggle(QCheckBox):
    def __init__(
            self,
            width = 60,
            bg_color = "#777",
            circle_color = "#DDD",
            active_color = "#00BCff"
    ):
        QCheckBox.__init__(self)

        #Set default parameters
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        #Colores
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Connect state changed
        self.stateChanged.connect(self.debug)


    def debug(self):
        print(f"Status: {self.isChecked()}")

    # Set new hit area
    def hitButton(self, pos:QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        # Set painter
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # Set as no pen
        p.setPen(Qt.NoPen)

        # Dibuja un rectangulo
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            # Draw BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(3, 3, 22, 22)

        else:
            # Draw BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self.width()-26, 3, 22, 22)

        p.end()



