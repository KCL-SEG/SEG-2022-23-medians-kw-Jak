"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)

median_index = length // 2
if length % 2 == 1:
    median = numbers[median_index]
else:
    median = (numbers[median_index] + numbers[median_index-1])/2

print(median)
