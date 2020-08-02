total_bill = float(input("Total bill amount? "))#prompt user for bill amount
service = input("Level of Service? ")#prompt user for service level
split = int(input("Split how many ways?  "))#prompt user for split
try:#error handling for different levels of service
    if service == 'good':
        tip_amount = (total_bill*0.20)
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount/split
    elif service == 'fair':
        tip_amount = (total_bill*0.15)
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount/split
    elif service == 'bad':
        tip_amount = (total_bill*0.10)
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount/split
    print("Tip amount: $%.2f" % (tip_amount))
    print("Total amount: $%.2f" % (total_amount))
    print("Amount per person: $%.2f" % (amount_per_person))
except:
        print('Restart program and verify numeric input for total bill and good, fair or bad for service')
