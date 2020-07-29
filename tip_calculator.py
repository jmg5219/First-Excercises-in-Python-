total_bill = float(input("Total bill amount? "))
service = input("Level of Service? ")
try:
    if service == 'good':
        tip_amount = (total_bill*0.20)
        total_amount = total_bill + tip_amount
    elif service == 'fair':
        tip_amount = (total_bill*0.15)
        total_amount = total_bill + tip_amount
    elif service == 'bad':
        tip_amount = (total_bill*0.10)
        total_amount = total_bill + tip_amount
    print("Tip amount: $%.2f" % (tip_amount))
    print("Total amount: $%.2f" % (total_amount))
except:
        print('Restart program and verify numeric input for total bill and good, fair or bad for service')
