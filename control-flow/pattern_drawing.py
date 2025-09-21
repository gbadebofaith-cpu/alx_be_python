size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    j = 0
    while j < size:
        print("*", end=" ")  # print star on same line
        j += 1
    print()  # move to the next line after finishing a row
    i += 1
