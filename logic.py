TAX_RATE_ESTIMATE = 0.05  # 5% City Council Tax

def validate_input(name, amount_raw):
    """Validates user input before sending it to the database."""
    if not name.strip():
        return False, "Please enter a valid Customer or Item name."
    try:
        amount = float(amount_raw)
        if amount <= 0:
            return False, "Amount must be greater than zero."
        return True, amount
    except ValueError:
        return False, "Please enter a valid numeric amount."

def calculate_totals(transactions):
    """Loops through the database records to calculate financial totals."""
    total_sales = 0.0
    total_expenses = 0.0

    for t in transactions:
        if t['Type'] == 'Sale':
            total_sales += t['Amount']
        elif t['Type'] == 'Expense':
            total_expenses += t['Amount']

    gross_profit = total_sales - total_expenses
    tax = total_sales * TAX_RATE_ESTIMATE if gross_profit > 0 else 0.0
    net_profit = gross_profit - tax

    return total_sales, total_expenses, gross_profit, tax, net_profit

def evaluate_health(net_profit):
    """Uses decision structures to evaluate business performance."""
    if net_profit > 1000:
        return "EXCELLENT (Safe to restock/expand)"
    elif net_profit > 0:
        return "STABLE (Profitable, monitor expenses)"
    elif net_profit == 0:
        return "BREAK-EVEN (Working just to pay expenses)"
    else:
        return "CRITICAL LOSS (Cut expenses immediately)"