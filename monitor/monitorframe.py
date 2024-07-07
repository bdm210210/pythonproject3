from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from monitor.mfui import Ui1_Dialog
from monitor.Video import Video
from pet.PetFrame import PetInfoDialog  # 确保导入路径正确
from dibiao.landFrame import LandDialog
from dibiao.land import Ui_lDialog

class MonitorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui1_Dialog()
        self.ui.setupUi(self)
        self.video_thread = Video(r'E:\pythonProject3\data\vd.mp4')
        self.video_thread.send_frame.connect(self.update_image)
        self.video_thread.send_detected_info.connect(self.update_detected_info)
        self.video_thread.start()
        self.ui.pushButton.clicked.connect(self.goto)
        self.ui.pushButton_2.clicked.connect(self.goin)  # 假设第二个按钮是用来跳转到LandDialog的

    def update_image(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self.ui.video1.setPixmap(pixmap.scaled(self.ui.video1.size(), QtCore.Qt.KeepAspectRatio))

    def update_detected_info(self, info):
        print(f"Detected Info: {info}")  # 调试输出
        if hasattr(self, 'pet_info_dialog') and self.pet_info_dialog.isVisible():
            self.pet_info_dialog.update_text(info)
        if hasattr(self, 'land_info_dialog') and self.land_info_dialog.isVisible():
            self.land_info_dialog.update_text(info)

    def closeEvent(self, event):
        self.video_thread.stop()
        event.accept()

    def goto(self):
        self.video_thread.set_detect_type('pet')  # 设置为宠物检测
        self.pet_info_dialog = PetInfoDialog(self)
        self.pet_info_dialog.show()

    def goin(self):
        self.video_thread.set_detect_type('land')  # 设置为地标检测
        self.land_info_dialog = LandDialog(self)
        self.land_info_dialog.show()
