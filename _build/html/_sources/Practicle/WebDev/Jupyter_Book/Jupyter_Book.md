# Jupyter Book

***

[Jupyter Book]('https://jupyterbook.org/en/stable/intro.html')

**Examples**
- list
- list (pick from website)

***

## Description

The perfect tool to *Build beautiful, publication-quality books and documents from computational content*

## How it works

take a collection of `markdown` files and trasnform them into a **static web site** (link HTML Course)

```{warning}
Try to understand how the build work. 
- Can get a bit messy !
```

### Sphinx

[How they relate]('https://jupyterbook.org/en/stable/explain/sphinx.html') to one another.

## Functionality

### Citation

reference files using `references.bib`
```
{cite}`Deguin2018`
```

```{note}
Create specific naming convention for the different .bib file
```


### Formatting

The formatting is taken care of by [Sphinx]()

#### Admonitions

##### How to

Admonition can be added easily. Jupyter Book has a few:

````
```{note}
note
```

# Markdown friendly 

:::{admonition} title
note supporting **Markdown**
:::

````


##### Examples

```{warning}
warning
```

:::{admonition} To add
note that support **Markdown syntax**
:::

```{tips}
tips
```
... and you can create your owns

##### Get creative 

```{note}
add explosion html in title
```


#### Cards 


## Teaching

### Create your own admonition

Jupyter Book allow you to create your own admonition (which is pretty cool)
- [HTML admonition](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-html-admonition)

<div class="admonition" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title">This is the **title**</p>
This is the *content*
</div>

This is how it comes out, direct from the provided example, but with a bit of code in the **custom.css** file in the _static folder :

```html
<div class="admonition_dialogue" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title_dial"> <img src="Docs/Svg_icons/dark-dialogue-bubble-svgrepo-com.svg" class="picto" alt=">">This is the **title** <img src="Docs/Svg_icons/Docs/Svg_icons/flag-for-flag-france-svgrepo-com.svg" class="picto"></p>
This is the *content*
</div>
```
modify class name ...

add image via html - link towards html teaching

<div class="admonition_dialogue" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title_dial"> <img src="../../Docs/Svg_icons/dark-dialogue-bubble-svgrepo-com.svg" class="picto" alt=">">This is the **title** <img src="../../Docs/Svg_icons/Docs/Svg_icons/flag-for-flag-france-svgrepo-com.svg" class="picto"></p>
This is the *content*
</div>

<div class="admonition">
<p>Some **content**</p>
  <div class="admonition tip">
  <div class="title">A *title*</div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  </div>
</div>

```{admonition} Dialogue ![flag alt >](../../Docs/Svg_icons/dark-dialogue-bubble-svgrepo-com.svg) - ![flag alt >](../../Docs/Svg_icons/flag-for-flag-france-svgrepo-com.svg)
:class: dropdown
French Dialogue admonition Baby :)
```

Explain how I tried a solution with what I know (ie html), and a quick (how to walk around the problem) think through help to resolve the issue 

- [CSS admonition](https://jupyterbook.org/en/stable/advanced/html.html?highlight=javascript#custom-css-or-javascript)

### Insert your own Javascript

Link to picture example.

- Insert your .js script file into the static folder

## Other

 ### Multiple book embeded 

 Architecture

 [Github Repo](https://github.com/choldgraf/jupyter-multi-book)

[Demo](https://predictablynoisy.com/jupyter-multi-book/index.html)