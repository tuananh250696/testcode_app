
import cv2
from PyQt5.QtCore  import pyqtSlot
from PyQt5.QtGui import QImage , QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 750)
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(10, 470, 191, 251))
        self.TEXT.setObjectName("TEXT")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(210, 120, 871, 621))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.SHOW = QtWidgets.QPushButton(Dialog)
        self.SHOW.setGeometry(QtCore.QRect(10, 140, 191, 81))
        self.SHOW.setObjectName("SHOW")
        self.CAPTURE = QtWidgets.QPushButton(Dialog)
        self.CAPTURE.setGeometry(QtCore.QRect(10, 220, 191, 81))
        self.CAPTURE.setObjectName("CAPTURE")
        self.NEXT = QtWidgets.QPushButton(Dialog)
        self.NEXT.setGeometry(QtCore.QRect(680, 40, 161, 81))
        self.NEXT.setObjectName("NEXT")
        self.imgLabel_2 = QtWidgets.QLabel(Dialog)
        self.imgLabel_2.setGeometry(QtCore.QRect(0, 0, 1922, 41))
        self.imgLabel_2.setAutoFillBackground(False)
        self.imgLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_2.setText("")
        self.imgLabel_2.setPixmap(QtGui.QPixmap("ngang2.png"))
        self.imgLabel_2.setObjectName("imgLabel_2")
        self.imgLabel_3 = QtWidgets.QLabel(Dialog)
        self.imgLabel_3.setGeometry(QtCore.QRect(1080, 40, 271, 701))
        self.imgLabel_3.setAutoFillBackground(False)
        self.imgLabel_3.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_3.setText("")
        self.imgLabel_3.setObjectName("imgLabel_3")
        self.NEXT_2 = QtWidgets.QPushButton(Dialog)
        self.NEXT_2.setGeometry(QtCore.QRect(0, 40, 181, 81))
        self.NEXT_2.setObjectName("NEXT_2")
        self.NEXT_4 = QtWidgets.QPushButton(Dialog)
        self.NEXT_4.setGeometry(QtCore.QRect(180, 40, 171, 81))
        self.NEXT_4.setObjectName("NEXT_4")
        self.NEXT_5 = QtWidgets.QPushButton(Dialog)
        self.NEXT_5.setGeometry(QtCore.QRect(350, 40, 171, 81))
        self.NEXT_5.setObjectName("NEXT_5")
        self.CAPTURE_2 = QtWidgets.QPushButton(Dialog)
        self.CAPTURE_2.setGeometry(QtCore.QRect(10, 300, 191, 81))
        self.CAPTURE_2.setObjectName("CAPTURE_2")
        self.CAPTURE_3 = QtWidgets.QPushButton(Dialog)
        self.CAPTURE_3.setGeometry(QtCore.QRect(520, 40, 161, 81))
        self.CAPTURE_3.setObjectName("CAPTURE_3")
        self.NEXT_3 = QtWidgets.QPushButton(Dialog)
        self.NEXT_3.setGeometry(QtCore.QRect(10, 380, 191, 81))
        self.NEXT_3.setObjectName("NEXT_3")
        self.NEXT_7 = QtWidgets.QPushButton(Dialog)
        self.NEXT_7.setGeometry(QtCore.QRect(840, 40, 161, 81))
        self.NEXT_7.setObjectName("NEXT_7")
        self.TEXT.raise_()
        self.imgLabel.raise_()
        self.SHOW.raise_()
        self.NEXT.raise_()
        self.imgLabel_3.raise_()
        self.NEXT_2.raise_()
        self.NEXT_4.raise_()
        self.NEXT_5.raise_()
        self.imgLabel_2.raise_()
        self.CAPTURE.raise_()
        self.CAPTURE_2.raise_()
        self.CAPTURE_3.raise_()
        self.NEXT_3.raise_()
        self.NEXT_7.raise_()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SHOW.setText(_translate("Dialog", "Show"))
        self.CAPTURE.setText(_translate("Dialog", "Capture"))
        self.NEXT.setText(_translate("Dialog", "Zomm-"))
        self.NEXT_2.setText(_translate("Dialog", "Chọn thiết bị"))
        self.NEXT_4.setText(_translate("Dialog", "Tùy chọn"))
        self.NEXT_5.setText(_translate("Dialog", "Thêm mới"))
        self.CAPTURE_2.setText(_translate("Dialog", "VideoRecoder"))
        self.CAPTURE_3.setText(_translate("Dialog", "Zoom+"))
        self.NEXT_3.setText(_translate("Dialog", "IN PHIẾU KHÁM"))
        self.NEXT_7.setText(_translate("Dialog", "Đóng"))

        self.logic = 0
        self.value = 1
        self.SHOW.clicked.connect(self.onClicked)
        self.TEXT.setText("Kindly Press 'Show' to connect with webcam.")
        self.CAPTURE.clicked.connect(self.CaptureClicked)
    @QtCore.pyqtSlot()

    def onClicked(self):
        self.TEXT.setText('Kindly Press "Capture Image " to Capture image')
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            self.CAPTURE.clicked.connect(self.CaptureClicked)
            if ret == True:
                print('here')
                self.displayImage(frame, 1)
                cv2.waitKey()
                if (self.logic == 2):
                    self.value = self.value + 1
                    cv2.imwrite('%s.png' % (self.value), frame)
                    self.logic = 1
                    self.TEXT.setText('your Image have been Saved')
            else:
                print('not found')
        cap.release()
        cv2.destroyAllWindows()

    def CaptureClicked(self):
        self.logic = 2



    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
