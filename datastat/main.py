"""
Main.py(where to run the project)

"""
import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Adds the current script's directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adds project root

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Initialize Django
django.setup()

#utilities used for the assessment
from datastat.utils import GetStat, recursive_linear_search, generate_and_convert, fibonacci_sum

# dictionary for all colors worn by staff on the corresponding day of the week
shirts_colors_worn_through_the_week = {
    "MONDAY": [
        "GREEN",
        "YELLOW",
        "GREEN",
        "BROWN",
        "BLUE",


        "PINK",
        "BLUE",
        "YELLOW",
        "ORANGE",
        "CREAM",
        "ORANGE",
        "RED",
        "WHITE",
        "BLUE",
        "WHITE",
        "BLUE",
        "BLUE",
        "BLUE",
        "GREEN",
    ],
    "TUESDAY": [
        "ASH",
        "BROWN",
        "GREEN",
        "BROWN",
        "BLUE",
        "BLUE",
        "BLUE",
        "PINK",
        "PINK",
        "ORANGE",
        "ORANGE",
        "RED",
        "WHITE",
        "BLUE",
        "WHITE",
        "WHITE",
        "BLUE",
        "BLUE",
        "BLUE",
    ],
    "WEDNESDAY": [
        "GREEN",
        "YELLOW",
        "GREEN",
        "BROWN",
        "BLUE",
        "PINK",
        "RED",
        "YELLOW",
        "ORANGE",
        "RED",
        "ORANGE",
        "RED",
        "BLUE",
        "BLUE",
        "WHITE",
        "BLUE",
        "BLUE",
        "WHITE",
        "WHITE",
    ],
    "THURSDAY": [
        "BLUE",
        "BLUE",
        "GREEN",
        "WHITE",
        "BLUE",
        "BROWN",
        "PINK",
        "YELLOW",
        "ORANGE",
        "CREAM",
        "ORANGE",
        "RED",
        "WHITE",
        "BLUE",
        "WHITE",
        "BLUE",
        "BLUE",
        "BLUE",
        "GREEN",
    ],
    "FRIDAY": [
        "GREEN",
        "WHITE",
        "GREEN",
        "BROWN",
        "BLUE",
        "BLUE",
        "BLACK",
        "WHITE",
        "ORANGE",
        "RED",
        "RED",
        "RED",
        "WHITE",
        "BLUE",
        "WHITE",
        "BLUE",
        "BLUE",
        "BLUE",
        "WHITE",
    ],
}

getstat = GetStat(shirts_colors_worn_through_the_week)

# ______________  1  _______________

# Find the most frequent color (mean color)
mean_color = getstat.find_mean_color()
print(f"The mean color for the week is: {mean_color[0]} with {mean_color[1]} occurrences.")


# _____________ 2 ______________
# The most commonly wore dress is also the mean color which is:
common_color = getstat.find_mean_color()
print(f"The most worn color throughout the week is: {common_color[0]} with {common_color[1]} occurrences.")


# _____________ 3 ______________
# Find the median color
median = getstat.median_color()
print(f"The median colors for the week is: {median[0]}" if median[1] else f"The median color for the week is: {median[0]}")


# _____________ 4 ______________
# Calculate the variance of the colors
variance = getstat.color_variance()
print(f"The variance of the color frequencies is: {variance}")


# _____________ 5 ______________
# Save the data in the Postgresql db
saved_in_db = getstat.save_color_frequencies()

if saved_in_db:
    print("Successful")

# _____________ 6 ______________
# Recursive Linear Search (For Unsorted List)
numbers = [10, 25, 30, 5, 40, 15]
target = int(input("Enter a number to search: "))

result = recursive_linear_search(numbers, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")



# _____________ 7 ______________
# binary to decimal equivalent
binary, decimal = generate_and_convert()
print(f"Generated Binary Number: {binary}")
print(f"Decimal Equivalent: {decimal}")


# _____________ 8 ______________
# fibonnacci calculator
result = fibonacci_sum(50)
print(f"The sum of the first 50 Fibonacci numbers is: {result}")









