""" ###############_____________READ ME______________############### """
#All the instructions for running the code are at the end of the document.
#Author: George Bemrose
#Date: 18/03/19
#Time:12:00
#Assignment 2
#Computing 301
#Thanks!
#
""" ###############_____________TASK 1 CODE______________############### """

import numpy as np
import matplotlib.pyplot as plt

def plot(condition):
    
    X,Y,P,count,typ = laplace(condition)
    
    plt.title('Graph of potential for: ' + typ)
    plt.contourf(X, Y, P, 100, cmap=plt.cm.jet)
    plt.colorbar()
    d = np.gradient(P)
    plt.streamplot(X, Y, -d[1], -d[0], density = 1, color = 'black')
    plt.show()
    
    
    print(typ,'interations:',count)   
    
def laplace(condition):
    
    P, lenX, lenY, delta, typ = condition
    
    X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))
    
    before = [1]
    after = [2]
    count = 0
    while abs(np.mean(before) - np.mean(after)) > 1e-15:
    
        for i in range(1, lenX-1, delta):
            for j in range(1, lenY-1, delta):
                
                before = np.copy(P)
                if typ == 'Finite Capacitor' or typ == 'Infinite Capacitor':
                    if P[i,j] == 100 or P[i,j] == -100:
                        pass
                    else:
                        P[i,j] = 0.25 * (P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])
                else:
                    P[i,j] = 0.25 * (P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])
                after = np.copy(P)
        count += 1
        
    return(X,Y,P,count, typ)
    
def setup(lenX,lenY,delta, Ptop,Pbottom,Pleft,Pright,Pguess, typ = '0'):
    P = np.empty((lenX, lenY))
    P.fill(Pguess)
  
    P[(lenY-1):, :] = Ptop
    P[:1, :] = Pbottom
    P[:, (lenX-1):] = Pright
    P[:, :1] = Pleft
    
    if typ == 'Finite Capacitor':
         P[lenY//3+4:(lenY//3 + 5), lenX//4:3*lenX//4] = -100
         P[lenY//3 + lenY//4,lenX//4:3*lenX//4] = 100
    if typ == 'Infinite Capacitor':
         P[lenY//3 + 4:(lenY//3 + 5),:] = -100
         P[lenY//3 + lenY//4,:] = 100
            
    return(P, lenX, lenY, delta, typ)    

def iterations(length):
    lenA = []
    countA = []
    
    for i in range(1,int(length/10)+1):
        len = i*10
        lenA.append(len)
        X,Y,P,count,typ = laplace(setup(len,len,1,100,0,0,0,1,'Top Down'))
        countA.append(count)
        print("Dimension", len)
        print("count",count)
        print("--------------------------")
        print("")

    xaxis = np.linspace(10,length,5)
    z = np.polyfit(lenA,countA,2)
    p = np.poly1d(z)
    plt.title('Effect of increasing grid dimension to number of iterations.')
    plt.xlabel('Dimensions of grid')
    plt.ylabel('Number of iterations')
    plt.plot(lenA,countA,'.',xaxis,p(xaxis),'--')
    
    return()
        
""" ###############_____________TASK 2 CODE______________############### """
def poker(nodes,nT,time,ice):
    dx = 0.5/nodes #0.5m long poker
    dt = time/nT
    alp = 59/(450*7900)
    w = (alp*dt)/((dx)**2)
    
    
    pMatrix = np.zeros((nodes,nodes))
    temp = np.empty((nodes,1))
    temp.fill(21)
    
    for i in range(1,nodes-1):
        pMatrix[i,i] = 1+2*w
        pMatrix[i,i+1] = - w
        pMatrix[i,i-1] = -w
        
    pMatrix[0,0] = 1+3*w
    pMatrix[-1,-1] = 1+w
    pMatrix[0,1] = -w
    pMatrix[-1,-2] = -w
    
    if ice == 'Ice Bath':
        pMatrix[-1,-1] = 1+3*w
        
    for k in range(nT):
        temp[0] += 2*w*1000
        
        if ice == 'Ice Bath':
            temp[-1] = 0
        
        temp = np.linalg.solve(pMatrix,temp)
        
    return temp

def lineRodTempGraph(nodes,nT,h, ice ,maxT): 
    for i in range(10,maxT,h):
        Temp = poker(nodes,nT,i,ice)
        plotMultiLine(nodes,Temp,i,ice)    
    plt.show()

def plotMultiLine(nodes, Temp, i, ice):
    plt.plot(np.linspace(0,0.5,nodes),Temp, label='T='+str(i) +'s')
    plt.xlabel('Position (m)')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Poker Rod with: '+ ice)
    plt.legend(loc = 'center left', bbox_to_anchor = (1,0.5))
    
def plotContour(nodes,nT,time,ice):
    plt.cur_axes = plt.gca()
    plt.cur_axes.axes.get_xaxis().set_ticks([])
    plt.imshow(poker(nodes,nT,time,ice), cmap='jet', vmin=0, extent = [0,17,50,0])
    plt.ylabel('Position along rod (cm)')
    plt.title('Temperature gradient along rod with: ' + ice + ', ' + str(time) +'s')
    plt.colorbar(label= 'Temperature (Celsius)')
    plt.show()


""" ###############_____________INSTRUCTIONS______________############### """

####################___________PART 1__________#######################
""" Uncomment below for potential from top, i.e. a temperature gradient """
#plot(setup(20,20,1,100,0,0,0,1,'Top Down')) # For potential from the top
""" Uncomment below for a finite capacitor """
#plot(setup(20,20,1,0,0,0,0,0,'Finite Capacitor')) 

""" Uncomment below for an infinite capacitor """
#plot(setup(20,20,1,0,0,0,0,0,'Infinite Capacitor')) 

""" Uncomment below to plot the graph of increased grid dimension with number of iterations."""
""" Warning, this is extremely long to compute. """
#parameter is the dimension size
#iterations(30)
#iterations(40)

#iterations(100)


####################___________PART 2__________#######################
""" Uncomment below for temperature against time for the ice bath."""
#lineRodTempGraph(100,100,500,'Ice Bath',5000) 
""" Uncomment below for temperature against time for no heat loss. """
#lineRodTempGraph(100,100,2000,'No Heat Loss',25000)
""" Uncomment below for the contour plot of temperature for the ice bath.  """
#plotContour(100,500,6000,'Ice Bath')
""" Uncomment below for the contour plot of temperature for no heat loss. """
#plotContour(100,500,6000,'No Heat Loss')

"""
Thanks!!!
"""
