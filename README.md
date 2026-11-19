# 🌍 World Happiness Report – Data Analysis and Visualization

## Sub-title
A Python-based data analysis project that explores the World Happiness Report dataset, handles missing and duplicate values, performs statistical analysis, and creates visualizations using Pandas, Matplotlib, and Seaborn.

## 1. Features

- **Explore Data**
  - Display first 5 rows.
  - Display last 5 rows.
  - Display dataset information.
  - Display data types.

- **Clear Data**
  - Check missing values.
  - Delete missing data.
  - Fill missing values.
  - Check duplicate records.

- **Perform Data Analysis**
  - Calculate the sum of Happiness Rank.
  - Calculate the sum of Happiness Score.
  - Find the maximum Family value.
  - Calculate average GDP per Capita.
  - Calculate average Health (Life Expectancy).

- **Data Visualization**
  - Bar Chart
  - Pie Chart
  - Line Chart
  - Scatter Plot
  - Histogram

- **Data Analysis Report**
  - Total Happiness Rank.
  - Total Happiness Score.
  - Maximum Family.
  - Average GDP per Capita.
  - Average Life Expectancy.
  - Total Countries.
  - Total Columns.
  - Missing Values.
  - Duplicate Records.

## 2. Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## 3. Concepts Used

- Data Analysis
- Data Visualization
- Data Cleaning
- Python Conditional Statements (`if-elif-else`)
- User Input (`input()`)
- Type Conversion (`int()`)
- Pandas DataFrame
- DataFrame Operations
- Statistical Functions (`sum()`, `mean()`, `max()`)
- Missing Value Handling (`isnull()`, `dropna()`, `fillna()`)
- Duplicate Value Detection (`duplicated()`)
- Data Visualization using Matplotlib

## 4. How to Use

1. Run the Python program.
2. Enter your dataset filename (Example: `happiness.csv`).
3. Select an option from the main menu.

**Main Menu:**

1. Explore Data
2. Clear Data
3. Perform Data Analysis
4. Visualization Data
5. Data Analysis Report

4. Select the required operation.
5. View the results in the terminal.
6. For visualization, select a chart type to display the graph.

## 5. Installation

**Step 1: Install Python**

Download Python from:

https://www.python.org/downloads/

**Step 2: Install Required Libraries**

Open the terminal and execute:

```bash
pip install pandas matplotlib seaborn
```

**Step 3: Download the Dataset**

Keep your `happiness.csv` dataset in the same folder as your Python file.

**Step 4: Create Python File**

Save your source code as:

```text
world_happiness.py
```

**Step 5: Run the Program**

```bash
python world_happiness.py
```

## 6. Example Output

**Main Menu**

```text
==========================================
Welcome TO The World Happiness Report
==========================================

1. Explore Data
2. Clear Data
3. Perform Data Analysis
4. Visualization Data
5. Data Analysis Report

Enter The Number Between (1-5) :- 5

Load Data
Enter The File Name Eg(happiness.csv):- happiness.csv

Data Loaded Successfully!
```

**Data Analysis Report**

```text
========== HAPPINESS ANALYSIS ==========

Total Happiness Rank       : 12246
Total Happiness Score      : 763.25
Maximum Family             : 1.87
Average GDP Per Capita     : 0.85
Average Life Expectancy    : 0.63

========== DATASET INFORMATION ==========

Total Countries            : 158
Total Columns              : 12
Missing Values             : 0
Duplicate Records          : 0
```

*Note: The above values are illustrative. Actual results depend on your CSV dataset.*

**Visualization Examples**

- Bar Chart – Happiness Score vs Happiness Rank.
- Pie Chart – Happiness Score distribution.
- Line Chart – Happiness Score trends.
- Scatter Plot – Relationship between Happiness Score and Happiness Rank.
- Histogram – Distribution of Happiness Scores.

## 7. Project Structure

```text

│
├── README.md
│
├── happiness.csv
│
└── main.py
```

## 8. Author
Dev Thakkar
