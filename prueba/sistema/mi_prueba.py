from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("hola a todos")
        self.show()



app = QApplication(sys.argv)

v = Ventana()

app.exec()
import math

d = math.pow(12,23)
d = math.sqrt(d)
print(d)
