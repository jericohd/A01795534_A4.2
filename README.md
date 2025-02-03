# 📊 Compute Statistics

## Description
`compute_statistics.py` is a Python script designed to read numerical data from a file, calculate basic statistics such as **mean**, **median**, **mode**, **variance**, and **standard deviation**, and display the results both in the console and in a results file named `StatisticsResults.txt`.

## 🚀 Features
- Calculation of basic statistics:
  - Mean
  - Median
  - Mode
  - Variance
  - Standard Deviation
- Error handling for invalid data.
- Execution time logging.

## 🗂️ Project Structure
```
├── compute_statistics.py
├── StatisticsResults.txt  # Automatically generated file
└── data/
    └── fileWithData.txt    # Input data file
```

## ⚙️ Requirements
- **Python 3.x**

## 🚀 How to Run
1. Ensure that `compute_statistics.py` and your data file (e.g., `fileWithData.txt`) are in the same directory.
2. Run the following command:

```bash
python3 compute_statistics.py data/fileWithData.txt
```

## 📥 Input Format
- A text file containing numbers separated by spaces or new lines.

**Example of `fileWithData.txt`:**
```
45 67 89 23 45
12 56 78
90 34
```

## 📤 Output Format
A file named `StatisticsResults.txt` will be generated with the following format:

```
Mean: 56.78
Median: 45.0
Mode: 45
Variance: 540.12
Standard Deviation: 23.24
Elapsed Time: 0.0032 seconds
```

## 🚩 Error Handling
- Invalid data will be ignored, and a message will be displayed in the console:

```
Invalid data ignored in fileWithData.txt: ABC
```

## 💻 Best Practices
- Compliance with **PEP-8** coding standards.
- Use of specific exceptions for error handling.
- Function documentation using docstrings.

## ✍️ Author
- **Jerico Hernández**

