# Learning Sistemas Dinamicos
# author: Thiago Mosqueiro @ Jan 2015
# 
# 
# Inspired by Prof. Dr. Reynaldo Pinto's Dynamical Systems class


import numpy as np
import pylab as pl
import matplotlib.animation as animation
from scipy.integrate import odeint
from math import *


def Ex1(y,t):
    dy1 = y[0]*( 4. - y[0] ) - 2.*y[0]*y[1]
    dy2 = y[1]*( 3. - y[1] ) - y[1]*y[0]
    return [dy1,dy2]

def Pend(y,t):
    dy1 = y[1]
    dy2 = -mu*sin(y[0])
    return [dy1, dy2] 

def YS(y,t):
    dy1 = y[1]
    dy2 = -mu*( y[0]**2 + y[1]**2 - a )*y[1] - y[0]
    return [dy1, dy2] 

def vanDerPol(y,t):
    dy1 = y[1]
    dy2 = mu*( a - y[0]**2 )*y[1] - y[0]
    return [dy1, dy2] 




mu = 1.2
a  = 3.0


class LSD:
    
    def __init__(self):
        
        ## Integration parameters
        self.tf       = 20.
        self.np1      = 10
        self.t        = np.linspace(0, self.tf, int(self.tf)*self.np1)
        
        ## Plotting region
        self.xlim_m   = -3.5
        self.xlim_p   = 3.5
        self.ylim_m   = -3.
        self.ylim_p   = 3.
        
        ## Animation interval
        self.interval = 1.
        
        return
        
    def setSystem(self,ODE):
        self.f = ODE
    
    
    def solve(self, y0):
        soln = odeint(self.f, y0, self.t, rtol=1e-6, atol=1e-9)
        
        y1 = soln[:,0]
        y2 = soln[:,1]
        
        return y1, y2
    
    
    def filterSolution(self):
        
        epsilon = 1.
        
        # Filtering y1
        y1 = self.y1[ self.y1 > self.xlim_m - epsilon ]
        y2 = self.y2[ self.y1 > self.xlim_m - epsilon ]
        
        y1 = y1[ y1 < self.xlim_p + epsilon ]
        y2 = y2[ y1 < self.xlim_p + epsilon ]
        
        # Filtering y2
        y1 = y1[ y2 > self.ylim_m - epsilon ]
        y2 = y2[ y2 > self.ylim_m - epsilon ]
        
        y1 = y1[ y2 < self.ylim_p + epsilon ]
        y2 = y2[ y2 < self.ylim_p + epsilon ]
        
        self.y1 = y1
        self.y2 = y2
        
        return
    
    
    def start(self):
        print 'Click on the plot!!'
        
        self.fig = pl.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(self.xlim_m, self.xlim_p)
        self.ax.set_ylim(self.ylim_m, self.ylim_p)
        
        self.cid = self.fig.canvas.mpl_connect('button_press_event', \
                                               self.onclick)
        
        pl.show()
        
    
    
    def onclick(self, event):
        
        print 'Using as initial conditions (',event.xdata, event.ydata,')'
        
        
        ## Integrating the system
        self.y1, self.y2 = self.solve([event.xdata, event.ydata])
        
        ## Cutting out any part of the solution that doesn't fit the screen
        self.filterSolution()
        
        
        #self.updateBoundaries()
        self.ax.set_xlim(self.xlim_m, self.xlim_p)
        self.ax.set_ylim(self.ylim_m, self.ylim_p)

        
        ## Animating the new trajectory 
        
        # Creating the animated objects
        self.mark, = self.ax.plot([], [], 'o', markeredgecolor='blue', \
                                  markerfacecolor='blue', markersize=10.)
        self.line, = self.ax.plot([], [], '--')
        
        # Animating
        ani1 = animation.FuncAnimation(self.fig, self.update_plot,  \
                                      len( self.y1 ), blit = False, \
                                      interval = self.interval, repeat=False )
        
        ## Plotting the initial condition as a small black point
        self.ax.plot([event.xdata], [event.ydata], 'o', \
                     markerfacecolor = 'black', markeredgecolor = 'black', \
                     markersize = 5.)
        
        # Updating everything
        self.fig.canvas.draw()
        return 
    
    
    def updateBoundaries(self):
        self.xlim_m = min( self.xlim_m, min( self.y1 ) )
        self.xlim_p = max( self.xlim_p, max( self.y1 ) )
        self.ylim_m = min( self.ylim_m, min( self.y2 ) )
        self.ylim_p = max( self.ylim_p, max( self.y2 ) )
        return
    
    def update_plot(self, num):
        
        self.mark.set_data( [ self.y1[num] ], [ self.y2[num] ] )
        self.line.set_data( self.y1[:num], self.y2[:num] )
        
        if num >= 0.98*len(self.y1):
            self.mark.set_data( [], [] )
        
        return self.line, self.mark,




if __name__=="__main__":
    
    print '\nLearning Sistemas Dinamicos\n\n'
    
    LSDinst = LSD()
    LSDinst.setSystem(Pend)
    LSDinst.start()
    
    print '\nThe end, my friend.'
