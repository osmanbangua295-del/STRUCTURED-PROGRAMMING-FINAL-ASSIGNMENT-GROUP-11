import csv
import os

FILE_NAME = "salone_kiosk_ledger.csv"

def init_db():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Customer/Item", "Amount", "Type"])

def add_transaction(customer_name, amount, trans_type):
    """Appends a new customer transaction to the CSV file."""
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([customer_name, amount, trans_type])

def get_all_transactions():
    """Reads all transactions from the CSV file and returns them as a list of dictionaries."""
    transactions = []
    if not os.path.exists(FILE_NAME):
        return transactions
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Ensure the amount is treated as a number for calculations
                row['Amount'] = float(row['Amount'])
                transactions.append(row)
            except ValueError:
                pass # Skip any corrupted rows
    return transactions