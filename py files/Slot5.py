_author_ = "Oguzhan Onder"
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
class Ui_Dialog5(object):
    def get_length_value5(self):
        val_length5 = self.doubleSpinBox.value()
        return val_length5
    def get_diameter_1_5(self):
        val_diam_1_5 = self.doubleSpinBox_2.value()
        return val_diam_1_5
    def get_diameter_2_5(self):
        val_diam_2_5 = self.doubleSpinBox_3.value()
        return val_diam_2_5
    
    def get_cylinder_button5(self):
        shape_name_5 = self.pushButton.text()
        self.label_2.setText("Selected: {}".format(shape_name_5))
        self.doubleSpinBox_3.setEnabled(False)
        self.label_8.setEnabled(False)
        self.doubleSpinBox_3.setValue(0)
        self.label_angle.setEnabled(False)
        self.doubleSpinBox_angle.setEnabled(False)
        self.doubleSpinBox_angle.setValue(0)
        return shape_name_5        
    def get_angle5(self):
        return self.doubleSpinBox_angle.value()
    def get_trapezoid_button5(self):
        shape_name_5 = self.pushButton_2.text()
        self.label_2.setText("Selected: {}".format(shape_name_5))
        self.doubleSpinBox_3.setEnabled(True)
        self.label_8.setEnabled(True)
        self.label_angle.setEnabled(True)
        self.doubleSpinBox_angle.setEnabled(True)
      
        return shape_name_5    
    def get_conic_button5(self):
        shape_name_5 = self.pushButton_3.text()
        self.label_2.setText("Selected: {}".format(shape_name_5))
        self.doubleSpinBox_3.setEnabled(False)
        self.label_8.setEnabled(False)
        self.doubleSpinBox_3.setValue(0)
        self.label_angle.setEnabled(False)
        self.doubleSpinBox_angle.setEnabled(False)
        self.doubleSpinBox_angle.setValue(0)
        return shape_name_5 
    
    # def error_message5(self):
    #     if self.get_length_value5() == 0 or self.get_diameter_1_5() == 0 or self.get_diameter_2_5() == 0:
    #         msg = QMessageBox()
    #         msg.setWindowTitle("Error")
    #         msg.setText("Please set values before click OK!")
    #         msg.setIcon(QMessageBox.Critical)
    #         x = msg.exec_()
    def clear_values(self):
        self.doubleSpinBox.setValue(0)
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_3.setValue(0)
        self.doubleSpinBox_angle.setValue(0)
        self.label_2.setText("Selected :")
    def calculate_properties5(self):
        R_1_5 = self.get_diameter_1_5()/2
        R_2_5 = self.get_diameter_2_5()/2
        L_5 = self.get_length_value5()
        
        if self.label_2.text() == "Selected: Cylinder":
            volume_5 = np.pi*R_1_5**2*L_5
            surface_area_5 = 2*np.pi*R_1_5*L_5
    
        elif self.label_2.text() == "Selected: Cylindrical Trapezoid":
            volume_5 = (1/3)*np.pi*(R_1_5**2+R_1_5*R_2_5+R_2_5**2)*L_5
            surface_area_5 = np.pi*(R_1_5+R_2_5)*np.sqrt((R_1_5-R_2_5)**2+L_5**2)
        elif self.label_2.text() == "Selected: Conic":
            volume_5 = (1/3)*np.pi*R_1_5**2*L_5
            surface_area_5 = np.pi*R_1_5*np.sqrt(L_5**2+R_1_5**2)
        else:
            volume_5 = 0
            surface_area_5 = 0 
        return volume_5,surface_area_5
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(150, 360, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 50, 81, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/geometric/cone-removebg-preview.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 280, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 250, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 130, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 91, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/geometric/trapezoid-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 221, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 130, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 220, 71, 16))
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(150, 220, 111, 22))
        self.doubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox.setDecimals(7)
        self.doubleSpinBox.setMaximum(9999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(150, 250, 111, 22))
        self.doubleSpinBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_2.setDecimals(7)
        self.doubleSpinBox_2.setMaximum(9999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(150, 280, 111, 22))
        self.doubleSpinBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_3.setDecimals(7)
        self.doubleSpinBox_3.setMaximum(9999999.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/geometric/Cylinder-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_angle = QtWidgets.QLabel(Dialog)
        self.label_angle.setGeometry(QtCore.QRect(80, 310, 221, 16))
        self.label_angle.setObjectName("label_angle")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 365, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.doubleSpinBox_angle = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_angle.setGeometry(QtCore.QRect(150, 310, 111, 22))
        self.doubleSpinBox_angle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_angle.setDecimals(7)
        self.doubleSpinBox_angle.setMaximum(9999999.0)
        self.doubleSpinBox_angle.setMinimum(-9999999.0)
        self.doubleSpinBox_angle.setObjectName("doubleSpinBox_angle")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        # self.buttonBox.accepted.connect(self.error_message5)
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ##
        self.doubleSpinBox.valueChanged.connect(self.get_length_value5)
        self.doubleSpinBox_2.valueChanged.connect(self.get_diameter_1_5)
        self.doubleSpinBox_3.valueChanged.connect(self.get_diameter_2_5)
        self.doubleSpinBox_angle.valueChanged.connect(self.get_angle5)
        ##        
        self.pushButton.clicked.connect(self.get_cylinder_button5)
        self.pushButton_2.clicked.connect(self.get_trapezoid_button5)
        self.pushButton_3.clicked.connect(self.get_conic_button5)
        self.pushButton_4.clicked.connect(self.clear_values)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Slot5"))
        self.label_8.setText(_translate("Dialog", "Diameter 2 :"))
        self.label_7.setText(_translate("Dialog", "Diameter 1 :"))
        self.label.setText(_translate("Dialog", "SLOT 5"))
        self.pushButton_3.setText(_translate("Dialog", "Conic"))
        self.label_2.setText(_translate("Dialog", "Selected : "))
        self.pushButton.setText(_translate("Dialog", "Cylinder"))
        self.pushButton_2.setText(_translate("Dialog", "Cylindrical Trapezoid"))
        self.label_6.setText(_translate("Dialog", "Length       :"))
        self.label_angle.setText(_translate("Dialog", "Angle          :"))
        self.pushButton_4.setText(_translate("Dialog","Clear"))
import resource_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
