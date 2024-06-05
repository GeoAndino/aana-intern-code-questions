# Question 6
# Python-Specific Questions:
# Question: Implement a Python function that takes a string and 
# returns a dictionary where the keys are the unique words in the string, 
# and the values are the frequencies of each word.

# Code solution here

## create function called wordFrequencies which takes in a srtring

def wordFrequencies(word) :
## creates an empty dictionary and splits the string into words based on white space
    uniqueDic = {}
    words = word.split()
## use for loop to iterate through the list of words and determine whether to increase the count by 1 or set it to default value of 1
    for w in words: 
        if ((uniqueDic.get(w, 0)) != 0) :
            uniqueDic[w] += 1
        elif () :
            uniqueDic.setdefault(w, 1)
    return uniqueDic