#!/usr/bin/env python
# coding: utf-8

# # Getting Started with Python - Functions
# 
# Version 0.1 Jul 2020
# 
# This notebook introduces a key concept in programming which is functions. You will discover what functions are and how to use them in Python.
# 
# 
# [1. Functions: what are they?](#Functions)
# 
# [2. Building your own function](#Building)
# 
# [3. Modules](#Modules)
# 
# [Answers of the exercises](#Exercise-Answers)
# 
# **FILE:** `Functions_PyPS.ipnyb`
# ***

# <a id="Functions"></a> 
# ## 1. Functions: what are they?

# Programs often involve running the same sequence of instructions several (or many) times. Where there are situations like this, it is usually possible to group these instructions into a named block of code that can be deployed as and when needed. These blocks are called **Functions**. Some functions are supplied as part of Python or in a *library* that you can easily access. For library functions, the block of code that makes up the function is something you would not normally be able to see or edit. 
# 
# You have already used some functions, but here we will go into a bit more detail about what they are. So, you have already seen and used the functions `print()` and `type()`. All functions are used in a similar way: when a program uses a function, there will be some code of the form `name_of_function(input)`. This will *call* the function, which then returns something depending on the value of `input`. 
# 
# For instance, the function `type()` you saw that given a variable as input, the function returns its type. 
# 
# We won't make an exhaustive list of all existing Python functions, rather, we will show a few examples that you might encounter that will help you understand how to use functions in general.
# 
# Firstly, variable types can be changed using functions. This particularly useful for converting a number given in text (i.e. as string) into a number that can be used in calculation. 
# 
# The function `int()` converts its input into an integer. So, this function can be used to convert strings to integers as can be seen by running the following example. 

# In[ ]:


# Example showing how int() converts strings to integers
string_1 = "234"
string_2 = "790"

total = int(string_1) + int(string_2)

print(total)


# Another situation might be that we need to convert a float to an integer. Note that in such a conversion, any part after the decimal point is simply removed or *truncated* (note that `int()` does **not** round to the nearest integer) as shown by running the following example. 

# In[ ]:


# Example showing how int() converts a float to an integer
x = 8
y = 3

# Find and print x/y - it will be a float
print(x/y)

# Now use int() to convert x/y to integer and print this value
index = int(x/y)
print(index)


# Similarly, the functions `float`, and `str` allow you to convert the input into either a float or a string as shown by running the following example. You may want to try removing the `float()` and `str()`
# functions (lines 4 and 14) to see what happens.

# In[ ]:


# Example showing use of float() and str()

# Convert a number as a string to a float
mass_kg = float("4.5")

# Carry out a calculation
mass_g = mass_kg * 1000. 

# Define some output strings
string_1 = "Mass of body: "
string_2 = " g"

# Concatenate the strings, with the mass coverted to a string
string_3 = string_1 + str(mass_g) + string_2

# Print the output
print(string_3)


# An important point to note is that many functions operate with input variables of different types. So in the example of `int()` above, we saw that the function works appropriately regardless of whether the input type is `str` or `float`.
# 
# 
# Moreover, the input to a function need not be a single simple variable and functions can be applied to more complex objects like lists. For instance, if you wish to find the number of elements in a list or sum them, you can use the function `len()` or `sum()` as you can see by running the following example.

# In[ ]:


# Example showing use of list functions
# Some data in a list
list = [3, 19, 29, 456, 4.78, "item"]

# Find and print the length of the list
print("The length of the first list is ", len(list))

# A second list where all elements are of the same type
second_list = [1, 3, 56, 9]

# Sum the elements in this list and print the result
print("The sum of the elements of the second list is", sum(second_list))


# You can  see in this example that functions can sometimes take several variables as inputs and these are separated by commas. In the above example the function `print()` has two inputs (and can take more).
# 
# Note also that functions can be combined as in the above example where `len()`  and `sum()` are called from within the input parameter list of `print()`. 

# <a id="Exercise1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
#     
# The following code cell assigns a list of numbers. Write a program that returns a list containing the truncated integer values of the items in the first list.
# 
# Hint: you will need to create an output list, and iterate on all the elements of the input list to take their integer values before appending them successively to the output list.
# </div>

# In[ ]:


# Code for Exercise 1.1
list_numbers = [23.5, -10.3, -0.234, 0.92, 10.29, -3.0]

# Type your code here 


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.1)

# One last useful function is `input()`. This allows you to ask the user of the program for value. Let us see how it works on the following example: try running the following cell, and when prompted for your year of birth, enter it in the box and press return. 

# In[ ]:


# Ask the user to input their birth year
birth_year = input("In what year were you born? ") 

# Convert input to integer
year = int(birth_year)

print("In 2015 your age was", 2015 - year)


# This program asks for your birth year and answers with you your age as it was in the year 2015. The first instruction is the `input()` function that prints the given string and takes an input from the user. This is input stored in the variable `birth_year`. This input is automatically input in text format i.e. as `str` type. Therefore, to be able to calculate your age in the given year, this text has to be converted into an integer with the `int()` function.

# <a id="Exercise1.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.2</b> <br> 
# 
# The code cell below calculates the cumulative mass of input masses. Explain (using `#` comments) what each line of this this program does.
# 
# </div>

# In[ ]:


# Exercise 1.2
totmass = 0. 
more_input = True
while (more_input):
    answer=input("Mass of item in kg? (enter stop when finished) ")
    if answer == "stop":
        more_input = False
    else: 
        mass = float(answer)
        totmass = totmass + mass
print("Total mass:", totmass, "kilograms")


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.2)

# ### Functions - summary 
# 
# In this part, you learned what functions are and how to use some pre-defined ones. You saw that the functions `int()`, `float()` and `str()` convert variable types and how the `input()` function allows you to prompt the user to supply a value for a variable. You also learnt more about how to use the `print` function and that it can call several variables of different types that need to be comma-separated.
# ***

# <a id="Building"></a> 
# ## 2. How to build your own functions

# Using existing functions from Python libraries is very powerful but sometimes you will want to create your own functions to carry out specific tasks. 
# 
# Let us see an example how this is done in Python by running the following:

# In[ ]:


## This program calculates the energy (in eV) of the state of a hydrogen atom with principal quantum number n

# We define the function that calculates the energy of a state 
# of the hydrogen atom with principal quantum number n
def energy(n):
    # Rydberg constant in eV
    ryd_constant=13.6
    ener = - ryd_constant/(n*n)
    return ener

# The main program starts here
# ask user for principal quantum number n
n = int(input("Input the principal quantum number:"))

print("Energy of the hydrogen atom in this state:", energy(n), "eV")


# In the program, a function named `energy()` is defined. The function block starts with the line `def energy(n):` and ends with the `return ener` statement. The function takes a single input variable `n` and returns the value of the energy contained in the variable `ener`. Similarly to the selection (if) and iteration statements (for or while), the indentation is important here. Note also that the line `return ener` indicates the variable to be returned when the function is called.
# 
# The main program starts at line 11 and prompts the user to input the principal quantum number `n`. Then, in line 13, when the `print()` function calls `energy(n)`, the program jumps to the definition of the function and executes all the instructions contained within it (i.e. everything that is indented). When it reaches the `return ener` statement, it jumps back to the line that called the function (i.e. the `print` function) and then continues executing the rest of the instructions in the program.
# 
# Note also that the name of the variable within the user defined function does not have to be the same as the name of the variable outside the function. Here, a variable `n` and passed to the function. The function uses the same name for that variable (n). You could, if you wish, use a different variable name (say m) within the function. Try changing the program yourself to see this. This feature can be useful if you call the same function multiple times within the same program, but using a different variable each time.
# 
# As you have already seen, unctions can also take more than one variable as input. Properly, these are called *arguments* and they are written to the right of the function (inside the brackets) separated by commas. Remember the colon at the end of the `def` line: the program won’t work if you forget it.
# 
# One last thing to note in the program is that we defined the variable `ryd_constant` to contain the value of the Rydberg constant inside the function. This means that you can't use this particular variable outside the function (we say it is a *local* variable). (You can test this by adding `print(ryd_constant)` so that you output the value of the Rydberg constant either outside or inside the function block. One of these will give you an error message.)

# <a id="Exercise2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
# 
# Write a program that uses the function `energy()` defined above to calculate the energy difference between two states of the hydrogen atom. The program should ask the user to provide the principal quantum number of the states.
# 
# Hint: The program needs to use the function `energy()` twice, using the principal quantum numbers provided by the user.
# </div>

# In[ ]:


# Code for Exercise 2.1
# We define the function that calculates the energy of a state 
# of the hydrogen atom with principal quantum number n
def energy(n):
    # Rydberg constant in eV
    ryd_constant=13.6
    ener = - ryd_constant/(n*n)
    return ener

# The main program starts here
# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers2.1)

# ### Build your own functions - summary 
# 
# In this part, you have seen how to define your own function, how to call it and how the function returns a certain value to the main program. You have also seen than variables that are only defined within functions are called *local* variables and that these are not accessible from the main program.
# ***

# <a id="Modules"></a> 
# ## 3. Modules and Packages

# We saw earlier that it is possible to use a few pre-built functions to automatically perform some operations. Then we learned how to go about writing our own functions. But you don't want to lose precious time reinventing the wheel if a function already exists. Fortunately in Python, many function libraries have been developed and are available to you! They are called **Modules** and **Packages**.
# 
# As we've already mentioned, Python is an extremely popular programming language and there are huge numbers of people out there using it to do specialist things. Python is managed by the Python Software Foundation (https://www.python.org/psf/) which guides its development. 
# 
# One example of a module is the `math` module. This is built into Python and contains useful mathematical functions such as `sqrt()` (square root). Packages are collections of related modules, and these are often produced and distributed as extensions to the Python language.
# 
# There are lots of packages written either specifically for Physics, Astronomy and Data Science or more generally for science and technology (as well as Machine learning, A.I., natural language processing, web development, ... and so on). Part of the skill of developing code in Python is being able to find and use modules that have been developed by others.
# 
# As an example, we will focus in this section on the `math` module for you to see how it works, and how you use it.  Following the same sort of approach, you will then be able to use many other available modules.
# 
# The first step is to load the module; this is done at the beginning of your program (or at least before you call any function from the module) by an instruction line of the form:

# In[ ]:


import math as m


# Running this instruction will import the `math` module and allows you to call any of the functions it contains. 
# 
# Note that the `as` statement tells Python to replace `math` with `m`. To access e.g. the `sqrt()` function from `math` you would call it using `m.sqrt()`. While it isn't necessary to shorten the name of the module (from `math` to `m`) it is such common practice that you need to be aware of it. If you don't use the `as` statement, you would have to give the full name for the function, which in this case would be `math.sqrt()`.
# 
# So, let's try using it by running a simple example:

# In[ ]:


list_of_squares=[0.,1.,4.,9.,16.,25.]
for x in list_of_squares:
    print(m.sqrt(x))


# Sometimes, you don't want to load the full module just for one function. It is possible to load only the required function from the module. This is done using an instruction of the form:

# In[ ]:


from math import sqrt


# Running this will import only the function square root but not the other `math` functions. When loaded in this way, the function can be called without any prefix (i.e. without `math.`). For example, we can now call the `sqrt()` function by running:

# In[ ]:


print(sqrt(144.))


# Many calculations in the physical sciences require functions from the `math` module. Some of the many functions available are:
# - `factorial(x)`	The factorial of the number x.
# - `exp(x)`	The exponential of the number x (i.e. e to the power x)
# - `log(x)`	The natural logarithm of the number x (i.e. the log to the base e of x)
# - `log10(x)`	The logarithm to the base 10 of the number x
# - `sin(x)`	The sine of the number x, where x is in radians
# - `cos(x)`	The cosine of the number x, where x is in radians
# - `tan(x)`	The tangent of the number x, where x is in radians
# - `asin(x)`	The arcsine of the number x (i.e. the angle in radians whose sine is x)
# - `acos(x)`	The arccosine of the number x (i.e. the angle in radians whose cosine is x)
# - `atan(x)`	The arctangent of the number x (i.e. the angle in radians whose tangent is x)
# - `e`         The base of natural logarithms (i.e. the number 2.71828182846…)
# - `pi`       	The ratio of the circumference of a circle to its diameter (i.e. the number 3.14159265359…)
# 
# They are very numerous and it might be interesting to have a look at the module documentation online (https://docs.python.org/3/library/math.html). However, do note that much of the documentation about modules does contain a lot more information that what you need at the moment, but you can always refer back to it as you become more advanced in your programing skills.   

# Let's use all you have learned so far in a concluding activity:

# <a id="Exercise3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# In the the expansion of $(1+x)^{n}$, the integer coefficient of $x^{n}$ is called the binomial coefficient. 
# 
# These coefficients are given by $\frac{n!}{k! (n-k)!}$ for all integer values of $k$ from 1 to $n$. 
#     
# Write a function that takes two integers $a$ and $b$ as input and returns $\frac{a!}{b! (a-b)!}$. 
# 
# Hence write a program that calculates the all the binomial coefficients for $n=10$.
# 
# </div>

# In[ ]:


# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers3.1)

# ### Modules and Packages - summary 
# 
# In this part, you have learnt how you can load packages of modules of pre-defined functions to be able to use them. You have played with some functions of the `math` module. 
# ***

# <a id="Exercise-Answers"></a> 
# ## Exercises - Answers
# 

# <a id="ExerciseAnswers1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
# 
# Have a look at the following example answer.
# </div>

# In[ ]:


# Code for Exercise 1.1 (Answer)
list_numbers = [23.5, -10.3, -0.234, 0.92, 10.29, -3.0]

# Type your code here 

list_number_abs = []

for number in list_numbers:
    
    list_number_abs.append(int(number))
    
print(list_number_abs)


# [Back to Exercise 1.1](#Exercise1.1)

# <a id="ExerciseAnswers1.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.2</b> <br> 
# The working of the program is explained in comments on each line in the code cell below.
# </div>

# In[ ]:


# Code for Exercise 1.2 (Answer)
totmass = 0.          # Initialise the total mass in kilograms
more_input = True    # Define a Boolean variable to define whether more input should be requested. Initialise to True
while (more_input):  # Loop while we expect more input, otherwise jump to end of this loop
    answer=input("Mass of item in kg? (enter stop when finished)")   # Ask user for an input mass or stop when finished 
    if answer == 'stop':    # Test whether the user has entered the stop condition  
        more_input = False  # If so, set the variable more_input to False
    else:                   # Otherwise we have another mass to add
        mass = float(answer)# Convert the input string to a float
        totmass = totmass + mass # Add this mass to the cumulative total 
print("Total mass:", totmass, "kilograms") # After the while loop, print the current value of the cumulative mass.


# [Back to Exercise 1.2](#Exercise1.2)

# <a id="ExerciseAnswers2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
# 
# A working example is given below
# </div>

# In[ ]:


# Code for Exercise 2.1 (Answer)
# We define the function that calculates the energy of a state 
# of the hydrogen atom with principal quantum number n
def energy(n):
    # Rydberg constant in eV
    ryd_constant = 13.6
    ener = - ryd_constant/(n*n)
    return ener

# The main program starts here
# ask user for the first principal quantum number
first_number = int(input("What is the first principal quantum number? "))
# ask user for the second principal quantum number
second_number = int(input("What is the second principal quantum number? "))

# Calculate the energy difference by calling the function energy

energy_difference = (energy(first_number) - energy(second_number))

# Print the energy difference

print("Energy difference between the two states :", energy_difference, "eV")


# [Back to Exercise 2.1](#Exercise2.1)

# <a id="ExerciseAnswers3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# 
# A working example is given below
# </div>

# In[ ]:


# First we will need to load the factorial function from the math module

from math import factorial

# Then we define a function that calculates the binomial coefficients.

def binomial(a,b):
    binomial = factorial(a)/(factorial(b)*factorial(a-b))
    return binomial

# we initialize at 10 the order and a running integer at 1

order = 10
running_integer = 1

# Then we loop on all the integers from 1 to order with a while loop

while running_integer < order + 1:
    
    print(binomial(order, running_integer))
    running_integer = running_integer + 1


# [Back to Exercise 3.1](#Exercise3.1)
