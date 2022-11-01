# Python Exercice 1

***
**Title:** Loading a file

**Author:** Tom Webley
***
Have you ever wondered how to load a file in Python?

It's pretty easy!
```
    with open("file.txt") as f:
    contents = f.read()
```

As long as the python file is saved in the same folder as 'file.txt', this code will load the entire contents of the file and dump it into the variable 'contents'.

(programmers usually call a 'folder' a 'directory')

This uses a new sort of block, called a 'with block'!

It's mostly used for loading from a file in the way I have done it here. smile

You will often want to read a file line by line, then make a list. you can do this using .splitlines()...

```
    with open(filename) as f:
        contents = f.read().splitlines()
```

So, I will now upload some folders and set you a challenge (should you choose to accept it)!!!

cf files:

- magic8.py
- response_list.txt

I have uploaded a python file which has a function for loading lines from a file plus a data file for you to load.

The data file contains all 20 responses used on the original magic 8 ball!!!

If you save these two in the same directory and run the python file, it should output the following...

['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

Your challenge is this: Use this code to create your very own magic 8 ball program!

Hopefully this will be lots of fun, and we can have a look at each others programs in the next online chat. smile


