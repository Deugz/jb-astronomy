#!/usr/bin/env python
# coding: utf-8

# ## ASTR777 Star and Planet Formation Problem Set 5
# ### Protoplanetary disk SED
# ### Pseudo code hackathon hints

# Integrate a modified blackbody over all radii for an input surface density and temperature profile,
# $$ F_\nu = \int_{R_{\rm min}}^{R_{\rm max}} B_\nu(T)\ \left[1-\exp(-\kappa_\nu\Sigma\,/\cos i)\right]\ \frac{2\pi r\, dr\cos i}{d^2}.$$

# with power law forms for the dust opacity from Beckwith et al. 1990,
# $$\kappa_\nu = \kappa_0\left(\frac{\nu}{\nu_0}\right)^\beta \equiv 10\left(\frac{\nu}{10^{12}{\rm Hz}}\right) {\rm cm^2/g},$$

# and parameterized surface density, and temperature,
# $$\Sigma(r) = \Sigma_1\left(\frac{r}{r_1}\right)^{-1} ~~~~~ T(r) = T_1\left(\frac{r}{r_1}\right)^{-q}.$$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy import constants as c
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# blackbody
def Bnu(nu,T):
    return(2 * h * nu**3 / c**2 / (np.exp(h * nu / (k * T))))


# In[6]:


# simple addition here (could also use np.trapz or scipy modules for more precision)
# note imprecise nomenclature Fnu because it still needs to be divided by d^2 in au units

# T and Sigma are arrays with same size as r
# this routine integrates over r and the nu dependence is implicit in the python use of vectors
def integrate_disk(nu, r, T, Sigma, beta, incl):
    Fnu = np.zeros(nu.size)
    loop over r:
        kappa_nu = function of nu
        tau_nu = kappa_nu * Sigma / cos(incl)
        Fnu += Bnu(nu, T(r)) * (1 - np.exp(-tau_nu))* 2 * np.pi * r * cosi * dr
    return Fnu


# In[7]:


# correct for extinction based on Wang & Chen 2019
# inputs are wavelength in microns, flux in Jy, A_V = visual extinction in magnitudes
def extinct(wl, F, A_V):
    F_extincted = np.zeros(F.size)
    for i, wl1 in enumerate(wl):
        if wl1 < 1:
            Y = (1/wl1) - 1.82
            scale = function of Y
        elif wl1 < 3:
            scale = different function of Y
        else:
            scale = 0.0
        F_extincted[i] = F[i] * function of scale*A_V
    return F_extincted


# In[6]:


def plotdata():
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)

    ax.set_xlim(2e-1, 5e3)
    ax.set_ylim(5e-18, 2e-12)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'$\lambda$ ($\mu$m)', fontsize=14)
    ax.set_ylabel(r'$\nu F_\nu$ (W m$^{-2}$)', fontsize=14)
    
    # data
    wl_obs, Fnu_obs, sigsys, cal, ref = np.genfromtxt('aa_tau.txt', unpack=True)
    nu_obs = 3e-12 / wl_obs
    Fnu_sigma = np.sqrt(sigsys**2 + (cal*Fnu_obs)**2)
    ax.plot(wl_obs, nu_obs*Fnu_obs, 'ko', label='Observations')
    #ax.errorbar(wl_obs, nu_obs*Fnu_obs, yerr=nu_obs*Fnu_sigma, fmt='o', ecolor='black', elinewidth=0.5, mfc='black', ms=5, mec='None')

    x_labels = ['1','10','100','1000']
    x_loc = np.array([float(x) for x in x_labels])
    ax.set_xticks(x_loc)
    ax.set_xticklabels(x_labels)

    return fig, ax


# ### Flat disk SED, $T \propto r^{-3/4}$

# In[7]:


# luminosity and temperature of the star from Andrews et al. 2013
# note that I've increased the extinction from his value of 1.24 to fit the star SED
logT = 3.6085
logL = -0.059
A_V = 1.4
# disk inclination from Loomis et al. 2017
incl = 59
# distance from Gaia = 135pc
Gaia_parallax = look it up!
d_pc = 1000/Gaia_parallax
d_au = d_pc * 2.06e5

# derived stellar radius (squared)
Rstar_sq = function of L and T
# stellar solid angle
Omega_star = stellar area divided by d**2

Rmin = 0.03

# plot observations
fig, ax = plotdata()

# calculate SED from 0.1 microns to 1cm
wl = np.logspace(-1,4,100)  # microns
nu = (3e14 / wl) * u.Hz

# stellar SED = blackbody
Fnu_star = Bnu(nu, 10**logT*u.K) * Omega_star   # make sure you get units right
Fnu_star_extincted = extinct(wl, Fnu_star, A_V)
ax.plot(wl, 3e-12*Fnu_star_extincted/wl, color='black', lw=1, ls='--', label='Star')

# integrate disk over annuli from Rmin to Rmax
Rmax = 100   # au
r = np.logspace(np.log10(Rmin), np.log10(Rmax), 1000)

# dust opacity spectral index, fixed following problem set
beta = 1

# flat disk q = 0.75
T1 = your choice * u.K  # best value for flat disk
T = T1 / r**0.75

# play around with surface density normalization to fit the millimeter points
# note that its large because the disk is so cold
Sigma1 = your choice                # g/cm2
Sigma = Sigma1 / r

Fnu_disk = (integrate_disk(nu, r, T, Sigma, beta, incl) / d_au**2 / u.Jy).decompose()
Fnu_disk_extincted = extinct(wl, Fnu_disk, A_V)
ax.plot(wl, 3e-12*Fnu_disk_extincted/wl, color='black', lw=1, ls=':', label='Flat Disk')
ax.plot(wl, 3e-12*(Fnu_star_extincted + Fnu_disk_extincted)/wl, color='black', lw=2, ls='-', label='Star+Disk')
    
ax.legend()
fig.tight_layout(rect=[0.0,0.0,1.0,1.0])
plt.savefig('flat_disk_SED.pdf')


# ### Add a second temperature component to account for the flaring

# ### Change dust opacity index and radial range of integration

# beta makes the SED change in what way?
# Rmin does what?
# Rmax does what?

# ### Simple ring model

# What happens when you put a ring in the middle of the disk?

# In[ ]:




