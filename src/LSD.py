# Learning Sistemas Dinamicos
# author: Thiago Mosqueiro @ Jan 2015
# 

# Standard libraries
import numpy as np
import pylab as pl
from argparse import ArgumentParser
import matplotlib.animation as animation
from scipy.integrate import odeint
from math import *

# Library with the dynamical system functions
import DynSystemsLibrary


class LSD:
    
    def __init__(self, xmin = -1, xmax = 1, ymin = -1, ymax = 1.,
                 np1 = 10, totalTime = 20, simInterval = 1.):
        
        ## Integration parameters
        self.tf       = totalTime
        self.np1      = np1
        self.t        = np.linspace(0, self.tf, int(self.tf)*self.np1)
        
        ## Plotting region
        self.xlim_m   = xmin
        self.xlim_p   = xmax
        self.ylim_m   = ymin
        self.ylim_p   = ymax
        
        ## Animation interval
        self.interval = simInterval
        
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



DynSystems_dictionary = {
    "pendulum"   : DynSystemsLibrary.Pend,
    "ex1"        : DynSystemsLibrary.Ex1,
    "YS"         : DynSystemsLibrary.YokoSiqueira,
    "vanDerPol"  : DynSystemsLibrary.vanDerPol
}


if __name__=="__main__":
    
    print '\nLearning Sistemas Dinamicos\n\n'

    # Instantiating the parser
    parser = ArgumentParser()

    # Creating each of the arguments
    parser.add_argument("-d", dest="dynsys",
                        help="Sets which dynamical system to simulate",
                        default="pendulum")
    parser.add_argument("-xmin", dest="xmin",
                        help="Sets the x minimal limit for plotting",
                        default=-3.5, type=float)
    parser.add_argument("-xmax", dest="xmax",
                        help="Sets the x maximal limit for plotting",
                        default=3.5, type=float)
    parser.add_argument("-ymin", dest="ymin",
                        help="Sets the y minimal limit for plotting",
                        default=-3.5, type=float)
    parser.add_argument("-ymax", dest="ymax",
                        help="Sets the y maximal limit for plotting",
                        default=3.5, type=float)
    parser.add_argument("-T", dest="totalTime",
                        help="Simulation total time",
                        default=20., type=float)
    parser.add_argument("-np", dest="h",
                        help="Set how many steps / unit time",
                        default=10, type=int)
    parser.add_argument("-f", dest="f",
                        help="Set how many steps / unit time",
                        default=1., type=float)
    
    # Parsing the arguments
    args = parser.parse_args()
    
    LSDinst = LSD(xmin = args.xmin, xmax = args.xmax,
                  ymin = args.ymin, ymax = args.ymax,
                  np1 = args.h, totalTime = args.totalTime,
                  simInterval = args.f)
    LSDinst.setSystem( DynSystems_dictionary[args.dynsys] )
    LSDinst.start()
    
    print '\nThe end, my friend.'
