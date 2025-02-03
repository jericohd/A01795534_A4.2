"""
Module: compute_statistics

This script reads numbers from files, performs basic statistical calculations
(mean, median, mode, variance, and standard deviation), and outputs the
results to the console and a file.
"""

import sys
import time


def read_numbers(file_path):
    """Reads numbers from the specified file."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for item in line.strip().split():
                    try:
                        number = float(item)
                        numbers.append(number)
                    except ValueError:
                        print(f"Invalid data ignored in {file_path}: {item}")
    except (FileNotFoundError, IOError, OSError) as error:
        print(f"Error reading file {file_path}: {error}")
        sys.exit(1)

    return numbers


def calculate_statistics(numbers):
    """Calculates basic statistics: mean, median, mode, variance, and standard deviation."""
    if not numbers:
        return None

    n = len(numbers)
    mean = sum(numbers) / n

    sorted_numbers = sorted(numbers)
    median = (sorted_numbers[n // 2] if n % 2 != 0
              else (sorted_numbers[(n - 1) // 2] + sorted_numbers[n // 2]) / 2)

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get)

    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return mean, median, mode, variance, std_dev


def save_results(statistics, elapsed_time):
    """Saves statistical results and elapsed time to a file."""
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
        mean, median, mode, variance, std_dev = statistics
        file.write(f"Mean: {mean}\n")
        file.write(f"Median: {median}\n")
        file.write(f"Mode: {mode}\n")
        file.write(f"Variance: {variance}\n")
        file.write(f"Standard Deviation: {std_dev}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")


def main():
    """Main function to read data, calculate statistics, and display results."""
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers(file_path)
    if not numbers:
        print("No valid numbers found.")
        sys.exit(1)

    statistics = calculate_statistics(numbers)
    elapsed_time = time.time() - start_time

    mean, median, mode, variance, std_dev = statistics
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")

    save_results(statistics, elapsed_time)


if __name__ == "__main__":
    main()
