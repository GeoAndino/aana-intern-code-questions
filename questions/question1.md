# Question 1
### Algorithmic Questions (Pseudocode):

**Question:** Write a function that takes an array of integers and returns the sum of the two largest numbers in the array.
```
# Write pseudocode solution here
```
## create a function called "sumTwoLargest" which takes in an array and returns an int value

def sumTwoLargest(arr):

## check if the array is at least of length 2
    if (len(arr) < 2) {
        raise Exception("The list needs at least two numbers")
    }

## assigns the first two values of the array as the two largest numbers to sum
    one = arr[0]
    two = arr[1]
    
## sorts the numbers where one is the larger number and two is the second largest
    if(two > one) :
        temp = one
        one = two 
        two = temp

## a for loop iterating through the array
    for i in range (2, len(arr)) :
## check if the element is larger than both numbers
        if (i > one) :
            two = one
            one = i
## check if just larger than the second largest
        elif (i > two) :
            two = i
## returns the sum of the two numbers
    return one + two    



