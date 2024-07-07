from PyQt5.QtWidgets import QDialog
from dibiao.land import Ui_lDialog  # 确保路径正确

class LandDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_lDialog()
        self.ui.setupUi(self)
        print("LandDialog initialized.")  # 确认对话框初始化

    def update_text(self, text):
        print(f"Updating text: {text}")  # 调试输出
        if text:
            self.ui.textBrowser.setPlainText(text)
        else:
            self.ui.textBrowser.setPlainText("No landmark information detected.")
