try:#error handling for input
    total_bill = float(input("Total bill amount? "))#prompting user for a total bill amount
    service = input("Level of Service? ")#prompting user for level of service
    if service == 'good':#various tip levels
        tip_amount = (total_bill*0.20)
        total_amount = total_bill + tip_amount
    elif service == 'fair':
        tip_amount = (total_bill*0.15)
        total_amount = total_bill + tip_amount
    elif service == 'bad':
        tip_amount = (total_bill*0.10)
        total_amount = total_bill + tip_amount
    print("Tip amount: $%.2f" % (tip_amount))#printing tip amount
    print("Total amount: $%.2f" % (total_amount))#printing total amount
except:
        print('Restart program and verify numeric input for total bill and good, fair or bad for service')
