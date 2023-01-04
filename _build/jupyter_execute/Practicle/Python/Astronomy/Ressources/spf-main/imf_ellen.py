#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.stats import ks_2samp


# # Problem 1
# 
# Given that we observe $N=1000$ stars for $\log_{10}M > 1$, we can integrate the IMF to obtain $N$ for an arbitrary mass. First, rewrite the IMF.
# 
# $$
# \begin{align}
# \frac{dN}{d\log_{10}M} & = a M^{-1.35} \\
# \frac{dN}{d log_{10}M} & = \ln(10) \frac{dN}{d \ln M} \\
# & = M ln(10) \frac{dN}{dM} \\
# \frac{dN}{dM} & = \frac{a}{\ln(10)} M^{-2.35} = c M^{-2.35}
# \end{align}
# $$
# 
# Now, use the initial condition to find the constant $c$.
# 
# $$
# \begin{align}
# \int_0^{1000} dN & = \int_1^{\infty} c M^{-2.35} dM \\
# 1000 & = -c M^{-1.35} \Big|_1^{\infty} \\
# 1000 & = \frac{c}{1.35} \\
# c & = 1350
# \end{align}
# $$
# 
# Note that $c = 1.35 N_0$ where $N_0$ is the number of stars that are $1 M_{\odot}$ and above. We can use this to find the number of stars we expect for $M > 16 M_{\odot}$.
# 
# $$
# \begin{align}
# \int_0^n dN & = \int_{16}^{\infty} 1350  M^{-2.35} dM \\
# n & = -\frac{1350}{1.35} M^{-1.35} \Big|_{16}^{\infty} \\
# & = 1000 \times 16^{-1.35} \\
# & = \boxed{23.7}
# \end{align}
# $$
# 
# So we'd expect to find around 23 O-type stars.

# # Problem 2
# 
# The Poisson distribution is
# 
# $$
# P = \frac{\lambda^x}{x!} e^{-\lambda}
# $$
# 
# where $x$ is the number of events and $\lambda$ is the expected value. The expected number of $M>50M_{\odot}$ stars is
# 
# $$
# \begin{align}
# \int_0^{\lambda} dN & = \int_{50}^{\infty} 1.35 N_0  M^{-2.35} dM \\
# \lambda & = 1.35 N_0 \times 50^{-1.35} \\
# \lambda & = 6.9 \times 10^{-3} N_0
# \end{align}.
# $$
# 
# The probability of finding at least one very massive star is then
# 
# $$
# \begin{align}
# P(\text{one or more}) & = 1 - P(\text{zero}) \\
# & = 1 - \frac{\lambda^0}{0!} e^{-\lambda} \\
# & = 1 - e^{-6.9 \times 10^{-3} N_0}
# \end{align}
# $$
# 
# which we can set equal to 0.5 to find $N_0$.
# 
# $$
# \begin{align}
# 1 - e^{6.9 \times 10^{-3} N_0} & = 0.5 \\
# 6.9 \times 10^{-3} N_0 & = -\ln(0.5) \\ 
# N_0 & = \boxed{101}
# \end{align}
# $$
# 
# 
# In order to have a 50% chance of finding a very massive star, the cluster should be around 101 stars in size.

# # Problem 3
# 
# The CDF of the desired PDF maps between a uniform distribution and the PDF.
# https://en.wikipedia.org/wiki/Inverse_transform_sampling

# In[2]:


def imf(m, x):
    """
    Returns the value of the IMF dN/d(logM) for the given value of m.
    
    PARAMETERS
    m: (float) the mass in solar masses
    x: (float) the Salpeter slope
    """
    a1 = 0.158
    m_c = 0.079
    s = 0.69
    a2 = 0.0443
    
    f1 = lambda m: a1*np.exp(-(np.log10(m/m_c))**2/(2*s**2))
    f2 = lambda m: a2*m**(-x)
    return np.where(m<=1, f1(m), f2(m))

    
def imf_generator(n, ms, x):
    """
    Returns a sample of size n drawn from the defined imf.
    
    PARAMETERS
    n: (int) the number of values to be generated
    ms: (array) the range of masses covered by the imf
    x: (float) the Salpeter slope
    """    
    # compute the CDF and normalize, then invert to get generator
    cdf = np.cumsum(imf(ms, x))
    cdf = cdf / np.max(cdf)
    cdf_invert_spl = interp1d(cdf, ms, bounds_error=False, fill_value=0)
    
    # feed random numbers into the generator
    nums = np.random.uniform(0, 1, n)
    res = np.zeros(n)
    for i in range(n):
        res[i] = cdf_invert_spl(nums[i])
    return res


# need to extend pretty far at the edges so that interpolation is ok
lo, hi = -5, 3
masses = np.logspace(lo, hi, 1000)
Nsamp = 10000
x0 = 1.3

plt.figure(figsize=(10,8))
plt.plot(masses, imf(masses, x0)*Nsamp, linewidth=2, c='teal', label=r'PDF')
plt.hist(imf_generator(Nsamp, masses, x0), bins=np.logspace(lo, hi, 30),
         color='aquamarine', edgecolor='black', linewidth=0.5, label='Generated')
plt.xlim(0.01, 100)
plt.ylim(1, 2000)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=12)
plt.xlabel(r'$M (M_{\odot})$', fontsize=14)
plt.ylabel(r'$N$', fontsize=14)
plt.show()


# In[3]:


def cluster_mass_function(n, m_min, x):
    """
    Returns the distribution of masses of a cluster.
    
    PARAMETERS:
    n: (int) the size of the cluster
    m_min: (float) the observational lower mass limit in solar masses
    x: (float) the Salpeter slope
    """
    ms = np.logspace(np.log10(m_min), 2, 1000)
    return imf_generator(n, ms, x)

N_cluster = [100, 500]
x = [1, 2]
M_min = [0.5, 1]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8), tight_layout=True)
for i in range(2):
    for j in range(2):
        samp = cluster_mass_function(N_cluster[i], M_min[j], x[j])
        test = cluster_mass_function(N_cluster[i], M_min[j], x0)
        ks_result = ks_2samp(samp, test)
        
        axes[i,j].hist(samp, bins=np.logspace(-1, 3, 30), color='teal', edgecolor='black', 
                       linewidth=0.5, label=r'$x=$' + str(x[j]) + ', $M_{min}=$' + str(M_min[j]) + '$M_{\odot}$', alpha=0.7)
        axes[i,j].hist(test, bins=np.logspace(-1, 3, 30), color='aquamarine', edgecolor='black',
                       linewidth=0.5, label=r'$x=1.35$' + ', $M_{min}=$' + str(M_min[j]) + '$M_{\odot}$', alpha=0.7)
        axes[i,j].set_yscale('log')
        axes[i,j].set_xlim(M_min[j], 100)
        axes[i,j].set_xscale('log')
        axes[i,j].legend()
        axes[i,j].title.set_text('$N_{cluster}=$' + str(N_cluster[i]) + ', $p=$' + '{0:.2f}'.format(ks_result[1]))
fig.supxlabel(r'$M (M_{\odot})$', fontsize=14)
fig.supylabel(r'$N$', fontsize=14)
plt.show()


# A two-sample K-S test calculates the probability that the two samples were drawn from the same parent population. Let $p<0.05$ correspond to a significant difference between the samples. The case with the lower Salpeter slope ($x=1$) requires a larger sample size (hundreds of stars) to be able to meaningfully distinguish it from the original $x=1.35$ case. Although the $x=2$ case has a higher value of $M_{min}$, the greater difference in slope means that it is somewhat easier to distinguish with smaller sample sizes (*maybe* around 100). However, running the code multiple times shows that there can be quite a bit of variation in the $p$ values for both cases. One needs a very large cluster size (thousands or more) to consistently determine changes in $x$.

# In[ ]:




