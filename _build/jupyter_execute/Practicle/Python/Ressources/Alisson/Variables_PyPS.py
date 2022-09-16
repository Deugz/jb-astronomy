#!/usr/bin/env python
# coding: utf-8

# # Getting Started with Python - Variables
# 
# Version 0.1 Jul 2020
# 
# This notebook introduces the concept of variables in Python programming. You will discover what variables are, and see that every variable in Python has a type. You will also find out more about lists in Python.   
# 
# [1. Variables](#Variables)
# 
# [2. Types](#Types)
# 
# [3. More about Lists](#Lists)
# 
# [Answers to exercises](#Exercise-Answers)
# 
# **FILE:** `Variables_PyPS.ipnyb`
# ***

# <a id="Variables"></a> 
# ## 1. Variables

# A **variable** is a named entity that stores some information within a computer program. Variables provide a way for programmers to store information so that they can retrieve and reuse this information as many times as they want, just by calling its name. 
# 
# Using variables in Python starts usually starts with an *assignment statement*, such as
# 
# `variable_name = (value)`

# In plain English, you could translate this statement as: save the given value in a variable called name `variable_name`. Consider a simple example (run the following code cell).

# In[1]:


number_of_apples = 56


# This statement puts the number 56 into the variable called `number_of_apples`. 

# On assignment, provided that the variable name has not been used before, Python will create a new variable with this name. However, if a variable with this name already exists, its value will be overwritten as you can see by running the following example.

# In[2]:


number_of_apples = 35
print("The value in number_of_apples is", number_of_apples)
number_of_apples = 49
print("The value in number_of_apples is", number_of_apples)


# In passing, note that if you want to find out the value of a variable, then instead of using the `print` function you can also run a code cell that only contains the variable name. This will return the current value of the variable. Try this now by running the code cell below. 

# In[3]:


number_of_apples 


# Variable names can be chosen at your convenience, but with a few important restictions:
# 1. Variable names cannot start with a number: for instance `3things` is not valid. However, variables names may contain or end with a number: so `things3` is valid, as is `thi3ngs`.
# 1. Variables names are *case sensitive* which means that `Thing`, `THING`, `thing` and `thinG` are four different names and would correspond to different variables. 
# 1. In variable names, you must not use spaces, or special characters such as `!`, `:` or `#`, although the underscore character (`_`) is allowed. It is usually preferable to stick to names that comprise only letters, numbers and the underscore ('_').
# 1. Variable names cannot be the same as any of the keywords that have special meaning in Python. These are: `and, del, from, none, True, False, as, elif, global, nonlocal, try, assert, else, if, not, while, break, except, import, or, with, class, in, pass, yield, continue, finally, is, raise, def, for, lambda, return`.
# 
# Given the freedom that you have in choosing variable names, it is good to remember that such names are also important for the readability of your code, and it is good practice to choose names that are meaningful and unambigious.  

# During assignment, it is also possible to define variables with other variables and overwrite them with their previous self. 
# 
# Let's see this with a small exercise.

# <a id="Exercise1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
#     
# The following code defines the value of the variables `height` and `length`. What are their values at the end of the cell ?
# </div>

# In[4]:


# Code for Exercise 1.1
height = 35
length = height - 10
height = height + 4


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.1)

# You can see that in this exercise, the original value of `height` has been lost. You should be careful not to overwrite information that you cannot retrieve! 
# 
# Let's see how to hold onto important values in the following exercise.

# <a id="Exercise1.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.2</b> <br> 
#     
# In the following code cell two variables are defined:
#  
# `red_lights` is assigned the value `5`
#  
# `blue_lights` is assigned the value `18`
# 
# How can you switch them so that the value of `red_lights` is in `blue_lights` and vice-versa ? If you suceed, the cell should return `18 5`.
#     
# 
# </div>

# In[5]:


# Code for Exercise 1.2
red_lights = 5
blue_lights = 18
# Type your code here

# Do not modify after this line
print(red_lights, blue_lights)


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.2)

# ### Variables - summary 
# 
# To recap then: 
# - Variables are places where you can store information in the computer under a given name. You can then retrieve and use this information just by calling its name.
# - Variables are created by an *assignment statement*. If the variable name has not previously been used, Python will create it. If it has already been used, the old value will be overwritten with the new value.
# - Variable names may be chosen relatively freely as long as they adhere to the restrictions mentioned above. 
# - Variable names should be chosen so as to help the readability of your code. 
# 
# ***

# <a id="Types"></a> 
# ## 2. Types

# As you can imagine, variables can be used in many more applications than just moving integers from one box to another (as you saw in Exercise 1.2). In fact, numbers are only one flavour of data that you might be handling with Python. 
# 
# When any new variable is defined using an assignment in Python, the kernel automatically attributes a *type* to it. You have come across several types of data already in this course, but we haven't yet discussed them explicitly. So, let's briefly introduce the most common variable types in Python.
# 
# 1. Integers (`int`) – these are whole numbers, either positive or negative (1, 2, −3456, ...)
# 1. Floating point numbers (`float`) – these are numbers with decimal places (1.0, 3.142, −0.000361, ...). As on a calculator, you can also use scientific notation for floating point numbers (e.g. 1.23e2 to represent $1.23 \times 10^{2}$)
# 1. Strings (`str`) – are a sequence of characters, such as might be used for words or sentences. These are indicated by either single or double quotes (‘fred’, “1”, ‘World’, ‘3.142’). It is important to note that strings containing only digits (e.g. ‘1’ and “3.142”) are treated as text and cannot be manipulated as if they were numbers.
# 1. Boolean (`bool`) - these are variables that can only take the values `True` or `False`. 
# 
# In case of doubt, you can use the Python function `type()` to find the type of a variable. This is done using `type(variable_name)`. 

# <a id="Exercise2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
#     
# In the following window, six variables have been defined. Can you work out what their types are? Check your answers by using the `type` function.
# </div>

# In[6]:


# Code for Execise 2.1
variable_one = "five"
variable_two = 3.49
variable_three = "4"
variable_four = 9
variable_five = "five - 3"
variable_six = False
# Type your code here to try the type function; example type(variable_one)


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers2.1)

# These different types of variable are different in nature and therefore may behave differently when combined with operations. For instance, the use of addition (`+`) with two floats or two strings as shown below:

# In[7]:


float_1 = 4.0
float_2 = 6.85

sum_of_floats = float_1 + float_2

print("The sum of the two floats is", sum_of_floats)

string_1 = "Hello"
string_2 = "World"

sum_of_strings = string_1 + string_2

print("The sum of the two string is", sum_of_strings)


# When you run this example, you'll see that the addition of two floats performs arithmetic summation as expected, whereas addition of two strings gives the string made by joining together (or *concatenating*) the two input strings. You should also note that the variable created by the addition of two floats is also a float, and similarly with string.
# 
# In general, different variable types cannot be mixed. Let us see what happens if you try to sum a float with a string:

# In[8]:


float_1 = 4.0
string_1 = "Hello"

sum_mixed = float_1 + string_2

print("The sum of a float and a string is", sum_mixed)


# Running this code will give an error message, because it is not permissable to add a string to a float. This example shows you that you should keep track of the types of your variables so you don't mix them together in a forbidden way. 
# 
# The exception to the general prohibition on mixing data types occurs with floats and integers. It is acceptable to carry arithmetic operations that mix floats and integers, but note that the results will usually be converted to floats. This isn't usually problematic for calculations, but it can be a problem if you then use that result to do something in Python that requires an integer input.
# 

# ### Types - summary 
# 
# To recap this section: 
#    - Every variable in Python has a specific type.  
#    - Four of the main variable types are: *integers* (`int`), *floats* (`float`), *strings* (`str`)  and *Booleans* (`bool`). 
#    - The type of a variable can be found using the function `type()`.
#    - Variables can usually only be combined together if they are of the same type. An exception is the arithmetic combination of `int` and `float`. 
# ***

# <a id="Lists"></a> 
# ## 3. More about Lists

# We quickly introduced lists when we talked about iteration. Let us be a bit more thorough in describing what Python means by a list. Recalling the definition we used before, lists are sequences of elements that can be anything from numbers to words. They are represented by the form:
# 
# [element 1, element 2, element 3, .... element n]
# 
# where elements are separated by commas within square brackets.
# 
# It is natural to imagine lists of similar elements like integers for instance, but lists in Python can be composed of elements with mixed data types as you can see by running the following:

# In[ ]:


example_of_list = [1, 3.56, "Good Morning", 78]


# As you see in this example, lists are defined in the same way as variables, i.e. by using an assignment statement. Here, the list has four elements. 
# 
# If you want to refer to a specific element of a list, this is done using `name_of_list[index_of_element]`, where `index_of_element` represents the position of the element in the list. Note that in Python, list indicies start at 0; for example, the first element of the previous list is `example_of_list[0]` and the third is `example_of_list[2]`. 
# 
# Let us make sure of this by running:

# In[ ]:


print(example_of_list[2])


# Also note that the index should be an `int`. In the code cell above, try replacing the `2` with `2.0`.
# 
# You'll see that this gives a `TypeError` telling you that the index should be an `int` (or a `slice` - you will learn about slices when you have more experience in coding in Python). Thinking back to the previous section on variable types, here then is an example of a situation where it does matter whether a number is stored as an `int` or a `float`. 
# 

# There are several functions that are useful for handling lists:
# 
# 1. Empty lists can be created just by declaring a list to `[]`, (e.g. `name_of_list=[]`)
# 1. `name_of_list.append(element)` - this instruction will add the item `element` at the last position of the list named `name_of_list`
# 1. Lists can be concatenated by adding (`+`) them.
# 
# Run the following example to see how these features are used:

# In[ ]:


# Create an empty list
list_1 = []
# Append three entries to this list
list_1.append(2)
list_1.append(56)
list_1.append(93)

# Assign values to another list
list_2 = [3, 926, 59]

# Add these two lists together
list_3 = list_1 + list_2

print(list_3)


# Empty lists may seem like a strange idea, but they are very useful when you need to assign values to a list when you don't know at the start of a program how many elements you might need to store. By creating an empty list and appending to it as needed, you can create a list that is defined by the operation of the program. 

# Let us conclude this notebook with a concluding exercice where you will use what you learned during the Jupyter Notebooks *Program Control* and *Variables*.

# <a id="Exercise3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
#     
# A student has recieved marks from several tests in different courses and would like to know the global average mark. The marks are given in a separate list for each of three courses. Can you build a small program that will calculate and return the average mark?
# 
# Hint: you might want to concatenate the three lists and then iterate on each on the marks to sum them and calculate the total average.
#     
# </div>

# In[ ]:


# Code for Exercise 3.1
# List of marks for maths
marks_math = [14, 19, 5, 10]
# List of marks for English
marks_english = [10, 11, 13]
# List of marks for p.e.
marks_pe = [16, 18, 12]

# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers3.1)

# ### Lists - summary 
# 
# In this part, you learned what lists are and how to use them to store a set of information. You also saw how to retrieve the different elements of the list or append elements to it.
# ***

# <a id="Exercise-Answers"></a> 
# ## Exercises Answers
# 

# <a id="ExerciseAnswers1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
# 
# The final value of `length` is 35 - 10 so `25`.
# The final value of `height` is 35 +  4 so `39`
# </div>
# 
# [Back to Exercise 1.1](#Exercise1.1)

# <a id="ExerciseAnswers1.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.2</b> <br> 
# 
# The key idea is to create a third variable to store the information that we don't want to lose. Here we call this variable `auxiliary`. First we transfer the content of `red_lights` into it so that it is saved. Then we transfer the content of `blue_lights` into `red_lights` and transfer the content of `auxiliary` (which has the initial `red_lights` content) into `blue_lights`.
# </div>

# In[ ]:


# Code for Exercise 1.2 (Answer)
red_lights = 5
blue_lights = 18
# Type your code here
auxiliary = red_lights
red_lights = blue_lights
blue_lights = auxiliary
# Do not modify after this line
print(red_lights, blue_lights)


# [Back to Exercise 1.2](#Exercise1.2)

# <a id="ExerciseAnswers2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
# 
# By using the `type()` function for each variable in turn in the code cell below, you should find that:
# 
# `variable_one` is a `str`
# 
# `variable_two` is a `float`
# 
# `variable_three` is a `str`
# 
# `variable_four` is an `int`
# 
# `variable_five` is a `str`
# 
# `variable_six` is a `bool`
# </div>
# 
# 

# In[ ]:


# Code for Execise 2.1 (Answer)
variable_one = "five"
variable_two = 3.49
variable_three = "4"
variable_four = 9
variable_five = "five - 3"
variable_six = False
# Type your code here to try the type function; example type(variable_one)
type(variable_one)


# [Back to Exercise 2.1](#Exercise2.1)

# <a id="ExerciseAnswers3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# 
# The following code is a working example of a solution. 
# To test if your program is working, you can manually calculate the mark average and compare it to what your program yields.
# 
# </div>
# 
# 

# In[ ]:


# Code for Exercise 3.1 (Answer)
marks_math = [14, 19, 5, 10]
marks_english = [10, 11, 13]
marks_pe = [16, 18, 12]

# First, let us create a list with all the marks in it

list_marks = marks_math + marks_english + marks_pe

# Then we need to initialise two things ; the sum of the marks and the total numer of marks.

sum_of_marks = 0
number_of_marks = 0

# Now we want to iterate with a for loop on the elements on the list to count them and sum them

for mark in list_marks:
    
    number_of_marks = number_of_marks + 1 
    sum_of_marks = sum_of_marks + mark

# Then, let us create and calculate the average

average_of_marks = sum_of_marks/number_of_marks

# Now we can print the answer

print('The average of all marks is', average_of_marks)


# [Back to Exercise 3.1](#Exercise3.1)
