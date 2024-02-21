import win32com.client.dynamic
from webscrapping_airfoil import airfoil_points

def CATIA():
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
    body1.Name="Wing" # will change
    ###

    points = airfoil_points("naca4412-il") # will change
    
    ## Add Spline
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
    part1.Update()
    ###
    ### Scaling
    hybridBody1 = bodies1.Item("Wing") # It will change after GUI
    hybridShapes1 = hybridBody1.HybridShapes
    hybridShapeSpline1 = hybridShapes1.Item("Spline.1")
    reference1 = part1.CreateReferenceFromObject(hybridShapeSpline1)
    originElements1 = part1.OriginElements
    hybridShapePlaneExplicit1 = originElements1.PlaneXY
    reference2 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
    hybridShapeScaling1 = ShFactory.AddNewHybridScaling(reference1, reference2, 500) # It will change after GUI
    hybridShapeScaling1.VolumeResult = False
    body1.AppendHybridShape(hybridShapeScaling1)
    part1.InWorkObject = hybridShapeScaling1
    
    reference3 = part1.CreateReferenceFromObject(hybridShapeScaling1)
    originElements1= part1.OriginElements
    hybridShapePlaneExplicit1 = originElements1.PlaneYZ
    reference4 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit1)
    hybridShapeScaling2 = ShFactory.AddNewHybridScaling(reference3, reference4, 500) # It will change after GUI
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
    hybridShapeScaling3 = ShFactory.AddNewHybridScaling(reference5, reference6, 0.5) # It will change after GUI
    hybridShapeScaling3.VolumeResult = False
    body1.AppendHybridShape(hybridShapeScaling3)
    part1.InWorkObject = hybridShapeScaling3
    
    reference7 = part1.CreateReferenceFromObject(hybridShapeScaling3)
    originElements1= part1.OriginElements
    hybridShapePlaneExplicit2 = originElements1.PlaneYZ
    reference8 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit2)
    hybridShapeScaling4 = ShFactory.AddNewHybridScaling(reference7, reference8, 0.5) # It will change after GUI
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
    hybridShapeTranslate1.DistanceValue = 1000 # It will change later (half span)
    hybridShapeTranslate1.VolumeResult = False
    body1.AppendHybridShape(hybridShapeTranslate1)
    part1.InWorkObject = hybridShapeTranslate1
    selection1.Add(hybridShapeScaling4)
    selection1.Add(hybridShapeTranslate1)
    visPropertySet1.SetShow(1)
    selection1.Clear()
    part1.Update()
    #Sweep
    hybridShapePlaneExplicit4 = originElements1.PlaneYZ
    reference11 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit4)
    hybridShapeDirection1_sweep = ShFactory.AddNewDirection(reference11)
    hybridShapeTranslate1_sweep = ShFactory.AddNewEmptyTranslate()
    reference12 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
    hybridShapeTranslate1_sweep.ElemToTranslate = reference12
    hybridShapeTranslate1_sweep.VectorType = 0
    hybridShapeTranslate1_sweep.Direction = hybridShapeDirection1_sweep
    hybridShapeTranslate1_sweep.DistanceValue = 1000 # it will change
    hybridShapeTranslate1_sweep.VolumeResult = False
    body1.AppendHybridShape(hybridShapeTranslate1_sweep)
    part1.InWorkObject = hybridShapeTranslate1_sweep
    selection1.Add(hybridShapeTranslate1_sweep)
    visPropertySet1.SetShow(1)
    selection1.Clear()
    part1.Update()
    #Dihedral
    hybridShapePlaneExplicit5 = originElements1.PlaneXY
    reference13 = part1.CreateReferenceFromObject(hybridShapePlaneExplicit5)
    hybridShapeDirection1_dihedral = ShFactory.AddNewDirection(reference13)
    hybridShapeTranslate1_dihedral = ShFactory.AddNewEmptyTranslate()
    reference14 = part1.CreateReferenceFromObject(hybridShapeTranslate1)
    hybridShapeTranslate1_dihedral.ElemToTranslate = reference14
    hybridShapeTranslate1_dihedral.VectorType = 0
    hybridShapeTranslate1_dihedral.Direction = hybridShapeDirection1_dihedral
    hybridShapeTranslate1_dihedral.DistanceValue = 87.15 # change parameter
    hybridShapeTranslate1_dihedral.VolumeResult = False
    body1.AppendHybridShape(hybridShapeTranslate1_dihedral)
    part1.InWorkObject = hybridShapeTranslate1_dihedral
    selection1.Add(hybridShapeTranslate1_dihedral)
    visPropertySet1.SetShow(1)
    selection1.Clear()
    part1.Update()
    ###
    
    # Multi_sections_surface,fill,join and symetry
    hybridShapeDirection2 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
    reference15 = part1.CreateReferenceFromObject(hybridShapeScaling2)
    hybridShapeExtremum1 = ShFactory.AddNewExtremum(reference15, hybridShapeDirection2, 1)
    body1.AppendHybridShape(hybridShapeExtremum1)
    part1.InWorkObject = hybridShapeExtremum1
    
    hybridShapeDirection3 = ShFactory.AddNewDirectionByCoord(1, 2, 3)
    reference16 = part1.CreateReferenceFromObject(hybridShapeTranslate1_dihedral) #change parameter
    hybridShapeExtremum2 = ShFactory.AddNewExtremum(reference16, hybridShapeDirection3, 1)
    body1.AppendHybridShape(hybridShapeExtremum2)
    part1.InWorkObject = hybridShapeExtremum2
   
    hybridShapeLoft1 = ShFactory.AddNewLoft()
    hybridShapeLoft1.SectionCoupling = 1
    hybridShapeLoft1.Relimitation = 1
    hybridShapeLoft1.CanonicalDetection = 2
    
    reference17 = part1.CreateReferenceFromObject(hybridShapeScaling2)
    reference18 = part1.CreateReferenceFromObject(hybridShapeExtremum1)
    hybridShapeLoft1.AddSectionToLoft(reference17, 1, reference18)
    reference19 = part1.CreateReferenceFromObject(hybridShapeTranslate1_dihedral) # change parameter
    reference20 = part1.CreateReferenceFromObject(hybridShapeExtremum2)
    hybridShapeLoft1.AddSectionToLoft(reference19, 1, reference20)
    hybridBody1.AppendHybridShape(hybridShapeLoft1)
    part1.InWorkObject = hybridShapeLoft1
    selection1.Add(hybridShapeExtremum1)
    selection1.Add(hybridShapeExtremum2)
    selection1.Add(hybridShapeLoft1)
    visPropertySet1.SetShow(1)
    selection1.Clear()
    part1.Update()
    
    hybridShapeFill1 = ShFactory.AddNewFill()
    hybridShapeFill1.AddBound(hybridShapeTranslate1_dihedral) #change parameter
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
CATIA()