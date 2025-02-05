"""
Utilities for project
"""

from collections import Counter
from datastat.models import ColorFrequency  # Replace with the actual path to your app
import random

# Function to generate random 4-digit binary number and convert to base 10
def generate_and_convert():
    # Generate a random 4-digit binary number
    binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))

    # Convert the binary number to decimal
    decimal_number = int(binary_number, 2)

    return binary_number, decimal_number





class GetStat:

    def __init__(self, dataset: dict):
        self.dataset = dataset

    def find_mean_color(self):
        """Function to find the most frequent (mean) color"""
        # Flatten the list of colors across all days
        all_colors = [
            color for day_colors in self.dataset.values() for color in day_colors
        ]

        # Count the occurrences of each color
        color_counts = Counter(all_colors)

        # Find the color with the maximum frequency
        mean_color = color_counts.most_common(1)[0]

        return mean_color

    def median_color(self):
        """Claculate the median color from the dataset"""
        even = False
        # Flatten the list of colors across all days
        all_colors = [
            color for day_colors in self.dataset.values() for color in day_colors
        ]

        color_counts = Counter(all_colors)

        # Sort the colors based on their frequency in ascending order
        sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])

        # Find the median index
        median_index = len(sorted_colors) // 2

        # If the number of unique colors is odd, return the middle color
        if len(sorted_colors) % 2 == 1:
            median_color = sorted_colors[median_index][0]

        else:
            # If even, return the average of the two middle colors (this part could vary depending on how you define the median for categorical data)
            median_color = f"{sorted_colors[median_index-1][0]} & {sorted_colors[median_index][0]} "
            even = True

        return median_color, even

    def color_variance(self):
        """Calculate the variance for the dataset"""
        # Flatten the list of colors across all days
        all_colors = [
            color for day_colors in self.dataset.values() for color in day_colors
        ]

        # Get the count of each color
        color_counts = Counter(all_colors)

        # Calculate the mean frequency of colors
        mean_frequency = sum(color_counts.values()) / len(color_counts)

        # Calculate the squared differences from the mean for each frequency
        squared_diffs = [
            (count - mean_frequency) ** 2 for count in color_counts.values()
        ]

        # Calculate the variance
        variance = sum(squared_diffs) / len(color_counts)

        return variance

    def save_color_frequencies(self):
        # Flatten the list of colors across all days
        all_colors = [color for day_colors in self.dataset.values() for color in day_colors]

        # Count the frequency of each color
        color_counts = Counter(all_colors)

        # Save the colors and their frequencies to the database
        for color, frequency in color_counts.items():
            # Create a new record for each color
            ColorFrequency.objects.create(color=color, frequency=frequency)
        return True

################################################################################

def recursive_linear_search(arr, target, index=0):
    # Base case: If index exceeds list length, target is not found
    if index >= len(arr):
        return -1
    # If element is found, return its index
    if arr[index] == target:
        return index
    # Recur for the next index
    return recursive_linear_search(arr, target, index + 1)
################################################################################
def fibonacci_sum(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    total = 0

    # Loop through the sequence and sum the numbers
    for _ in range(n):
        total += a
        a, b = b, a + b  # Update a and b to the next numbers in the sequence

    return total



