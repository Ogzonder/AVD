import math
import numpy as np


class Nose_Cone_Points:
   
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

# a= Nose_Cone_Points()
# x,y = a.elliptical(100,20)
# print(x)
# print(y)