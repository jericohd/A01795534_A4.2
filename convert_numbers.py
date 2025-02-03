"""
Module: convert_numbers

This script reads numbers from a file, converts them to binary and hexadecimal, 
and outputs the results to the console and a file.
"""

import sys
import time


def read_numbers(file_path):
    """Reads numbers from the specified file."""
    numbers = []
    invalid_entries = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for item in line.strip().split():
                    try:
                        number = int(item)
                        numbers.append(number)
                    except ValueError:
                        invalid_entries.append(f"Invalid data ignored in {file_path}: {item}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except (IOError, OSError) as error:
        print(f"Error reading file {file_path}: {error}")
        sys.exit(1)

    # Display invalid data errors
    for error in invalid_entries:
        print(error)

    return numbers


def decimal_to_binary(n):
    """Converts a decimal number to binary using basic algorithm."""
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def decimal_to_hexadecimal(n):
    """Converts a decimal number to hexadecimal using basic algorithm."""
    if n == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    while n > 0:
        hexadecimal = hex_digits[n % 16] + hexadecimal
        n //= 16
    return hexadecimal


def convert_numbers(numbers):
    """Converts numbers to binary and hexadecimal."""
    conversions = [
        (num, decimal_to_binary(num), decimal_to_hexadecimal(num))
        for num in numbers
    ]
    return conversions


def save_results(conversions, elapsed_time):
    """Saves the conversion results to a file."""
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
        for num, binary, hexa in conversions:
            file.write(f"Decimal: {num}, Binary: {binary}, Hexadecimal: {hexa}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")


def main():
    """Main function to execute the conversion process."""
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers(file_path)
    if not numbers:
        print("No valid numbers found.")
        sys.exit(1)

    conversions = convert_numbers(numbers)
    elapsed_time = time.time() - start_time

    for num, binary, hexa in conversions:
        print(f"Decimal: {num}, Binary: {binary}, Hexadecimal: {hexa}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")

    save_results(conversions, elapsed_time)


if __name__ == "__main__":
    main()
