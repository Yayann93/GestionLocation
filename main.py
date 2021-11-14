from PyQt5.QtWidgets import QApplication, QLabel
import Affichage

lsLocation = Affichage.consulterLocation()
app = QApplication([])

for l in lsLocation:
    label = QLabel(l.__str__())
    label.show()
app.exec()