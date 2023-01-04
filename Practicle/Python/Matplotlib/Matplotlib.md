# Matplotlib

***

**Ressources**:

- [Matplotlib](https://matplotlib.org/cheatsheets/cheatsheets.pdf)


**Beyond Matplotlib**

- [Seaborn](https://seaborn.pydata.org/index.html) - Statistical data visualization
- [Cartopy](https://scitools.org.uk/cartopy/docs/latest/) - Geospatial data processing
- [yt](https://yt-project.org/doc/index.html) - Volumetric data visualization
- [mpld3](https://mpld3.github.io/) - Bringing Matplotlib to the browser
- [Datashader](https://datashader.org/) - Large data processing pipeline
- [plotnine](https://plotnine.readthedocs.io/en/latest/) - A grammar of graphics for Python

And probably much more ... If you want to promote a library you are using yourself, feel free to comment and let me know.


```{note}
Use one data set to set some examples 
```

***

## Introduction

:::::{grid} 2

::::{grid-item}

```python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 100)
Y = np.cos(X)

fig, ax = plt.subplots()
ax.plot(X, Y, color=’green’)

fig.savefig(“figure.pdf”)
fig.show()

```

::::

::::{grid-item}

**Explanation**

Just copy and paste this cell into your Jupyter Notebook editor and run the cell

Voila

You have just created your first plot, Congratulations

::::

:::::

Now lets have a look at ...

## Anatomy of a figure


```{figure} Docs/figure_anatomy.png
---
name: Figure_anatomy
width: 800px
---
source
```

## Plot

### <strong>&#187;  <u> Types </u></strong>

:::::{div} full-width
::::{grid} 2

:::{grid-item}

**Basic**

```{figure} Docs/Basic_plot.png
---
name: Basic_plot
width: 400px
---
source
```

:::

:::{grid-item}

**Advanced**

```{figure} Docs/Advanced_plot.png
---
name: Basic_plot
width: 400px
---
source
```

:::
::::
:::::

### <strong>&#187;  <u>  Styles </u></strong>

:::::{div} full-width
::::{grid} 2

:::{grid-item}

**Explanation**

```python
plt.style.use(style)
```

:::

:::{grid-item}

```{figure} Docs/Plot_style.png
---
name: Basic_plot
width: 500px
---
source
```

:::
::::
:::::

#### <strong>Markers</strong>

```{figure} Docs/Markers.png
---
name: Markers
width: 600px
---
source
```

#### <strong>Colors</strong>

::::::{div} full-width
:::::{dropdown} Color names

```{figure} Docs/Color_name.png
---
name: Color_names
width: 1200px
---
source
```

:::::
::::::


### <strong>&#187;  <u>  Subplots </u></strong>

#### <strong> layout </strong>

```{figure} Docs/subplots.png
---
name: subplots
width: 400px
---
source
```



## Animation

```python

import matplotlib.animation as mpla

T = np.linspace(0, 2*np.pi, 100)
S = np.sin(T)

line, = plt.plot(T, S)

def animate(i):
line.set_ydata(np.sin(T+i/50))
anim = mpla.FuncAnimation(

plt.gcf(), animate, interval=5)
plt.show()


```

