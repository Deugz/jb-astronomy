#!/usr/bin/env python
# coding: utf-8

# ## ASTR777 Star and Planet Formation Problem Set 1 student solutiun
# ## from Maria Vincent
# ## uses matplotlib animation

# In[1]:


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# basic modules for reading data and plotting images
from astropy.io import ascii, fits
from astropy.wcs import WCS
from astropy.visualization import (ImageNormalize, MinMaxInterval, SqrtStretch, LogStretch, AsinhStretch)

#modules for interactive widget and animation
from matplotlib import animation 
import pylab
from ipywidgets import interact, fixed, interactive
import ipywidgets as widgets
from IPython.display import display, HTML
import sys
#sys.path.append("your_path/ffmpeg/")

#%matplotlib inline


# In[2]:


# read in the fits file and get some basic information
#hdu = fits.open('your_path_to_the_data_cube/orionA_12co.fits')
hdu = fits.open('iram30m/orionA_12co.fits')
# create data array and header
im = hdu[0].data
hd = hdu[0].header


# In[3]:


# define velocity
v = hd['CRVAL3'] + (1 + np.arange(hd['NAXIS3']) - hd['CRPIX3']) * hd['CDELT3']

# range of indices (chosen by eye playing around with other image visualization tools)
k0 = 215
k1 = 245
nplot = k1-k0+1
frames = np.linspace(k0,k1,nplot,dtype=int)


# In[4]:


# animation using matplotlib

# a function to display each cube
def display_cubes_anim(cube, dur = 5, fccolor='black',axcolor='white'):
 
    # create a figure
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    fig.set_figheight(8)
    fig.set_figwidth(8)
    
    #show the image
    norm = ImageNormalize(np.nanmax(im,axis=0), stretch=AsinhStretch())
    implt = im[cube,:,:]
    image = ax.imshow(implt, cmap='gnuplot2', origin = 'lower',norm=norm)
    cbar = plt.colorbar(image,ax = ax,shrink=0.6)
    cbar.set_label('Peak Temperature (arb.units)', rotation=90,fontsize=12,color='white')
    
    #axes controls
    #changing axes from px to deg
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: "%.1f"%((x-hd['CRPIX1'])*hd['CDELT1'])))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: "%.1f"%((x-hd['CRPIX2'])*hd['CDELT2'])))
    ax.set_xlabel(r'$\Delta\alpha (deg)$',fontsize=12)
    ax.set_ylabel(r'$\Delta\delta (deg)$',fontsize=12)
    plt.xticks(fontsize=11.5)
    plt.yticks(fontsize=11.5)
    fig.canvas.draw()
    ax.tick_params(direction='in', which = 'major',length=0.5,colors='white');
    
    #this function defines the two things that change in each frame-- the image and title
    def animate(cube):
        image.set_data(im[cube])
        ax.set_title('velocity= {:.2f} m/s'.format(v[cube]),fontsize=14,color='yellow')
        return image
    
    #just playing with colors, coz why not?!
    fig.tight_layout()
    fig.set_facecolor(fccolor)
    ax.set_facecolor(axcolor)
    ax.xaxis.label.set_color('white')#setting up X-axis label color to white
    ax.yaxis.label.set_color('white')
    colax = plt.getp(cbar.ax.axes, 'yticklabels')
    plt.setp(colax, color='white')
    
    #the animated object which you defined using animate(cube)
    anim = animation.FuncAnimation(fig, animate, 
                                   frames=frames,
                                   interval=dur*1000 / len(im))
                                   
    plt.close()
    return anim


# In[5]:


#cube to animate
anim = display_cubes_anim(10, dur=50., fccolor='black', axcolor='black')
#create a playable widget
HTML(anim.to_jshtml())
#create video
# anim.save('datacube_modvel.mp4', writer=animation.FFMpegWriter(fps=1.2), dpi=300)


# In[6]:


# animation using ipywidgets

# a function to display each cube
def display_cubes_anim(cube):
 
    # read in the fits file and get some basic information
    hdu = fits.open('iram30m/orionA_12co.fits')
    # create data array and header
    im = hdu[0].data
    hd = hdu[0].header
    # define velocity
    v = hd['CRVAL3'] + (1 + np.arange(hd['NAXIS3']) - hd['CRPIX3']) * hd['CDELT3']
    
    # create a figure
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    fig.set_figheight(8)
    fig.set_figwidth(8)
    
    #show the image
    norm = ImageNormalize(np.nanmax(im,axis=0), stretch=AsinhStretch())
    implt = im[cube,:,:]
    image = ax.imshow(implt, cmap='gnuplot2', origin = 'lower',norm=norm)
    cbar = plt.colorbar(image,ax = ax,shrink=0.6)
    cbar.set_label('Peak Temperature (arb.units)', rotation=90,fontsize=12)
    ax.set_title('velocity= {:.2f} m/s'.format(v[cube]),fontsize=14)
    
    #axes controls
    #changing axes from px to deg
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: "%.1f"%((x-hd['CRPIX1'])*hd['CDELT1'])))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: "%.1f"%((x-hd['CRPIX2'])*hd['CDELT2'])))
    ax.set_xlabel(r'$\Delta\alpha (deg)$',fontsize=12)
    ax.set_ylabel(r'$\Delta\delta (deg)$',fontsize=12)
    plt.xticks(fontsize=11.5)
    plt.yticks(fontsize=11.5)
    fig.canvas.draw()
    ax.tick_params(direction='in', which = 'major',length=0.5,colors='white');
    
    
    #just playing with colors, coz why not?!
    fig.tight_layout()
    fig.set_facecolor('white')
    ax.set_facecolor('white') 
                                   
    # plt.close()
    return anim


# In[7]:


#using pywidgets
#displays the plot with a drop down menu to choose cubes
#include display cubes function from before
interactive_plot = interactive(display_cubes_anim,cube=frames)
output = interactive_plot.children[-1]  #interactive plot has multiple components, this points to the actual image
output.layout.height = '550px' #to prevent size change when being updated
output.layout.width = '550px' #to prevent size change when being updated
interactive_plot


# In[8]:


#displays the plot with a slider to choose cubes
interactive_plot = interactive(display_cubes_anim,cube=(k0,k1,1))
output = interactive_plot.children[-1] #interactive plot has multiple components, this points to the actual image
output.layout.height = '550px' #to prevent size change when being updated
output.layout.width = '550px' #to prevent size change when being updated
interactive_plot


# In[ ]:




