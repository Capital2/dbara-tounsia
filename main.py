import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5 import QtGui

from main_window_ui import Ui_MainWindow

from engine import RecipeSystem


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
    
    def addToIng(self):
        selected = self.alling.selectedItems()
        
        items = [self.ing.item(x).text() for x in range(self.ing.count())]

        if not selected:
            return
        if selected[0].text() in items:
            return # item added already
        
        self.ing.addItems([i.text() for i in selected])
        # self.alling.removeItemWidget(selected[0])
    
    def removeFromIng(self):
        selected = self.ing.selectedItems()
        if not selected:
            return

        self.ing.takeItem(self.ing.row(selected[0]))
    
    def suggest_recipe(self):
        engine = RecipeSystem()
        engine.ingredients = [self.ing.item(x).text() for x in range(self.ing.count())]
        engine.reset()
        engine.run()

        st = ""
        if not engine.recipes:
            st = "<p>ma3andek mattayeb, barra lel resto ya fa9ri</p>"
        else:
            for recipe in engine.recipes:
                st += f"<p>{recipe}</p>"

        QMessageBox.about(self, "Suggested recipes", st)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())