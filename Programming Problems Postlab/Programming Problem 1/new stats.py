# Mean Function
def mean(num):
    if not num:
        return None
    return sum(num) / len(num)

# Median Function
def median(num):
    if not num:
        return None
    num.sort()
    n = len(num)
    if n % 2 != 0:
        return num[n // 2]
    else:
        mid1 = num[(n // 2) - 1]
        mid2 = num[n // 2]
        return (mid1 + mid2) / 2

# Mode Function
from collections import Counter
def mode(num): 
    if not num:
        return None
    n = len(num)
    data = Counter(num)
    max_frequency = max(data.values())  # Find the maximum frequency

    # Get all elements with the maximum frequency
    modes = [key for key, value in data.items() if value == max_frequency]

    # If all numbers appear the same number of times, there is no mode
    if len(modes) == len(set(num)):
        return "No mode"
    return modes if len(modes) > 1 else modes[0]
