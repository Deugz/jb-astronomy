#!/usr/bin/env python
# coding: utf-8

# # Getting Started with Python - program control
# 
# Version 0.2 Aug 2020
# 
# This notebook demonstrates how programs in Python can run a set of instructions, and how those instructions can be made to depend on information generated or acquired at the time that the progam is run. Overall, this concept is called **program control** and we will look at three specific areas:
# 
# 
# [1. Sequence](#Sequence)
# 
# [2. Selection](#Selection)
# 
# [3. Iteration](#Iteration)
# 
# 
# [Answers to the Exercises](#Exercise-Answers)
# 
# **FILE:** `Program_Control.ipnyb`
# ***

# <a id="Sequence"></a> 
# ## 1. Sequence

# The simplest Python program is a **sequence** of instructions, written one per line, and executed one by one from top to bottom. Every time the program is run, the same operations are executed in the same order.
# 
# Our first program only has two lines of instructions in the code cell below. For this notebook, it helps to display the line numbers (these are displayed on the left hand side of a cell) - do this by selecting the `Toggle line numbers` option from the `View` menu (you can switch off line numbers by repeating this operation). Then **run** the cell. 

# In[1]:


result = 3 + 7
print("The sum of 3 and 7 is", result)


# The first instruction (line 1) is an `assignment`: the computer evaluates the expression to the right of the assignment (=) and stores the result in the variable (`result`) on the left of the assignment. Each piece of data that is needed by a program must be stored in a variable. Translating Python to English, the assignment states ‘let result be the sum of 3 and 7’. We could call the variable anything we want, such as `R` or `sum_of_two_numbers`, but the first of these is rather too short to be meaningful, and the second is rather long to type in. So a compromise for the variable name that's not too long, not too short, and which means something to anyone reading the program is usually the best option.
# 
# The second instruction, `print()` (in line 2), prints some text on the screen (in the left-hand pane), followed by the computed result. Note the following:
# 
# 1. The comma separates the two things to be printed, in the same way that we use commas in English to enumerate two, three, or more things.
# 2. Text is written between double quotes, which are not printed themselves. In Python, a sequence of characters surrounded by double quotes is called a *string*. (Note that single quotes can also be used and you may see them employed in Python programs.)
# 
# These details are important once you start writing your own programs. Computers are not as smart and accommodating as human readers; at the slightest spelling mistake (like `pint` instead of `print`) or missing punctuation (like forgetting the comma or double quotes), the computer will give up on running your code and will display an error message. 
# 
# On top of that, most error messages are rather cryptic. Therefore, it’s a good idea to get used to them by noting any error messages that you get and what caused them, so that you understand what might be wrong when faced with similar error messages as you develop your own programs. This is what you will do in the following exercise. 

# <a id="Exercise1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
# In the following code cell, insert double quotes around the 7 on the first line and then run the program. 
# 
# You will get an error message saying there is a TypeError. This means the code is mixing data of different types – mixing apples and oranges if you like. In this case, you are trying to add a number (3) to a string ("7"), which of course doesn’t make sense.

# In[2]:


result = 3 + 7
print("The sum of 3 and 7 is", result)


# Sometimes, more subtle errors can lead to unexpected results. This is akin to miscommunication, when other people understand something different from what you intended to say. The next exercise gives an example of such an error.

# <a id="Exercise1.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.2</b> <br> 
#     
# Now place double quotes around the the word `result` within the print statement on the second line and then run the cell. Try to explain the outcome before reading further.

# In[3]:


result = 3 + 7
print("The sum of 3 and 7 is", result)


# When putting double quotes around the variable name, it becomes a string. Hence, the computer will print the name literally, instead of printing the value stored in the variable.
# 
# To sum up, `"result"`, `"7"`, `result` and `7` are different things. The first two are strings (literal text), the third is a variable name, and the last is a number. In Python, there are different *types* of variables, used to represent different sorts of data (such as strings or numbers).  You will learn more about variables and types in a subsequent notebook.
# 
# Learning from mistakes is always helpful, so for this and the remaining programs, you may want to introduce deliberate errors and observe what message or output you get. Don’t forget to reset the program or undo your changes after each error.
# 
# Before moving on to more complicated programs, there is still more you can do with the simple two-line program above. In Python, as you might expect, you can also use different mathematical operators other than addition (`+`). These include the other arithmetic operators: subtraction (`-`), multiplication (`*`) and division (`/`). Raising a number to a power can be done using the double-asterisk operator (`**`). Just as when writing equations, it is good practice to enclose expressions in brackets to ensure they are calculated exactly in the way you intend. 
# 
# For example, the following simple program uses Pythagoras' theorem to calculate the length of the hypotenuse in a 3-4-5 triangle.  To do this, it works out the sum of 3 squared and 4 squared, then takes the square root (i.e. take the number to the power of one half).

# In[4]:


output = ( (3**2) + (4**2) )**0.5
print(output)


# Expressed as an equation, this would be written:
# 
# $$ \text{output} = \sqrt{3^2 + 4^2}$$
# 
# Compare this with the Python expression in the cell above, and make sure that you understand the correspondence between the Python expression and the written equation.

# <a id="Exercise1.3"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.3</b> <br> 
# Adapt the following code cell, which calculates and prints the sum of two numbers to work out:
# <ol>
#     <li>the difference between two numbers</li>
#     <li>the product of two numbers</li>
#     <li>the ratio of two numbers</li>
#     <li>one number to the power of another.</li>
# </ol>   
# 
# Remember that you can copy and paste cells using the relevant buttons on the toolbar. 
#     
# </div>
# 
# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.3)
# 

# In[5]:


# Exercise 1.3
result = 3 + 7
print("The sum of 3 and 7 is", result)


# ### Sequence - summary 
# 
# To recap then, in a sequence, all instructions are executed line by line. If one of the instructions causes an error, then the program will stop at the point that it encounters the error and provide an error message. 
# 
# While the ability to execute a sequence of instructions is useful, there are often times where we would like a program to selectively execute some instructions but not others. Selection is the subject of the next section. 
# 
# ***

# 
# <a id="Selection"></a> 
# ## 2. Selection
# 
# Imagine that you are developing software to solve a physics problem – where you need to work out the weight of a collection of objects. These may be items in a shopping basket for instance. You know that the weight in Newtons is equal to the total mass of the objects in kilograms multiplied by the acceleration due to gravity, at the surface of the Earth, in $\text{m s}^{−2}$. 
# 
# Here is a short program to do this – it’s a simple sequence of assignments and an output. (Use `View` | `Toggle Line Numbers` to see the line numbers if they are not already displayed.)

# In[6]:


totmass = 10.0   # total mass in kilograms
acc = 9.81       # acceleration in metres/(second squared)
weight = totmass * acc
print("Total weight:", weight, "Newtons")


# So in this case, the expression on line 3 calculates the total mass multiplied by the acceleration due to gravity and assigns the value to the variable `weight`. Notice that you do not need to use complete words for variable names, but it’s best to use a name that at least reminds you of what the variable represents. Note also that Python cares about capitalisation in variable names, so `weight`, `Weight` and `WEIGHT` would be three different variables. 
# 
# More generally, you should always choose the names of any variables carefully. Ideally, variable names should be self-explanatory and unambiguous. 
# 
# Also, as you saw in the last section, notice that in Python the multiplication operator is the asterisk (`*`), and that you can use it to multiply two variables together. 
# 
# Finally, notice the # symbol. On a given line, this indicates that whatever follows is a comment. The kernel ignores comments; they are simply notes made by the programmer to clarify any finer points about the working of the code. Comments come in very handy if the author (or someone else) needs to change the code later. In fact, different *components* of the program appear in different colours. It is usual for programming and editing software to include this type of *syntax highlighting* because it makes it easier for humans to read (unfortunately, the default highlighting colours are not always designed with colour-blind people in mind; fortunately, in many cases these defaults can be changed). 
# 
# In case you're wondering, any blank lines are simply ignored by Python. Like comments, you may put blank lines in where you wish, in order to help make your program more readable. Similarly, spaces within an expression are often disregarded. So line 3 above may be written as `weight = totmass * acc` (with spaces, as here), or without spaces as `weight=totmass*acc`.  Both of these will give the same result, although the spaces are preferred as they make the expression more readable.
# 
# It is time to be a little more precise with the weight calculation. You may know that the acceleration due to gravity at the surface of the Earth varies with latitude. As a first approximation of this variation, the acceleration can be set to $9.79\text{ m s}^{−2}$ for latitudes less than $45^\text{o}$, and to $9.82\text{ m s}^{−2}$ for latitudes of $45^\text{o}$ or more (these apply north and south of the equator). This then, is a very simple example of a calculation that is performed in different ways depending on some condition. In order to carry out the calculation properly, we need to select the appropriate route through the instructions, and so we use a process of *selection*.  
# 
# In this case we will need one more variable to store the latitude and some new instructions to handle both cases.
# In the following program, the steps that will be followed by the kernel depend on the value of this variable (here called `latitude`).
# 

# In[7]:


totmass = 10.0        # total mass in kilograms
latitude = 45.0       # latitude in degrees (N or S)
if latitude < 45.0:
  acc = 9.79          # acceleration in metres/(sec squared)
else:
  acc = 9.82          # acceleration in metres/(sec squared)
weight = totmass * acc
print("Total weight:", weight, "Newtons")


# Before moving onto the explanation, you should test this program out to ensure that it works as intended. In fact, much of the effort involved in developing new software is spent on testing. Good testing includes choosing enough inputs (preferably borderline cases) to exercise all possible conditions. In this case, you should at least test for latitudes of $44^\text{o}$ and $45^\text{o}$, the borderline where the acceleration due to gravity changes in this approximation. 

# <a id="Exercise2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1: Testing the <i>weight calculation</i> program</b> <br> 
# Change the latitude to $44^\text{o}$ and then $45^\text{o}$ and confirm that the weight is what you expect in each case.
#     
# </div>
# 
# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers2.1)

# Now looking at how the selection works, the process of selection uses the `if` statement.  In more detail, we have
# 
# `if (condition): 
#     (block 1) 
# else: 
#     (block 2)`
#     
# Such a structure chooses which block of code to execute as follows. The computer checks the condition after the `if` statement. If the condition is true, the computer executes the code in `block 1` (the indented instructions). If the condition is false, the computer executes the code in `block 2` instead.
# 
# For instance, if the latitude were $60^\text{o}$, the expression `latitude < 45` would be false and the `else` route would be executed. However, if the latitude were $30^\text{o}$, this expression would be true and the first route would be executed by the program. 
# 
# Note that the condition must be a *Boolean* expression that can only have two values: `True` or `False`. 
# 
# The indentation is needed to specify which instructions belong to which part. That is, `acc = 9.79` and `acc = 9.82` are indented to show that each of them belongs to a block of code. After the kernel has executed all the code in a selected block, the computer continues executing the non-indented instructions that follow the selection. 
# 
# Notice that there is a colon (`:`) at the end of the `if` and `else` lines. A missing colon and/or forgetting to indent the instructions will lead to error messages (try it).
# 
# Finally, returning to the physical problem, we can be even more precise about the way the acceleration due to gravity changes with latitude, and consider three ranges of latitude instead of two. In Python, several conditions can be chained as in the following example:

# In[8]:


totmass = 10.0  # total mass in kilograms 
latitude = 25.0  # latitude in degrees (N or S) 

if latitude < 30: 
    acc = 9.78  # acceleration in metres/(sec squared) 
elif latitude < 60: 
    acc = 9.81  # acceleration in metres/(sec squared) 
else: 
    acc = 9.83  # acceleration in metres/(sec squared) 
weight = totmass * acc 

print("Total weight:", weight, "Newtons")


# In plain English: 
# 
# - if the latitude is less than $30^\text{o}$, let the acceleration due to gravity be 
#   $9.78 \text{ m s}^{-2}$;
# - otherwise if (notice this is specified by the special statement `elif`, and not `else if`) it is less than $60^\text{o}$, let the acceleration due to gravity be $9.81 \text{ m s}^{-2}$; 
# 
# - otherwise let the acceleration due to gravity be $9.83 \text{ m s}^{-2}$.

# <a id="Exercise2.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.2: Testing the selection instruction</b> <br> 
# Test the code above with the four borderline cases: latitudes of $29^\text{o}$, $30^\text{o}$, $59^\text{o}$ and $60^\text{o}$.
#     
# </div>
# 
# You should attempt this exercise *before* looking at the [Exercise answers](#ExerciseAnswers2.2)

# Note that the order in which the conditions are written is crucial. This is because the kernel checks conditions sequentially from top to bottom, and on the first occasion that the test condition is true it will run the associated block of code before continuing with the code that follows the selection. Note also that the `else` block has no condition, so this last block is a catch-all in case no condition is true.

# <a id="Exercise2.3"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.3: Testing the selection instruction</b> <br> 
# Run the following code and test it by setting the value of the variable latitude to different values.
# Does the code provide correct results? Is there anything that needs changing?
#     
# </div>
# 
# You should attempt this exercise *before* looking at the [Exercise answers](#ExerciseAnswers2.3)

# In[9]:


# Exercise 2.3
totmass = 10.0          # total mass in kilograms
latitude = 25.0         # latitude in degrees (N or S)

if latitude < 60:
    acc = 9.81          # acceleration in metres/(sec squared)
elif latitude < 30:
    acc = 9.78          # acceleration in metres/(sec squared)
else:
    acc = 9.83          # acceleration in metres/(sec squared)
    
weight = totmass * acc

print("Total weight:", weight, "Newtons")


# The conditions that you have seen so far only use one criterion. What if you need to make a selection based on multiple criteria? As you might have guessed, Python allows you to do this. 
# 
# We noted above that conditional expressions are *Boolean* - they have values that are only either true or false, and it is useful here to note that Python calls these values `True` and `False` (note the capitalisation). We can combine two or more Boolean expressions using so-called logical operators: `and` and `or`. In fact, you can use the `and` operator to fix the version of the code that you considered at the end of the previous section. 
# 
# Inspect the following program and make sure you understand it. 

# In[10]:


totmass = 10.0      # total mass in kilograms 
latitude = 25.0     # latitude in degrees (N or S) 

if latitude < 60 and latitude >= 30: 
    acc = 9.81      # acceleration in metres/(sec squared) 
elif latitude < 30: 
    acc = 9.78      # acceleration in metres/(sec squared) 
else: 
    acc = 9.83      # acceleration in metres/(sec squared) 

weight = totmass * acc 

print("Total weight:", weight, "Newtons")


# Can you explain why this program, unlike the one in the previous section, provides correct results?
# 
# Because now the first `if` condition requires the latitude to be both smaller than $60^\text{o}$ and bigger than or equal to $30^\text{o}$. So, for angles smaller than $30^\text{o}$ this condition is not fulfilled and the program continues to the next `elif` condition.
# 
# There are a number of points to note:
# 
# Combine selections using the `and` operator if you require *both* selection conditions to be satisfied in order to execute the block.
# 
# Combine selections using the `or` operator if you require the block to be executed if *either* of the conditions is true. 
# 
# In fact, the `or` operator will be satisfied if either condition is satisfied and also if both conditions are satisfied.
# 
# Various comparison operators can be employed with numerical variables. For example, to check whether a variable is **greater than or equal to** a particular value, use `>=`. There are actually six comparison operators:
# 
# 1. `>` greater than
# 1. `<` less than
# 1. `>=` greater than or equal to
# 1. `<=` less than or equal to
# 1. `==` equal to
# 1. `!=` not equal to.
# 

# <a id="Exercise2.4"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.4: Testing the code and using comparison operators</b> <br> 
# <ol>
# <li> Test the code above with the four borderline cases: latitudes of $29^\text{o}$, $30^\text{o}$, $59^\text{o}$ and $60^\text{o}$. </li>
# <li> How would you change the code if you wanted the value of $9.78\text{ m s}^{−2}$ to be used when the latitude is exactly $30^\text{o}$ (with all other condutions being the same)? </li> 
# </ol>
# </div>
# 
# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers2.4)

# In[11]:


# Code for Exercise 2.4
totmass = 10.0      # total mass in kilograms 
latitude = 25.0     # latitude in degrees (N or S) 

if latitude < 60 and latitude >= 30: 
    acc = 9.81      # acceleration in metres/(sec squared) 
elif latitude < 30: 
    acc = 9.78      # acceleration in metres/(sec squared) 
else: 
    acc = 9.83      # acceleration in metres/(sec squared) 

weight = totmass * acc 

print("Total weight:", weight, "Newtons")


# ### Selection - summary
# ***
# In this section, you saw:
# - how to use `if` statement to control decision making within a simple program.
# - that combining `if` with `elif` and `else` statements can control more complex selection. 
# - that `and` and `or` statements can be used to combine multiple selection conditions.
# 
# This decision making ability is very useful as it allows to programs to alter how they operate depending on conditions that may only be known when the program is running. 
# 
# Now it is time to start learning about automation and how you can make a program peform a series of operations a certain number of times: a process called *iteration*.

# <a id="Iteration"></a> 
# ## 3. Iteration
# 
# Iteration is a very powerful concept as it allows you to repeat an operation a designated number of times. There are two main Python statements that produce iteration: `for` and `while`. Because the kernel repeatedly cycles through a block of code, you will often hear programmers refer to `for` loops and `while` loops as part of a computer program.  
# 
# We will introduce `for` and `while` below, before concluding with an activity that draws together much of what you have learned in this notebook.

# ### 3.1 For loops

# Imagine you have a selection of items for which you know the individual masses and you wish to calculate the total mass. As with any physical problem, the first stage is to set out the steps (the *algorithm*) that reaches the required solution. (At this point we aren't concerned about how we would program this in any particular programming language.)
# 
# 1. We have list of the masses of individual items.
# 
# 1. Let the total mass be zero.
# 
# 1. For each item in the list: add it to the total mass.
# 
# 1. Report the final total mass.
# 
# Step 3 is where the concept of iteration comes into play: we iterate through the list to process each item. 
# 
# This algorithm can be translated to Python as follows.

# In[12]:


list_of_items = [1.45, 2, 0.25, 4.4, 1.9]  # masses in kg 
totmass = 0 

for item in list_of_items: 
    print(item)
    totmass = totmass + item 
    
print("Total mass:", totmass, "kilograms")


# To explain what this Python code is doing, another type of object needs to be introduced: lists. A list a sequence of elements that can be numbers, strings or any other data type. They have the form:
# 
# `[element 1, element 2, element 3, .... element n]`
# 
# where elements are separated by commas and the entire list enclosed within square brackets.
# 
# In the example above, `list_of_items` is a list of numbers representing the masses of the different items. So the first line assigns the individual values to this list. This is then followed (line 2) by a statement that sets the total cumulative mass (`totmass`) to zero before we start adding the masses of the individual items. Such a step is called *initialisation* - it sets the initial value of `totmass`. Variables that have not been initialised properly are a common source of errors in computer programs.  
# 
# This is followed by the `for` loop itself. Generally this has the form:
# 
# `for (variable) in (list):
#     (block of code)`
# 
# In our example, the `for` loop goes through the given list `list_of_items`. It successively assigns each value of the list to the variable called `item` and executes the indented block of code, which in our case, adds the mass of the item to the total mass. This process is repeated until every element of the list has been used in this way. Note how the block of code in the loop explicitly uses the variable - this is usually the case (but not always, see the exercise below). 
# 
# As in the case of the `if` statement you used earlier, the line that defines the `for` loop must end in a semi-colon (`:`) and the block of code to be looped through must be indented. 
# 
# Of course, you don't have to call the list `list_of_items` or call the variable that steps through the list `item`. You could, for instance, define the list to be `b = [1.45,2.6,0.25,4.4,1.9]` and then write `for a in b:` where `a` is the variable that steps through the list `b`. You would then then change the next line to read `totmass = totmass + a`, and so on. However, as noted before, it helps to make your code much more understandable to other people if you use variable names that are meaningful and descriptive.
# 

# <a id="Exercise3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# The program in the following window is copied from the previous program. Adapt it to calculate and print the number of items in the list (i.e. there are 5 in the example above). 
#     
# First think about how to change the algorithm, and then translate the algorithm into Python code. 
#     
# Hint: you need to count the items in the list; their masses are irrelevant.
# </div>

# In[13]:


# Code for Exercise 3.1
items = [1.45, 2, 0.25, 4.4, 1.9]  # masses in kg 
totmass = 0 

for item in items: 
    print(item)
    totmass = totmass + item 
    
print("Total mass:", totmass, "kilograms")


# You should attempt this activity *before* looking at the [Exercise Answers](#ExerciseAnswers3.1)
# ***

# ### 3.2 While loops

# Another way for automating a series of instructions uses the `while` statement. Generally, it has the form:
# 
# `while (condition):
#     (block of code)`
# 
# As the name suggests, this will repeatedly execute the block of code as long as the condition is fulfilled (`True`). The expression for the condition must be Boolean (i.e. either `True` or `False`) similar to the examples with the `if` statement we saw previously. Typically the condition is a comparison operation and note that it is evaluated *before* the start of each iteration through the block of code. If the condition changes to `False` the kernel moves on to execute the code following the `while` loop.
# 
# Let us show you a first simple example that provides the multiplication table of a given number:

# In[14]:


number = 7          # Number we want the table of
counter = 1         # Counter

while counter < 10: # As long as i is less than 10.
    print(counter, "x", number, "=", (counter) * number)
    counter += 1    # Increment the Counter


# This example can be summarised as follows:
# 
# 1. First, the given number is set and the counter is initialised to one. 
# 
# 1. Then the loop starts and iterates the following steps:
# 
#     1. The value of the counter is compared to 10
# 
#     1. If the counter is below 10, the result of the multiplication of the counter by the given number is printed. Then the counter is increased
# 
#     1. If the counter is above or equal to 10, the loop is stopped
# 
# Note that in line 6 we have used the assignment `counter += 1`. This is just a shorter and more convenient way of writing `counter = counter + 1`.
# 
# `While` loops are very useful for performing repetitive operations. However caution is needed in using such loops! It is all too easy to accidentally define a condition that is always `True` - for instance in the previous example `while counter > 0` would run indefinitely as the counter is always positive and this would result in a never-ending, or infinite, loop. (Remember that you can stop programs that have got stuck like this using the `Kernel`,`Interrupt` menu item.)
# 
# Also note the importance of intialisation of `counter` in this example. If you had defined the variable `counter` previously (perhaps for some other loop), and it had a value of `10` or higher, then this `while` loop would not execute the code block at all.  
# 

# <a id="Exercise3.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.2: Euclid's Algorithm</b> <br> 
# As an example of a different use of the while loop, here is one of the oldest algorithms known, Euclid’s algorithm: used to find the greatest common divisor of two integers greater than zero, i.e. the greatest number that divides both without any remainder. For instance, the greatest common divisor of 3 and 7 is 1, and of 21 and 49 is 7. 
# This (for example) is needed to simplify fractions. Explaining the maths that makes the algorithm work is beyond the scope of this topic.
#     
# Below is a Python program which carries out Euclid's algorithm.
# </div>

# In[15]:


# Code for Exercise 3.2
# Euclid's greatest common divisor algorithm

# Initialisation of the two integers by the user
n = 7191 # First integer - can be changed by the user
m = 612  # Second integer - can be changed by the user

while (n != m):
    if (n > m):
        n = n - m
    else: 
        m = m - n
print("The greatest common divisor of the integers provided is", n)


# <div class="alert alert-block alert-info">
# 
# Based on what you have learned in this notebook, attempt the following:
# 
# 1. In a series of bullet points, explain what each of the lines in the program does.
#     
# 1. The algorithm will only work correctly if the two numbers input are greater than zero. How would you modify the program to prevent this issue by printing: 
#     "ERROR: The number entered is negative." ?

# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers3.2)

# ### Iteration - summary
# ***
# 
# In this section you have learned two ways to iterate an action for a certain number of times:
# 1. The **`for`** loop, which allows you to repeat an action on each element of a list.
# 1. The **`while`** loop, which repeats an action according to a logical condition that is evaluated before each iteration.
# 

# <a id="Exercise-Answers"></a> 
# ## Exercises - Answers
# 

# <a id="ExerciseAnswers1.3"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.3 - notes</b> <br> 
# </div>

# 1. The difference between two numbers

# In[16]:


result = 3 - 7
print("The difference between 3 and 7 is", result)


# 2. The product of two numbers

# In[17]:


result = 3 * 7
print("The product of 3 and 7 is", result)


# 3. The ratio of two numbers

# In[18]:


result = 3 / 7
print("The ratio of 3 divided by 7 is", result)


# 4. One number to the power of another

# In[19]:


result = 3 ** 7
print("3 to the power 7 is", result)


# [Back to Exercise 1.3](#Exercise1.3)

# <a id="ExerciseAnswers2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1 - answers</b> <br> 
# </div>

# 1. For an angle of $45^\text{o}$ and any angle above, the weight is 97.89999999999999 newtons
# 2. For an angle of $44^\text{o}$ and any angle below, the weight is 98.2 newtons
# 
# [Back to Exercise 2.1](#Exercise2.1)

# <a id="ExerciseAnswers2.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.2 - answers</b> <br> 
# </div>

# 1. For an angle of $29^\text{o}$ and any angle below, the weight is 97.8 newtons
# 2. For an angle of $30^\text{o}$, the weight is 98.1 newtons
# 3. For an angle of $59^\text{o}$, the weight is 98.1 newtons
# 4. For an angle of $60^\text{o}$ and any angle below, the weight is 98.3 newtons
# 
# [Back to Exercise 2.2](#Exercise2.2)

# <a id="ExerciseAnswers2.3"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.3 - answers</b> <br> 
# </div>

# The code provides incorrect results. If you set latitude to values smaller than $30^\text{o}$, it will not use the acceleration value of $9.78\text{ m s}^{−2}$. The reason is that the code will encounter the first if condition (`if latitude < 60`) and, because $30^\text{o}$ < $60^\text{o}$, it will set acc = 9.81. After this, the code will skip all the other if conditions and proceed to the line `weight = totmass * acc`.
# 
# One solution is to order the if conditions in the same way as the previous example. Another solution is explained in the next section.
# 
# [Back to Exercise 2.3](#Exercise2.3)

# <a id="ExerciseAnswers2.4"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.4 - answers</b> <br> 
# </div>

# 1. The cases give the following answers: 
#     1. For an angle of $29^\text{o}$ and any angle below, the weight is 97.8 newtons
#     1. For an angle of $30^\text{o}$, the weight is 98.1 newtons
#     1. For an angle of $59^\text{o}$, the weight is 98.1 newtons
#     1. For an angle of $60^\text{o}$ and any angle below, the weight is 98.3 newtons
# 
# 
# 2. You would change:
#     - line 5 - `if latitude < 60 and latitude >= 30` to `if latitude < 60 and latitude > 30`
#     - line 7 - `elif latitude < 30` to `elif latitude <= 30`. 
# 
# [Back to Exercise 2.4](#Exercise2.4)

# <a id="ExerciseAnswers3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1 - answers</b> <br> 
# </div>
# 
# As noted in the hint, you need only to count the items in the list since their masses are irrelevant.
# 
# The following code is an example of a working solution. It is likely that you will have something similar that reports that there are 5 items in the list.

# In[20]:


# Code for Exercise 3.1 (Answer)
items = [1.45, 2, 0.25, 4.4, 1.9]  # masses in kg 

nr_objects = 0 # This variable initialises the cumulative number of objects

for item in items: 
    nr_objects = nr_objects + 1 

print("Total number of items:", nr_objects)


# [Back to Exercise 3.1](#Exercise3.1)

# <a id="ExerciseAnswers3.2"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.2 - answers</b> <br> 
# </div>

# 1) The program executes the following steps:
# 
# 1. Initialisation: the two integers of which we want to know the greatest common divisor.
# 2. Loop: test whether `n` is not equal to `m`. If the condition is fulfilled, then execute the block of code for the loop, if not, then leave.
# 3. In the loop, 
#     - if `n` is greater than `m`, assign `n - m` to `n`
#     - if `n` is smaller than `m`, assign `m - n` to `m`
# 4. After the loop, print the value of `n` which is the greatest common divisor.
# 
# 2) In order to avoid the issue of initialisation of integers to negative values, one solution is to test if they are both positive and if so, perform the Euclid algorithm, and if either is negative, stop the program and print the error message.
# 
# The following cell provides an example solution.

# In[21]:


# Code for Exercise 3.2 (Answer)
# Euclid's greatest common divisor algorithm

# Initialisation of the two integers by the user
n = 7191 # First integer - can be changed by the user
m = 612  # Second integer - can be changed by the user

if n > 0 and m > 0:
    while (n != m):
        if (n > m):
            n = n - m
        else: 
            m = m - n
    print("The greatest common divisor of the integers provided is", n)
    
else:
    print("ERROR: The number entered is negative.")


# Try it with different cases to check that it works as you expect!
# 
# [Back to Exercise 3.2](#Exercise3.2)
