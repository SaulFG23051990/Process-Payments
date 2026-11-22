def  process_payments(balance: float, payments: list[float] )-> tuple[int, float]:
    """
    Input: Takes in a list of payments and the amount of money in the account
    Process: it will check if there is anything to pay and enough to pay it
    Output: it will output the successfull payments and remaining balance
    """
    index = 0 
    successful_payments=0 
    while index < len(payments) and balance > 0:
        current_payment = payments[index]
        
        # Condition 1: If the amount is zero or negative, skip it
        if current_payment <= 0:
            index += 1
            continue
            
        # Condition 2: If the payment exceeds the available balance, skip it
        if current_payment > balance:
            index += 1
            continue
            
        # Condition 3: Otherwise, process the payment
        balance -= current_payment
        successful_payments += 1
        index += 1  # Always move to the next item
        
    # The return must be completely OUTSIDE the while loop block
    return (successful_payments, balance)
        