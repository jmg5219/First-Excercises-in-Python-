start = int(input("Start From:"))#prompting user for the starting number
end = int(input("End on:"))#prompting user for the ending number

if start < end:#error handling in the event start number is greater than the end number
    i = start - 1 #intializing the incrementor
    while i < end:#while loop to print the numbers between start and end
        i += 1
        print(i)
elif start > end:
    print("Please restart the program and verify that start number is less than the end number")



