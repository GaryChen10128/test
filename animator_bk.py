# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:36:07 2019

@author: 180218
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animator(object):
#    @staticmethod
#    def figure(cls,**kwargs):
#    print('parameter setting...')
#    for keys in kwargs:
#        if keys=='path':
#            cls.path=kwargs[keys]
#            print('setting',keys)
#        if keys=='automode':
#            cls.path=kwargs[keys]
#            print('setting',keys)
    def __init__(self,x=None,y=None,t=None,animation_type=None,FF=None,interval=None):
        try:
            plt.style.use('ggplot')
        except:
            pass
        if interval is None:
            self.interval=100
        else:
            self.interval=interval
        # Set which type of animation will be plotted. One of:
        # line, pcolor, scatter, contour, quiver, labels
        if animation_type is None:
            self.animation_type = 'line'
        else:
            self.animation_type = animation_type
        
        # ----------------------------------------------------------------------------
        # Create data to plot. F is 2D array. G is 3D array
        
        # Create a two-dimensional array of data: F(x, t)
        if x is None:
            self.x = np.linspace(-3, 3, 91)
        else:
            self.x=x
        if t is None:   
            self.t = np.linspace(0, 25, 30)
        else:
            self.t=t
            
        self.X2, self.T2 = np.meshgrid(self.x, self.t)
        self.sinT2 = np.sin(2*np.pi*self.T2/self.T2.max())
        
        self.F = 0.9*self.sinT2*np.sinc(self.X2*(1 + self.sinT2))
        
        # Create three-dimensional array of data G(x, z, t)
        if y is None:
            self.y = np.linspace(-3, 3, 91)
        else:
            self.y=y
        self.X3, self.Y3, self.T3 = np.meshgrid(self.x, self.y, self.t)
        self.sinT3 = np.sin(2*np.pi*self.T3 /
                       self.T3.max(axis=2)[..., np.newaxis])
        self.G = (self.X3**2 + self.Y3**2)*self.sinT3
        self.FF=FF

        # ----------------------------------------------------------------------------
        # Set up the figure and axis
#        self.fig, self.ax = plt.subplots(figsize=(4, 3))
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        
        if self.animation_type not in ['line', 'scatter']:
            self.ax.set_aspect('equal')
        
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'line':
            self.ax.set(xlim=(-3, 3), ylim=(-1, 1))
        
            self.line = self.ax.plot(self.x, self.F[0, :], color='k', lw=2)[0]
        
            def animate(i):
                self.line.set_ydata(self.F[i, :])
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'pcolor':
            cax = self.ax.pcolormesh(self.x, self.y, self.G[:-1, :-1, 0], vmin=-1, vmax=1, cmap='Blues')
            self.fig.colorbar(cax)
        
            def animate(i):
                cax.set_array(self.G[:-1, :-1, i].flatten())
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'scatter':
#            self.ax.set(xlim=(-3, 3), ylim=(-1, 1))
            self.ax.set(xlim=(-20, 20), ylim=(-20, 20))
            self.ax.set_xlabel('left <--> right')
            self.ax.set_ylabel('backward <--> forward')
            scat = self.ax.scatter(self.x[::3], self.F[0, ::3])
        
            def animate(i):
#                print(i)
                # Must pass scat.set_offsets an N x 2 array
#                y_i = self.F[i, ::3]
#                scat.set_offsets(np.c_[self.x[::3], y_i])
                
#                print(np.c_[self.x[::3], y_i].shape)
#                print(np.c_[self.x[::3], y_i][0])
#                print(np.c_[self.x, self.y].shape)
#                scat.set_offsets(np.c_[self.x, self.y])
                
#                scat.set_offsets(self.FF[i,0],self.FF[i,1])
                scat.set_offsets(self.FF[i].reshape(1,2))
                print(self.FF[i].reshape(1,2))
                
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'contour':
            # Keyword options used in every call to contour
            contour_opts = {'levels': np.linspace(-9, 9, 10), 'cmap':'RdBu', 'lw': 2}
            cax = self.ax.contour(self.x, self.y, self.G[..., 0], **contour_opts)
        
            def animate(i):
                self.ax.collections = []
                self.ax.contour(self.x, self.y, self.G[..., i], **contour_opts)
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'quiver':
            self.ax.set(xlim=(-4, 4), ylim=(-4, 4))
        
            # Plot every 20th arrow
            step = 15
            x_q, y_q = self.x[::step], self.y[::step]
        
            # Create U and V vectors to plot
            U = self.G[::step, ::step, :-1].copy()
            V = np.roll(U, shift=4, axis=2)
        
            qax = self.ax.quiver(x_q, y_q, U[..., 0], V[..., 0], scale=100)
        
            def animate(i):
                qax.set_UVC(U[..., i], V[..., i])
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'labels':
            self.ax.set(xlim=(-1, 1), ylim=(-1, 1))
            string_to_type = 'abcdefghijklmnopqrstuvwxyz0123'
            label = self.ax.text(0, 0, string_to_type[0],
                            ha='center', va='center',
                            fontsize=12)
        
            def animate(i):
                label.set_text(string_to_type[:i+1])
                self.ax.set_ylabel('Time (s): ' + str(i/10))
                self.ax.set_title('Frame ' + str(i))
        
#        anim = FuncAnimation(fig, animate, interval=100, frames=len(t)-1, repeat=True)
#        fig.show()
#        self.start()
#        def start(self):
        self.anim = FuncAnimation(self.fig, animate, interval=self.interval, frames=len(self.t)-1, repeat=True)
        self.fig.show()
a=Animator(animation_type='line')
#a.start()
            