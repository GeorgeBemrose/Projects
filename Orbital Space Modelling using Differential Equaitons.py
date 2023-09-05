# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:11:15 2019

@author: George Bemrose
"""

import matplotlib.pyplot as plt
import numpy as np

"""
This is a plot function which allows graphs to plotted with labels, a title and a legend.
"""
def plot(x,y,z,w,f,h):
    plt.plot(x,y, label = h)
    plt.ylabel(z)
    plt.xlabel(w)
    plt.title(f, y = 1.08)
    plt.legend()
 
"""
Constants needed.
"""    
G = 6.67408*(10**(-11))
Mm = 7.348*(10**(22))
ym = 384400*(10**3)

#h = 1 


"""
This allows an float to be inputted and checked if it is, will produce an error until a float is inputted.
"""  

def floatInput(x):
 
 while True:   
    
    try:         
        
        y = float(input('Input a value of {} :'.format(x)))
        break
    
    except ValueError:
        
        print()
        print('The value you have entered for ',x,' is not a float, please try again.')
        
 return y  


"""
The reset function is used to reset all values to zero before calculating a new graph.
"""

def reset():
    X = []
    Y = []
    Vx = []
    Vy = []
    T = []
    KE = []
    PE = []
    TOT = []
    ke = 0
    pe = 0
    tot = 0
    t = 0
    
    
    return(X,Y,Vx,Vy,T,KE,PE,TOT,ke,pe,tot,t)
    
"""
The ax function calculates the acceleration of the rocket depending on if it is part a or b.
""" 
def ax(x,y,MyInput): 
    
    if (MyInput == 'a'):
        
        h = - (G*M*x)*((x**2 + y**2)**(-3/2))
        
    elif (MyInput == 'b'):
        
        h = - (G*M*x)*((x**2 + y**2)**(-3/2)) - (Mm*G*x)*(x**2 + (ym -y)**2)**(-3/2)
        
    return(h)


 
"""
The ay function calculates the acceleration of the rocket depending on if it is part a or b.
"""    
def ay(x,y,MyInput):
    
    if (MyInput == 'a'):
        
        h = - (G*M*y)*((x**2 + y**2)**(-3/2))
        
    elif (MyInput == 'b'):
        
        h = - (G*M*y)*((x**2 + y**2)**(-3/2)) + (Mm*G*(ym-y))*(x**2+(ym-y)**2)**(-3/2)
    
    return(h)



"""
The orbit function is the main function of the program which uses the Runge-Kutta method to calculate the velocity and acceleration in two dimensions.
"""
def orbit(x,y,vx,vy,length,m,MyInput,M,h):
    
    X,Y,Vx,Vy,T,KE,PE,TOT,ke,pe,tot, t = reset()
    
    for t  in range(0,length):
        
        
        k1x = vx
        k1y = vy 
        k1vx = float(ax(x,y,MyInput))
        k1vy = float(ay(x,y,MyInput))

    
        k2x = vx + h*(k1vx)*(0.5)
        k2y = vy + h*(k1vy)*(0.5)
        k2vx = float(ax(x + h*k1x*(0.5), y + h*k1y*(0.5),MyInput))
        k2vy = float(ay(x + h*k1x*(0.5), y + h*k1y*(0.5),MyInput))

    
        k3x = vx + h*(k2vx)*(0.5)
        k3y = vy + h*(k2vy)*(0.5)
        k3vx = float(ax(x + h*(k2x)*(0.5), y + h*(k2y)*(0.5),MyInput))
        k3vy = float(ay(x + h*(k2x)*(0.5), y + h*(k2y)*(0.5),MyInput))

    
        k4x = vx + h*(k3vx)
        k4y = vy + h*(k3vy)
        k4vx = float(ax(x + h*(k3x), y + h*(k3y),MyInput))
        k4vy = float(ay(x + h*(k3x), y + h*(k3y),MyInput))                                                   
 
    
        x = x + (h/6)*(k1x + 2*(k2x) + 2*(k3x) + k4x)
        y = y + (h/6)*(k1y + 2*(k2y) + 2*(k3y) + k4y)
        vx = vx + (h/6)*(k1vx + 2*(k2vx) + 2*(k3vx) + k4vx)
        vy = vy + (h/6)*(k1vy + 2*(k2vy) + 2*(k3vy) + k4vy)
        ke = (.5)*m*((vx**2 + vy**2)**(1/2))**2
        pe = (-G*M*m)*((x**2+y**2)**(-1/2))
        tot = ke + pe        
        t = t + h
    
    
    
        X.append(x)
        Y.append(y)
        Vx.append(vx)
        Vy.append(vy)
        KE.append(ke)
        PE.append(pe)
        TOT.append(tot)
    
        T.append(t)
        
        ############### Test for collisions into Moon and Earth ##################
        w =(x**2 + y**2)*(1/2)
        
        if ( w < 6371):
            
                print('Crashed into the Earth')
                break
            
            
        if (382663E3 <= w and w < 386137E3):
                print('Crashed into the Moon')
                break
    
    f = max(Y) - 386137E3
    
    return(X,Y,Vx,Vy,KE,PE,TOT,T,f)





"""
The function plota allows the plotting of graphs in part a.
"""
def plota(M,r,t):
    
    (X,Y,Vx,Vy,KE,PE,TOT,T,f) = orbit(r,0,0,vi,t,10000,MyInput,M,1)
    
    plt.scatter(0,0,s=20,color='green')
    plt.gca().set_aspect('equal', adjustable = 'box')
    p = 'Planetary Orbit ' + MyInput2 
    plot(X,Y,'Y postion (m) .','X position (m) .',p,'')
    plt.show()
    
    
    plot(T,KE,'Energy (J) ','t (s)','Energy against time graph, ' + MyInput2,'KE')
    plot(T,PE,'Energy (J)','t (s)','Energy against time graph, ' + MyInput2,'PE')
    plot(T,TOT,'Energy (J)','t (s)','Energy against time graph, ' + MyInput2,'Total')
    plt.show()
    
    
    h = 0.0001
    
    while h < 1:
                    
        (X,Y,Vx,Vy,KE,PE,TOT,T,f) = orbit(7000000,0,0,vi,86400,10000,MyInput,M, h)
        h = h*10
        plot(T,TOT,'Energy (J)','t (s)','Total energy against time graph, ' + MyInput2,h)
        
        
    plt.show()
    
"""
The menu system allows the user to ouput certain graphs with values they can input.
"""
 
MyInput = '' 
while MyInput != 'q':
        
    MyInput = input('Enter a choice, "a", "b" , or "q" to quit: ')
    print()
    print('You entered the choice: ',MyInput)
        
    if MyInput == 'a':
        
        print('You have chosen part (a).')
        MyInput2 = ''
        
        while MyInput2 != 'q':
            
            print('Planets: ')
            print()
            print('Earth,')
            print('Mars, ')
            print('Uranus, ')
            print('q to quit')
            
            
            MyInput2 = input('Enter a choice: ')
            
            """
            Each planet allows the user to input a velocity.
            """
            if MyInput2 == 'Earth':
                
                M = 5.972*(10**(24))
                print("V for circular:", np.sqrt(G*M/7000000),"m/s")
                vi = floatInput('the initial velocity')
                plota(M,7000000,86400)
                
                
                
            if MyInput2 == 'Mars':
                
                M = 6.39E23
                print("V for circular:", np.sqrt(G*M/7000000),"m/s")
                vi = floatInput('the initial velocity')
                plota(M,7000000,86400)
               
                
                
            if MyInput2 == 'Uranus':
                M = 6.833E13
                print("V for circular orbit: ", np.sqrt(G*M/70000), "m/s")
                vi = floatInput('the initial velocity')
                plota(M,70000,1728000)
                
                
               
    elif MyInput == 'b':
        
        """
        Plots the trajectory of the rocket around the moon and back.
        """
        
        print('You have chosen part (b)')
        M = 5.972*(10**(24))
        print('Optimum initial speed needed for a conserved orbit: -10.91615E3')
        print('Time needed for a journey and back is around 8.5E5s.' )
        
        
        vi = floatInput('the initial velocity')
        t = int(floatInput('time'))
        (X,Y,Vx,Vy,KE,PE,TOT,T,f) = orbit(0,-6560E3,vi,0,t,10000,MyInput,M,1)
        plt.scatter(0,0,s=20,color='green')
        plt.scatter(0,384400E3,s=2, color ='black')
        p = 'Orbit around the moon'
        
        plot(X,Y,'Y postion (m) .','X position (m) .',p,'')
        plt.show()
        
        
        plot(T,KE,'Energy (J) ','t (s)','Energy against time graph, ' + MyInput2,'KE')
        plot(T,PE,'Energy (J)','t (s)','Energy against time graph, ' + MyInput2,'PE')
        plot(T,TOT,'Energy (J)','t (s)','Energy against time graph, ' + MyInput2,'Total')
        plt.show()
        print('The closest approach which the rocket takes is:',round(f,2) ,'m.')
        
    elif MyInput != 'q':
        
        
        
        print('This is not a valid choice.')
        
        
    print('You have chosen to finish - goodbye.')
    
