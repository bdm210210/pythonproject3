from PyQt5.QtWidgets import QDialog
from pet.pet_info import Ui_PDialog

class PetInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PDialog()
        self.ui.setupUi(self)

    def update_text(self, text):
        self.ui.textBrowser.setPlainText(text)
