# Personal Finance Tracker

## Overview
Personal Finance Tracker is a Python-based application that helps you manage and analyze your financial transactions with ease. Track your income, expenses, and gain insights into your spending habits.

## Features
- Add income and expense transactions
- Categorize financial transactions
- Generate expense reports
- Visualize expense breakdown
- Calculate current balance
- Monthly financial summary
- Data persistence with JSON storage

## Prerequisites
- Python 3.7+
- matplotlib
- json (standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aditya19200/personal-finance-tracker.git
cd personal-finance-tracker
```

2. Install required dependencies:
```bash
pip install matplotlib
```

## Usage

### Running the Application
```bash
python finance_tracker.py
```



## Example
```python
tracker = FinanceTracker()
tracker.add_transaction(5000, 'Salary', 'income')
tracker.add_transaction(1500, 'Rent', 'expenses')
tracker.visualize_expenses()
```

## Project Structure
- `finance_tracker.py`: Main application logic
- `finance_data.json`: Stores transaction data
- `expense_breakdown.png`: Expense visualization




Project Link: [https://github.com/yourusername/personal-finance-tracker](https://github.com/aditya19200/personal-finance-tracker)

#screenshot 
![expense_breakdown](https://github.com/user-attachments/assets/ac857aa3-d863-44f9-964e-3496295bd678)

