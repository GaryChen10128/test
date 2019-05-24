# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:36:07 2019

@author: 180218
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animator(object):
    
    def __init__(self,data,animation_type=None,interval=None):
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

        self.data=data

        # ----------------------------------------------------------------------------
        # Set up the figure and axis
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        circle2 = plt.Circle((0, 0), 20, color='orange',alpha=0.3)
        self.ax.add_artist(circle2)
        self.fig.gca().set_aspect("equal")
        self.ax.set_title('COP on balance board')
        self.ax.set(xlim=(-25, 25), ylim=(-25, 25))
        self.ax.axvline(x=0, ymin=0.1, ymax=0.9,c='black')
        self.ax.axhline(y=0, xmin=0.1, xmax=0.9,c='black')
        self.ax.set_xlabel('left <--> right')
        self.ax.set_ylabel('backward <--> forward')
        self.ax.legend()
        
        
        
        if self.animation_type not in ['line', 'scatter']:
            self.ax.set_aspect('equal')
        # ----------------------------------------------------------------------------
#        if self.animation_type == 'line':
#            self.ax.set(xlim=(-3, 3), ylim=(-1, 1))
#        
#            self.line = self.ax.plot(self.x, self.F[0, :], color='k', lw=2)[0]
#        
#            def animate(i):
#                self.line.set_ydata(self.F[i, :])
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'pcolor':
            cax = ax.pcolormesh(x, y, G[:-1, :-1, 0], vmin=-1, vmax=1, cmap='Blues')
            fig.colorbar(cax)
        
            def animate(i):
                cax.set_array(G[:-1, :-1, i].flatten())
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'scatter':
            self.num=self.data.shape[2]
            self.l=len(self.data)
            texts = [self.ax.text(0.80, 0.95-i*0.05,  'initializing', transform=self.ax.transAxes) for i in range(self.num*2)]

            scats=[]
            color=['red','green','yellow','black']
            for j in range(self.num):
                scats.append(self.ax.scatter(self.data[::3,0,j], self.data[::3,1,j]))
                scats[j].set_color(color[j])
            
            
            def animate(i):
                temp=self.data[i,:,:].transpose()
                
                for j in range(self.num*2):
                    if (j%2)==0:
                        texts[j].set_text('dot %d, progress %d/%d'%(j/2,i,len(self.data)-1))
                    else:
                        index=int((j-1)/2)
                        texts[j].set_text('%s'%(temp[index]))
                for k in range(self.num):
                    scats[k].set_offsets((self.data[i,:,:].transpose())[k])
                    
        if self.animation_type == 'line':
            self.num=self.data.shape[2]
            self.l=len(self.data)
            texts = [self.ax.text(0.80, 0.95-i*0.05,  'initializing', transform=self.ax.transAxes) for i in range(self.num*2)]

            self.scats=[]
            color=['red','green','yellow','black']
            u=v=np.zeros([1,1])
            for j in range(self.num):
                self.scats.append(self.ax.plot(self.data[::3,0,j], self.data[::3,1,j],c=color[j])[0])
#                scats.append(self.ax.quiver(self.data[::3,0,j], self.data[::3,1,j]))
#                scats[j].set_color(color[j])
            
            def animate(i):
                temp=self.data[i,:,:].reshape(2,self.num).transpose()
                
                for j in range(self.num*2):
                    if (j%2)==0:
                        texts[j].set_text('dot %d, progress %d/%d'%(j/2,i,len(self.data)-1))
                    else:
                        index=int((j-1)/2)
                        texts[j].set_text('%s'%(temp[index]))
                for k in range(self.num):
#                    self.scats[k].set_offsets((self.data[i,:,:].reshape(2,self.num).transpose())[k])
#                    print((self.data[i,:,:].transpose()[k])[0])
                    self.scats[k].set_ydata([0,(self.data[i,:,:].transpose()[k])[1]])
                    self.scats[k].set_xdata([0,(self.data[i,:,:].transpose()[k])[0]])
        if self.animation_type == 'vector':
            self.num=self.data.shape[2]
            self.l=len(self.data)
            texts = [self.ax.text(0.80, 0.95-i*0.05,  'initializing', transform=self.ax.transAxes) for i in range(self.num*2)]

            self.scats=[]
            color=['red','green','yellow','black']
            u=v=np.zeros([0,0])
#            z1=np.zeros_like(self.data[::3,0,0)
            for j in range(self.num):
#                self.scats.append(z1,z1,self.ax.quiver(self.data[::3,0,j], self.data[::3,1,j],c=color[j])[0])
                self.scats.append(self.ax.quiver(0,0,self.data[::3,0,j], self.data[::3,1,j]))
#                scats[j].set_color(color[j])
            
            def animate(i):
                temp=self.data[i,:,:].reshape(2,self.num).transpose()
                
                for j in range(self.num*2):
                    if (j%2)==0:
                        texts[j].set_text('dot %d, progress %d/%d'%(j/2,i,len(self.data)-1))
                    else:
                        index=int((j-1)/2)
                        texts[j].set_text('%s'%(temp[index]))
                for k in range(self.num):
                    self.scats[k].set_UVC((self.data[i,:,:].transpose()[k])[0], (self.data[i,:,:].transpose()[k])[1])
                    

                    
                    
        # ----------------------------------------------------------------------------
        if self.animation_type == 'contour':
            # Keyword options used in every call to contour
            contour_opts = {'levels': np.linspace(-9, 9, 10), 'cmap':'RdBu', 'lw': 2}
            cax = ax.contour(x, y, G[..., 0], **contour_opts)
        
            def animate(i):
                ax.collections = []
                ax.contour(x, y, G[..., i], **contour_opts)
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'quiver':
            ax.set(xlim=(-4, 4), ylim=(-4, 4))
        
            # Plot every 20th arrow
            step = 15
            x_q, y_q = x[::step], y[::step]
        
            # Create U and V vectors to plot
            U = G[::step, ::step, :-1].copy()
            V = np.roll(U, shift=4, axis=2)
        
            qax = ax.quiver(x_q, y_q, U[..., 0], V[..., 0], scale=100)
        
            def animate(i):
                qax.set_UVC(U[..., i], V[..., i])
        
        # ----------------------------------------------------------------------------
        if self.animation_type == 'labels':
            ax.set(xlim=(-1, 1), ylim=(-1, 1))
            string_to_type = 'abcdefghijklmnopqrstuvwxyz0123'
            label = ax.text(0, 0, string_to_type[0],
                            ha='center', va='center',
                            fontsize=12)
        
            def animate(i):
                label.set_text(string_to_type[:i+1])
                ax.set_ylabel('Time (s): ' + str(i/10))
                ax.set_title('Frame ' + str(i))
        
        self.anim = FuncAnimation(self.fig, animate, interval=self.interval, frames=len(self.data)-1, repeat=True)
        self.fig.show()
#        def start(self):
#        self.animate=animate
#        self.anim = FuncAnimation(self.fig, self.__class__.animate, interval=self.interval, frames=len(self.data)-1, repeat=True)
#        self.fig.show()
#a=Animator()
#a.start()
            