from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from TemplateGUI import Ui_Form
import qdarkstyle


_, Window = uic.loadUiType("templateGUI.ui")
Form = Ui_Form

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

window.show()

form.viewer.loadImageFromFile("./logo_zetes.jpeg")
form.viewer.show()



app.exec_()