"""
Module: word_count

This script reads text from a file, counts the frequency of distinct words,
and outputs the results to the console and a file.
"""

import sys
import time


def read_file(file_path):
    """Reads the content of the specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except (IOError, OSError) as error:
        print(f"Error reading file {file_path}: {error}")
        sys.exit(1)


def count_words(text):
    """Counts the frequency of each word in the text."""
    word_counts = {}
    words = text.lower().split()

    for word in words:
        # Remove non-alphabetic characters
        clean_word = ''.join(
            char for char in word if char.isalpha()
        )
        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    return word_counts


def save_results(word_counts, elapsed_time):
    """Saves the word count results and elapsed time to a file."""
    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        for word, count in word_counts.items():
            file.write(f"{word}: {count}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")


def main():
    """Main function to execute the word counting process."""
    if len(sys.argv) != 2:
        print("Usage: python word_count.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    text = read_file(file_path)
    word_counts = count_words(text)
    elapsed_time = time.time() - start_time

    for word, count in word_counts.items():
        print(f"{word}: {count}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")

    save_results(word_counts, elapsed_time)


if __name__ == "__main__":
    main()
