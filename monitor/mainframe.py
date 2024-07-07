from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.mdui import Ui_Dialog
from monitor.mfui import Ui1_Dialog
from monitor.monitorframe import MonitorDialog
from pet.PetFrame import PetInfoDialog
from pet.pet_info import Ui_PDialog
import data.resources_rc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Dialog")
        self.resize(800, 600)

        # 创建一个主框架，用于放置所有子控件
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 创建一个布局，添加到主框架中
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # 创建一个 QLabel 用于显示背景图片
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(r"E:\pythonProject3\data\beijing.jpg")
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        self.layout.addWidget(self.label)

        # 初始化 UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        super(MainDialog, self).resizeEvent(event)

    def goin(self):
        self.monitorframe = MonitorDialog()
        self.monitorframe.show()
        self.close()


