# Learning Sistemas Dinamicos
# author: Thiago Mosqueiro @ Jan 2015
# 
# 
# Inspired by Prof. Dr. Reynaldo Pinto's Dynamical Systems class


import numpy as np
import pylab as pl
import matplotlib.animation as animation
from scipy.integrate import odeint



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
        self.tf = 10.
        self.np1 = 100
        self.t  = np.linspace(0, self.tf, int(self.tf)*self.np1)
        
        return
        
    def setSystem(self,ODE):
        self.f = ODE
    
    def solve(self, y0):
        soln = odeint(self.f, y0, self.t, rtol=1e-6, atol=1e-9)
        
        y1 = soln[:,0]
        y2 = soln[:,1]
        
        return y1, y2
    
    def start(self):
        print 'Click on the plot!!'
        
        self.fig = pl.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(-a*1.5, a*1.5)
        self.ax.set_ylim(-a*1.5, a*1.5)
        
        self.cid = self.fig.canvas.mpl_connect('button_press_event', \
                                               self.onclick)
        
        pl.show()
        
    
    def onclick(self, event):
        
        print 'Using as initial conditions (',event.xdata, event.ydata,')'
        
        
        self.y1, self.y2 = self.solve([event.xdata, event.ydata])
        
        self.mark, = self.ax.plot([], [], 'o', markeredgecolor='blue', \
                                  markerfacecolor='blue', markersize=10.)
        self.line, = self.ax.plot([], [], '--')

        #self.ax.plot(self.y1, self.y2, '--')
        
        ani1 = animation.FuncAnimation(self.fig, self.update_plot,  \
                                      len( self.y1 ), blit = True, \
                                      interval = 0.1, repeat=False )
        
        self.ax.plot([event.xdata], [event.ydata], 'o', \
                     markerfacecolor = 'black', markeredgecolor = 'black', \
                     markersize = 5.)
        self.fig.canvas.draw()
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
    LSDinst.setSystem(YS)
    LSDinst.start()
    
    print '\nThe end, my friend.'
