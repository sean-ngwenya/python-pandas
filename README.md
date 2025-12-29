# Python Pandas – Data Manipulation & Analysis

## Overview
This repository documents my structured learning and practical application of **Pandas** for data manipulation and analysis using Python.

It focuses on **core data analysis workflows** such as DataFrame creation, filtering, aggregation, handling missing data, and file input/output.  
The project is organized using a **professional, modular structure** aligned with real-world data analysis practices.

---

## Learning Objectives
By completing this repository, I demonstrate the ability to:

- Create and manipulate Pandas DataFrames
- Perform exploratory data analysis (EDA)
- Filter, sort, and transform tabular data
- Apply `groupby` operations and aggregations
- Handle missing data effectively
- Read from and write to CSV files
- Structure Python data projects professionally

---

## Repository Structure

python-pandas/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│ ├── raw/
│ │ └── people_data.csv
│ └── processed/
│
├── src/
│ ├── init.py
│ ├── create_dataframes.py
│ ├── basic_operations.py
│ ├── data_manipulation.py
│ ├── groupby_aggregation.py
│ ├── missing_data.py
│ ├── file_io.py
│
└── main.py

## Key Topics Covered

### 1. Creating DataFrames
- From Python dictionaries
- From NumPy arrays

### 2. Basic Operations
- Inspecting data with `info()`, `head()`, and `tail()`
- Descriptive statistics using `describe()`
- Column and row selection
- Conditional filtering

### 3. Data Manipulation
- Adding and modifying columns
- Dropping columns
- Sorting by one or multiple columns

### 4. GroupBy & Aggregation
- Aggregating numerical data by categories
- Applying multiple aggregation functions
- Frequency counts

### 5. Handling Missing Data
- Detecting missing values
- Dropping missing data
- Filling missing values with constants and statistical measures

### 6. File Input & Output
- Writing DataFrames to CSV files
- Reading CSV files into Pandas


## How to Run the Project

### 1. Clone the Repository

git clone https://github.com/sean-ngwenya/python-pandas.git

cd python-pandas

2. Create a Virtual Environment (Recommended)
bash

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate 
     # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Project
bash

python main.py


## Technologies Used
Python 3

Pandas

NumPy

Git & GitHub

Linux (Pop!_OS)

VS Code

Learning Context
This repository is part of my broader roadmap in:

Python Fundamentals

Scientific Computing

Data Analysis

Artificial Intelligence Foundations

It complements my NumPy and Python Fundamentals repositories.

License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this code with attribution.

Author
Sean Craig Ngwena
AI & ML Science Student

GitHub: https://github.com/sean-ngwenya
