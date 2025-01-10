'''
Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. 
The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the 
number that appears most frequently in the list. Define these functions in a module named stats.py. 
Also include a function named mean, which computes the average of a set of numbers. Each function expects a 
list of numbers as an argument and returns a single number
'''
from stats import mean, median, mode

# Ask User for Input
user_input = input("Enter a list of numbers separated by commas: ")

# Split User Input
data = [float(x) for x in user_input.split(',')]

# Display Results
print("Mean:", mean(data))
print("Median:", median(data))
