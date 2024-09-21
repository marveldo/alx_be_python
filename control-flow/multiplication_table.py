number = int(input("Enter a number to see its multiplication table: "))

for range_number in range(1,11):
    multiple = number * range_number
    print(f"{number} * {range_number} = {multiple}")