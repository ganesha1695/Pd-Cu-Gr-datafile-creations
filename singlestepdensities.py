#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:44:11 2020
step structure longer with single steps
change1
change2

@author: ganesha2
"""

import numpy as np

a=3.639087457 #Cu eamfs
#a=3.8904 Pd
#a=3.97344 #Pdreax

latvec1a=a*np.array([1,0,0])
latvec1b=a*np.array([0,1,0])
latvec1c=a*np.array([0,0,1])

            


#Add atom positions to lattice


rb0=[0,0,0]
#rb1=[0,0]
rb1 = rb0 + (latvec1a + latvec1b)/2
rb2 = rb0 + (latvec1b + latvec1c)/2
rb3 = rb0 + (latvec1c + latvec1a)/2





coordinates1=np.ndarray(shape=(16384000,3))    
b=0
while b < 16384000 :
    for j in range(-80,80):
        for i in range(-80,80):
            for k in range(-80,80):   
                coordinates1[b]=i*latvec1a + j*latvec1b + k*latvec1c +rb0
                #coordinates1[b][1]=atom_positions1[i][j][0][1]
                #coordinates1[b][2]=atom_positions1[i][j][0][2]
                coordinates1[b+1]=i*latvec1a + j*latvec1b + k*latvec1c +rb1
                #coordinates1[b+1][1]=atom_positions1[i][j][1][1]
                #coordinates1[b+1][2]=atom_positions1[i][j][1][2]
                coordinates1[b+2]=i*latvec1a + j*latvec1b + k*latvec1c +rb2
                coordinates1[b+3]=i*latvec1a + j*latvec1b + k*latvec1c +rb3
                b+=4
                

x=20
y=15

                
#Axes transformation
#############################################################################      
al=x*((20)**-1)
theta_x=np.arctan(al)#*np.pi/180
#x-rotation
tr_x=np.array([[np.cos(theta_x),0,-np.sin(theta_x)],[0,1,0],[np.sin(theta_x),0,np.cos(theta_x)]])
if x==0.0:
    theta_tr=np.pi*(2**-1)
else:
    theta_tr=np.arccos(((400*(x**2)**-1)+1)**-0.5)
b=y*np.sin(theta_tr)*(20**-1)
theta_y=np.arctan(b)#*np.pi/180
#x-rotation
tr_y=np.array([[1,0,0],[0,np.cos(theta_y),-np.sin(theta_y)],[0,np.sin(theta_y),np.cos(theta_y)]])

tr_xy=tr_y@tr_x
coordinates_tr=np.ndarray(shape=(16384000,3)) 

coordinates_tr2=np.ndarray(shape=(16384000,3))

coord=np.ndarray(shape=(300000,3))

e=0
for i in range(0,16384000):

    #coordinates_tr[i][0]=coordinates1[i][0]*tr_x[0][0] + coordinates1[i][1]*tr_x[0][1] + coordinates1[i][2]*tr_x[0][2]
    #coordinates_tr[i][1]=coordinates1[i][0]*tr_x[1][0] + coordinates1[i][1]*tr_x[1][1] + coordinates1[i][2]*tr_x[1][2]
    #coordinates_tr[i][2]=coordinates1[i][0]*tr_x[2][0] + coordinates1[i][1]*tr_x[2][1] + coordinates1[i][2]*tr_x[2][2]
        
 



#        for i in range(0,16384000):
#    
    #coordinates_tr2[i][0]=coordinates_tr[i][0]*tr_y[0][0] + coordinates_tr[i][1]*tr_y[0][1] + coordinates_tr[i][2]*tr_y[0][2]
    #coordinates_tr2[i][1]=coordinates_tr[i][0]*tr_y[1][0] + coordinates_tr[i][1]*tr_y[1][1] + coordinates_tr[i][2]*tr_y[1][2]
    #coordinates_tr2[i][2]=coordinates_tr[i][0]*tr_y[2][0] + coordinates_tr[i][1]*tr_y[2][1] + coordinates_tr[i][2]*tr_y[2][2]
    coordinates_tr2[i,:]=tr_xy@coordinates1[i,:]



    if (coordinates_tr2[i,0]>-0.01 and coordinates_tr2[i,0]<33.451  and coordinates_tr2[i,1]>-164.766 and coordinates_tr2[i,1]<164.768 and coordinates_tr2[i,2]>-100 and coordinates_tr2[i,2]<0.01):
        coord[e]=coordinates_tr2[i] + [0,0,0]
        e+=1
    if e>3 and coord[e-1,0]==0.0 and coord[e-1,1]==0.0 and coord[e-1,2]==0.0 and coord[e-2,0]==0.0 and coord[e-2,1]==0.0 and coord[e-2,2]==0.0:
        break
coordf2=coord[:e,:]

##############################################################################
#Step making
##############################################################################
coordf=np.copy(coordf2)

# =============================================================================
# for i in range(len(coordf)):
# 
# 
#     
#     
# #Height 3
#     if (0.284*coordf[i,1] + 2.21*coordf[i,2]>-4.7 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-4.5 and coordf[i,1]<-3.2):
#         if (coordf[i,1]>-3.21-1):
#             coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
#         else:     
#             coordf[i]+=[0,19.692,1.705]
#         
# #Height 5
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-9.37 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-9.35 and coordf[i,1]<-4.2):
#         coordf[i]+=[0,39.383-2*2.21,3.41+2*0.284]
# 
# #Height 7
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-14.05 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-14.0 and coordf[i,1]<-5.2):
#         if (coordf[i,1]>-5.2-1):
#             coordf[i]+=[1.287,2.21+6*1.005, 6*1.989-0.284]
#         else:
#             coordf[i]+=[0,59.075-2*2.21,5.115+2*0.284]
# 
# #Height 9
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-18.73 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-18.69 and coordf[i,1]<-6.2):
#         coordf[i]+=[0,78.767-4*2.21,6.82+4*0.284]
# 
# #Height 11
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-23.42 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-23.39 and coordf[i,1]<-7.2):
#         if (coordf[i,1]>-7.2-1):
#             #coordf[i]+=[0,0,1]
#             coordf[i]+=[1.287,2.21+10*1.005, 10*1.989-0.284]
#         else:
#             coordf[i]+=[0,98.458-4*2.21,8.525+4*0.284]
# #Height 13
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-28.1 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-28.05 and coordf[i,1]<-8.2):
#         coordf[i]+=[0,118.15-6*2.21,10.23+6*0.284]    
# =============================================================================
        
# =============================================================================
# #Height 15
#     elif (0.284*coordf[i,1] + 2.21*coordf[i,2]>-32.8 and 0.284*coordf[i,1] + 2.21*coordf[i,2]<-32.7 and coordf[i,1]<-9.2):
#         if (coordf[i,1]>-9.2-1):
#             coordf[i]+=[1.287,2.21+14*1.005, 14*1.989-0.284]
#         else:
#             coordf[i]+=[0,137.842-6*2.21,11.935+6*0.284] 
# =============================================================================


###############################################################################
#Rotation for plane normal search
###############################################################################


# =============================================================================
# h1_step=np.zeros((1196,3),dtype=float)
# h1_i=0
# 
# h15_step=np.zeros((19136,3),dtype=float)
# h15_i=0
# =============================================================================
# =============================================================================
# h13_step=np.zeros((12*1196,3),dtype=float)
# h13_i=0
# 
# for i in range(len(coordf)):
#      if  coordf[i,1]>6*-16.477 and coordf[i,1]<6*16.4765:
#         h13_step[h13_i]=coordf[i]
#         h13_i+=1    
# =============================================================================
# =============================================================================
#     #single step of height1    
#     if  coordf[i,1]>131.8 and coordf[i,1]<148.28:
#        h1_step[h1_i]=coordf[i]
#        h1_i+=1
# =============================================================================
# =============================================================================
#     if  coordf[i,1]>-131.814 and coordf[i,1]<131.8:
#        h15_step[h15_i]=coordf[i]
#        h15_i+=1
# =============================================================================
            


###############################################################################
#Duplication to make longer
###############################################################################

coordf_longer2=np.zeros((2*len(coordf),3),dtype=float)
coordf_longer2[:len(coordf),:]=coordf
coordf_longer2[len(coordf):(2*len(coordf)),:]=coordf +  [0,2*164.768+ 0*16.477,0]
#coordf_longer[(len(h15_step)+len(h1_step)):,:]=h15_step[:,:] + [0,263.626 + 0*16.477,0]

for i in range(len(coordf_longer2)):
     if (0.284*coordf_longer2[i,1] + 2.21*coordf_longer2[i,2]>-42.1521 and 1.989*coordf_longer2[i,1] - 1.005*coordf_longer2[i,2]<983.165):
#         #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
         coordf_longer2[i]=[0,0,0]
#         #coordf_longer[i]+=[1.286,196.512-(31*2.21),-21.026+(31*0.284)]

#            
coordf_longer=coordf_longer2[~np.all(coordf_longer2==0,axis=1)]



for i in range(len(coordf_longer)):
    #3step
    if (0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]>-47.5 and 0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]<-46.5 and coordf_longer[i,2]>-34.4-(0*0.284)):
        #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
        coordf_longer[i]+=[0,351.236-(0*2.21),-40.920+(0*0.284)]
        #coordf_longer[i]+=[1.286,196.512-(31*2.21),-21.026+(31*0.284)]
    if coordf_longer[i,1]>494.300 and coordf_longer[i,2]>-0.2 :
        coordf_longer[i]+=[1.286,-391.625,-34.384]
    #5step     
    if (0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]>-52 and 0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]<-51 and coordf_longer[i,2]>-30.7-(0*0.284)):
        #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
        coordf_longer[i]+=[0,397.451-(0*2.21),-42.825+(0*0.284)]
        #coordf_longer[i]+=[0,198.540-(30*2.21),-16.949+(30*0.284)]
    if coordf_longer[i,1]>493.29 and coordf_longer[i,2]>-2.0 :
        coordf_longer[i]+=[0,-261.618,-42.825]        
    #7step    
    if (0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]>-57 and 0.284*coordf_longer[i,1] + 2.21*coordf_longer[i,2]<-55 and coordf_longer[i,2]>-27.3-(0*0.284)):
        #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
        coordf_longer[i]+=[1.286,441.456-(0*2.21),-44.446+(0*0.284)]
        #coordf_longer[i]+=[0,198.540-(30*2.21),-16.949+(30*0.284)]
    if coordf_longer[i,1]>492.29 and coordf_longer[i,2]>-4.0 :
        coordf_longer[i]+=[1.286,-217.613,-44.446]
 
#after 7 step with 19 is made       
coordf_longer3=np.copy(coordf_longer)  

edge_x=np.array([274.68,231.68,188.68,145.678,102.678,59.678,16.678])
edge_xnext=edge_x-2.21
edge_y=np.array([-48.424,-44.814,-41.204,-37.794,-34.384,-30.974,-27.564])
edge_ynext=edge_y+0.284
edge_ycut=edge_y-0.05  

for k in range(1,19): 
    coordf_longer3=np.copy(coordf_longer)
    for i in range(len(coordf_longer3)):
        
        if (0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]>-47.5 and 0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]<-46.5 and coordf_longer3[i,2]>edge_ycut[4]-(k*0.284)):
            #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
            #coordf_longer[i]+=[0,351.236-(0*2.21),-40.920+(0*0.284)]
            coordf_longer3[i]+=[1.286*((k+1)%2),edge_xnext[2]-edge_x[4]-(k*2.21),edge_ynext[2]-edge_y[4]+(k*0.284)]
        
        if (0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]>-52 and 0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]<-51 and coordf_longer3[i,2]>edge_ycut[5]-((1+2*k)*0.284)):
            #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
            coordf_longer3[i]+=[0,edge_xnext[1]-edge_x[5]-((1+2*k)*2.21),edge_ynext[1]-edge_y[5]+((1+2*k)*0.284)]
            #coordf_longer[i]+=[0,198.540-(30*2.21),-16.949+(30*0.284)]
    
        if (0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]>-57 and 0.284*coordf_longer3[i,1] + 2.21*coordf_longer3[i,2]<-55 and coordf_longer3[i,2]>edge_ycut[6]-((2+3*k)*0.284)):
            #coordf[i]+=[1.287,2*1.005 +2.21,2*1.989-0.284]
            coordf_longer3[i]+=[1.286*((k+1)%2),edge_xnext[0]-edge_x[6]-((2+3*k)*2.21),edge_ynext[0]-edge_y[6]+((2+3*k)*0.284)]
            #coordf_longer[i]+=[0,198.540-(30*2.21),-16.949+(30*0.284)]
            
    
    ntype1=1
    ntype2=2    
    xlim=[0,33.4521 ] 
    ylim=[-164.768,3*164.768 + 0*16.477]
    zlim=[-110,100]
            
    print("writing")
    f=open('Cu_7multsingleh1_d%i_%i_%i' %((18-k),x,y),'w+')
    print("writing")
    f.write('(written by Ganesh A)\n\n')
    f.write('%d\tatoms\n'%(len(coordf_longer3)))
    f.write('3\tatom types\n')
    f.write('%.9g\t%.9g\txlo xhi\n'%(xlim[0],xlim[1]))
    f.write('%.9g\t%.9g\tylo yhi\n'%(ylim[0],ylim[1]))
    f.write('%.9g\t%.9g\tzlo zhi\n'%(zlim[0],zlim[1]))
    
    f.write('\n\n')
    f.write('Masses\n\n')
    
    f.write('1\t63.456\n')
    f.write('2\t12.00\n')
    f.write('3\t1\n\n')
    f.write('Atoms\n\n')
    i=0
    for i in range(len(coordf_longer3)):
        f.write('%d %d %d %d %1.3f %1.3f %1.3f %d %d %d\n'%(i+1,ntype1,ntype1,0,coordf_longer3[i,0],coordf_longer3[i,1],coordf_longer3[i,2],0,0,0))
    f.close()