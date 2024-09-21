pattern = int(input("Enter the size of the pattern: "))
current_pattern = 0

while current_pattern < pattern :

    for number in range(0,pattern):
        print("*", end="")
    print("\n")
    
    current_pattern += 1