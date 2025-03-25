import json
from datetime import datetime
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.categories = {
            'income': ['Salary', 'Freelance', 'Investments'],
            'expenses': ['Food', 'Transportation', 'Rent', 'Utilities', 'Entertainment', 'Shopping']
        }
        self.filename = 'finance_data.json'
        self.load_data()

    def add_transaction(self, amount, category, transaction_type, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if transaction_type not in ['income', 'expenses']:
            raise ValueError("Transaction type must be 'income' or 'expenses'")
        
        if category not in self.categories[transaction_type]:
            raise ValueError(f"Invalid category for {transaction_type}")
        
        transaction = {
            'amount': float(amount),
            'category': category,
            'type': transaction_type,
            'date': date
        }
        
        self.transactions.append(transaction)
        self.save_data()
        print(f"Transaction added: {transaction}")

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            self.transactions = []

    def get_balance(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expenses')
        return income - expenses

    def generate_expense_report(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expenses':
                category = transaction['category']
                amount = transaction['amount']
                expense_categories[category] = expense_categories.get(category, 0) + amount
        return expense_categories

    def visualize_expenses(self):
        expense_report = self.generate_expense_report()
        
        if not expense_report:
            print("No expense data to visualize.")
            return
        
        plt.figure(figsize=(10, 7))
        plt.pie(
            expense_report.values(), 
            labels=expense_report.keys(), 
            autopct='%1.1f%%'
        )
        plt.title('Expense Breakdown')
        plt.axis('equal')
        plt.savefig('expense_breakdown.png')
        plt.close()

    def monthly_summary(self):
        monthly_data = {}
        for transaction in self.transactions:
            month = datetime.strptime(transaction['date'], "%Y-%m-%d").strftime("%Y-%m")
            
            if month not in monthly_data:
                monthly_data[month] = {'income': 0, 'expenses': 0}
            
            if transaction['type'] == 'income':
                monthly_data[month]['income'] += transaction['amount']
            else:
                monthly_data[month]['expenses'] += transaction['amount']
        
        return monthly_data

def main():
    tracker = FinanceTracker()
    
    tracker.add_transaction(5000, 'Salary', 'income', '2024-01-15')
    tracker.add_transaction(1500, 'Rent', 'expenses', '2024-01-20')
    tracker.add_transaction(300, 'Food', 'expenses', '2024-01-25')
    tracker.add_transaction(200, 'Transportation', 'expenses', '2024-01-28')
    
    print(f"Current Balance: ${tracker.get_balance():.2f}")
    
    tracker.visualize_expenses()
    
    monthly_summary = tracker.monthly_summary()
    for month, data in monthly_summary.items():
        print(f"\nMonth: {month}")
        print(f"Income: ${data['income']:.2f}")
        print(f"Expenses: ${data['expenses']:.2f}")
        print(f"Net: ${data['income'] - data['expenses']:.2f}")

if __name__ == "__main__":
    main()
