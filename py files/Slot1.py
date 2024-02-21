_author_ = "Oguzhan Onder"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from scipy.integrate import quad
import numpy as np
import sympy as smp
import nce
import math
import threading
class Ui_Dialog1(object):
    def haack_series(self,length,diameter,C):
        # C = 0 is LD-Haack (Von Karman)
        # C = 1/3 is LV-Haack
        # C = 2/3 is Tangent
        global xposition_list
        global yposition_list
        xposition_list = [i for i in np.linspace(0,length)]  
        theta_list = [math.acos(1-((2*j)/length)) for j in xposition_list]   
        yposition_list = [(diameter*math.sqrt(k-(math.sin(2*k)/2)+(C*((math.sin(k))**3))))/math.sqrt(math.pi) for k in theta_list]
        return xposition_list,yposition_list
        
    def power_series(self,length,diameter,n):
         # n = 0 is Cylinder
         # n = 1/2 is Half (Parabola)
         # n = 3/4 is Three Quarter
         # n = 1 is Cone
        global xposition_list
        global yposition_list
        xposition_list = [i for i in np.linspace(0,length)]
        yposition_list = [(diameter*((k/length)**n)) for k in xposition_list] 
        return xposition_list,yposition_list        
         
    def biconic(self,L_1,D_1,L_2,D_2):
        # L_1 is top cone length
        # L_2 is rest part of nose length
        # R_1 is top cone's radius
        # R_2 is rest part's radius of nose
        global xposition_list
        global yposition_list
        length = L_1 + L_2        
        xtop_list = [k for k in np.linspace(0,L_1,25)]
        ytop_list = [(j*D_1)/L_1 for j in xtop_list]
    
        xrest_list = [k for k in np.linspace(L_1,length,26)]
        yrest_list = [(D_1 + ((i-L_1)*(D_2-D_1))/L_2) for i in xrest_list[1:]]
         
        yposition_list = ytop_list + yrest_list
        xposition_list = xtop_list + xrest_list[1:]
        return xposition_list,yposition_list
    def conic(self,length,diameter):
        global xposition_list
        global yposition_list
        xposition_list = [i for i in np.linspace(0,length)]
        yposition_list = [(k*(diameter))/length for k in xposition_list]
        return xposition_list,yposition_list
    # def spherically_blunted_conic(self,r_n):
    #     #r_n is radius of spherical nose cap
    #     x_a = (self.length**2*(math.sqrt(r_n**2/(self.radius**2+self.length**2))))/self.radius + math.sqrt(r_n**2-((self.length**2*(math.sqrt(r_n**2/(self.radius**2+self.length**2))))/self.radius)**2)
    #     self.length = self.length + x_a
    #     x_t = (self.length**2*(math.sqrt(r_n**2/(self.radius**2+self.length**2))))/self.radius
    #     y_t = (x_t*self.radius)/self.length
    #     x_0 = x_a + r_n
    #     for i in np.arange(x_a,x_t+1):
    #         yarcposition = math.sqrt((i-x_0**2)-x_0**2)
    #         ylist.append(yarcposition)
    #     for k in np.arange(x_a,self.length-x_t+1):
    #         yrestpositions = y_t+((k*self.radius)/self.length)
    #         ylist.append(yrestpositions)
    
    def tangent_ogive(self,length,diameter):
        global xposition_list
        global yposition_list
        rho = (diameter**2+length**2)/(2*diameter)
        xposition_list = [k for k in np.linspace(0,length)]
        yposition_list = [(math.sqrt(rho**2-(length-i)**2)+diameter-rho) for i in xposition_list] 
        return xposition_list,yposition_list           
    
    def secant_ogive(self,length,diameter,rho):
        global xposition_list
        global yposition_list
        alpha = math.degrees(math.acos(math.sqrt(length**2+diameter**2)/(2*rho)))-math.degrees(math.atan(diameter/length))
        xposition_list = [k for k in np.linspace(0,length)]
        yposition_list = [(math.sqrt(rho**2-(rho*(math.cos(math.radians(alpha)))-i)**2)-(rho*(math.sin(math.radians(alpha))))) for i in xposition_list]
        return xposition_list,yposition_list           
                       
    def elliptical(self,length,diameter):
        global xposition_list
        global yposition_list
        xposition_list = [k for k in np.linspace(0,length,25)]
        yposition_list = [diameter*math.sqrt(1-(i**2/length**2)) for i in xposition_list]
        yposition_list.reverse()       
        return xposition_list,yposition_list
    def parabolic(self,length,diameter,K):
        global xposition_list
        global yposition_list
        # K = 0 is Cone
        # K = 1/2 is Half
        # K = 3/4 is Three Quarter
        # K = 1 is Full
        xposition_list = [j for j in np.linspace(0,length,5) ]
        yposition_list = [diameter*((2*(i/length)-K*(i/length**2))/(2-K)) for i in xposition_list]
        return xposition_list,yposition_list
    def get_index(self):
        return self.select_type_combo_box.currentIndex()
    def images_and_name(self):
        global name_nose 
        if self.select_type_combo_box.currentIndex() == 1:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Conic_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 2:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Tangent_Ogive_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 3:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Elliptical_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 4:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Parabolic_(Half)_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 5:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Parabolic_(Three-Quarter)_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 6:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Parabolic_(Full)_Nose_Cone_Render.png"))
        elif self.select_type_combo_box.currentIndex() == 7:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Power_Series_(Half)_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 8:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/Power_Series_(Three-Quarter)_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 9:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/LD-Haack_Series_(Von_Kármán)_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 10:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/LV-Haack_Series_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        elif self.select_type_combo_box.currentIndex() == 11:
            self.label_2.setPixmap(QtGui.QPixmap(":/nosecone/LV-Haack_Series_Nose_Cone_Render.png"))
            name_nose = self.select_type_combo_box.currentText()
        else:
            self.label_2.setPixmap(QtGui.QPixmap())
            name_nose = None
        return self.select_type_combo_box.currentIndex()
    def get_length_value1(self):
        global val_length1
        val_length1 = self.Length_spinbox.value()
        # print(val_length1)
        return val_length1
    
    def get_base_diameter_value(self):
        global val_base_diameter
        val_base_diameter = self.diam_spinbox.value()
        # print(val_base_diameter)
        return val_base_diameter
    
    def applications_of_equations(self):
        
        if  self.get_index() == 1 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.conic(self.get_length_value1(),(self.get_base_diameter_value()/2))
                    #print(x,y)
                
                # Tangent Ogive
        elif self.get_index() == 2  and self.get_length_value1() > 0 and  (self.get_base_diameter_value()/2) > 0:
                    x,y= self.tangent_ogive(self.get_length_value1(),self.get_base_diameter_value()/2)  
                
                # Elliptical
        elif self.get_index() ==3  and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.elliptical(self.get_length_value1(),self.get_base_diameter_value()/2)
                    
                
                # Parabolic (Half)
        elif self.get_index() == 4 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.parabolic(self.get_length_value1(),self.get_base_diameter_value()/2,1/2)
                   
                
                # Parabolic (Three Quarter)
        elif self.get_index() == 5  and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y= self.parabolic(self.get_length_value1(),self.get_base_diameter_value()/2,3/4)
                  
                # Parabolic (Full)
        elif self.get_index() == 6  and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y= self.parabolic(self.get_length_value1(),self.get_base_diameter_value()/2,1)  
             
                
                # Power Series (Half)
        elif self.get_index() == 7 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.power_series(self.get_length_value1(),self.get_base_diameter_value()/2,1/2)    
                  
                
                # Power Series (Three-Quarter)
        elif self.get_index() == 8 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y =self.power_series(self.get_length_value1(),self.get_base_diameter_value()/2,3/4)    
               
                # Haack Series (LD-Haack)
        elif self.get_index() == 9 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.haack_series(self.get_length_value1(),self.get_base_diameter_value()/2,0)    
                 
                
                # Haack Series (LV-Haack)
        elif self.get_index() == 10 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.haack_series(self.get_length_value1(),self.get_base_diameter_value()/2,1/3)    
              
                
                # Haack Series (Tangent)
        elif self.get_index() == 11 and self.get_length_value1() > 0 and  self.get_base_diameter_value()/2 > 0:
                    x,y = self.haack_series(self.get_length_value1(),self.get_base_diameter_value()/2,2/3)
        return x,y
    
    def create_points_nose_cone_matrix(self):
           global y_array_cone
           global x_array_cone
           x,y = self.applications_of_equations()
           y_array_cone = np.array([y]).reshape(len(y),1)      
           x_array_cone = np.array([x]).reshape(len(x),1)
           concatenate_x_y_arrays_nose_cone = np.concatenate([x_array_cone,y_array_cone],axis=1)
           return concatenate_x_y_arrays_nose_cone
         
    
    def error_message1(self):
        if self.select_type_combo_box.currentIndex() == 0 or self.get_length_value1() == 0 or self.get_base_diameter_value() ==0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select nose cone type or set values before click OK!")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
    
    def calculate_properties1(self):
        
        R = self.get_base_diameter_value()/2
        L = self.get_length_value1()
        x,z = smp.symbols('x z')
        smp.init_printing(use_unicode=True)
        theta = smp.acos(1-(2*x/L))
        t_theta_list = []
        t_x_list = []
        
        
        if self.select_type_combo_box.currentIndex() == 1:
            volume = (1/3)*np.pi*R**2*L
            slant_height = np.sqrt(R**2+L**2)
            surface_area = np.pi*R*slant_height
            return volume, surface_area

        
        elif self.select_type_combo_box.currentIndex() == 2:
            rho = (R**2+L**2)/(2*R)
            integrand = lambda x: np.pi*(np.sqrt(rho**2-(L-x)**2)+R-rho)**2
            volume,volume_error = quad(integrand,0,L)
            y_eq = smp.sqrt(rho**2-(L-x)**2)+R-rho

        
        elif self.select_type_combo_box.currentIndex() == 3:
            integrand = lambda x: smp.pi*(R*smp.sqrt(1-x**2/L**2))**2
            volume,volume_error = quad(integrand,0,L) 
            y_eq = R*smp.sqrt(1-(x**2/L**2))
        #
        elif self.select_type_combo_box.currentIndex() == 4:
            integrand = lambda x: smp.pi*(R*((2*x/L)-(0.5*(x/L)**2))/(2-0.5))
            volume,volume_error = quad(integrand,0,L) 
            y_eq = R*((2*x/L)-(0.5*(x/L)**2))/(2-0.5)
        
        elif self.select_type_combo_box.currentIndex() == 5:
            integrand = lambda x: smp.pi*(R*((2*x/L)-(0.75*(x/L)**2))/(2-0.75))
            volume,volume_error = quad(integrand,0,L) 
            y_eq = R*((2*x/L)-(0.75*(x/L)**2))/(2-0.75)
        
        elif self.select_type_combo_box.currentIndex() == 6:
            integrand = lambda x: smp.pi*(R*((2*x/L)-(1*(x/L)**2))/(2-1))
            volume,volume_error = quad(integrand,0,L) 
            y_eq = R*((2*x/L)-(1*(x/L)**2))/(2-1)
        #
        elif self.select_type_combo_box.currentIndex() == 7:
            integrand = lambda x: np.pi*(R*(x/L)**(1/2))**2
            volume,volume_error = quad(integrand,0,L)
            y_eq = R*(x/L)**0.5
        elif self.select_type_combo_box.currentIndex() == 8:
            integrand = lambda x: np.pi*(R*(x/L)**(3/4))**2
            volume,volume_error = quad(integrand,0,L)
            y_eq = R*(x/L)**0.75
        elif self.select_type_combo_box.currentIndex() == 9:
            integrand = lambda x: np.pi*((R/2*np.sqrt(np.pi))*np.sqrt(np.arccos(1-2*x/L)-(np.sin(2*np.arccos(1-2*x/L))/2)))
            volume,volume_error = quad(integrand,0,L)
            y_eq = (R/(2*smp.pi))*smp.sqrt(theta-(smp.sin(2*theta)/2))
        elif self.select_type_combo_box.currentIndex() == 10:
            integrand = lambda x: np.pi*((R/2*np.sqrt(np.pi))*np.sqrt(np.arccos(1-2*x/L)-(np.sin(2*np.arccos(1-2*x/L))/2)+((1/3)*(np.sin(np.arccos(1-2*x/L)))**3)))
            volume,volume_error = quad(integrand,0,L)
            y_eq = (R/(2*smp.pi))*smp.sqrt(theta-(smp.sin(2*theta)/2)+(0.333*smp.sin(theta)**3))
        elif self.select_type_combo_box.currentIndex() == 11:
            integrand = lambda x: np.pi*((R/2*np.sqrt(np.pi))*np.sqrt(np.arccos(1-2*x/L)-(np.sin(2*np.arccos(1-2*x/L))/2)+((2/3)*(np.sin(np.arccos(1-2*x/L)))**3)))
            volume,volume_error = quad(integrand,0,L)
            y_eq = (R/(2*smp.pi))*smp.sqrt(theta-(smp.sin(2*theta)/2)+(0.667*smp.sin(theta)**3))
        
        vec = [y_eq*smp.cos(z), y_eq*smp.sin(z),x]
        for i in vec:    
            t_theta = smp.diff(i,z)
            t_x = smp.diff(i,x)
            t_theta_list.append(t_theta)
            t_x_list.append(t_x)    
            
        t_theta_array = np.array(t_theta_list)
        t_x_array = np.array(t_x_list)
        
        cross_product = np.cross(t_theta_array,t_x_array)
        # print(cross_product)
        magnitude = smp.sqrt(cross_product[0]**2+cross_product[1]**2+cross_product[2]**2).simplify()
        # print(magnitude)
        integrand1_num = smp.lambdify([x],magnitude)
        # print(integrand1_num)
        surface_area = quad(integrand1_num,0,L)[0]
        
        return volume,2*np.pi*surface_area
        
         
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(312, 443)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 390, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Length_spinbox = QtWidgets.QDoubleSpinBox(Dialog)
        self.Length_spinbox.setGeometry(QtCore.QRect(100, 90, 201, 22))
        self.Length_spinbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Length_spinbox.setMaximum(9999999.99)
        self.Length_spinbox.setDecimals(8)
        self.Length_spinbox.setObjectName("Length_spinbox")
        self.diam_spinbox = QtWidgets.QDoubleSpinBox(Dialog)
        self.diam_spinbox.setGeometry(QtCore.QRect(100, 120, 201, 22))
        self.diam_spinbox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.diam_spinbox.setMaximum(9999999.99)
        self.diam_spinbox.setDecimals(8)
        self.diam_spinbox.setObjectName("diam_spinbox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 261, 211))
        self.label_2.setStyleSheet("")
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setText("")
        
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.select_type_combo_box = QtWidgets.QComboBox(Dialog)
        self.select_type_combo_box.setGeometry(QtCore.QRect(10, 50, 291, 21))
        self.select_type_combo_box.setMinimumSize(QtCore.QSize(181, 21))
        self.select_type_combo_box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.select_type_combo_box.setEditable(False)
        self.select_type_combo_box.setFrame(True)
        self.select_type_combo_box.setObjectName("select_type_combo_box")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.select_type_combo_box.addItem("")
        self.Length = QtWidgets.QLabel(Dialog)
        self.Length.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.Length.setObjectName("Length")
        self.BaseDiameter = QtWidgets.QLabel(Dialog)
        self.BaseDiameter.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.BaseDiameter.setObjectName("BaseDiameter")

        self.retranslateUi(Dialog)
        
        self.buttonBox.clicked.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.error_message1) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ##
        self.select_type_combo_box.activated.connect(self.images_and_name)
        self.Length_spinbox.valueChanged.connect(self.get_length_value1)
        self.diam_spinbox.valueChanged.connect(self.get_base_diameter_value)
       
        ##
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Slot1"))
        self.label.setText(_translate("Dialog", "SLOT 1 "))
        self.select_type_combo_box.setCurrentText(_translate("Dialog", "Select Nose Cone Type..."))
        self.select_type_combo_box.setItemText(0, _translate("Dialog", "Select Nose Cone Type..."))
        self.select_type_combo_box.setItemText(1, _translate("Dialog", "Conic"))
        self.select_type_combo_box.setItemText(2, _translate("Dialog", "Tangent ogive"))
        self.select_type_combo_box.setItemText(3, _translate("Dialog", "Elliptical"))
        self.select_type_combo_box.setItemText(4, _translate("Dialog", "Parabolic (Half)"))
        self.select_type_combo_box.setItemText(5, _translate("Dialog", "Parabolic (Three Quarter)"))
        self.select_type_combo_box.setItemText(6, _translate("Dialog", "Parabolic (Full)"))
        self.select_type_combo_box.setItemText(7, _translate("Dialog", "Power Series (Half)"))
        self.select_type_combo_box.setItemText(8, _translate("Dialog", "Power Series (Three Quarter)"))
        self.select_type_combo_box.setItemText(9, _translate("Dialog", "Haack Series (LD-Haack)"))
        self.select_type_combo_box.setItemText(10, _translate("Dialog", "Haack Series (LV-Haack)"))
        self.select_type_combo_box.setItemText(11, _translate("Dialog", "Haack Series (Tangent)"))
        self.Length.setText(_translate("Dialog", "Length             :"))
        self.BaseDiameter.setText(_translate("Dialog", "Base Diameter :"))
import resource_img
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
