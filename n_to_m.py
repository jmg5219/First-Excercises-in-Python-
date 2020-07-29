start = int(input("Start From:"))
end = int(input("End on:"))

if start < end:
    i = start - 1 
    while i < end:
        i += 1
        print(i)
elif start > end:
    print("Please restart the program and verify that start number is less than the end number")



