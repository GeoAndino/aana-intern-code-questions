# Question 3
### Algorithmic Questions (Pseudocode):
**Question:** Write a function that takes a sorted array of integers and a target sum. The function should find two numbers in the array that add up to the target sum and return their indices. Assume there is exactly one solution.
```
# Write pseudocode solution here
```
## the function is created called targetSum
def targetSum(arr, sum):
## the count for the inner loop
    count = 1
## the empty array that will be returned
    array = []

    for i in range(len(arr)) :
        for j in range (count, len(arr)) :
## the conditional that checks if the elements sum to the target
            if ((i + j) == sum) :
                array.append(i)
                array.append(j)
                i = len(arr)
        count++
## want to return an array which holds the indexes of the two elements that add to target sum
    return array

