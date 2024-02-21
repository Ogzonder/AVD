_author_ = "Oguzhan Onder"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QAction
from Slot1 import Ui_Dialog1
from Slot2 import Ui_Dialog2
from Slot3 import Ui_Dialog3
from Slot4 import Ui_Dialog4
from Slot5 import Ui_Dialog5
import win32com.client.dynamic
from webscrapping_airfoil import airfoil_points
import math


class Ui_MainWindow(object):
    def open_window_slot1(self):
        self.window1.show()
    def open_window_slot2(self):
        self.slot3.setEnabled(True)
        self.slot4.setEnabled(True)
        self.slot5.setEnabled(True)
        self.window2.show()
    def open_window_slot3(self):
        if self.ui2.get_angle2() !=0:
            self.slot4.setEnabled(False)
            self.slot5.setEnabled(False)
            self.ui4.doubleSpinBox.setValue(0)
            self.ui4.doubleSpinBox_2.setValue(0)
            self.ui4.doubleSpinBox_3.setValue(0)
            self.ui4.doubleSpinBox_angle.setValue(0)
            self.ui5.doubleSpinBox.setValue(0)
            self.ui5.doubleSpinBox.setValue(0)
            self.ui5.doubleSpinBox.setValue(0)
            self.ui5.doubleSpinBox_angle.setValue(0)
        elif self.ui2.get_angle2() ==0:
            self.slot4.setEnabled(True)
            self.slot5.setEnabled(True)
            self.window3.show()
    def open_window_slot4(self):
        if self.ui3.get_angle3() !=0:
            self.ui5.doubleSpinBox.setValue(0)
            self.ui5.doubleSpinBox_2.setValue(0)
            self.ui5.doubleSpinBox_3.setValue(0)
            self.ui5.doubleSpinBox_angle.setValue(0)
            self.slot5.setEnabled(False)
        elif self.ui3.get_angle3() ==0:
            self.slot5.setEnabled(True)
            self.window4.show()
    
    def open_window_slot5(self):
        if self.ui4.get_angle4() !=0:
            self.slot5.setEnabled(False)
        elif self.ui4.get_angle4() ==0:
            self.window5.show()
        
    def fuselage_properties(self):
        volume1,surface_area1 = self.ui1.calculate_properties1()
        volume2,surface_area2 = self.ui2.calculate_properties2()
        volume3,surface_area3 = self.ui3.calculate_properties3()
        volume4,surface_area4 = self.ui4.calculate_properties4()
        volume5,surface_area5 = self.ui5.calculate_properties5()
        length1 = self.ui1.get_length_value1()
        length2 = self.ui2.get_length_value2()
        length3 = self.ui3.get_length_value3()
        length4 = self.ui4.get_length_value4()
        length5 = self.ui5.get_length_value5()
        max_diameter_val = max(self.ui1.get_base_diameter_value(),
                               self.ui2.get_diameter_1_2(),
                               self.ui2.get_diameter_2_2(),
                               self.ui3.get_diameter_1_3(),
                               self.ui3.get_diameter_2_3(),
                               self.ui4.get_diameter_1_4(),
                               self.ui4.get_diameter_2_4(),
                               self.ui5.get_diameter_1_5(),
                               self.ui5.get_diameter_2_5())
        total_length = length1+length2+length3+length4+length5
        fineness_ratio_val = total_length/max_diameter_val
        self.volume_fuselage_2.setText(str(round((volume1+volume2+volume3+volume4+volume5),3)))
        self.surface_area_fuselage_2.setText(str(round((surface_area1+surface_area2+surface_area3+surface_area4+surface_area5),3)))
        self.length_2.setText(str(total_length))
        self.max_diameter_2.setText(str(max_diameter_val))
        self.fineness_ratio_2.setText(str(round(fineness_ratio_val,3)))
    
    def get_wing_span_value(self):
        return self.wing_span.value()
    def get_root_chord_value(self):
        return self.root_chord.value()
    def get_tip_chord_value(self):
        return self.tip_chord.value()
    def get_setting_angle_value(self):
        return self.setting_angle.value()
    def get_root_twist_angle_value(self):
        return self.root_twist_angle.value()
    def get_tip_twist_angle_value(self):
        return self.tip_twist_angle.value()
    def get_sweep_angle_value(self):
        return self.sweep_angle.value()
    def get_dihedral_angle_value(self):
        return self.dihedral_angle.value()
    def get_Hlocation_value(self):
        return self.horizontal_location.value()
    def get_Vlocation_value(self):
        return self.wing_location.value()
    def get_airfoil_value(self):
        return self.airfoil.currentText()
    def get_airfoil_value_index(self):
        return self.airfoil.currentIndex()
    def get_VS_airfoil_value(self):
        return self.VSairfoil.currentText()
    def get_VS_airfoil_value_index(self):
        return self.VSairfoil.currentIndex()
    def get_VS_span_value(self):
        return self.VS_tailspan_2.value()
    def get_VS_rootchord_value(self):
        return self.VS_rootchord_2.value()
    def get_VS_tipchord_value(self):
        return self.VS_tipchord_2.value()
    def get_VS_sweepangle_value(self):
        return self.VS_sweepangle_2.value()

    def get_HS_airfoil_value(self):
        return self.HS_airfoil.currentText()
    def get_HS_airfoil_value_index(self):
        return self.HS_airfoil.currentIndex()
    def get_HS_span_value(self):
        return self.HS_tailspan_2.value()
    def get_HS_rootchord_value(self):
        return self.HS_rootchord_2.value()
    def get_HS_tipchord_value(self):
        return self.HS_tipchord_2.value()
    def get_HS_sweepangle_value(self):
        return self.HS_sweepangle_2.value()
   
    def get_tail_dihedralangle_value(self):
        return self.dihedral_angle.value()
    def get_horizontal_location_tail(self):
        return self.horizontal_location_3.value()
    ###
    def write_txt(self):
       with open('values.txt', 'w') as f:
           f.write("FUSELAGE")
           f.write("\n")
           f.write("SLOT1")
           f.write("\n")
           f.write(str(self.ui1.get_index()))
           f.write("\n")
           f.write(str(self.ui1.get_length_value1()))
           f.write("\n")
           f.write(str(self.ui1.get_base_diameter_value()))
           f.write("\n")
           
           
           f.write("SLOT2")
           f.write("\n")
           f.write(str(self.ui2.label_2.text()))
           f.write("\n")
           f.write(str(self.ui2.get_length_value2()))
           f.write("\n")
           f.write(str(self.ui2.get_diameter_1_2()))
           f.write("\n")
           f.write(str(self.ui2.get_diameter_2_2()))
           f.write("\n")
           f.write(str(self.ui2.get_angle2()))
           f.write("\n")
           
           f.write("SLOT3")
           f.write("\n")
           f.write(str(self.ui3.label_2.text()))
           f.write("\n")
           f.write(str(self.ui3.get_length_value3()))
           f.write("\n")
           f.write(str(self.ui3.get_diameter_1_3()))
           f.write("\n")
           f.write(str(self.ui3.get_diameter_2_3()))
           f.write("\n")
           f.write(str(self.ui3.get_angle3()))
           f.write("\n")
           
           f.write("SLOT4")
           f.write("\n")
           f.write(str(self.ui4.label_2.text()))
           f.write("\n")
           f.write(str(self.ui4.get_length_value4()))
           f.write("\n")
           f.write(str(self.ui4.get_diameter_1_4()))
           f.write("\n")
           f.write(str(self.ui4.get_diameter_2_4()))
           f.write("\n")
           f.write(str(self.ui4.get_angle4()))
           f.write("\n")
           
           f.write("SLOT5")
           f.write("\n")
           f.write(str(self.ui5.label_2.text()))
           f.write("\n")
           f.write(str(self.ui5.get_length_value5()))
           f.write("\n")
           f.write(str(self.ui5.get_diameter_1_5()))
           f.write("\n")
           f.write(str(self.ui5.get_diameter_2_5()))
           f.write("\n")
           f.write(str(self.ui5.get_angle5()))
           f.write("\n")
           
           f.write("WING")
           f.write("\n")
           f.write(str(self.get_airfoil_value_index()))
           f.write("\n")
           f.write(str(self.get_wing_span_value()))
           f.write("\n")
           f.write(str(self.get_root_chord_value()))
           f.write("\n")
           f.write(str(self.get_tip_chord_value()))
           f.write("\n")
           f.write(str(self.get_setting_angle_value()))
           f.write("\n")
           f.write(str(self.get_root_twist_angle_value()))
           f.write("\n")
           f.write(str(self.get_tip_twist_angle_value()))
           f.write("\n")
           f.write(str(self.get_sweep_angle_value()))
           f.write("\n")
           f.write(str(self.get_dihedral_angle_value()))
           f.write("\n")
           f.write(str(self.get_Vlocation_value()))
           f.write("\n")
           f.write(str(self.get_Hlocation_value()))
           f.write("\n")
           
           f.write("VS TAIL")
           f.write("\n")
           f.write(str(self.get_VS_airfoil_value_index()))
           f.write("\n")
           f.write(str(self.get_VS_span_value()))
           f.write("\n")
           f.write(str(self.get_VS_rootchord_value()))
           f.write("\n")
           f.write(str(self.get_VS_rootchord_value()))
           f.write("\n")
           f.write(str(self.get_VS_sweepangle_value()))
           f.write("\n")
           
           f.write("HS TAIL")
           f.write("\n")
           f.write(str(self.get_HS_airfoil_value_index()))
           f.write("\n")
           f.write(str(self.get_HS_span_value()))
           f.write("\n")
           f.write(str(self.get_HS_rootchord_value()))
           f.write("\n")
           f.write(str(self.get_HS_tipchord_value()))
           f.write("\n")
           f.write(str(self.get_HS_sweepangle_value()))
           f.write("\n")
           f.write(str(self.get_horizontal_location_tail()))
           f.close()
    
    def load_values(self):
        with open('values.txt', 'r') as f:
            lines = f.readlines()
            self.ui1.select_type_combo_box.setCurrentIndex(int(lines[2]))
            self.ui1.Length_spinbox.setValue(float(lines[3]))
            self.ui1.diam_spinbox.setValue(float(lines[4]))
            
            if len(lines[6]) == 19:
                self.ui2.get_cylinder_button2()
            elif len(lines[6]) == 32:
                 self.ui2.get_trapezoid_button2()
            elif len(lines[6]) == 16:
                 self.ui2.get_conic_button2()
            else:
                 pass
            
            self.ui2.doubleSpinBox.setValue(float(lines[7]))
            self.ui2.doubleSpinBox_2.setValue(float(lines[8]))
            self.ui2.doubleSpinBox_3.setValue(float(lines[9]))
            self.ui2.doubleSpinBox_angle.setValue(float(lines[10]))
            
            if len(lines[12]) == 19:
                self.ui3.get_cylinder_button3()
            elif len(lines[12]) == 32:
                 self.ui3.get_trapezoid_button3()
            elif len(lines[12]) == 16:
                 self.ui3.get_conic_button3()
            else:
                 pass
           
            self.ui3.doubleSpinBox.setValue(float(lines[13]))
            self.ui3.doubleSpinBox_2.setValue(float(lines[14]))
            self.ui3.doubleSpinBox_3.setValue(float(lines[15]))
            self.ui3.doubleSpinBox_angle.setValue(float(lines[16]))
            
            if len(lines[18]) == 19:
                self.ui4.get_cylinder_button4()
            elif len(lines[18]) == 32:
                 self.ui4.get_trapezoid_button4()
            elif len(lines[18]) == 16:
                 self.ui4.get_conic_button4()
            else:
                 pass
            self.ui4.doubleSpinBox.setValue(float(lines[19]))
            self.ui4.doubleSpinBox_2.setValue(float(lines[20]))
            self.ui4.doubleSpinBox_3.setValue(float(lines[21]))
            self.ui4.doubleSpinBox_angle.setValue(float(lines[22]))
            
            if len(lines[24]) == 19:
                self.ui5.get_cylinder_button5()
            elif len(lines[24]) == 32:
                 self.ui5.get_trapezoid_button5()
            elif len(lines[24]) == 16:
                 self.ui5.get_conic_button5()
            else:
                 pass
            
            self.ui5.doubleSpinBox.setValue(float(lines[25]))
            self.ui5.doubleSpinBox_2.setValue(float(lines[26]))
            self.ui5.doubleSpinBox_3.setValue(float(lines[27]))
            self.ui5.doubleSpinBox_angle.setValue(float(lines[28]))
            self.airfoil.setCurrentIndex(int(lines[30]))
            self.wing_span.setValue(float(lines[31]))
            self.root_chord.setValue(float(lines[32]))
            self.tip_chord.setValue(float(lines[33]))
            self.setting_angle.setValue(float(lines[34]))
            self.root_twist_angle.setValue(float(lines[35]))
            self.tip_twist_angle.setValue(float(lines[36]))
            self.sweep_angle.setValue(float(lines[37]))
            self.dihedral_angle.setValue(float(lines[38]))
            self.wing_location.setValue(float(lines[39]))
            self.horizontal_location.setValue(float(lines[40]))
            
            self.VSairfoil.setCurrentIndex(int(lines[42]))
            self.VS_tailspan_2.setValue(float(lines[43]))
            self.VS_rootchord_2.setValue(float(lines[44]))
            self.VS_tipchord_2.setValue(float(lines[45]))
            self.VS_sweepangle_2.setValue(float(lines[46]))
            self.HS_airfoil.setCurrentIndex(int(lines[48]))
            self.HS_tailspan_2.setValue(float(lines[49]))
            self.HS_rootchord_2.setValue(float(lines[50]))
            self.HS_tipchord_2.setValue(float(lines[51]))
            self.HS_sweepangle_2.setValue(float(lines[52]))
            self.horizontal_location_3.setValue(float(lines[53]))
            f.close()
    
    def openSaveDialog(self):
       global file
       option = QFileDialog.Options()
       file = QFileDialog.getSaveFileName(MainWindow,"Save File","values.txt","*.txt",options=option)
       self.write_txt()
       
    
    def openLoadDialog(self):
        file_dialog = QFileDialog.getOpenFileName(MainWindow, 'Open File')
        file_path = file_dialog[0]
        self.load_values()
    
    def CATIA(self):
        CATIA = win32com.client.Dispatch("CATIA.Application")
        documents1 = CATIA.Documents
        partDocument1 = documents1.Add("Part")
        part1 = partDocument1.Part
        ShFactory = part1.HybridShapeFactory
        selection1 = partDocument1.Selection
        visPropertySet1 = selection1.VisProperties
        
        # Add Geometrical set
        bodies1 = part1.HybridBodies
        body1 = bodies1.Add()
        body1.Name="Wing" 
        ###
        body2 = bodies1.Add()
        body2.Name = "Fuselage"
        ###
        body3 = bodies1.Add()
        body3.Name = "Tail"
        ## FUSELAGE ###
        ### SLOT1#####
        try:
            spline2 = ShFactory.AddNewSpline()
            spline2.SetSplineType(0)
            spline2.SetClosing(0)
            
            for i in self.ui1.create_points_nose_cone_matrix():
                point1 = ShFactory.AddNewPointCoord(i[0], i[1],0)
                body2.AppendHybridShape(point1)
                spline2.AddPoint(point1)
                selection1.Add(point1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
            body2.AppendHybridShape(spline2)
        
            part1.Update()
            originElements2= part1.OriginElements
            hybridShapePlaneExplicit6 = originElements2.PlaneYZ
            
            reference33 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit6)
            reference34 = part1.CreateReferenceFromObject(spline2)
            hybridShapePointCoord1_1 = ShFactory.AddNewPointCoord(0.000000, 0.000000, 0.000000)
            body2.AppendHybridShape(hybridShapePointCoord1_1)
            reference35 = part1.CreateReferenceFromObject(hybridShapePointCoord1_1)
            hybridShapeLineNormal1 = ShFactory.AddNewLineNormal(reference33, reference35, 0.000000, 20.000000, False)
            body2.AppendHybridShape(hybridShapeLineNormal1)
            reference36 = part1.CreateReferenceFromObject(hybridShapeLineNormal1)
            hybridShapeRevol1 = ShFactory.AddNewRevol(reference34, 360.000000, 0.000000, reference36)
            body2.AppendHybridShape(hybridShapeRevol1)
            part1.InWorkObject = hybridShapeRevol1
            selection1.Add(spline2)
            selection1.Add(hybridShapeLineNormal1)
            selection1.Add(hybridShapePointCoord1_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        except:
            pass
        #### SLOT 2 ########
        try:
           
            if self.ui2.label_2.text() == "Selected: Cylinder":
                hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1(), 0.000000, self.ui1.get_base_diameter_value()/2)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui1.get_base_diameter_value()/2)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_2 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_2)
                part1.InWorkObject = hybridShapeRevol2_2
                part1.Update()
            
            elif self.ui2.label_2.text() == "Selected: Cylindrical Trapezoid":
                if self.ui2.doubleSpinBox_angle.value() == 0:
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1(), 0.000000, self.ui1.get_base_diameter_value()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui2.get_diameter_2_2()/2)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_2 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_2)
                    part1.InWorkObject = hybridShapeRevol2_2
                    part1.Update()
                
                elif self.ui2.doubleSpinBox_angle.value() != 0:
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1(), 0.000000, 0.000000)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, math.tan(math.radians(self.ui2.get_angle2()))*self.ui2.get_length_value2()+self.ui2.get_diameter_2_2()/2-(self.ui2.get_diameter_1_2()/2))
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                  
                    hybridShapeCircleCenterAxis1 = ShFactory.AddNewCircleCenterAxis(reference36, reference37, self.ui2.get_diameter_1_2(), False)
                    hybridShapeCircleCenterAxis1.DiameterMode = True
                    hybridShapeCircleCenterAxis1.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis1)
                    part1.InWorkObject = hybridShapeCircleCenterAxis1
                    part1.Update() 
                    
                    hybridShapeCircleCenterAxis2 = ShFactory.AddNewCircleCenterAxis(reference36, reference38, self.ui2.get_diameter_2_2(), False)
                    hybridShapeCircleCenterAxis2.DiameterMode = True
                    hybridShapeCircleCenterAxis2.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis2)
                    part1.InWorkObject = hybridShapeCircleCenterAxis2
                    part1.Update() 
                    
                    hybridShapeDirection1_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference5_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    hybridShapeExtremum1_angle = ShFactory.AddNewExtremum(reference5_angle, hybridShapeDirection1_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum1_angle)
                    part1.InWorkObject = hybridShapeExtremum1_angle
                    part1.Update ()
                    hybridShapeDirection2_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference6_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    hybridShapeExtremum2_angle = ShFactory.AddNewExtremum(reference6_angle, hybridShapeDirection2_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum2_angle)
                    part1.InWorkObject = hybridShapeExtremum2_angle
                    part1.Update() 
                    
                    hybridShapeLoft1_angle_2 = ShFactory.AddNewLoft()
                    hybridShapeLoft1_angle_2.SectionCoupling = 1
                    hybridShapeLoft1_angle_2.Relimitation = 1
                    hybridShapeLoft1_angle_2.CanonicalDetection = 2
                    reference7_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    reference8_angle = part1.CreateReferenceFromObject(hybridShapeExtremum1_angle)
                    hybridShapeLoft1_angle_2.AddSectionToLoft(reference7_angle, 1, reference8_angle)
                    reference9_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    reference10_angle = part1.CreateReferenceFromObject(hybridShapeExtremum2_angle)
                    hybridShapeLoft1_angle_2.AddSectionToLoft(reference9_angle, 1, reference10_angle)
                    body2.AppendHybridShape(hybridShapeLoft1_angle_2)
                    part1.InWorkObject = hybridShapeLoft1_angle_2
                    selection1.Add(hybridShapeCircleCenterAxis2)
                    selection1.Add(hybridShapeCircleCenterAxis1)
                    selection1.Add(hybridShapeExtremum1_angle)
                    selection1.Add(hybridShapeExtremum2_angle)
                    selection1.Add(hybridShapePointCoord2_2)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update() 
                    
            elif self.ui2.label_2.text() == "Selected: Conic":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1(), 0.000000, self.ui1.get_base_diameter_value()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, 0.00000)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_2 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_2)
                    part1.InWorkObject = hybridShapeRevol2_2
                    part1.Update()
            selection1.Add(hybridShapePointCoord2_2)
            selection1.Add(hybridShapeLinePtPt2_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        except:
           pass
        ### SLOT3 ###
        try:
            if self.ui3.label_2.text() == "Selected: Cylinder":
                if self.ui2.label_2.text() == "Selected: Cylindrical Trapezoid":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui2.get_diameter_2_2()/2)
                elif self.ui2.label_2.text() == "Selected: Cylinder":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui2.get_diameter_1_2()/2)
                
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_1_3()/2)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_3 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_3)
                part1.InWorkObject = hybridShapeRevol2_3
                part1.Update()
           
            
            elif self.ui3.label_2.text() == "Selected: Cylindrical Trapezoid":
                
                if self.ui3.doubleSpinBox_angle.value() == 0:
                    if self.ui2.label_2.text() == "Selected: Cylindrical Trapezoid":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui2.get_diameter_2_2()/2)
                    elif self.ui2.label_2.text() == "Selected: Cylinder":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui2.get_diameter_1_2()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_2_3()/2)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_3 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_3)
                    part1.InWorkObject = hybridShapeRevol2_3
                    part1.Update()
                
                elif self.ui3.doubleSpinBox_angle.value() != 0:
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, 0.000000)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, math.tan(math.radians(self.ui3.get_angle3()))*self.ui3.get_length_value3()+self.ui3.get_diameter_2_3()/2-(self.ui3.get_diameter_1_3()/2))
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                  
                    hybridShapeCircleCenterAxis1 = ShFactory.AddNewCircleCenterAxis(reference36, reference37, self.ui3.get_diameter_1_3(), False)
                    hybridShapeCircleCenterAxis1.DiameterMode = True
                    hybridShapeCircleCenterAxis1.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis1)
                    part1.InWorkObject = hybridShapeCircleCenterAxis1
                    part1.Update() 
                    
                    hybridShapeCircleCenterAxis2 = ShFactory.AddNewCircleCenterAxis(reference36, reference38, self.ui3.get_diameter_2_3(), False)
                    hybridShapeCircleCenterAxis2.DiameterMode = True
                    hybridShapeCircleCenterAxis2.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis2)
                    part1.InWorkObject = hybridShapeCircleCenterAxis2
                    part1.Update() 
                    
                    hybridShapeDirection1_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference5_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    hybridShapeExtremum1_angle = ShFactory.AddNewExtremum(reference5_angle, hybridShapeDirection1_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum1_angle)
                    part1.InWorkObject = hybridShapeExtremum1_angle
                    part1.Update ()
                    hybridShapeDirection2_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference6_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    hybridShapeExtremum2_angle = ShFactory.AddNewExtremum(reference6_angle, hybridShapeDirection2_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum2_angle)
                    part1.InWorkObject = hybridShapeExtremum2_angle
                    part1.Update() 
                    
                    hybridShapeLoft1_angle_3 = ShFactory.AddNewLoft()
                    hybridShapeLoft1_angle_3.SectionCoupling = 1
                    hybridShapeLoft1_angle_3.Relimitation = 1
                    hybridShapeLoft1_angle_3.CanonicalDetection = 2
                    reference7_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    reference8_angle = part1.CreateReferenceFromObject(hybridShapeExtremum1_angle)
                    hybridShapeLoft1_angle_3.AddSectionToLoft(reference7_angle, 1, reference8_angle)
                    reference9_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    reference10_angle = part1.CreateReferenceFromObject(hybridShapeExtremum2_angle)
                    hybridShapeLoft1_angle_3.AddSectionToLoft(reference9_angle, 1, reference10_angle)
                    body2.AppendHybridShape(hybridShapeLoft1_angle_3)
                    part1.InWorkObject = hybridShapeLoft1_angle_3
                    selection1.Add(hybridShapeCircleCenterAxis2)
                    selection1.Add(hybridShapeCircleCenterAxis1)
                    selection1.Add(hybridShapeExtremum1_angle)
                    selection1.Add(hybridShapeExtremum2_angle)
                    selection1.Add(hybridShapePointCoord2_2)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update() 
            elif self.ui3.label_2.text() == "Selected: Conic":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2(), 0.000000, self.ui3.get_diameter_1_3()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, 0.00000)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_3 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_3)
                    part1.InWorkObject = hybridShapeRevol2_3
                    part1.Update()
            selection1.Add(hybridShapePointCoord2_2)
            selection1.Add(hybridShapeLinePtPt2_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        except:
            pass
        ### SLOT4 ###
        try:
            
            if self.ui4.label_2.text() == "Selected: Cylinder":
                if self.ui3.label_2.text() == "Selected: Cylindrical Trapezoid":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_2_3()/2)
                elif self.ui3.label_2.text() == "Selected: Cylinder":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_1_3()/2)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_1_4()/2)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_4 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_4)
                part1.InWorkObject = hybridShapeRevol2_4
                part1.Update()
            
            elif self.ui4.label_2.text() == "Selected: Cylindrical Trapezoid":
                if self.ui4.doubleSpinBox_angle.value() == 0:
                    if self.ui3.label_2.text() == "Selected: Cylindrical Trapezoid":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_2_3()/2)
                    elif self.ui3.label_2.text() == "Selected: Cylinder":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui3.get_diameter_1_3()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_2_4()/2)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_4 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_4)
                    part1.InWorkObject = hybridShapeRevol2_4
                    part1.Update()
                if self.ui4.doubleSpinBox_angle.value() != 0:
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, 0.000000)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, math.tan(math.radians(self.ui4.get_angle4()))*self.ui4.get_length_value4()+self.ui4.get_diameter_2_4()/2-(self.ui4.get_diameter_1_4()/2))
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                  
                    hybridShapeCircleCenterAxis1 = ShFactory.AddNewCircleCenterAxis(reference36, reference37, self.ui4.get_diameter_1_4(), False)
                    hybridShapeCircleCenterAxis1.DiameterMode = True
                    hybridShapeCircleCenterAxis1.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis1)
                    part1.InWorkObject = hybridShapeCircleCenterAxis1
                    part1.Update() 
                    
                    hybridShapeCircleCenterAxis2 = ShFactory.AddNewCircleCenterAxis(reference36, reference38, self.ui4.get_diameter_2_4(), False)
                    hybridShapeCircleCenterAxis2.DiameterMode = True
                    hybridShapeCircleCenterAxis2.SetLimitation(1)
                    body2.AppendHybridShape(hybridShapeCircleCenterAxis2)
                    part1.InWorkObject = hybridShapeCircleCenterAxis2
                    part1.Update() 
                    
                    hybridShapeDirection1_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference5_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    hybridShapeExtremum1_angle = ShFactory.AddNewExtremum(reference5_angle, hybridShapeDirection1_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum1_angle)
                    part1.InWorkObject = hybridShapeExtremum1_angle
                    part1.Update ()
                    hybridShapeDirection2_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                    reference6_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    hybridShapeExtremum2_angle = ShFactory.AddNewExtremum(reference6_angle, hybridShapeDirection2_angle, 1)
                    body2.AppendHybridShape(hybridShapeExtremum2_angle)
                    part1.InWorkObject = hybridShapeExtremum2_angle
                    part1.Update() 
                    
                    hybridShapeLoft1_angle_4 = ShFactory.AddNewLoft()
                    hybridShapeLoft1_angle_4.SectionCoupling = 1
                    hybridShapeLoft1_angle_4.Relimitation = 1
                    hybridShapeLoft1_angle_4.CanonicalDetection = 2
                    reference7_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                    reference8_angle = part1.CreateReferenceFromObject(hybridShapeExtremum1_angle)
                    hybridShapeLoft1_angle_4.AddSectionToLoft(reference7_angle, 1, reference8_angle)
                    reference9_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                    reference10_angle = part1.CreateReferenceFromObject(hybridShapeExtremum2_angle)
                    hybridShapeLoft1_angle_4.AddSectionToLoft(reference9_angle, 1, reference10_angle)
                    body2.AppendHybridShape(hybridShapeLoft1_angle_4)
                    part1.InWorkObject = hybridShapeLoft1_angle_4
                    selection1.Add(hybridShapeCircleCenterAxis2)
                    selection1.Add(hybridShapeCircleCenterAxis1)
                    selection1.Add(hybridShapeExtremum1_angle)
                    selection1.Add(hybridShapeExtremum2_angle)
                    selection1.Add(hybridShapePointCoord2_2)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update() 
            elif self.ui4.label_2.text() == "Selected: Conic":
                hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3(), 0.000000, self.ui4.get_diameter_1_4()/2)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, 0.00000)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_4 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_4)
                part1.InWorkObject = hybridShapeRevol2_4
                part1.Update()
            selection1.Add(hybridShapePointCoord2_2)
            selection1.Add(hybridShapeLinePtPt2_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        except:
            pass
        ### SLOT5 ###
        try:
            
            if self.ui5.label_2.text() == "Selected: Cylinder":
                if self.ui4.label_2.text() == "Selected: Cylindrical Trapezoid":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_2_4()/2)
                elif self.ui4.label_2.text() == "Selected: Cylinder":
                    hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_1_4()/2)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4()+self.ui5.get_length_value5(), 0.000000, self.ui5.get_diameter_1_5()/2)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_5 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_5)
                part1.InWorkObject = hybridShapeRevol2_5
                part1.Update()
            
            elif self.ui5.label_2.text() == "Selected: Cylindrical Trapezoid":
                if self.ui5.doubleSpinBox_angle.value() == 0:
                    if self.ui4.label_2.text() == "Selected: Cylindrical Trapezoid":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_2_4()/2)
                    elif self.ui4.label_2.text() == "Selected: Cylinder":
                        hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui4.get_diameter_1_4()/2)
                    selection1.Add(hybridShapePointCoord2_1)
                    body2.AppendHybridShape(hybridShapePointCoord2_1)
                    reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                    selection1.Add(hybridShapePointCoord2_1)
                    visPropertySet1.SetShow(1)
                    selection1.Clear()
                    part1.Update()
                    hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4()+self.ui5.get_length_value5(), 0.000000, self.ui5.get_diameter_2_5()/2)
                    body2.AppendHybridShape(hybridShapePointCoord2_2)
                    reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                    hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                    body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                    part1.InWorkObject = hybridShapeLinePtPt2_1
                    reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                    hybridShapeRevol2_5 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                    body2.AppendHybridShape(hybridShapeRevol2_5)
                    part1.InWorkObject = hybridShapeRevol2_5
                    part1.Update()
            if self.ui5.doubleSpinBox_angle.value() != 0:
                hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, 0.000000)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4()+self.ui5.get_length_value5(), 0.000000, math.tan(math.radians(self.ui5.get_angle5()))*self.ui5.get_length_value5()+self.ui5.get_diameter_2_5()/2-(self.ui5.get_diameter_1_5()/2))
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
              
                hybridShapeCircleCenterAxis1 = ShFactory.AddNewCircleCenterAxis(reference36, reference37, self.ui5.get_diameter_1_5(), False)
                hybridShapeCircleCenterAxis1.DiameterMode = True
                hybridShapeCircleCenterAxis1.SetLimitation(1)
                body2.AppendHybridShape(hybridShapeCircleCenterAxis1)
                part1.InWorkObject = hybridShapeCircleCenterAxis1
                part1.Update() 
                
                hybridShapeCircleCenterAxis2 = ShFactory.AddNewCircleCenterAxis(reference36, reference38, self.ui5.get_diameter_2_5(), False)
                hybridShapeCircleCenterAxis2.DiameterMode = True
                hybridShapeCircleCenterAxis2.SetLimitation(1)
                body2.AppendHybridShape(hybridShapeCircleCenterAxis2)
                part1.InWorkObject = hybridShapeCircleCenterAxis2
                part1.Update() 
                
                hybridShapeDirection1_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                reference5_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                hybridShapeExtremum1_angle = ShFactory.AddNewExtremum(reference5_angle, hybridShapeDirection1_angle, 1)
                body2.AppendHybridShape(hybridShapeExtremum1_angle)
                part1.InWorkObject = hybridShapeExtremum1_angle
                part1.Update ()
                hybridShapeDirection2_angle = ShFactory.AddNewDirectionByCoord(1.000000, 2.000000, 3.000000)
                reference6_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                hybridShapeExtremum2_angle = ShFactory.AddNewExtremum(reference6_angle, hybridShapeDirection2_angle, 1)
                body2.AppendHybridShape(hybridShapeExtremum2_angle)
                part1.InWorkObject = hybridShapeExtremum2_angle
                part1.Update() 
                
                hybridShapeLoft1_angle_5 = ShFactory.AddNewLoft()
                hybridShapeLoft1_angle_5.SectionCoupling = 1
                hybridShapeLoft1_angle_5.Relimitation = 1
                hybridShapeLoft1_angle_5.CanonicalDetection = 2
                reference7_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis1)
                reference8_angle = part1.CreateReferenceFromObject(hybridShapeExtremum1_angle)
                hybridShapeLoft1_angle_5.AddSectionToLoft(reference7_angle, 1, reference8_angle)
                reference9_angle = part1.CreateReferenceFromObject(hybridShapeCircleCenterAxis2)
                reference10_angle = part1.CreateReferenceFromObject(hybridShapeExtremum2_angle)
                hybridShapeLoft1_angle_5.AddSectionToLoft(reference9_angle, 1, reference10_angle)
                body2.AppendHybridShape(hybridShapeLoft1_angle_5)
                part1.InWorkObject = hybridShapeLoft1_angle_5
                selection1.Add(hybridShapeCircleCenterAxis2)
                selection1.Add(hybridShapeCircleCenterAxis1)
                selection1.Add(hybridShapeExtremum1_angle)
                selection1.Add(hybridShapeExtremum2_angle)
                selection1.Add(hybridShapePointCoord2_2)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update() 
            
            elif self.ui5.label_2.text() == "Selected: Conic":
                hybridShapePointCoord2_1 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4(), 0.000000, self.ui5.get_diameter_1_5()/2)
                selection1.Add(hybridShapePointCoord2_1)
                body2.AppendHybridShape(hybridShapePointCoord2_1)
                reference37 = part1.CreateReferenceFromObject(hybridShapePointCoord2_1)
                selection1.Add(hybridShapePointCoord2_1)
                visPropertySet1.SetShow(1)
                selection1.Clear()
                part1.Update()
                hybridShapePointCoord2_2 = ShFactory.AddNewPointCoord(self.ui1.get_length_value1()+self.ui2.get_length_value2()+self.ui3.get_length_value3()+self.ui4.get_length_value4()+self.ui5.get_length_value5(), 0.000000, 0.00000)
                body2.AppendHybridShape(hybridShapePointCoord2_2)
                reference38 =part1.CreateReferenceFromObject(hybridShapePointCoord2_2) 
                hybridShapeLinePtPt2_1 = ShFactory.AddNewLinePtPt(reference37, reference38)
                body2.AppendHybridShape(hybridShapeLinePtPt2_1)
                part1.InWorkObject = hybridShapeLinePtPt2_1
                reference39 = part1.CreateReferenceFromObject(hybridShapeLinePtPt2_1)  
                hybridShapeRevol2_5 = ShFactory.AddNewRevol(reference39, 360.000000, 0.000000, reference36)
                body2.AppendHybridShape(hybridShapeRevol2_5)
                part1.InWorkObject = hybridShapeRevol2_5
                part1.Update()
            selection1.Add(hybridShapePointCoord2_2)
            selection1.Add(hybridShapeLinePtPt2_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        except:
            pass
        # ###########################################
        #Join
        try:
            
            reference44 = part1.CreateReferenceFromObject(hybridShapeRevol1)
            if self.ui2.get_length_value2()>0 and self.ui2.get_diameter_1_2() >0:
                if self.ui2.get_angle2() != 0 and self.ui2.label_2.text() == "Selected: Cylindrical Trapezoid":
                    reference40 = part1.CreateReferenceFromObject(hybridShapeLoft1_angle_2)
                else:
                    reference40 = part1.CreateReferenceFromObject(hybridShapeRevol2_2)
            hybridShapeAssemble3 = ShFactory.AddNewJoin(reference44, reference40)
            
            if self.ui3.get_length_value3()>0 and self.ui3.get_diameter_1_3() >0:    
                if self.ui3.get_angle3() != 0 and self.ui3.label_2.text() == "Selected: Cylindrical Trapezoid":
                    reference40_3 = part1.CreateReferenceFromObject(hybridShapeLoft1_angle_3)
                else:
                    reference40_3 = part1.CreateReferenceFromObject(hybridShapeRevol2_3)
                hybridShapeAssemble3.AddElement(reference40_3)
            
            if self.ui4.get_length_value4()>0 and self.ui4.get_diameter_1_4() >0:
                if self.ui4.get_angle4() != 0 and self.ui4.label_2.text() == "Selected: Cylindrical Trapezoid":
                    reference40_4 = part1.CreateReferenceFromObject(hybridShapeLoft1_angle_4)
                else:
                    reference40_4 = part1.CreateReferenceFromObject(hybridShapeRevol2_4)
                hybridShapeAssemble3.AddElement(reference40_4)
            
            if self.ui5.get_length_value5()>0 and self.ui5.get_diameter_1_5() >0:
                if self.ui5.get_angle5() != 0 and self.ui5.label_2.text() == "Selected: Cylindrical Trapezoid":
                    reference40_5 = part1.CreateReferenceFromObject(hybridShapeLoft1_angle_5)
                else:
                    reference40_5 = part1.CreateReferenceFromObject(hybridShapeRevol2_5)
                hybridShapeAssemble3.AddElement(reference40_5)
                
            hybridShapeAssemble3.SetConnex(1)
            hybridShapeAssemble3.SetManifold(0)
            hybridShapeAssemble3.SetSimplify(0)
            hybridShapeAssemble3.SetSuppressMode(0)
            hybridShapeAssemble3.SetDeviation(0.001000)
            hybridShapeAssemble3.SetAngularToleranceMode(0)
            hybridShapeAssemble3.SetAngularTolerance(0.500000)
            hybridShapeAssemble3.SetFederationPropagation(0)
            body2.AppendHybridShape(hybridShapeAssemble3)
            part1.InWorkObject = hybridShapeAssemble3
            selection1.Add(hybridShapeRevol2_2)
            selection1.Add(hybridShapeRevol1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update() 
        except:
            pass
        ##### WING #####
        ## Add Spline
        part1.InWorkObject = body1
        points = airfoil_points(self.get_airfoil_value())
        spline1 = ShFactory.AddNewSpline()
        spline1.SetSplineType(0)
        spline1.SetClosing(0)
        for i in points[::-1]:    
            point1 = ShFactory.AddNewPointCoord(i[0], 0,i[1])
            body1.AppendHybridShape(point1)
            spline1.AddPoint(point1)
            selection1.Add(point1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        point0 = ShFactory.AddNewPointCoord(points[-1][0], 0,points[-1][1])
        spline1.AddPoint(point0)
        body1.AppendHybridShape(spline1)
        part1.InWorkObject = spline1
        part1.Update()
        ##
        ### Scaling
        hybridBody1 = bodies1.Item("Wing")
        hybridShapes1 = hybridBody1.HybridShapes
        reference1 = part1.CreateReferenceFromObject(spline1)
        originElements1 = part1.OriginElements
        hybridShapePlaneExplicit1 = originElements1.PlaneXY
        reference2 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
        hybridShapeScaling1 = ShFactory.AddNewHybridScaling(reference1, reference2, self.get_root_chord_value()) # It will change after GUI
        hybridShapeScaling1.VolumeResult = False
        body1.AppendHybridShape(hybridShapeScaling1)
        part1.InWorkObject = hybridShapeScaling1
        
        reference3 = part1.CreateReferenceFromObject(hybridShapeScaling1)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit1 = originElements1.PlaneYZ
        reference4 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
        hybridShapeScaling2 = ShFactory.AddNewHybridScaling(reference3, reference4, self.get_root_chord_value()) # It will change after GUI
        hybridShapeScaling2.VolumeResult = False
        body1.AppendHybridShape(hybridShapeScaling2)
        part1.InWorkObject = hybridShapeScaling2
        selection1.Add(spline1)
        selection1.Add(hybridShapeScaling1)
        selection1.Add(hybridShapeScaling2)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        ###
        # Make tip airfoil
        reference5 = part1.CreateReferenceFromObject(hybridShapeScaling2)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit1 = originElements1.PlaneXY
        reference6 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
        hybridShapeScaling3 = ShFactory.AddNewHybridScaling(reference5, reference6, self.get_tip_chord_value()/self.get_root_chord_value()) # It will change after GUI
        hybridShapeScaling3.VolumeResult = False
        body1.AppendHybridShape(hybridShapeScaling3)
        part1.InWorkObject = hybridShapeScaling3
        
        reference7 = part1.CreateReferenceFromObject(hybridShapeScaling3)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit2 = originElements1.PlaneYZ
        reference8 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit2)
        hybridShapeScaling4 = ShFactory.AddNewHybridScaling(reference7, reference8, self.get_tip_chord_value()/self.get_root_chord_value()) # It will change after GUI
        hybridShapeScaling4.VolumeResult = False
        body1.AppendHybridShape(hybridShapeScaling4)
        part1.InWorkObject = hybridShapeScaling4
        
        selection1.Add(hybridShapeScaling3)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        # Half-span value
        hybridShapePlaneExplicit3 = originElements1.PlaneZX
        reference9 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit3)
        hybridShapeDirection1 = ShFactory.AddNewDirection(reference9)
        hybridShapeTranslate1 = ShFactory.AddNewEmptyTranslate()
        reference10 = part1.CreateReferenceFromObject(hybridShapeScaling4)
        hybridShapeTranslate1.ElemToTranslate = reference10
        hybridShapeTranslate1.VectorType = 0
        hybridShapeTranslate1.Direction=hybridShapeDirection1
        hybridShapeTranslate1.DistanceValue = self.get_wing_span_value()/2 
        hybridShapeTranslate1.VolumeResult = False
        body1.AppendHybridShape(hybridShapeTranslate1)
        part1.InWorkObject = hybridShapeTranslate1
        selection1.Add(hybridShapeScaling4)
        selection1.Add(hybridShapeTranslate1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        #Root Twist
        hybridShapeRotate1 = ShFactory.AddNewEmptyRotate()
        hybridShapeRotate1.ElemToRotate = reference5
        hybridShapeRotate1.VolumeResult = False
        hybridShapeRotate1.RotationType = 0
        hybridShapeRotate1.Axis = reference9
        hybridShapeRotate1.AngleValue = self.get_root_twist_angle_value() 
        body1.AppendHybridShape(hybridShapeRotate1)
        part1.InWorkObject = hybridShapeRotate1
        selection1.Add(hybridShapeRotate1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        reference12 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
        #Sweep
        if self.get_sweep_angle_value() !=0 and self.get_dihedral_angle_value() ==0:
            hybridShapePlaneExplicit4 = originElements1.PlaneYZ
            reference11 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit4)
            hybridShapeDirection1_sweep = ShFactory.AddNewDirection(reference11)
            hybridShapeTranslate2 = ShFactory.AddNewEmptyTranslate()
            hybridShapeTranslate2.ElemToTranslate = reference12
            hybridShapeTranslate2.VectorType = 0
            hybridShapeTranslate2.Direction = hybridShapeDirection1_sweep
            if self.get_sweep_angle_value()>0:
               hybridShapeTranslate2.DistanceValue = (self.get_wing_span_value()/2*math.tan(math.radians(self.get_sweep_angle_value())))-(self.get_tip_chord_value()*0.25)+(self.get_root_chord_value()*0.25) # it will change
            elif self.get_sweep_angle_value()<0:
               hybridShapeTranslate2.DistanceValue = (self.get_wing_span_value()/2*math.tan(math.radians(self.get_sweep_angle_value())))+(self.get_tip_chord_value()*0.25)-(self.get_root_chord_value()*0.25) # it will change
            hybridShapeTranslate2.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate2)
            part1.InWorkObject =hybridShapeTranslate2
            selection1.Add(hybridShapeTranslate2)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        
        #Dihedral
        elif self.get_sweep_angle_value() == 0 and self.get_dihedral_angle_value() !=0:
            hybridShapePlaneExplicit5 = originElements1.PlaneXY
            reference13 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit5)
            hybridShapeDirection1_dihedral = ShFactory.AddNewDirection(reference13)
            hybridShapeTranslate2 = ShFactory.AddNewEmptyTranslate()
            reference14 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
            hybridShapeTranslate2.ElemToTranslate = reference14
            hybridShapeTranslate2.VectorType = 0
            hybridShapeTranslate2.Direction = hybridShapeDirection1_dihedral
            hybridShapeTranslate2.DistanceValue = self.get_wing_span_value()/2*math.tan(math.radians(self.get_dihedral_angle_value())) # change parameter
            hybridShapeTranslate2.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate2)
            part1.InWorkObject =hybridShapeTranslate2
            selection1.Add(hybridShapeTranslate2)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        elif self.get_sweep_angle_value() != 0 and self.get_dihedral_angle_value() !=0:
            hybridShapePlaneExplicit5 = originElements1.PlaneXY
            reference13 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit5)
            hybridShapeDirection1_dihedral = ShFactory.AddNewDirection(reference13)
            hybridShapeTranslate2_1 = ShFactory.AddNewEmptyTranslate()
            reference14 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
            hybridShapeTranslate2_1.ElemToTranslate = reference14
            hybridShapeTranslate2_1.VectorType = 0
            hybridShapeTranslate2_1.Direction = hybridShapeDirection1_dihedral
            hybridShapeTranslate2_1.DistanceValue = self.get_wing_span_value()/2*math.tan(math.radians(self.get_dihedral_angle_value())) 
            hybridShapeTranslate2_1.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate2_1)
            part1.InWorkObject =hybridShapeTranslate2_1
            selection1.Add(hybridShapeTranslate2_1)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
            
            
            hybridShapePlaneExplicit4 = originElements1.PlaneYZ
            reference11 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit4)
            hybridShapeDirection1_sweep_dihedral = ShFactory.AddNewDirection(reference11)
            hybridShapeTranslate2 = ShFactory.AddNewEmptyTranslate()
            reference12_1 = part1.CreateReferenceFromObject(hybridShapeTranslate2_1)
            hybridShapeTranslate2.ElemToTranslate = reference12_1
            hybridShapeTranslate2.VectorType = 0
            hybridShapeTranslate2.Direction = hybridShapeDirection1_sweep_dihedral
            if self.get_sweep_angle_value()>0:
                hybridShapeTranslate2.DistanceValue = (self.get_wing_span_value()/2*math.tan(math.radians(self.get_sweep_angle_value())))-(self.get_tip_chord_value()*0.25)+(self.get_root_chord_value()*0.25) 
            elif self.get_sweep_angle_value()<0:
                hybridShapeTranslate2.DistanceValue = (self.get_wing_span_value()/2*math.tan(math.radians(self.get_sweep_angle_value())))+(self.get_tip_chord_value()*0.25)-(self.get_root_chord_value()*0.25) 
            hybridShapeTranslate2.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate2)
            part1.InWorkObject =hybridShapeTranslate2
            selection1.Add(hybridShapeTranslate2)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        else:
            hybridShapeTranslate2 = hybridShapeTranslate1
        ###
        #Tip Twist
        hybridShapeDirection2 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        reference15 = part1.CreateReferenceFromObject(hybridShapeScaling2)
        hybridShapeExtremum1 = ShFactory.AddNewExtremum(reference15, hybridShapeDirection2, 1)
        body1.AppendHybridShape(hybridShapeExtremum1)
        part1.InWorkObject = hybridShapeExtremum1
        
        hybridShapeDirection3 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        if self.get_sweep_angle_value() !=0 or self.get_dihedral_angle_value() != 0:
            reference16 = part1.CreateReferenceFromObject(hybridShapeTranslate2) #change parameter
        else:
            reference16 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
        hybridShapeExtremum2 = ShFactory.AddNewExtremum(reference16, hybridShapeDirection3, 1)
        body1.AppendHybridShape(hybridShapeExtremum2)
        part1.InWorkObject = hybridShapeExtremum2
        reference20 = part1.CreateReferenceFromObject(hybridShapeExtremum2)
        reference19 = part1.CreateReferenceFromObject(hybridShapeTranslate2)
        
        hybridShapePointCoord1 = ShFactory.AddNewPointCoord(0.000000, 0.000000, 0.000000)
        body1.AppendHybridShape(hybridShapePointCoord1)
        hybridShapePointOnCurve1 = ShFactory.AddNewPointOnCurveWithReferenceFromPercent(reference19, reference20, 0.500000, False)
        body1.AppendHybridShape(hybridShapePointOnCurve1)
        reference26 = part1.CreateReferenceFromObject(hybridShapePointCoord1)
        reference27 = part1.CreateReferenceFromObject(hybridShapePointOnCurve1)
        hybridShapeLinePtPt1 = ShFactory.AddNewLinePtPt(reference26, reference27)
        body1.AppendHybridShape(hybridShapeLinePtPt1)
        part1.InWorkObject = hybridShapeLinePtPt1
        part1.Update()
        reference28 = part1.CreateReferenceFromObject(hybridShapeLinePtPt1)
        hybridShapeRotate2 = ShFactory.AddNewEmptyRotate()
        if self.get_sweep_angle_value() !=0 or self.get_dihedral_angle_value() !=0: 
            hybridShapeRotate2.ElemToRotate = reference19
        elif self.get_sweep_angle_value() == 0 and self.get_dihedral_angle_value() ==0:
            hybridShapeRotate2.ElemToRotate = reference12
            
        hybridShapeRotate2.VolumeResult = False
        hybridShapeRotate2.RotationType = 0
        hybridShapeRotate2.Axis = reference28
        hybridShapeRotate2.AngleValue = self.get_tip_twist_angle_value() 
        body1.AppendHybridShape(hybridShapeRotate2)
        part1.InWorkObject = hybridShapeRotate2
        selection1.Add(hybridShapeRotate2)
        selection1.Add(hybridShapeLinePtPt1)
        selection1.Add(hybridShapePointOnCurve1)
        selection1.Add(hybridShapePointCoord1)
        selection1.Add(hybridShapeExtremum1)
        selection1.Add(hybridShapeExtremum2)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        ####
        # Multi_sections_surface,fill,join and symetry
        hybridShapeDirection2 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        reference15 = part1.CreateReferenceFromObject(hybridShapeScaling2)
        hybridShapeExtremum1 = ShFactory.AddNewExtremum(reference15, hybridShapeDirection2, 1)
        body1.AppendHybridShape(hybridShapeExtremum1)
        part1.InWorkObject = hybridShapeExtremum1
        selection1.Add(hybridShapeExtremum1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        hybridShapeDirection3 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        if self.get_sweep_angle_value() !=0 or self.get_dihedral_angle_value() != 0:
            reference16 = part1.CreateReferenceFromObject(hybridShapeTranslate2) 
        else:
            reference16 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
        
        if self.get_tip_twist_angle_value() != 0:
            reference16 = part1.CreateReferenceFromObject(hybridShapeRotate2)
        if self.get_root_twist_angle_value() != 0:
            reference15 = part1.CreateReferenceFromObject(hybridShapeRotate1)
            hybridShapeExtremum1 = ShFactory.AddNewExtremum(reference15, hybridShapeDirection3, 1)
            
        hybridShapeExtremum2 = ShFactory.AddNewExtremum(reference16, hybridShapeDirection3, 1)
        body1.AppendHybridShape(hybridShapeExtremum2)
        part1.InWorkObject = hybridShapeExtremum2
       
        hybridShapeLoft1 = ShFactory.AddNewLoft()
        hybridShapeLoft1.SectionCoupling = 1
        hybridShapeLoft1.Relimitation = 1
        hybridShapeLoft1.CanonicalDetection = 2
        
        reference18 = part1.CreateReferenceFromObject(hybridShapeExtremum1)
        hybridShapeLoft1.AddSectionToLoft(reference15, 1, reference18)
        reference20 = part1.CreateReferenceFromObject(hybridShapeExtremum2)
        hybridShapeLoft1.AddSectionToLoft(reference16, 1, reference20)
        hybridBody1.AppendHybridShape(hybridShapeLoft1)
        part1.InWorkObject = hybridShapeLoft1   
        selection1.Add(hybridShapeExtremum1)
        selection1.Add(hybridShapeExtremum2)
        selection1.Add(hybridShapeLoft1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        
        hybridShapeFill1 = ShFactory.AddNewFill()
        if self.get_sweep_angle_value() !=0 and self.get_dihedral_angle_value() ==0 and self.get_tip_twist_angle_value() == 0:
            hybridShapeFill1.AddBound(hybridShapeTranslate2) #change parameter
        elif self.get_sweep_angle_value() == 0 and self.get_dihedral_angle_value() !=0 and self.get_tip_twist_angle_value() == 0:
            hybridShapeFill1.AddBound(hybridShapeTranslate2) #change parameter
        elif self.get_sweep_angle_value() != 0 and self.get_dihedral_angle_value() !=0 and self.get_tip_twist_angle_value() == 0:
            hybridShapeFill1.AddBound(hybridShapeTranslate2) #change parameter
        elif self.get_tip_twist_angle_value() != 0:
            hybridShapeFill1.AddBound(hybridShapeRotate2) #change parameter
        else:
            hybridShapeFill1.AddBound(hybridShapeTranslate1)
        
        
        hybridShapeFill1.Continuity = 0
        hybridBody1.AppendHybridShape(hybridShapeFill1)
        part1.InWorkObject = hybridShapeFill1
        part1.Update()
        reference21 = part1.CreateReferenceFromObject(hybridShapeFill1)
        reference22 = part1.CreateReferenceFromObject(hybridShapeLoft1)
        hybridShapeAssemble1 = ShFactory.AddNewJoin(reference21, reference22)
        hybridShapeAssemble1.SetConnex(1)
        hybridShapeAssemble1.SetManifold(0)
        hybridShapeAssemble1.SetSimplify(0)
        hybridShapeAssemble1.SetSuppressMode(0)
        hybridShapeAssemble1.SetDeviation(0.001000)
        hybridShapeAssemble1.SetAngularToleranceMode(0)
        hybridShapeAssemble1.SetAngularTolerance(0.500000)
        hybridShapeAssemble1.SetFederationPropagation(0)
        hybridBody1.AppendHybridShape(hybridShapeAssemble1)
        part1.InWorkObject = hybridShapeAssemble1
        selection1.Add(hybridShapeFill1)
        visPropertySet1.SetShow(1)
        part1.Update()
        reference23 = part1.CreateReferenceFromObject(hybridShapeAssemble1)
        hybridShapeSymmetry1 = ShFactory.AddNewSymmetry(reference23, reference9)
        hybridShapeSymmetry1.VolumeResult = False
        hybridBody1.AppendHybridShape(hybridShapeSymmetry1)
        part1.InWorkObject = hybridShapeSymmetry1
        part1.Update() 
        reference23 = part1.CreateReferenceFromObject(hybridShapeAssemble1)
        reference24 = part1.CreateReferenceFromObject(hybridShapeSymmetry1)
        hybridShapeAssemble2 = ShFactory.AddNewJoin(reference23, reference24)
        hybridShapeAssemble2.SetConnex(1)
        hybridShapeAssemble2.SetManifold(0)
        hybridShapeAssemble2.SetSimplify(0)
        hybridShapeAssemble2.SetSuppressMode(0)
        hybridShapeAssemble2.SetDeviation(0.001000)
        hybridShapeAssemble2.SetAngularToleranceMode(0)
        hybridShapeAssemble2.SetAngularTolerance(0.500000)
        hybridShapeAssemble2.SetFederationPropagation(0)
        hybridBody1.AppendHybridShape(hybridShapeAssemble2)
        selection1.Add(hybridShapeAssemble1)
        selection1.Add(hybridShapeSymmetry1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        ###
        #Setting Angle
        if self.get_setting_angle_value() != 0:
            hybridShapeRotate1_wing = ShFactory.AddNewEmptyRotate()
            reference29 = part1.CreateReferenceFromObject(hybridShapeAssemble2)
            hybridShapeRotate1_wing.ElemToRotate = reference29
            hybridShapeRotate1_wing.VolumeResult = False
            hybridShapeRotate1_wing.RotationType = 0
            hybridShapeRotate1_wing.Axis = reference9
            hybridShapeRotate1_wing.AngleValue = self.get_setting_angle_value() 
            body1.AppendHybridShape(hybridShapeRotate1_wing)
            reference30 = part1.CreateReferenceFromObject(hybridShapeRotate1_wing)
            part1.InWorkObject = hybridShapeRotate1
            selection1.Add(hybridShapeAssemble2)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        #Horizontal Locaiton 
        if self.get_Hlocation_value() != 0:
            hybridShapeTranslate_wing = ShFactory.AddNewEmptyTranslate()
            reference29 = part1.CreateReferenceFromObject(hybridShapeAssemble2)
            if self.get_setting_angle_value() != 0:
                hybridShapeTranslate_wing.ElemToTranslate = reference30
            else:
                hybridShapeTranslate_wing.ElemToTranslate = reference29
            hybridShapeTranslate_wing.VectorType = 0
            hybridShapeDirection_wing = ShFactory.AddNewDirection(reference8)
            hybridShapeTranslate_wing.Direction = hybridShapeDirection_wing
            hybridShapeTranslate_wing.DistanceValue = self.get_Hlocation_value()
            hybridShapeTranslate_wing.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate_wing)
            reference32 = part1.CreateReferenceFromObject(hybridShapeTranslate_wing)
            part1.InWorkObject = hybridShapeTranslate_wing
            if self.get_setting_angle_value() != 0:
                selection1.Add(hybridShapeRotate1_wing)
            else:
                selection1.Add(hybridShapeAssemble2)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        # Vertical Location
        hybridShapeTranslate1_Hwing = ShFactory.AddNewEmptyTranslate()
        reference31 = part1.CreateReferenceFromObject(hybridShapeAssemble2)
        
        if self.get_Vlocation_value() != 0:
            if self.get_Hlocation_value() != 0:
                hybridShapeTranslate1_Hwing.ElemToTranslate = reference32
            if self.get_setting_angle_value() != 0 and self.get_Hlocation_value() == 0:
                hybridShapeTranslate1_Hwing.ElemToTranslate = reference30
            if self.get_Hlocation_value() == 0 and self.get_setting_angle_value() == 0:
                hybridShapeTranslate1_Hwing.ElemToTranslate = reference31
            
            hybridShapeTranslate1_Hwing.VectorType = 0
            hybridShapeDirection_Hwing = ShFactory.AddNewDirection(reference6)
            hybridShapeTranslate1_Hwing.Direction = hybridShapeDirection_Hwing
            hybridShapeTranslate1_Hwing.DistanceValue = self.get_Vlocation_value()
            hybridShapeTranslate1_Hwing.VolumeResult = False
            body1.AppendHybridShape(hybridShapeTranslate1_Hwing)
            if self.get_Hlocation_value() != 0:
                selection1.Add(hybridShapeTranslate_wing)
                visPropertySet1.SetShow(1)
                selection1.Clear()
            if self.get_setting_angle_value() != 0 and self.get_Hlocation_value() == 0:
                selection1.Add(hybridShapeRotate1_wing)
                visPropertySet1.SetShow(1)
                selection1.Clear()
            if self.get_Hlocation_value() == 0 and self.get_setting_angle_value() == 0:
                selection1.Add(hybridShapeAssemble2)
                visPropertySet1.SetShow(1)
                selection1.Clear()
            part1.InWorkObject = hybridShapeTranslate1_Hwing
            part1.Update()
        
        #Split Wing-Fuselage
        try:
            if self.get_Hlocation_value() != 0 and self.get_Vlocation_value() ==0:
                reference46 = part1.CreateReferenceFromObject(hybridShapeTranslate_wing)
            else:  
                reference46 = part1.CreateReferenceFromObject(hybridShapeTranslate1_Hwing)
            reference47 = part1.CreateReferenceFromObject(hybridShapeAssemble3)
            hybridShapeSplit1 = ShFactory.AddNewHybridSplit(reference46, reference47, -1)
            ShFactory.GSMVisibility(reference46, 0)
            body2.AppendHybridShape(hybridShapeSplit1)
            part1.InWorkObject = hybridShapeSplit1
            part1.Update()
        except:
          pass
    
        #TAIL
        part1.InWorkObject = body3
        #V Tail
        points_Vtail = airfoil_points(self.get_VS_airfoil_value()) 
        spline1_Vtail = ShFactory.AddNewSpline()
        spline1_Vtail.SetSplineType(0)
        spline1_Vtail.SetClosing(0)
        for i in points_Vtail[::-1]:    
            point1_Vtail = ShFactory.AddNewPointCoord(i[0],i[1],0)
            body3.AppendHybridShape(point1_Vtail)
            spline1_Vtail.AddPoint(point1_Vtail)
            selection1.Add(point1_Vtail)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        point0_Vtail = ShFactory.AddNewPointCoord(points_Vtail[-1][0], points_Vtail[-1][1],0)
        spline1_Vtail.AddPoint(point0_Vtail)
        body3.AppendHybridShape(spline1_Vtail)
        part1.InWorkObject = spline1_Vtail
        part1.Update()
        
        #Root chord V tail
        hybridBody1_Vtail = bodies1.Item("Tail")
        reference48 = part1.CreateReferenceFromObject(spline1_Vtail)
        hybridShapePlaneExplicit1_Vtail = originElements1.PlaneYZ
        reference49 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1_Vtail)
        hybridShapeScaling1_Vtail = ShFactory.AddNewHybridScaling(reference48, reference49, self.get_VS_rootchord_value()) 
        hybridShapeScaling1_Vtail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling1_Vtail)
        part1.InWorkObject = hybridShapeScaling1_Vtail
        
        reference50 = part1.CreateReferenceFromObject(hybridShapeScaling1_Vtail)
        hybridShapePlaneExplicit1 = originElements1.PlaneZX
        reference51 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
        hybridShapeScaling2_Vtail = ShFactory.AddNewHybridScaling(reference50, reference51, self.get_VS_rootchord_value()) 
        hybridShapeScaling2_Vtail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling2_Vtail)
        part1.InWorkObject = hybridShapeScaling2_Vtail
        selection1.Add(spline1_Vtail)
        selection1.Add(hybridShapeScaling1_Vtail)
        selection1.Add(hybridShapeScaling2_Vtail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        # Make tip airfoil V tail
        reference52 = part1.CreateReferenceFromObject(hybridShapeScaling2_Vtail)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit1_Vtail = originElements1.PlaneYZ
        reference54 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1_Vtail)
        hybridShapeScaling3_Vtail = ShFactory.AddNewHybridScaling(reference52, reference54, self.get_VS_tipchord_value()/self.get_VS_rootchord_value()) 
        hybridShapeScaling3_Vtail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling3_Vtail)
        part1.InWorkObject = hybridShapeScaling3_Vtail
        
        reference52 = part1.CreateReferenceFromObject(hybridShapeScaling3_Vtail)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit2 = originElements1.PlaneZX
        reference8 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit2)
        hybridShapeScaling4_Vtail = ShFactory.AddNewHybridScaling(reference52, reference8, self.get_VS_tipchord_value()/self.get_VS_rootchord_value())
        hybridShapeScaling4_Vtail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling4_Vtail)
        part1.InWorkObject = hybridShapeScaling4_Vtail
        
        selection1.Add(hybridShapeScaling3_Vtail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        # Half-span value V tail
        hybridShapePlaneExplicit3 = originElements1.PlaneXY
        reference9_V = part1.CreateReferenceFromObject(hybridShapePlaneExplicit3)
        hybridShapeDirection1 = ShFactory.AddNewDirection(reference9_V)
        hybridShapeTranslate1_Vtail = ShFactory.AddNewEmptyTranslate()
        reference53 = part1.CreateReferenceFromObject(hybridShapeScaling4_Vtail)
        hybridShapeTranslate1_Vtail.ElemToTranslate = reference53
        hybridShapeTranslate1_Vtail.VectorType = 0
        hybridShapeTranslate1_Vtail.Direction=hybridShapeDirection1
        hybridShapeTranslate1_Vtail.DistanceValue = self.get_VS_span_value() 
        hybridShapeTranslate1_Vtail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeTranslate1_Vtail)
        part1.InWorkObject = hybridShapeTranslate1_Vtail
        selection1.Add(hybridShapeScaling4_Vtail)
        selection1.Add(hybridShapeTranslate1_Vtail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        #Sweep V tail
        reference85 =  part1.CreateReferenceFromObject(hybridShapeTranslate1_Vtail)
        if self.get_VS_sweepangle_value() !=0:
            hybridShapePlaneExplicit4_VS = originElements1.PlaneYZ
            reference11_VS = part1.CreateReferenceFromObject(hybridShapePlaneExplicit4_VS)
            hybridShapeDirection1_VS = ShFactory.AddNewDirection(reference11_VS)
            hybridShapeTranslate2_VS = ShFactory.AddNewEmptyTranslate()
            hybridShapeTranslate2_VS.ElemToTranslate = reference85
            hybridShapeTranslate2_VS.VectorType = 0
            hybridShapeTranslate2_VS.Direction = hybridShapeDirection1_VS
            if self.get_VS_sweepangle_value()>0:
               hybridShapeTranslate2_VS.DistanceValue = (self.get_VS_span_value()/2*math.tan(math.radians(self.get_VS_sweepangle_value()))-(self.get_VS_tipchord_value()*0.25)+(self.get_VS_rootchord_value()*0.25)) 
            elif self.get_VS_sweepangle_value()<0:
               hybridShapeTranslate2_VS.DistanceValue = (self.get_VS_span_value()/2*math.tan(math.radians(self.get_VS_sweepangle_value()))+(self.get_VS_tipchord_value()*0.25)-(self.get_VS_rootchord_value()*0.25)) 
            hybridShapeTranslate2_VS.VolumeResult = False
            body3.AppendHybridShape(hybridShapeTranslate2_VS)
            part1.InWorkObject =hybridShapeTranslate2_VS
            selection1.Add(hybridShapeTranslate2_VS)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        # V tail Multi Section Surface Fill Join
        hybridShapeDirection2_Vtail = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        reference55 = part1.CreateReferenceFromObject(hybridShapeScaling2_Vtail)
        hybridShapeExtremum1_Vtail = ShFactory.AddNewExtremum(reference55, hybridShapeDirection2_Vtail, 1)
        body3.AppendHybridShape(hybridShapeExtremum1_Vtail)
        part1.InWorkObject = hybridShapeExtremum1_Vtail
        
        hybridShapeDirection3_Vtail = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        if self.get_VS_sweepangle_value() ==0:
            reference56 = part1.CreateReferenceFromObject(hybridShapeTranslate1_Vtail)
        elif self.get_VS_sweepangle_value() !=0:
            reference56 = part1.CreateReferenceFromObject(hybridShapeTranslate2_VS)
        
        hybridShapeExtremum2_Vtail = ShFactory.AddNewExtremum(reference56, hybridShapeDirection3_Vtail, 1)
        body3.AppendHybridShape(hybridShapeExtremum2_Vtail)
        part1.InWorkObject = hybridShapeExtremum2_Vtail
       
        hybridShapeLoft1_Vtail = ShFactory.AddNewLoft()
        hybridShapeLoft1_Vtail.SectionCoupling = 1
        hybridShapeLoft1_Vtail.Relimitation = 1
        hybridShapeLoft1_Vtail.CanonicalDetection = 2
        
        reference57 = part1.CreateReferenceFromObject(hybridShapeExtremum1_Vtail)
        hybridShapeLoft1_Vtail.AddSectionToLoft(reference55, 1, reference57)
        reference58 = part1.CreateReferenceFromObject(hybridShapeExtremum2_Vtail)
        hybridShapeLoft1_Vtail.AddSectionToLoft(reference56, 1, reference58)
        body3.AppendHybridShape(hybridShapeLoft1_Vtail)
        part1.InWorkObject = hybridShapeLoft1_Vtail
        selection1.Add(hybridShapeExtremum1_Vtail)
        selection1.Add(hybridShapeExtremum2_Vtail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        
        hybridShapeFill1_Vtail = ShFactory.AddNewFill()
        if self.get_VS_sweepangle_value() ==0: 
            hybridShapeFill1_Vtail.AddBound(hybridShapeTranslate1_Vtail) #change parameter
        elif self.get_VS_sweepangle_value() !=0:
            hybridShapeFill1_Vtail.AddBound(hybridShapeTranslate2_VS)
        hybridShapeFill1_Vtail.Continuity = 0
        body3.AppendHybridShape(hybridShapeFill1_Vtail)
        part1.InWorkObject = hybridShapeFill1_Vtail
        part1.Update()
        
        reference59 = part1.CreateReferenceFromObject(hybridShapeFill1_Vtail)
        reference60 = part1.CreateReferenceFromObject(hybridShapeLoft1_Vtail)
        hybridShapeAssemble1_Vtail = ShFactory.AddNewJoin(reference59, reference60)
        hybridShapeAssemble1_Vtail.SetConnex(1)
        hybridShapeAssemble1_Vtail.SetManifold(0)
        hybridShapeAssemble1_Vtail.SetSimplify(0)
        hybridShapeAssemble1_Vtail.SetSuppressMode(0)
        hybridShapeAssemble1_Vtail.SetDeviation(0.001000)
        hybridShapeAssemble1_Vtail.SetAngularToleranceMode(0)
        hybridShapeAssemble1_Vtail.SetAngularTolerance(0.500000)
        hybridShapeAssemble1_Vtail.SetFederationPropagation(0)
        body3.AppendHybridShape(hybridShapeAssemble1_Vtail)
        part1.InWorkObject = hybridShapeAssemble1_Vtail
        selection1.Add(hybridShapeFill1_Vtail)
        selection1.Add(hybridShapeLoft1_Vtail)
        visPropertySet1.SetShow(1)
        part1.Update()
        
        #H Tail
        points_Htail = airfoil_points(self.get_HS_airfoil_value()) 
        spline1_Htail = ShFactory.AddNewSpline()
        spline1_Htail.SetSplineType(0)
        spline1_Htail.SetClosing(0)
        for i in points_Htail[::-1]:    
            point1_Htail = ShFactory.AddNewPointCoord(i[0],0,i[1])
            body3.AppendHybridShape(point1_Htail)
            spline1_Htail.AddPoint(point1_Htail)
            selection1.Add(point1_Htail)
            visPropertySet1.SetShow(1)
            selection1.Clear()
        point0_Htail = ShFactory.AddNewPointCoord(points_Htail[-1][0],0,points_Htail[-1][1])
        spline1_Htail.AddPoint(point0_Htail)
        body3.AppendHybridShape(spline1_Htail)
        part1.InWorkObject = spline1_Htail
        part1.Update()
        
        #Root chord H tail
        hybridBody1_Htail = bodies1.Item("Tail")
        reference61 = part1.CreateReferenceFromObject(spline1_Htail)
        hybridShapePlaneExplicit1_Htail = originElements1.PlaneXY
        reference62 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1_Htail)
        hybridShapeScaling1_Htail = ShFactory.AddNewHybridScaling(reference61, reference62, self.get_HS_rootchord_value()) 
        hybridShapeScaling1_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling1_Htail)
        part1.InWorkObject = hybridShapeScaling1_Htail
        
        reference63 = part1.CreateReferenceFromObject(hybridShapeScaling1_Htail)
        hybridShapePlaneExplicit1 = originElements1.PlaneYZ
        reference64 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
        hybridShapeScaling2_Htail = ShFactory.AddNewHybridScaling(reference63, reference64, self.get_HS_rootchord_value()) 
        hybridShapeScaling2_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling2_Htail)
        part1.InWorkObject = hybridShapeScaling2_Htail
        selection1.Add(spline1_Htail)
        selection1.Add(hybridShapeScaling1_Htail)
        selection1.Add(hybridShapeScaling2_Htail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        # Make tip airfoil H tail
        reference65 = part1.CreateReferenceFromObject(hybridShapeScaling2_Htail)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit1_Htail = originElements1.PlaneXY
        reference66 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1_Htail)
        hybridShapeScaling3_Htail = ShFactory.AddNewHybridScaling(reference65, reference66, self.get_HS_tipchord_value()/self.get_HS_rootchord_value()) 
        hybridShapeScaling3_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling3_Htail)
        part1.InWorkObject = hybridShapeScaling3_Htail
        
        reference67 = part1.CreateReferenceFromObject(hybridShapeScaling3_Htail)
        originElements1= part1.OriginElements
        hybridShapePlaneExplicit2 = originElements1.PlaneYZ
        reference68 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit2)
        hybridShapeScaling4_Htail = ShFactory.AddNewHybridScaling(reference67, reference68, self.get_HS_tipchord_value()/self.get_HS_rootchord_value()) 
        hybridShapeScaling4_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeScaling4_Htail)
        part1.InWorkObject = hybridShapeScaling4_Htail
        
        selection1.Add(hybridShapeScaling3_Htail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        # Half-span value H tail
        hybridShapePlaneExplicit3 = originElements1.PlaneZX
        reference69 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit3)
        hybridShapeDirection1 = ShFactory.AddNewDirection(reference69)
        hybridShapeTranslate1_Htail = ShFactory.AddNewEmptyTranslate()
        reference70 = part1.CreateReferenceFromObject(hybridShapeScaling4_Htail)
        hybridShapeTranslate1_Htail.ElemToTranslate = reference70
        hybridShapeTranslate1_Htail.VectorType = 0
        hybridShapeTranslate1_Htail.Direction=hybridShapeDirection1
        hybridShapeTranslate1_Htail.DistanceValue = self.get_HS_span_value()/2 
        hybridShapeTranslate1_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeTranslate1_Htail)
        part1.InWorkObject = hybridShapeTranslate1_Htail
        selection1.Add(hybridShapeScaling4_Htail)
        selection1.Add(hybridShapeTranslate1_Htail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        #Sweep H tail
        reference86_H =  part1.CreateReferenceFromObject(hybridShapeTranslate1_Htail)
        if self.get_HS_sweepangle_value() !=0:
            hybridShapePlaneExplicit4_HS = originElements1.PlaneYZ
            reference11_HS = part1.CreateReferenceFromObject(hybridShapePlaneExplicit4_HS)
            hybridShapeDirection1_HS = ShFactory.AddNewDirection(reference11_HS)
            hybridShapeTranslate2_HS = ShFactory.AddNewEmptyTranslate()
            hybridShapeTranslate2_HS.ElemToTranslate = reference86_H
            hybridShapeTranslate2_HS.VectorType = 0
            hybridShapeTranslate2_HS.Direction = hybridShapeDirection1_HS
            if self.get_HS_sweepangle_value()>0:
               hybridShapeTranslate2_HS.DistanceValue = (self.get_HS_span_value()/2*math.tan(math.radians(self.get_HS_sweepangle_value()))-(self.get_HS_tipchord_value()*0.25)+(self.get_HS_rootchord_value()*0.25)) 
            elif self.get_HS_sweepangle_value()<0:
               hybridShapeTranslate2_HS.DistanceValue = (self.get_HS_span_value()/2*math.tan(math.radians(self.get_HS_sweepangle_value()))+(self.get_HS_tipchord_value()*0.25)-(self.get_HS_rootchord_value()*0.25)) 
            hybridShapeTranslate2_HS.VolumeResult = False
            body3.AppendHybridShape(hybridShapeTranslate2_HS)
            part1.InWorkObject =hybridShapeTranslate2_HS
            selection1.Add(hybridShapeTranslate2_HS)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        # H tail Multi Section Surface Fill Join
        hybridShapeDirection2_Htail = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        reference71 = part1.CreateReferenceFromObject(hybridShapeScaling2_Htail)
        hybridShapeExtremum1_Htail = ShFactory.AddNewExtremum(reference71, hybridShapeDirection2_Htail, 1)
        body3.AppendHybridShape(hybridShapeExtremum1_Htail)
        part1.InWorkObject = hybridShapeExtremum1_Htail
        
        hybridShapeDirection3_Htail = ShFactory.AddNewDirectionByCoord(1, 2, 3)
        
        if self.get_HS_sweepangle_value() ==0:
            reference72 = part1.CreateReferenceFromObject(hybridShapeTranslate1_Htail)
        elif self.get_HS_sweepangle_value() !=0:
            reference72 = part1.CreateReferenceFromObject(hybridShapeTranslate2_HS)
            
    
        hybridShapeExtremum2_Htail = ShFactory.AddNewExtremum(reference72, hybridShapeDirection3_Htail, 1)
        body3.AppendHybridShape(hybridShapeExtremum2_Htail)
        part1.InWorkObject = hybridShapeExtremum2_Htail
       
        hybridShapeLoft1_Htail = ShFactory.AddNewLoft()
        hybridShapeLoft1_Htail.SectionCoupling = 1
        hybridShapeLoft1_Htail.Relimitation = 1
        hybridShapeLoft1_Htail.CanonicalDetection = 2
        
        reference73 = part1.CreateReferenceFromObject(hybridShapeExtremum1_Htail)
        hybridShapeLoft1_Htail.AddSectionToLoft(reference71, 1, reference73)
        reference74 = part1.CreateReferenceFromObject(hybridShapeExtremum2_Htail)
        hybridShapeLoft1_Htail.AddSectionToLoft(reference72, 1, reference74)
        body3.AppendHybridShape(hybridShapeLoft1_Htail)
        part1.InWorkObject = hybridShapeLoft1_Htail
        selection1.Add(hybridShapeExtremum1_Htail)
        selection1.Add(hybridShapeExtremum2_Htail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        hybridShapeFill1_Htail = ShFactory.AddNewFill()
        if self.get_HS_sweepangle_value() ==0: 
            hybridShapeFill1_Htail.AddBound(hybridShapeTranslate1_Htail) 
        elif self.get_HS_sweepangle_value() !=0:
            hybridShapeFill1_Htail.AddBound(hybridShapeTranslate2_HS)
       
        hybridShapeFill1_Htail.Continuity = 0
        body3.AppendHybridShape(hybridShapeFill1_Htail)
        part1.InWorkObject = hybridShapeFill1_Htail
        part1.Update()
        
        reference75 = part1.CreateReferenceFromObject(hybridShapeFill1_Htail)
        reference76 = part1.CreateReferenceFromObject(hybridShapeLoft1_Htail)
        hybridShapeAssemble1_Htail = ShFactory.AddNewJoin(reference75, reference76)
        hybridShapeAssemble1_Htail.SetConnex(1)
        hybridShapeAssemble1_Htail.SetManifold(0)
        hybridShapeAssemble1_Htail.SetSimplify(0)
        hybridShapeAssemble1_Htail.SetSuppressMode(0)
        hybridShapeAssemble1_Htail.SetDeviation(0.001000)
        hybridShapeAssemble1_Htail.SetAngularToleranceMode(0)
        hybridShapeAssemble1_Htail.SetAngularTolerance(0.500000)
        hybridShapeAssemble1_Htail.SetFederationPropagation(0)
        body3.AppendHybridShape(hybridShapeAssemble1_Htail)
        part1.InWorkObject = hybridShapeAssemble1_Htail
        selection1.Add(hybridShapeFill1_Htail)
        selection1.Add(hybridShapeLoft1_Htail)
        visPropertySet1.SetShow(1)
        part1.Update()
        #Symetry
        reference77 = part1.CreateReferenceFromObject(hybridShapeAssemble1_Htail)
        hybridShapeSymmetry1_Htail = ShFactory.AddNewSymmetry(reference77, reference9)
        hybridShapeSymmetry1_Htail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeSymmetry1_Htail)
        part1.InWorkObject = hybridShapeSymmetry1_Htail
        part1.Update() 
        reference78 = part1.CreateReferenceFromObject(hybridShapeAssemble1_Htail)
        reference79 = part1.CreateReferenceFromObject(hybridShapeSymmetry1_Htail)
        hybridShapeAssemble2_Htail = ShFactory.AddNewJoin(reference78, reference79)
        hybridShapeAssemble2_Htail.SetConnex(1)
        hybridShapeAssemble2_Htail.SetManifold(0)
        hybridShapeAssemble2_Htail.SetSimplify(0)
        hybridShapeAssemble2_Htail.SetSuppressMode(0)
        hybridShapeAssemble2_Htail.SetDeviation(0.001000)
        hybridShapeAssemble2_Htail.SetAngularToleranceMode(0)
        hybridShapeAssemble2_Htail.SetAngularTolerance(0.500000)
        hybridShapeAssemble2_Htail.SetFederationPropagation(0)
        body3.AppendHybridShape(hybridShapeAssemble2_Htail)
        selection1.Add(hybridShapeAssemble1_Htail)
        selection1.Add(hybridShapeSymmetry1_Htail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        #Trim Tail
        reference83_t = part1.CreateReferenceFromObject(hybridShapeAssemble2_Htail)
        reference84_t = part1.CreateReferenceFromObject(hybridShapeAssemble1_Vtail)
        hybridShapeSplit1_tail1 = ShFactory.AddNewHybridSplit(reference84_t, reference83_t, 1)
        ShFactory.GSMVisibility(reference83_t, 0)
        body3.AppendHybridShape(hybridShapeSplit1_tail1)
        part1.InWorkObject = hybridShapeSplit1_tail1
        part1.Update()
        # Join Tail
        reference80 = part1.CreateReferenceFromObject(hybridShapeAssemble2_Htail)
        reference81 = part1.CreateReferenceFromObject(hybridShapeSplit1_tail1)
        hybridShapeAssemble_tail = ShFactory.AddNewJoin(reference80, reference81)
        hybridShapeAssemble_tail.SetConnex(0)
        hybridShapeAssemble_tail.SetManifold(0)
        hybridShapeAssemble_tail.SetSimplify(0)
        hybridShapeAssemble_tail.SetSuppressMode(0)
        hybridShapeAssemble_tail.SetDeviation(0.001000)
        hybridShapeAssemble_tail.SetAngularToleranceMode(0)
        hybridShapeAssemble_tail.SetAngularTolerance(0.500000)
        hybridShapeAssemble_tail.SetFederationPropagation(0)
        body3.AppendHybridShape(hybridShapeAssemble_tail)
        selection1.Add(hybridShapeAssemble2_Htail)
        selection1.Add(hybridShapeSplit1_tail1)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        
        #Horizontal Locaiton Tail
        hybridShapeTranslate_tail = ShFactory.AddNewEmptyTranslate()
        reference82 = part1.CreateReferenceFromObject(hybridShapeAssemble_tail)
        hybridShapeTranslate_tail.ElemToTranslate = reference82
        hybridShapeTranslate_tail.VectorType = 0
        hybridShapeDirection_tail = ShFactory.AddNewDirection(reference33)
        hybridShapeTranslate_tail.Direction = hybridShapeDirection_tail
        hybridShapeTranslate_tail.DistanceValue = self.get_horizontal_location_tail()
        hybridShapeTranslate_tail.VolumeResult = False
        body3.AppendHybridShape(hybridShapeTranslate_tail)
        reference32 = part1.CreateReferenceFromObject(hybridShapeTranslate_tail)
        part1.InWorkObject = hybridShapeTranslate_tail
        selection1.Add(hybridShapeAssemble_tail)
        selection1.Add(hybridShapeAssemble1_Vtail)
        visPropertySet1.SetShow(1)
        selection1.Clear()
        part1.Update()
        
        if self.ui2.doubleSpinBox_angle.value() != 0 or self.ui3.doubleSpinBox_angle.value() != 0 or self.ui4.doubleSpinBox_angle.value() != 0 or self.ui5.doubleSpinBox_angle.value() != 0:
            hybridShapeTranslate_tail_c = ShFactory.AddNewEmptyTranslate()
            reference82_c = part1.CreateReferenceFromObject(hybridShapeTranslate_tail)
            hybridShapeTranslate_tail_c.ElemToTranslate = reference82_c
            hybridShapeTranslate_tail_c.VectorType = 0
            hybridShapeDirection_tail_c = ShFactory.AddNewDirection(reference2)
            hybridShapeTranslate_tail_c.Direction = hybridShapeDirection_tail_c
            if self.ui2.doubleSpinBox_angle.value() != 0:
                hybridShapeTranslate_tail_c.DistanceValue = math.tan(math.radians(self.ui2.get_angle2()))*self.ui2.get_length_value2()+self.ui2.get_diameter_2_2()/2-(self.ui2.get_diameter_1_2()/2)
            elif self.ui3.doubleSpinBox_angle.value() != 0:
                hybridShapeTranslate_tail_c.DistanceValue = math.tan(math.radians(self.ui3.get_angle3()))*self.ui3.get_length_value3()+self.ui3.get_diameter_2_3()/2-(self.ui3.get_diameter_1_3()/2)
            elif self.ui4.doubleSpinBox_angle.value() != 0:
                hybridShapeTranslate_tail_c.DistanceValue = math.tan(math.radians(self.ui4.get_angle4()))*self.ui4.get_length_value4()+self.ui4.get_diameter_2_4()/2-(self.ui4.get_diameter_1_4()/2)
            elif self.ui5.doubleSpinBox_angle.value() != 0:
                hybridShapeTranslate_tail_c.DistanceValue = math.tan(math.radians(self.ui5.get_angle5()))*self.ui5.get_length_value5()+self.ui5.get_diameter_2_5()/2-(self.ui5.get_diameter_1_5()/2)
            
            hybridShapeTranslate_tail_c.VolumeResult = False
            body3.AppendHybridShape(hybridShapeTranslate_tail_c)
            
            selection1.Add(hybridShapeTranslate_tail)
            visPropertySet1.SetShow(1)
            selection1.Clear()
            part1.Update()
        #Split Tail-Fuselage
        try:
            reference83 = part1.CreateReferenceFromObject(hybridShapeTranslate_tail)
            reference84 = part1.CreateReferenceFromObject(hybridShapeAssemble3)
            reference100 = part1.CreateReferenceFromObject(hybridShapeTranslate_tail_c)
            if self.ui2.doubleSpinBox_angle.value() != 0 or self.ui3.doubleSpinBox_angle.value() != 0 or self.ui4.doubleSpinBox_angle.value() != 0 or self.ui5.doubleSpinBox_angle.value() != 0:
                 hybridShapeSplit1_tail = ShFactory.AddNewHybridSplit(reference100, reference84, -1)
                 ShFactory.GSMVisibility(reference100, 0)    
            else:
                hybridShapeSplit1_tail = ShFactory.AddNewHybridSplit(reference83, reference84, -1)
                ShFactory.GSMVisibility(reference83, 0)
                
            body3.AppendHybridShape(hybridShapeSplit1_tail)
            part1.InWorkObject = hybridShapeSplit1_tail
            part1.Update()
        except:
          pass
        
    ########################################################################################
    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 370)
        MainWindow.setMinimumSize(QtCore.QSize(840, 370))
        MainWindow.setMaximumSize(QtCore.QSize(840, 380))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setWindowIcon(QtGui.QIcon("airplane_logo.jpg"))
        
        self.window1 = QtWidgets.QDialog()
        self.ui1 = Ui_Dialog1()
        self.ui1.setupUi(self.window1)
        
        self.window2 = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog2()
        self.ui2.setupUi(self.window2)
        
        self.window3 = QtWidgets.QDialog()
        self.ui3 = Ui_Dialog3()
        self.ui3.setupUi(self.window3)
        
        self.window4 = QtWidgets.QDialog()
        self.ui4 = Ui_Dialog4()
        self.ui4.setupUi(self.window4)
        
        self.window5 = QtWidgets.QDialog()
        self.ui5 = Ui_Dialog5()
        self.ui5.setupUi(self.window5)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 811, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.fuselage = QtWidgets.QWidget()
        self.fuselage.setObjectName("fuselage")
        # self.active_fuselage = QtWidgets.QCheckBox(self.fuselage)
        # self.active_fuselage.setGeometry(QtCore.QRect(0, 10, 70, 17))
        # self.active_fuselage.setChecked(True)
        # self.active_fuselage.setObjectName("active_fuselage")
        self.slot1 = QtWidgets.QPushButton(self.fuselage)
        self.slot1.setEnabled(True)
        self.slot1.setGeometry(QtCore.QRect(540, 60, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.slot1.setFont(font)
        self.slot1.setAutoFillBackground(False)
        self.slot1.setStyleSheet("border-image: url(:/slot/square frame.png);")
        self.slot1.setAutoDefault(False)
        self.slot1.setDefault(False)
        self.slot1.setFlat(False)
        self.slot1.setObjectName("slot1")
        self.slot2 = QtWidgets.QPushButton(self.fuselage)
        self.slot2.setEnabled(True)
        self.slot2.setGeometry(QtCore.QRect(460, 60, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.slot2.setFont(font)
        self.slot2.setAutoFillBackground(False)
        self.slot2.setStyleSheet("border-image: url(:/slot/square frame.png);")
        self.slot2.setAutoDefault(False)
        self.slot2.setDefault(False)
        self.slot2.setFlat(True)
        self.slot2.setObjectName("slot2")
        self.slot3 = QtWidgets.QPushButton(self.fuselage)
        self.slot3.setEnabled(True)
        self.slot3.setGeometry(QtCore.QRect(380, 60, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.slot3.setFont(font)
        self.slot3.setAutoFillBackground(False)
        self.slot3.setStyleSheet("border-image: url(:/newPrefix/square frame.png);\n"
"border-image: url(:/slot/square frame.png);")
        self.slot3.setAutoDefault(False)
        self.slot3.setDefault(False)
        self.slot3.setFlat(True)
        self.slot3.setObjectName("slot3")
        self.slot4 = QtWidgets.QPushButton(self.fuselage)
        self.slot4.setEnabled(True)
        self.slot4.setGeometry(QtCore.QRect(300, 60, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.slot4.setFont(font)
        self.slot4.setAutoFillBackground(False)
        self.slot4.setStyleSheet("border-image: url(:/slot/square frame.png);")
        self.slot4.setAutoDefault(False)
        self.slot4.setDefault(False)
        self.slot4.setFlat(True)
        self.slot4.setObjectName("slot4")
        self.slot5 = QtWidgets.QPushButton(self.fuselage)
        self.slot5.setEnabled(True)
        self.slot5.setGeometry(QtCore.QRect(220, 60, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.slot5.setFont(font)
        self.slot5.setAutoFillBackground(False)
        self.slot5.setStyleSheet("border-image: url(:/slot/square frame.png);")
        self.slot5.setAutoDefault(False)
        self.slot5.setDefault(False)
        self.slot5.setFlat(True)
        self.slot5.setObjectName("slot5")
        self.update_fuselage = QtWidgets.QPushButton(self.fuselage)
        self.update_fuselage.setGeometry(QtCore.QRect(730, 220, 71, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/lightning/png-clipart-emoji-pop-lightning-sticker-thunder-icon-emoji-angle-cloud-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_fuselage.setIcon(icon)
        self.update_fuselage.setObjectName("update_fuselage")
        self.fineness_ratio = QtWidgets.QLabel(self.fuselage)
        self.fineness_ratio.setGeometry(QtCore.QRect(420, 150, 121, 20))
        self.fineness_ratio.setObjectName("fineness_ratio")
        self.max_diameter = QtWidgets.QLabel(self.fuselage)
        self.max_diameter.setGeometry(QtCore.QRect(420, 180, 111, 20))
        self.max_diameter.setObjectName("max_diameter")
        self.surface_area_fuselage = QtWidgets.QLabel(self.fuselage)
        self.surface_area_fuselage.setGeometry(QtCore.QRect(220, 210, 91, 20))
        self.surface_area_fuselage.setObjectName("surface_area_fuselage")
        self.length = QtWidgets.QLabel(self.fuselage)
        self.length.setGeometry(QtCore.QRect(220, 150, 91, 20))
        self.length.setObjectName("length")
        self.volume_fuselage = QtWidgets.QLabel(self.fuselage)
        self.volume_fuselage.setGeometry(QtCore.QRect(220, 180, 91, 20))
        self.volume_fuselage.setObjectName("volume_fuselage")
        self.length_2 = QtWidgets.QLineEdit(self.fuselage)
        self.length_2.setGeometry(QtCore.QRect(320, 150, 81, 20))
        self.length_2.setReadOnly(True)
        self.length_2.setObjectName("length_2")
        self.volume_fuselage_2 = QtWidgets.QLineEdit(self.fuselage)
        self.volume_fuselage_2.setGeometry(QtCore.QRect(320, 180, 81, 20))
        self.volume_fuselage_2.setReadOnly(True)
        self.volume_fuselage_2.setObjectName("volume_fuselage_2")
        self.max_diameter_2 = QtWidgets.QLineEdit(self.fuselage)
        self.max_diameter_2.setGeometry(QtCore.QRect(520, 180, 81, 20))
        self.max_diameter_2.setReadOnly(True)
        self.max_diameter_2.setObjectName("max_diameter_2")
        self.fineness_ratio_2 = QtWidgets.QLineEdit(self.fuselage)
        self.fineness_ratio_2.setGeometry(QtCore.QRect(520, 150, 81, 20))
        self.fineness_ratio_2.setReadOnly(True)
        self.fineness_ratio_2.setObjectName("fineness_ratio_2")
        self.surface_area_fuselage_2 = QtWidgets.QLineEdit(self.fuselage)
        self.surface_area_fuselage_2.setGeometry(QtCore.QRect(320, 210, 81, 20))
        self.surface_area_fuselage_2.setReadOnly(True)
        self.surface_area_fuselage_2.setObjectName("surface_area_fuselage_2")
        self.tabWidget.addTab(self.fuselage, "")
        self.wing = QtWidgets.QWidget()
        self.wing.setObjectName("wing")
        # self.active_wing = QtWidgets.QCheckBox(self.wing)
        # self.active_wing.setGeometry(QtCore.QRect(0, 10, 70, 17))
        # self.active_wing.setChecked(True)
        # self.active_wing.setObjectName("active_wing")
        self.wing_span_2 = QtWidgets.QLabel(self.wing)
        self.wing_span_2.setGeometry(QtCore.QRect(80, 60, 111, 16))
        self.wing_span_2.setObjectName("wing_span_2")
        self.root_chord_2 = QtWidgets.QLabel(self.wing)
        self.root_chord_2.setGeometry(QtCore.QRect(80, 90, 111, 16))
        self.root_chord_2.setObjectName("root_chord_2")
        self.tip_chord_2 = QtWidgets.QLabel(self.wing)
        self.tip_chord_2.setGeometry(QtCore.QRect(80, 120, 101, 16))
        self.tip_chord_2.setObjectName("tip_chord_2")
        self.setting_angle_2 = QtWidgets.QLabel(self.wing)
        self.setting_angle_2.setGeometry(QtCore.QRect(80, 150, 111, 16))
        self.setting_angle_2.setObjectName("setting_angle_2")
        self.root_twist_angle_2 = QtWidgets.QLabel(self.wing)
        self.root_twist_angle_2.setGeometry(QtCore.QRect(330, 60, 121, 16))
        self.root_twist_angle_2.setObjectName("root_twist_angle_2")
        self.tip_twist_angle_2 = QtWidgets.QLabel(self.wing)
        self.tip_twist_angle_2.setGeometry(QtCore.QRect(330, 90, 121, 16))
        self.tip_twist_angle_2.setObjectName("tip_twist_angle_2")
        self.sweep_angle_2 = QtWidgets.QLabel(self.wing)
        self.sweep_angle_2.setGeometry(QtCore.QRect(330, 120, 131, 16))
        self.sweep_angle_2.setObjectName("sweep_angle_2")
        self.dihedral_angle_2 = QtWidgets.QLabel(self.wing)
        self.dihedral_angle_2.setGeometry(QtCore.QRect(330, 150, 131, 16))
        self.dihedral_angle_2.setObjectName("dihedral_angle_2")
        self.wing_span = QtWidgets.QDoubleSpinBox(self.wing)
        self.wing_span.setGeometry(QtCore.QRect(190, 60, 101, 22))
        self.wing_span.setDecimals(8)
        self.wing_span.setMaximum(9999999.0)
        self.wing_span.setObjectName("wing_span")
        self.root_chord = QtWidgets.QDoubleSpinBox(self.wing)
        self.root_chord.setGeometry(QtCore.QRect(190, 90, 101, 22))
        self.root_chord.setDecimals(8)
        self.root_chord.setMaximum(9999999.0)
        self.root_chord.setObjectName("root_chord")
        self.tip_chord = QtWidgets.QDoubleSpinBox(self.wing)
        self.tip_chord.setGeometry(QtCore.QRect(190, 120, 101, 22))
        self.tip_chord.setDecimals(8)
        self.tip_chord.setMaximum(9999999.0)
        self.tip_chord.setObjectName("tip_chord")
        self.setting_angle = QtWidgets.QDoubleSpinBox(self.wing)
        self.setting_angle.setGeometry(QtCore.QRect(190, 150, 101, 22))
        self.setting_angle.setMaximum(360)
        self.setting_angle.setMinimum(-360)
        self.setting_angle.setObjectName("setting_angle")
        self.root_twist_angle = QtWidgets.QDoubleSpinBox(self.wing)
        self.root_twist_angle.setGeometry(QtCore.QRect(460, 60, 101, 22))
        self.root_twist_angle.setMaximum(15)
        self.root_twist_angle.setMinimum(-15)
        self.root_twist_angle.setObjectName("root_twist_angle")
        self.tip_twist_angle = QtWidgets.QDoubleSpinBox(self.wing)
        self.tip_twist_angle.setGeometry(QtCore.QRect(460, 90, 101, 22))
        self.tip_twist_angle.setMaximum(15)
        self.tip_twist_angle.setMinimum(-15)
        self.tip_twist_angle.setObjectName("tip_twist_angle")
        self.sweep_angle = QtWidgets.QDoubleSpinBox(self.wing)
        self.sweep_angle.setGeometry(QtCore.QRect(460, 120, 101, 22))
        self.sweep_angle.setMaximum(360)
        self.sweep_angle.setMinimum(-360)
        self.sweep_angle.setObjectName("sweep_angle")
        self.dihedral_angle = QtWidgets.QDoubleSpinBox(self.wing)
        self.dihedral_angle.setGeometry(QtCore.QRect(460, 150, 101, 22))
        self.dihedral_angle.setMaximum(360)
        self.dihedral_angle.setMinimum(-360)
        self.dihedral_angle.setObjectName("dihedral_angle")
        self.airfoil = QtWidgets.QComboBox(self.wing)
        self.airfoil.setGeometry(QtCore.QRect(80, 20, 210, 22))
        self.airfoil.setMinimumSize(QtCore.QSize(210, 22))
        self.airfoil.setMaximumSize(QtCore.QSize(210, 22))
        self.airfoil.setObjectName("airfoil")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
        self.airfoil.addItem("")
      
        self.vertical_location = QtWidgets.QLabel(self.wing)
        self.vertical_location.setGeometry(QtCore.QRect(590, 70, 121, 16))
        self.vertical_location.setObjectName("vertical_location")
        self.horizontal_location_2 = QtWidgets.QLabel(self.wing)
        self.horizontal_location_2.setGeometry(QtCore.QRect(590, 120, 101, 61))
        self.horizontal_location_2.setWordWrap(True)
        self.horizontal_location_2.setObjectName("horizontal_location_2")
        self.wing_location = QtWidgets.QDoubleSpinBox(self.wing)
        self.wing_location.setGeometry(QtCore.QRect(690, 70, 101, 22))
        self.wing_location.setObjectName("wing_location")
        self.wing_location.setDecimals(8)
        self.wing_location.setMaximum(9999999.0)
        self.wing_location.setMinimum(-999999.0)
        self.horizontal_location = QtWidgets.QDoubleSpinBox(self.wing)
        self.horizontal_location.setGeometry(QtCore.QRect(690, 140, 101, 22))
        self.horizontal_location.setDecimals(8)
        self.horizontal_location.setMaximum(999999999.0)
        self.horizontal_location.setObjectName("horizontal_location")
        self.tabWidget.addTab(self.wing, "")
        self.tail = QtWidgets.QWidget()
        self.tail.setObjectName("tail")
        self.VSairfoil = QtWidgets.QComboBox(self.tail)
        self.VSairfoil.setGeometry(QtCore.QRect(40, 20, 210, 22))
        self.VSairfoil.setMinimumSize(QtCore.QSize(210, 22))
        self.VSairfoil.setMaximumSize(QtCore.QSize(210, 22))
        self.VSairfoil.setObjectName("VSairfoil")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VSairfoil.addItem("")
        self.VS_tailspan = QtWidgets.QLabel(self.tail)
        self.VS_tailspan.setGeometry(QtCore.QRect(40, 60, 111, 16))
        self.VS_tailspan.setObjectName("VS_tailspan")
        self.VS_rootchord = QtWidgets.QLabel(self.tail)
        self.VS_rootchord.setGeometry(QtCore.QRect(40, 90, 111, 16))
        self.VS_rootchord.setObjectName("VS_rootchord")
        self.VS_tailspan_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.VS_tailspan_2.setGeometry(QtCore.QRect(150, 60, 101, 22))
        self.VS_tailspan_2.setDecimals(8)
        self.VS_tailspan_2.setMaximum(9999999.0)
        self.VS_tailspan_2.setObjectName("VS_tailspan_2")
        self.VS_rootchord_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.VS_rootchord_2.setGeometry(QtCore.QRect(150, 90, 101, 22))
        self.VS_rootchord_2.setDecimals(8)
        self.VS_rootchord_2.setMaximum(9999999.0)
        self.VS_rootchord_2.setObjectName("VS_rootchord_2")
        self.VS_tipchord_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.VS_tipchord_2.setGeometry(QtCore.QRect(150, 120, 101, 22))
        self.VS_tipchord_2.setDecimals(8)
        self.VS_tipchord_2.setMaximum(9999999.0)
        self.VS_tipchord_2.setObjectName("VS_tipchord_2")
        self.VS_sweepangle = QtWidgets.QLabel(self.tail)
        self.VS_sweepangle.setGeometry(QtCore.QRect(40, 150, 101, 16))
        self.VS_sweepangle.setObjectName("VS_sweepangle")
        self.VS_sweepangle_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.VS_sweepangle_2.setGeometry(QtCore.QRect(150, 150, 101, 22))
        self.VS_sweepangle_2.setDecimals(8)
        self.VS_sweepangle_2.setMaximum(9999999.0)
        self.VS_sweepangle_2.setMinimum(-9999999.0)
        self.VS_sweepangle_2.setObjectName("VS_sweepangle_2")
        
        self.horizontal_location_4 = QtWidgets.QLabel(self.tail)
        self.horizontal_location_4.setGeometry(QtCore.QRect(530, 60, 101, 61))
        self.horizontal_location_4.setWordWrap(True)
        self.horizontal_location_4.setObjectName("horizontal_location_4")
        self.VS_tipchord = QtWidgets.QLabel(self.tail)
        self.VS_tipchord.setGeometry(QtCore.QRect(40, 120, 101, 16))
        self.VS_tipchord.setObjectName("VS_tipchord")
        self.vertical_location_2 = QtWidgets.QLabel(self.tail)
        self.vertical_location_2.setGeometry(QtCore.QRect(530, 130, 121, 16))
        self.vertical_location_2.setObjectName("vertical_location_2")
        
        self.HS_airfoil = QtWidgets.QComboBox(self.tail)
        self.HS_airfoil.setGeometry(QtCore.QRect(270, 20, 210, 22))
        self.HS_airfoil.setMinimumSize(QtCore.QSize(210, 22))
        self.HS_airfoil.setMaximumSize(QtCore.QSize(210, 22))
        self.HS_airfoil.setObjectName("HS_airfoil")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_airfoil.addItem("")
        self.HS_tailspan = QtWidgets.QLabel(self.tail)
        self.HS_tailspan.setGeometry(QtCore.QRect(270, 60, 111, 16))
        self.HS_tailspan.setObjectName("HS_tailspan")
        self.HS_tailspan_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.HS_tailspan_2.setGeometry(QtCore.QRect(380, 60, 101, 22))
        self.HS_tailspan_2.setDecimals(8)
        self.HS_tailspan_2.setMaximum(9999999.0)
        self.HS_tailspan_2.setObjectName("HS_tailspan_2")
        self.HS_rootchord = QtWidgets.QLabel(self.tail)
        self.HS_rootchord.setGeometry(QtCore.QRect(270, 90, 111, 16))
        self.HS_rootchord.setObjectName("HS_rootchord")
        self.HS_tipchord = QtWidgets.QLabel(self.tail)
        self.HS_tipchord.setGeometry(QtCore.QRect(270, 120, 101, 16))
        self.HS_tipchord.setObjectName("HS_tipchord")
        self.HS_rootchord_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.HS_rootchord_2.setGeometry(QtCore.QRect(380, 90, 101, 22))
        self.HS_rootchord_2.setDecimals(8)
        self.HS_rootchord_2.setMaximum(9999999.0)
        self.HS_rootchord_2.setObjectName("HS_rootchord_2")
        self.HS_tipchord_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.HS_tipchord_2.setGeometry(QtCore.QRect(380, 120, 101, 22))
        self.HS_tipchord_2.setDecimals(8)
        self.HS_tipchord_2.setMaximum(9999999.0)
        self.HS_tipchord_2.setObjectName("HS_tipchord_2")
        self.horizontal_location_3 = QtWidgets.QDoubleSpinBox(self.tail)
        self.horizontal_location_3.setGeometry(QtCore.QRect(650, 80, 101, 22))
        self.horizontal_location_3.setDecimals(8)
        self.horizontal_location_3.setMaximum(999999999.0)
        self.horizontal_location_3.setObjectName("horizontal_location_3")
        self.HS_sweepangle = QtWidgets.QLabel(self.tail)
        self.HS_sweepangle.setGeometry(QtCore.QRect(270, 150, 101, 16))
        self.HS_sweepangle.setObjectName("HS_sweepangle")
        self.HS_sweepangle_2 = QtWidgets.QDoubleSpinBox(self.tail)
        self.HS_sweepangle_2.setGeometry(QtCore.QRect(380, 150, 101, 22))
        self.HS_sweepangle_2.setDecimals(8)
        self.HS_sweepangle_2.setMaximum(9999999.0)
        self.HS_sweepangle_2.setMinimum(-9999999.0)
        self.HS_sweepangle_2.setObjectName("HS_sweepangle_2")
        self.tabWidget.addTab(self.tail, "")
        self.export_to_catia = QtWidgets.QPushButton(self.centralwidget)
        self.export_to_catia.setGeometry(QtCore.QRect(350, 290, 151, 31))
        self.export_to_catia.setObjectName("export_to_catia")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionLoad)
        self.menubar.addAction(self.menuHelp.menuAction())
        
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # counter variables
        # self.submit_counter_1 = 0
        # self.submit_counter_2 = 0
        # self.submit_counter_3 = 0
        # self.submit_counter_4 = 0
        # self.submit_counter_5 = 0
        #connections
        # self.active_fuselage.stateChanged.connect(self.activeness_fuselage)
        # self.active_wing.stateChanged.connect(self.activeness_wing)
        self.slot1.clicked.connect(self.open_window_slot1)
        self.slot2.clicked.connect(self.open_window_slot2)
        self.slot3.clicked.connect(self.open_window_slot3)
        self.slot4.clicked.connect(self.open_window_slot4)
        self.slot5.clicked.connect(self.open_window_slot5)
        self.update_fuselage.clicked.connect(self.fuselage_properties)
    
        self.wing_span.valueChanged.connect(self.get_wing_span_value)
        self.root_chord.valueChanged.connect(self.get_root_chord_value)
        self.tip_chord.valueChanged.connect(self.get_tip_chord_value)
        self.setting_angle.valueChanged.connect(self.get_setting_angle_value)
        self.root_twist_angle.valueChanged.connect(self.get_root_twist_angle_value)
        self.tip_twist_angle.valueChanged.connect(self.get_tip_twist_angle_value)
        self.sweep_angle.valueChanged.connect(self.get_sweep_angle_value)
        self.dihedral_angle.valueChanged.connect(self.get_dihedral_angle_value)
        self.horizontal_location.valueChanged.connect(self.get_Hlocation_value)
        self.wing_location.valueChanged.connect(self.get_Vlocation_value)
        self.airfoil.activated.connect(self.get_airfoil_value)
        
        
        self.VSairfoil.activated.connect(self.get_VS_airfoil_value)
        self.VS_tailspan_2.valueChanged.connect(self.get_VS_span_value)
        self.VS_rootchord_2.valueChanged.connect(self.get_VS_rootchord_value)
        self.VS_tipchord_2.valueChanged.connect(self.get_VS_tipchord_value)
        self.VS_sweepangle_2.valueChanged.connect(self.get_VS_sweepangle_value)
        
        self.HS_airfoil.activated.connect(self.get_HS_airfoil_value)
        self.HS_tailspan_2.valueChanged.connect(self.get_HS_span_value)
        self.HS_rootchord_2.valueChanged.connect(self.get_HS_rootchord_value)
        self.HS_tipchord_2.valueChanged.connect(self.get_HS_tipchord_value)
        self.HS_sweepangle_2.valueChanged.connect(self.get_HS_sweepangle_value)
        
        self.horizontal_location_3.valueChanged.connect(self.get_horizontal_location_tail)
        self.export_to_catia.clicked.connect(self.CATIA)
       
        self.actionSave.triggered.connect(self.openSaveDialog)
        self.actionLoad.triggered.connect(self.openLoadDialog)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AVD"))
        # self.active_fuselage.setText(_translate("MainWindow", "Active"))
        self.slot1.setText(_translate("MainWindow", "Slot 1"))
        self.slot2.setText(_translate("MainWindow", "Slot 2"))
        self.slot3.setText(_translate("MainWindow", "Slot 3"))
        self.slot4.setText(_translate("MainWindow", "Slot 4"))
        self.slot5.setText(_translate("MainWindow", "Slot 5"))
        self.fineness_ratio.setText(_translate("MainWindow", "Fineness Ratio:"))
        self.max_diameter.setText(_translate("MainWindow", "Max. Diameter:"))
        self.surface_area_fuselage.setText(_translate("MainWindow", "Surface Area :"))
        self.length.setText(_translate("MainWindow", "Length:"))
        self.volume_fuselage.setText(_translate("MainWindow", "Volume:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fuselage), _translate("MainWindow", "Fuselage"))
        # self.active_wing.setText(_translate("MainWindow", "Active"))
        self.wing_span_2.setText(_translate("MainWindow", "Wing Span:"))
        self.root_chord_2.setText(_translate("MainWindow", "Root Chord:"))
        self.tip_chord_2.setText(_translate("MainWindow", "Tip Chord:"))
        self.setting_angle_2.setText(_translate("MainWindow", "Setting Angle (deg.):"))
        self.root_twist_angle_2.setText(_translate("MainWindow", "Root Twist Angle (deg.):"))
        self.tip_twist_angle_2.setText(_translate("MainWindow", "Tip Twist Angle (deg.):"))
        self.sweep_angle_2.setText(_translate("MainWindow", "Sweep Angle (deg.):"))
        self.dihedral_angle_2.setText(_translate("MainWindow", "Dihedral Angle (deg.):"))
        self.airfoil.setCurrentText(_translate("MainWindow", "Select Airfoil..."))
        self.airfoil.setItemText(0, _translate("MainWindow", "Select Airfoil..."))
        self.airfoil.setItemText(1, _translate("MainWindow", "naca1408-il"))
        self.airfoil.setItemText(2, _translate("MainWindow", "naca1410-il"))
        self.airfoil.setItemText(3, _translate("MainWindow", "naca1412-il"))
        self.airfoil.setItemText(4, _translate("MainWindow", "naca2408-il"))
        self.airfoil.setItemText(5, _translate("MainWindow", "naca2410-il"))
        self.airfoil.setItemText(6, _translate("MainWindow", "naca2412-il"))
        self.airfoil.setItemText(7, _translate("MainWindow", "naca2415-il"))
        self.airfoil.setItemText(8, _translate("MainWindow", "naca2418-il"))
        self.airfoil.setItemText(9, _translate("MainWindow", "naca2421-il"))
        self.airfoil.setItemText(10, _translate("MainWindow", "naca2424-il"))
        self.airfoil.setItemText(11, _translate("MainWindow", "naca4412-il"))
        self.airfoil.setItemText(12, _translate("MainWindow", "naca4415-il"))
        self.airfoil.setItemText(13, _translate("MainWindow", "naca4418-il"))
        self.airfoil.setItemText(14, _translate("MainWindow", "naca4421-il"))
        self.airfoil.setItemText(15, _translate("MainWindow", "naca4424-il"))
        self.airfoil.setItemText(16, _translate("MainWindow", "naca23018-il"))
        self.airfoil.setItemText(17, _translate("MainWindow", "naca23021-il"))
        self.airfoil.setItemText(18, _translate("MainWindow", "naca23024-il"))
        self.airfoil.setItemText(19, _translate("MainWindow", "naca63206-il"))
        self.airfoil.setItemText(20, _translate("MainWindow", "naca63209-il"))
        self.airfoil.setItemText(21, _translate("MainWindow", "naca632615-il"))
        self.airfoil.setItemText(22, _translate("MainWindow", "naca632a015-il"))
        self.airfoil.setItemText(23, _translate("MainWindow", "naca633018-il"))
        self.airfoil.setItemText(24, _translate("MainWindow", "naca633218-il"))
        self.airfoil.setItemText(25, _translate("MainWindow", "naca643418-il"))
        self.airfoil.setItemText(26, _translate("MainWindow", "naca643618-il"))
        self.airfoil.setItemText(27, _translate("MainWindow", "naca644221-il"))
        self.airfoil.setItemText(28, _translate("MainWindow", "naca644421-il"))
        self.airfoil.setItemText(29, _translate("MainWindow", "naca64a210-il"))
        self.airfoil.setItemText(30, _translate("MainWindow", "naca64a410-il"))
        self.airfoil.setItemText(31, _translate("MainWindow", "naca651212-il"))
        self.airfoil.setItemText(32, _translate("MainWindow", "naca651212a06-il"))
        self.airfoil.setItemText(33, _translate("MainWindow", "naca651412-il"))
        self.airfoil.setItemText(34, _translate("MainWindow", "naca65206-il"))
        self.airfoil.setItemText(35, _translate("MainWindow", "naca65209-il"))
        self.airfoil.setItemText(36, _translate("MainWindow", "naca65210-il"))
        self.airfoil.setItemText(37, _translate("MainWindow", "naca652215-il"))
        self.airfoil.setItemText(38, _translate("MainWindow", "naca652415-il"))
        self.airfoil.setItemText(39, _translate("MainWindow", "naca652415a05-il"))
        self.airfoil.setItemText(40, _translate("MainWindow", "naca653218-il"))
        self.airfoil.setItemText(41, _translate("MainWindow", "naca65410-il"))
        self.airfoil.setItemText(42, _translate("MainWindow", "naca654221-il"))
        self.airfoil.setItemText(43, _translate("MainWindow", "naca654421-il"))
        self.airfoil.setItemText(44, _translate("MainWindow", "naca654421a05-il"))
        self.airfoil.setItemText(45, _translate("MainWindow", "naca661212-il"))
        self.airfoil.setItemText(46, _translate("MainWindow", "naca66206-il"))
        self.airfoil.setItemText(47, _translate("MainWindow", "naca66209-il"))
        self.airfoil.setItemText(48, _translate("MainWindow", "naca66210-il"))
        self.airfoil.setItemText(49, _translate("MainWindow", "naca662215-il"))
        self.airfoil.setItemText(50, _translate("MainWindow", "naca662415-il"))
        self.airfoil.setItemText(51, _translate("MainWindow", "naca663218-il"))
        self.airfoil.setItemText(52, _translate("MainWindow", "naca663418-il"))
        self.airfoil.setItemText(53, _translate("MainWindow", "naca664221-il"))
        self.airfoil.setItemText(54, _translate("MainWindow", "naca0008-il"))
        self.airfoil.setItemText(55, _translate("MainWindow", "naca0010-il"))
        self.airfoil.setItemText(56, _translate("MainWindow", "naca0015-il"))
        self.airfoil.setItemText(57, _translate("MainWindow", "naca0018-il"))
        self.airfoil.setItemText(58, _translate("MainWindow", "naca0021-il"))
        self.airfoil.setItemText(59, _translate("MainWindow", "naca0024-il"))
        self.airfoil.setItemText(60, _translate("MainWindow", "naca671215-il"))
        self.VSairfoil.setCurrentText(_translate("MainWindow", "Select V.S. VSairfoil..."))
        self.VSairfoil.setItemText(0, _translate("MainWindow", "Select V.S. Airfoil..."))
        self.VSairfoil.setItemText(1, _translate("MainWindow", "naca1408-il"))
        self.VSairfoil.setItemText(2, _translate("MainWindow", "naca1410-il"))
        self.VSairfoil.setItemText(3, _translate("MainWindow", "naca1412-il"))
        self.VSairfoil.setItemText(4, _translate("MainWindow", "naca2408-il"))
        self.VSairfoil.setItemText(5, _translate("MainWindow", "naca2410-il"))
        self.VSairfoil.setItemText(6, _translate("MainWindow", "naca2412-il"))
        self.VSairfoil.setItemText(7, _translate("MainWindow", "naca2415-il"))
        self.VSairfoil.setItemText(8, _translate("MainWindow", "naca2418-il"))
        self.VSairfoil.setItemText(9, _translate("MainWindow", "naca2421-il"))
        self.VSairfoil.setItemText(10, _translate("MainWindow", "naca2424-il"))
        self.VSairfoil.setItemText(11, _translate("MainWindow", "naca4412-il"))
        self.VSairfoil.setItemText(12, _translate("MainWindow", "naca4415-il"))
        self.VSairfoil.setItemText(13, _translate("MainWindow", "naca4418-il"))
        self.VSairfoil.setItemText(14, _translate("MainWindow", "naca4421-il"))
        self.VSairfoil.setItemText(15, _translate("MainWindow", "naca4424-il"))
        self.VSairfoil.setItemText(16, _translate("MainWindow", "naca23018-il"))
        self.VSairfoil.setItemText(17, _translate("MainWindow", "naca23021-il"))
        self.VSairfoil.setItemText(18, _translate("MainWindow", "naca23024-il"))
        self.VSairfoil.setItemText(19, _translate("MainWindow", "naca63206-il"))
        self.VSairfoil.setItemText(20, _translate("MainWindow", "naca63209-il"))
        self.VSairfoil.setItemText(21, _translate("MainWindow", "naca632615-il"))
        self.VSairfoil.setItemText(22, _translate("MainWindow", "naca632a015-il"))
        self.VSairfoil.setItemText(23, _translate("MainWindow", "naca633018-il"))
        self.VSairfoil.setItemText(24, _translate("MainWindow", "naca633218-il"))
        self.VSairfoil.setItemText(25, _translate("MainWindow", "naca643418-il"))
        self.VSairfoil.setItemText(26, _translate("MainWindow", "naca643618-il"))
        self.VSairfoil.setItemText(27, _translate("MainWindow", "naca644221-il"))
        self.VSairfoil.setItemText(28, _translate("MainWindow", "naca644421-il"))
        self.VSairfoil.setItemText(29, _translate("MainWindow", "naca64a210-il"))
        self.VSairfoil.setItemText(30, _translate("MainWindow", "naca64a410-il"))
        self.VSairfoil.setItemText(31, _translate("MainWindow", "naca651212-il"))
        self.VSairfoil.setItemText(32, _translate("MainWindow", "naca651212a06-il"))
        self.VSairfoil.setItemText(33, _translate("MainWindow", "naca651412-il"))
        self.VSairfoil.setItemText(34, _translate("MainWindow", "naca65206-il"))
        self.VSairfoil.setItemText(35, _translate("MainWindow", "naca65209-il"))
        self.VSairfoil.setItemText(36, _translate("MainWindow", "naca65210-il"))
        self.VSairfoil.setItemText(37, _translate("MainWindow", "naca652215-il"))
        self.VSairfoil.setItemText(38, _translate("MainWindow", "naca652415-il"))
        self.VSairfoil.setItemText(39, _translate("MainWindow", "naca652415a05-il"))
        self.VSairfoil.setItemText(40, _translate("MainWindow", "naca653218-il"))
        self.VSairfoil.setItemText(41, _translate("MainWindow", "naca65410-il"))
        self.VSairfoil.setItemText(42, _translate("MainWindow", "naca654221-il"))
        self.VSairfoil.setItemText(43, _translate("MainWindow", "naca654421-il"))
        self.VSairfoil.setItemText(44, _translate("MainWindow", "naca654421a05-il"))
        self.VSairfoil.setItemText(45, _translate("MainWindow", "naca661212-il"))
        self.VSairfoil.setItemText(46, _translate("MainWindow", "naca66206-il"))
        self.VSairfoil.setItemText(47, _translate("MainWindow", "naca66209-il"))
        self.VSairfoil.setItemText(48, _translate("MainWindow", "naca66210-il"))
        self.VSairfoil.setItemText(49, _translate("MainWindow", "naca662215-il"))
        self.VSairfoil.setItemText(50, _translate("MainWindow", "naca662415-il"))
        self.VSairfoil.setItemText(51, _translate("MainWindow", "naca663218-il"))
        self.VSairfoil.setItemText(52, _translate("MainWindow", "naca663418-il"))
        self.VSairfoil.setItemText(53, _translate("MainWindow", "naca664221-il"))
        self.VSairfoil.setItemText(54, _translate("MainWindow", "naca0008-il"))
        self.VSairfoil.setItemText(55, _translate("MainWindow", "naca0010-il"))
        self.VSairfoil.setItemText(56, _translate("MainWindow", "naca0015-il"))
        self.VSairfoil.setItemText(57, _translate("MainWindow", "naca0018-il"))
        self.VSairfoil.setItemText(58, _translate("MainWindow", "naca0021-il"))
        self.VSairfoil.setItemText(59, _translate("MainWindow", "naca0024-il"))
        self.VSairfoil.setItemText(60, _translate("MainWindow", "naca671215-il"))
        self.VS_tailspan.setText(_translate("MainWindow", "Tail Span:"))
        self.VS_rootchord.setText(_translate("MainWindow", "Root Chord:"))
        self.horizontal_location_4.setText(_translate("MainWindow", "Horizontal Location Respect to the Leading Edge and Fuselage\'s Tip:"))
        self.VS_tipchord.setText(_translate("MainWindow", "Tip Chord:"))
        self.VS_sweepangle.setText(_translate("MainWindow", "Sweep Angle:"))
        self.HS_sweepangle.setText(_translate("MainWindow", "Sweep Angle:"))
        self.HS_airfoil.setCurrentText(_translate("MainWindow", "Select H.S. Airfoil..."))
        self.HS_airfoil.setItemText(0, _translate("MainWindow", "Select H.S. Airfoil..."))
        self.HS_airfoil.setItemText(1, _translate("MainWindow", "naca1408-il"))
        self.HS_airfoil.setItemText(2, _translate("MainWindow", "naca1410-il"))
        self.HS_airfoil.setItemText(3, _translate("MainWindow", "naca1412-il"))
        self.HS_airfoil.setItemText(4, _translate("MainWindow", "naca2408-il"))
        self.HS_airfoil.setItemText(5, _translate("MainWindow", "naca2410-il"))
        self.HS_airfoil.setItemText(6, _translate("MainWindow", "naca2412-il"))
        self.HS_airfoil.setItemText(7, _translate("MainWindow", "naca2415-il"))
        self.HS_airfoil.setItemText(8, _translate("MainWindow", "naca2418-il"))
        self.HS_airfoil.setItemText(9, _translate("MainWindow", "naca2421-il"))
        self.HS_airfoil.setItemText(10, _translate("MainWindow", "naca2424-il"))
        self.HS_airfoil.setItemText(11, _translate("MainWindow", "naca4412-il"))
        self.HS_airfoil.setItemText(12, _translate("MainWindow", "naca4415-il"))
        self.HS_airfoil.setItemText(13, _translate("MainWindow", "naca4418-il"))
        self.HS_airfoil.setItemText(14, _translate("MainWindow", "naca4421-il"))
        self.HS_airfoil.setItemText(15, _translate("MainWindow", "naca4424-il"))
        self.HS_airfoil.setItemText(16, _translate("MainWindow", "naca23018-il"))
        self.HS_airfoil.setItemText(17, _translate("MainWindow", "naca23021-il"))
        self.HS_airfoil.setItemText(18, _translate("MainWindow", "naca23024-il"))
        self.HS_airfoil.setItemText(19, _translate("MainWindow", "naca63206-il"))
        self.HS_airfoil.setItemText(20, _translate("MainWindow", "naca63209-il"))
        self.HS_airfoil.setItemText(21, _translate("MainWindow", "naca632615-il"))
        self.HS_airfoil.setItemText(22, _translate("MainWindow", "naca632a015-il"))
        self.HS_airfoil.setItemText(23, _translate("MainWindow", "naca633018-il"))
        self.HS_airfoil.setItemText(24, _translate("MainWindow", "naca633218-il"))
        self.HS_airfoil.setItemText(25, _translate("MainWindow", "naca643418-il"))
        self.HS_airfoil.setItemText(26, _translate("MainWindow", "naca643618-il"))
        self.HS_airfoil.setItemText(27, _translate("MainWindow", "naca644221-il"))
        self.HS_airfoil.setItemText(28, _translate("MainWindow", "naca644421-il"))
        self.HS_airfoil.setItemText(29, _translate("MainWindow", "naca64a210-il"))
        self.HS_airfoil.setItemText(30, _translate("MainWindow", "naca64a410-il"))
        self.HS_airfoil.setItemText(31, _translate("MainWindow", "naca651212-il"))
        self.HS_airfoil.setItemText(32, _translate("MainWindow", "naca651212a06-il"))
        self.HS_airfoil.setItemText(33, _translate("MainWindow", "naca651412-il"))
        self.HS_airfoil.setItemText(34, _translate("MainWindow", "naca65206-il"))
        self.HS_airfoil.setItemText(35, _translate("MainWindow", "naca65209-il"))
        self.HS_airfoil.setItemText(36, _translate("MainWindow", "naca65210-il"))
        self.HS_airfoil.setItemText(37, _translate("MainWindow", "naca652215-il"))
        self.HS_airfoil.setItemText(38, _translate("MainWindow", "naca652415-il"))
        self.HS_airfoil.setItemText(39, _translate("MainWindow", "naca652415a05-il"))
        self.HS_airfoil.setItemText(40, _translate("MainWindow", "naca653218-il"))
        self.HS_airfoil.setItemText(41, _translate("MainWindow", "naca65410-il"))
        self.HS_airfoil.setItemText(42, _translate("MainWindow", "naca654221-il"))
        self.HS_airfoil.setItemText(43, _translate("MainWindow", "naca654421-il"))
        self.HS_airfoil.setItemText(44, _translate("MainWindow", "naca654421a05-il"))
        self.HS_airfoil.setItemText(45, _translate("MainWindow", "naca661212-il"))
        self.HS_airfoil.setItemText(46, _translate("MainWindow", "naca66206-il"))
        self.HS_airfoil.setItemText(47, _translate("MainWindow", "naca66209-il"))
        self.HS_airfoil.setItemText(48, _translate("MainWindow", "naca66210-il"))
        self.HS_airfoil.setItemText(49, _translate("MainWindow", "naca662215-il"))
        self.HS_airfoil.setItemText(50, _translate("MainWindow", "naca662415-il"))
        self.HS_airfoil.setItemText(51, _translate("MainWindow", "naca663218-il"))
        self.HS_airfoil.setItemText(52, _translate("MainWindow", "naca663418-il"))
        self.HS_airfoil.setItemText(53, _translate("MainWindow", "naca664221-il"))
        self.HS_airfoil.setItemText(54, _translate("MainWindow", "naca0008-il"))
        self.HS_airfoil.setItemText(55, _translate("MainWindow", "naca0010-il"))
        self.HS_airfoil.setItemText(56, _translate("MainWindow", "naca0015-il"))
        self.HS_airfoil.setItemText(57, _translate("MainWindow", "naca0018-il"))
        self.HS_airfoil.setItemText(58, _translate("MainWindow", "naca0021-il"))
        self.HS_airfoil.setItemText(59, _translate("MainWindow", "naca0024-il"))
        self.HS_airfoil.setItemText(60, _translate("MainWindow", "naca671215-il"))
        self.HS_tailspan.setText(_translate("MainWindow", "Tail Span:"))
        self.HS_rootchord.setText(_translate("MainWindow", "Root Chord:"))
        self.HS_tipchord.setText(_translate("MainWindow", "Tip Chord:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tail), _translate("MainWindow", "Tail"))
        
        
        
        self.vertical_location.setText(_translate("MainWindow", "Vertical Location:"))
        self.horizontal_location_2.setText(_translate("MainWindow", "Horizontal Location Respect to the Leading Edge and Fuselage\'s Tip:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wing), _translate("MainWindow", "Wing"))
        self.export_to_catia.setText(_translate("MainWindow", "Export to CATIA"))
        self.menuHelp.setTitle(_translate("MainWindow", "File"))
        self.update_fuselage.setText(_translate("MainWindow", "Update"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
import resource_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
