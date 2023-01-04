#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python and Jupyter notebooks
# 
# *Authors: Enze Chen and Mark Asta (University of California, Berkeley)*
# 
# Welcome!
# In this notebook, we will introduce the [**Python programming language**](https://www.python.org/) and [**Jupyter notebook**](https://jupyter.org/) programming environment.
# If you already have extensive experience with both of these concepts, that's great!
# We hope you don't mind the quick refresher, and maybe some of our protips will be new for you. 😀
# 
# ```{note}
# This is an interactive exercise, so you will want to click the {fa}`rocket` and open the notebook in DataHub (or Colab for non-UCB students).
# ```

# ## Did you say... Python?
# 
# ````{margin}
# ```{figure} ../../assets/fig/week_1/01/python.png
# :alt: python
# :width: 30%
# :align: center
# Python logo.
# ```
# ````
# 
# By now, many people know (or at least have heard of) the Python programming language, but what they don't know is that the language is not named after the snake 🐍, but rather the television show [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)! 📺
# 
# Since its introduction in 1991, Python has [skyrocketed in popularity](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) in recent years to become one of the most popular programming languages used in computer science, and arguably the _most_ popular language in data science.
# This growth is in part due to:
# 
# ````{sidebar} Python
# ```{figure} ../../assets/fig/week_1/01/python_xkcd.png
# :alt: python_xkcd
# :width: 90%
# :align: center
# [xkcd comic 353](https://xkcd.com/353/).
# ```
# ````
# 
# 1. Its _readability_. Python is designed to be simple and reads like English, using common keywords instead of symbols (e.g., `and` vs. `&&`).
# 1. Its _extensibility_. Python makes it easy for developers to write _modules_ that extend its functionalities for applications in data science, [scientific computing](https://www.nature.com/articles/s41586-020-2649-2), [imaging black holes](https://numfocus.org/case-studies/first-photograph-black-hole), and [flying drones on Mars](https://twitter.com/ThePSF/status/1362516507918483458?s=20).
# 1. Its _open-source_ properties. This means anyone can contribute to Python development and anyone can use it—for free!
# 
# For these reasons (and more), we will be using Python for this module.
# **If you're new to Python, that's OK!**
# The rest of today will be spent on [re]acquainting ourselves with Python and introducing the necessarity functionalities.

# ### Using Python code
# 
# In this module, we're going to take a somewhat practical approach to using Python, in the sense that we view it as just another tool in our toolbox for expanding our understanding of materials.
# We'll discuss Python concepts, syntax, and style along the way, but the _focus_ will always be on applying it to solve relevant MSE problems in a data-driven fashion.
# Therefore, our focus as mentors will be to teach you only what's relevant for this module, and unfortunately won't have much time to extensively cover the details of the language or various packages during the tutorials (you're welcome to ask in OH!).
# 
# While this strategy risks leaving you with only a cursory understanding of Python, we want to offer three points of solace and why this might not actually be the case:
# 1. Based on the initial survey, many of you have some programming experience already, even if it's in a different language. 
# We think you'll be surprised to find that, both at a theoretical and applied level, Python is not _too_ different from other languages that you may have seen (e.g., C++, MATLAB) and that a lot of your prior knowledge will transfer to help you understand Python.
# 1. Solving scientific problems algorithmically (e.g., in a data-driven way) often requires a lot more than being able to program, irrespective of the programming language. 
# Therefore, while we're teaching you Python programming syntax and tools, what we're really hoping to communicate is a _way of thinking_ like a computer, which is quite different than the way humans think.
# And so you might find that you're spending more time _formulating_ data-driven solutions than actually _writing code_.
# A little planning goes a long way.
# For more on this topic, see Jeannette Wing's article on **computational thinking** assigned in the {doc}`homework_01`.
# 1. The third point isn't really related to Python but to the internship more broadly, and that is our desire to expose you to the graduate school research experience, which encompasses a lot more than hammering out lines of code.
# We have designed this module in such a way that surfaces these other elements (the pleasant ones, anyways 😉) which we hope you will come to appreciate as well.
# 
# 
# ### Running Python code
# 
# You can _write_ Python code just about anywhere (even in Microsoft Word, lol), but in order to _execute_ the code, you will need a Python **kernel**.
# For this module (at least, for these tutorials), we will use Jupyter notebooks for running the Python code we write.

# ## Philosophy of Jupyter notebooks
# 
# The main design philosophy behind Jupyter notebooks could be summarized as the following: A platform for creating _computational narratives_ to promote _literate computing_.
# The creators of Project Jupyter, one of whom is UC Berkeley Statistics Professor [Fernando Pérez](https://statistics.berkeley.edu/people/fernando-perez), wanted to create a tool that made computational research easier to communicate and more reproducible, which led to the development of Jupyter notebooks.
# The interleaving of code with prose and graphics has made programming a lot more accessible to general audiences and the interactivity of these notebooks also makes them great teaching tools!

# ### Organization of Jupyter notebooks
# 
# The information in Jupyter notebooks is organized into **cells**, which come in many forms.
# This cell is called a **Markdown cell**, which is used for text that can be formatted with the [Markdown](https://www.markdownguide.org/) markup language.
# This is a fairly simple, yet extremely powerful markup language that allows you to do most of the basic styles, such as add emphasis, make itemized lists, create headings, write inline code, add links, include external images, and use HTML (see [here](https://www.markdownguide.org/cheat-sheet/) for a cheat sheet).
# You know this is a Markdown cell because when you select this cell (click on it such that a <font color="blue">blue bar</font> appears on the left), the menu bar at the top shows "`Markdown  v`" in the second row:
# 
# ![jupyter_menu](../../assets/fig/week_1/01/jupyter_menu.png)
# 
# As an example, here is an itemized list:
# 
# - spam
# - eggs
# 
# And here is a code block _in the Markdown cell_ with Python syntax highlighting:
# ```python
# print('Hello, World!')
# ```
# 
# And if you love $\LaTeX$ as much as we do, it can handle that too. 😍

# ### Making edits
# 
# To **edit** a Markdown cell, double-click on it until you see your cursor flashing in the cell and the cell change color from <font color="blue">blue</font> to <font color="green">green</font>.
# The cell's background will also change color from white to a light gray.
# 
# **EXERCISE:** Double click on this cell and answer the following question by replacing the underscores:
# 
# What is your name? _________
# 
# ----
# 
# To leave "edit mode" and show your changes, press <kbd>Shift</kbd>+<kbd>Enter</kbd> when you're done.
# 
# Notice how we included several Markdown cells in a row rather than putting all this information into a single, giant cell.
# It's often a nice design choice to split your work into smaller chunks to improve readability. 👀

# ## Introducing the code cell
# 
# Notice how the next cell looks a little different. 
# It is a **code cell**, which you can distinguish in a few ways. 
# 
# - If you click in the cell, the menu bar at the top will now show "`Code   v`."
# - The cell will always have a gray background.
# - You may also notice a `In [ ]:` tag in the left margin.
# 
# You can write Python code in these cells and then **execute the code** with <kbd>Shift</kbd>+<kbd>Enter</kbd>.
# Or you can click the <kbd>▶ Run</kbd> button in the menu bar.
# 
# **EXERCISE:** In the space below, enter your name between the quotation marks and then run the code cell.

# In[ ]:


# inline comments in Python start with "#"
name = ""                  # enter your name here as a string
print(f'Hello, {name}!')   # this is a formatted string literal, or f-string, and it's f-ing awesome


# Now you might notice that some output appeared after you executed the cell (which makes sense because we called `print()`) and a number also appeared between the square brackets!
# (e.g., `In [1]:`)
# This number indicates the sequence of code cell execution, which can be handy for a few reasons:
# 
# - You can clearly tell which cells have been executed and which cells have not.
# A cell's variables and functions are only usable in the notebook after it has been executed.
# - Accordingly, for better or worse, the variables and functions in one code cell (at the global _scope_) can be accessed in other code cells that are executed later.
# This allows you to split code among several code blocks and run them sequentially.
# - For better or worse, you can execute code cells in Jupyter notebooks in _whatever order you want_. 
# We still recommend top to bottom, but this does give us flexibility to change an earlier code cell (and rerun it!) if we later deem it necessary.

# ### EXERCISE: Change this Markdown cell into a code cell using the menu bar and run it
# 
# a = 4
# a             # what do you see?

# ## DataHub
# 
# If you are a UC Berkeley student, you may be reading this Jupyter notebook on the school's DataHub (a [JupyterHub](https://jupyter.org/hub) instance), which has been graciously provisioned for this module by the [Division of Computing, Data Science, and Society](https://data.berkeley.edu/).
# With DataHub, all of our Python code will be saved and executed in the cloud, which saves us _a lot_ of hassle with software installation. 
# Everything is also automatically synced with the Jupyter Book!

# ### Installing extra packages
# 
# Perhaps the only "catch," which may come up as you work on your research project, is that you will still have to manually install Python packages that are not included with the default DataHub deployment _every time_ you load DataHub.
# In order to install new packages, use the `pip` package manager directly within a Jupyter code cell.
# 
# **EXERCISE**: Let's demonstrate this below by adding a new code cell and installing the `mendeleev` package.

# We'll also quickly demonstrate how to navigate to the root directory for you to see all the files in DataHub and upload new ones as needed.
# Note that when you close a DataHub notebook, your edits and outputs are preserved, but the variables (kernel) will be reset.

# ## General programming principles and tips ☝
# 
# **EXERCISE**: Before we set you loose to work on practice problems, let's spend some time discussing some general programming principles and best practices.
# 
# I'll start us off with one: **save your work frequently**.
# Just because a code cell runs or a Markdown cell renders does _not_ mean that your work is saved. 
# Jupyter notebook kernels are known to crash pretty randomly, so save your work by clicking the symbol in the menu bar or using <kbd>Ctrl</kbd>+<kbd>S</kbd> (or <kbd>Command</kbd>+<kbd>S</kbd> on Macs).

# In[ ]:


# Tip #1: iterative refinement
names = ['alexa', 'eddie', 'enze', 'kevin', 'luis', 'mack', 'mark', 'megan']


# In[ ]:


# Tip #2: decomposition 🍁
pos = [1, 1, 0]
print( (sum([p ** 2 for p in pos])) ** 0.5 )


# Tip #3: `print()` is your friend. [Stack Overflow](https://stackoverflow.com/) is an even better friend.

# In[ ]:


# Tip #4: block comments (in addition to regular comments!)
# Highlight, and then "Ctrl + /"
a = 'This'
b = 'is'
c = 'unused'
d = 'code'
e = 'but'
f = 'might'
g = 'be'
h = 'helpful'
i = 'later'


# Tip #5: Reset and run all (Jupyter only). ⏩

# In[ ]:


# Tip #6: How to get help from Jupyter with Shift+Tab and ?


# ## Resources
# 
# - If you want to read more about the design of Jupyter notebooks, please see the short paper by [Kluyver, T. et al. _Positioning and power in academic publishing: Players, agents and agendas_, 2016](https://ebooks.iospress.nl/publication/42900).
# - If you want to see a [very long] list of interesting Jupyter notebooks, see [here](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks).
# - More tutorials on using Python in Jupyter notebooks can be found with a quick web search. 
# - For a Markdown **cheat sheet**, see [here](https://www.markdownguide.org/cheat-sheet/).
