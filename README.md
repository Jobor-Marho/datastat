# Project README

## Overview

This project is a Python-based application that performs various statistical operations on a dataset of shirt colors worn by staff throughout the week. It also includes additional utilities such as recursive linear search, binary to decimal conversion, and Fibonacci sequence calculation. The project is built using Django for database operations and includes a set of utility functions to handle the data.

## Features

1. **Mean Color Calculation**: Finds the most frequently worn color (mean color) throughout the week.
2. **Median Color Calculation**: Determines the median color from the dataset.
3. **Color Variance Calculation**: Calculates the variance of the color frequencies.
4. **Database Integration**: Saves the color frequencies in a PostgreSQL database.
5. **Recursive Linear Search**: Performs a recursive linear search on an unsorted list of numbers.
6. **Binary to Decimal Conversion**: Generates a random binary number and converts it to its decimal equivalent.
7. **Fibonacci Sequence Calculation**: Calculates the sum of the first 50 Fibonacci numbers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure you have PostgreSQL installed and running.
   - Create a `.env` file in the project root and add your database configuration:
     ```plaintext
     DATABASE_URL=postgres://username:password@localhost:5432/dbname
     ```
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the application**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Running the Script

To run the main script that performs all the operations:

```bash
python your_script_name.py
```

### Example Output

```plaintext
The mean color for the week is: BLUE with 45 occurrences.

The most worn color throughout the week is: BLUE with 45 occurrences.

The median color for the week is: BLUE

The variance of the color frequencies is: 12.34

Successful
Enter a number to search: 25

Number found at index 1

Generated Binary Number: 101010

Decimal Equivalent: 42

The sum of the first 50 Fibonacci numbers is: