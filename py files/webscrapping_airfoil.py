import requests
from bs4 import BeautifulSoup
import numpy as np

def airfoil_points(airfoil):
    global x_point_list
    global y_point_list
    global concatenate_x_y_arrays
    x_point_list = []
    y_point_list = []
    r = requests.get("http://airfoiltools.com/airfoil/details?airfoil={}".format(airfoil))
    soup = BeautifulSoup(r.content,"lxml")
    polar_data_set = soup.find_all("td",attrs ={"class":"cell2"})
    
    for data in polar_data_set:    
        try:    
            polar_data = data.find("pre").find(text=True)
            # print(polar_data)
        except:
            pass
    
    with open("airfoil_points.txt", "w") as a:
             a.write(polar_data)
             a.close()    
    
    with open("airfoil_points.txt","r+") as f:
        lines = f.readlines()
        for line in lines[3::]:
            x_point = line.lstrip()[0:9]
            y_point = line.lstrip()[10:20]
            
            x_point_list.append(float(x_point))
            y_point_list.append(float(y_point))
        f.close()
    
    x_points_array = np.array([x_point_list]).reshape(len(x_point_list),1)
    y_points_array = np.array([y_point_list]).reshape(len(y_point_list),1)
    concatenate_x_y_arrays = np.concatenate([x_points_array,y_points_array],axis=1)
    return concatenate_x_y_arrays 

# airfoil_points("naca4412-il")
# # print(concatenate_x_y_arrays)
# # airfoil_points("naca4412-il")
# # # # # # # # # # # print(x_point_list)
# # # # # # # # # # # print(y_point_list)
# print(concatenate_x_y_arrays)