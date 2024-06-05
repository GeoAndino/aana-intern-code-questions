# Question 5
# Python-Specific Questions:
# Question: Write a Python function that takes a list of integers and returns a 
# new list containing only the even numbers from the input list.

# Code solution here

## create the function called onlyEvens which accepts an int array
def onlyEvens(arr) :

## initialize the empty evens array
    evens = []

## for loop goes through range of original array and checks if each element is even
    for value in range(len(arr)) :
        if ((value % 2) == 0) :
## append element to empty array
            evens.append(value)
    
    return evens
