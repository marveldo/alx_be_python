number = int(input("Enter a number to see its multiplication table: "))
number_list = [1,2,3,4,5,6,7,8,9,10]
for range_number in number_list:
    multiple = number * range_number
    print(f"{number} * {range_number} = {multiple}")