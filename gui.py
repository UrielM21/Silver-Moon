from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from temp import Ui_MainWindow




_, Window = uic.loadUiType("temp.ui")
Form = Ui_MainWindow

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()