from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage  # 添加这行
import cv2
from ai.pet import pet_detect
from ai.land import land_detect

class Video(QThread):
    send_frame = pyqtSignal(QImage)  # 定义信号传递 QImage 对象
    send_detected_info = pyqtSignal(str)  # 定义信号传递检测到的信息

    def __init__(self, video_path, detect_type='pet'):
        super().__init__()
        self.video_path = video_path
        self.running = True
        self.detect_type = detect_type

    def set_detect_type(self, detect_type):
        self.detect_type = detect_type

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Cannot open video file.")
            return

        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("Error: Cannot read frame.")
                break

            if self.detect_type == 'pet':
                detected_info = pet_detect(frame)  # 调用 pet_detect 获取返回的字符串
            elif self.detect_type == 'land':
                detected_info = land_detect(frame)  # 调用 land_detect 获取返回的字符串
            else:
                detected_info = "未知检测类型"

            # 发送检测到的信息
            self.send_detected_info.emit(detected_info)

            # 转换 frame 为 QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            qt_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.send_frame.emit(qt_image)

            self.msleep(30)  # 控制播放速度

        cap.release()

    def stop(self):
        self.running = False
        self.wait()