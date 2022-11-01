---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: pandoc
      format_version: 2.10
      jupytext_version: 1.11.5
  nbformat: 4
  nbformat_minor: 5
---

::: {.cell .markdown}
# Water Ice

Even though water is a relatively simple molecule, the third most abundant molecule in the Universe (after H2 and CO), and the most abundant molecule on Earth

------------------------------------------------------------------------

:::::{div} full-width
::::{grid} 4
:::{grid-item}
**Plan**
:::
:::{grid-item}
**Key Litterature**:

-   1
-   2
    :::
    :::{grid-item}
    **Links**
-   [lsbcu](https://water.lsbu.ac.uk/water/water_structure_science.html) *Martin Chaplin*
    :::
    :::{grid-item}
    `{image} Docs/animated_water.gif :alt: Water_moleucule :width: 100px :align: center`
    :::
    ::::
    :::::

------------------------------------------------------------------------

## Going up in scale

`````` {.{margin}}
`````{admonition} **Definitions**
:class: note

<span class="hovertext" data-hover="Yep, like that!">Hover</span> the term to see definition appear or click on the link to be directed toward Teaching. Classified per difficulty (&#11088;)
<br>
<br>

&#11088;

- <span class="hovertext" data-hover="Definition">Atoms</span>  &#x2192; &#128064; [Link](https://deugz.github.io/nb-teaching/_build/html/Bitesize/Astronomy/Astronomy_101/Astronomy_101.html)
- <span class="hovertext" data-hover="Definition">Molecules</span>

<br>
<br>

&#11088; &#11088;

- <span class="hovertext" data-hover="Definition">Polarisability </span>
<br>
<br>

&#11088; &#11088; &#11088;

- <span class="hovertext" data-hover="Definition">Simulation</span>
    - <span class="hovertext" data-hover="Monte Carlo, ">MC</span>
    - <span class="hovertext" data-hover="Molecular Dynamics">MD</span>
- Gibbs free energy
-Chemical potential
<br>
<br>

`````
``````

```{=html}
<h3>
<strong>» <u>Water molecule </u></strong>
</h3>
```
```{=html}
<h4>
<strong>Atomic formula</strong>
</h4>
```
Water is a tri atomique molecule made of 1 Oxygen et 2 Hydrogens.

::::{grid} 2

**Hydrogen**
\^\^\^
`{image} Docs/H.png :alt: Water_moleucule :width: 70px :align: left`
Hydrogen is the must abundant atoms in the Universe (by far). 1 proton, 1 electron, couldn't be more simple

-   Isotopes:
    -   Deuterium (D)
    -   Tritium (T)
-   ISM abundances

**Oxygen**
\^\^\^

`{image} Docs/O.png :alt: Water_moleucule :width: 70px :align: left`
Oxygen however is a bit more heavy and it's isotopes are keys to unveil history of the Solar System {cite:p}`Ito2022`

-   Isotopes
    -   O`<sup>`{=html}16`</sup>`{=html}
    -   O`<sup>`{=html}17`</sup>`{=html}
    -   O`<sup>`{=html}18`</sup>`{=html}
-   ISM abundances

::::

```{=html}
<h4>
<strong>Molecular structure</strong>
</h4>
```
```{=html}
<h5>
<strong><u>OH covalent bonds</u></strong>
</h5>
```
::::{grid} 2
:::{grid-item}
:columns: 4

  \`\`\`{figure} Docs/Water_structure_MC.PNG
  --------------------------------------------
  name: MC_1
  width: 400px

Explain: source Wikimedia

    :::

    :::{grid-item}
    :columns: 8

    **Geometry**: HOH angle = 104.48 deg (Hoy 1979) - different than in tetrahedral configuration (109.47). Each molecule is electrically neutral but also <span class="hovertext" data-hover="define">polar</span> due to the Oxygen atom having a higher <span class="hovertext" data-hover="define">electronegativity</span> than the two Hydrogens. Length


    **Electron density**: The Oxygen has 2 lone pair of electrons.


    **Strength**

    :::
    ::::


    <h5><strong><u>Oxygen lone electron pairs</u></strong></h5> 

    ::::{grid} 2
    :::{grid-item}
    :columns: 4

    ```{figure} Docs/Water_HB_MC.PNG
    ---
    name: MC_3
    width: 400px
    ---
    Explain: source Wikimedia

:::

:columns: 8

**tetraedral**

``` {.{note}}
- The lone electron pair may not be similar (2s vs 2p orbitals), unless they are degenerated.

How would that affect the strength (geometry) of the Hydrogen bonds ?
```

::::

```{=html}
<h5>
<strong><u>Molecular Orbitals for water</u></strong>
</h5>
```
  \`\`\`{figure} Docs/Water_Orbitals_MC.PNG
  -------------------------------------------
  name: MC_5
  width: 400px

Explain: [source](https://water.lsbu.ac.uk/water/h2o_orbitals.html)

    <h4><strong>Properties</strong></h4>

    Water is known for it's <strong>anomalous properties</strong> including a 
    So let's have a look to it's molecular properties to see how they arise

    <h5><strong><u>Molecular vibration</u></strong></h5> 

    :::::{div} full-width



    ::::{grid} 2
    :::{grid-item}
    :columns: 4

    <span class="hovertext" data-hover="Definition">Polarizability</span> leads to an induced **Dipole moment** that makes the water molecule IR active.

    3 fundamental **atomic vibration modes**:
    - (v1) Symmetric Stretching 
    - (v3) Assymetric Stretching 
    - (v2) Bending 


    :::

    :::{grid-item}
    :columns: 8

    ```{figure} Docs/Water-vibrations.gif
    ---
    name: MC_4
    width: 400px
    ---
    Explain: source Wikimedia

  \`\`\`{figure} Docs/Energie_diagram_MC.PNG
  --------------------------------------------
  name: MC_2
  width: 600px

Explain: source Wikimedia

    :::
    ::::
    :::::

    <h5><strong><u>Hydrogen bonding</u></strong></h5> 

    ::::{margin}
    ```{image} Docs/HB-pic.png
    :alt: Water_moleucule
    :width: 160px
    :align: center

::::

One of the most crucial propertie of water is it's ability to form Hydrogen bonds (with itself or other molecules/atoms)

``` {.{note}}
- How is Hydrogen Bonding affecting the molecular vibration shown above is one of the key research questions we are trying to adress 
```

```{=html}
<h5>
<strong><u> Solvatation </u></strong>
</h5>
```
```{=html}
<h5>
<strong><u>More ? </u></strong>
</h5>
```
```{=html}
<h4>
<strong>Phase Diagram</strong>
</h4>
```
:::::{div} full-width

::::{grid} 2

Water can exist in all three 3 physical states under Earth conditions. We are quite familiar with liquid water, however I would like to point your attention on the solid phase of water, ice. Many `<span class="hovertext" data-hover="Definition">`{=html}polymorphs`</span>`{=html}, the one you know being Hexagonal ice (Ih).

Phase lines on this phase diagram represents a `<strong>`{=html}phase boundary`</strong>`{=html} and gives the conditions when two phases may stably coexist in any relative proportions (having the same Gibbs free energy and identical chemical potential)

:::{grid-item}
`{figure} Docs/Phase_diagram_of_water.svg --- name: PT Diagram width: 800px --- Explain: source Wikimedia`
:::
::::
:::::

```{=html}
<h4>
<strong>Water models</strong>
</h4>
```
Now we have seen some of water properties let' have a look at how scientists model the water molecule to push further their investigations. A key point is that:

-   There is **no universal water model** that can explain all the water properties

{cite:p}`Ouyang2015` reviewed the different models created over time (up to 2015) and classified them in 4 groups:

-   1
-   2
-   3
-   4

  \`\`\`{figure} Docs/Water_model_O.PNG
  ---------------------------------------
  name: Water Model timeline
  width: 1000px

Explain: source {cite:p}`Ouyang2015`

    The <strong>Lennard-Jones</strong> relationship





    - Models for individual molecules to perform <span class="hovertext" data-hover="MD: Definition">Molecular Dynamics</span> simulations.



    <h3><strong>&#187;  <u>Gas </u></strong></h3>

    Gas: weakly interacting molecules 

    <h4><strong>Thermodynamic properties</strong></h4>


    <h3><strong>&#187;  <u>Cluster </u></strong></h3>

    <h4><strong> Hydrogen Bonding </strong></h4>

    With two other water molecules

    - DDAA
    - ...

    <h5> <strong><u>Small clusters </u></strong> </h5>

    <h5> <strong><u>Large clusters </u></strong> </h5>


    <h4><strong> Network Description </strong></h4>

    How do we describe an assembly of water molecules

    - Protonated Water Cluster (PW)

    <h5>Modeling Clusters</h5>

    **Thole-type model**

    - [1999](https://sci-hub.ru/10.1063/1.478797)

    - [2002](https://sci-hub.ru/10.1063/1.1423942)

    - [Hydrogen-bond pattern to characterize water network](https://www.degruyter.com/document/doi/10.1515/pac-2018-0721/html)
    - The dipole moment of a constituent molecule in a water cluster is enhanced depending on the local HB network around the water molecule

    <h3><strong>&#187;  <u>Liquid </u></strong></h3>


    ```{note}

    - description of the science in liquid water ...

    - Low T vs High T liquid - subject of polemic 

Constant breaking and reorganisation of individual hydrogen bonds on a `<strong>`{=html}picosecond`</strong>`{=html} timescale. However

## Ice

```{=html}
<h3>
<strong>» <u> Overview </u></strong>
</h3>
```
Ice rules (or Bernal--Fowler rules): basic principles that govern arrangement of atoms in water ice

-   Each oxygen is covalently bonded to two hydrogen atoms
-   The oxygen atom in each water molecule forms two hydrogen bonds with other water molecules

```{=html}
<h4>
<strong>Hexagonal Ice </strong>
</h4>
```
Ih

```{=html}
<h3>
<strong>» <u>Water ice polymorphism </u></strong>
</h3>
```
```{=html}
<h3>
<strong>» <u> Amorphous vs Crystaline Ice </u></strong>
</h3>
```
```{=html}
<h4>
<strong> Comparison </strong>
</h4>
```
```{=html}
<article id="P1">

<h4>
Crystaline
</h4>

-   Polymorph: 18 ?  
-   Ice rules

<h4>
Amorphous
</h4>

-   Polymorph: 5

</article>
```
Amorphous Solid Water

```{=html}
<h3>
<strong>» <u>Crystalisation</u></strong>
</h3>
```
At molecular scales (few molecules up to 100 ?) - Matrix isolation techniques

`{image} Docs/crystal-min-size.png :alt: Water_moleucule :width: 600px :align: center`
:::