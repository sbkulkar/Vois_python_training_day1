fees = {}

def pay_fee(roll, amount):
    fees[roll] = amount

def fee_status(roll):
    return "Paid" if fees.get(roll, 0) >= 50000 else "Pending"
