def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input('Enter the item you want to add: ')
            shopping_list.append(item)
            print(f'{item} Added !')
        elif choice == '2':
            item_to_remove = input('Enter the Item to remove: ')
            if item_to_remove in shopping_list :
                shopping_list.remove(item_to_remove)
                print(f'{item_to_remove} Removed !')
            else :
                print('The item youre searching for is not in the shopping click 1 to add it')
        elif choice == '3':
            for item in shopping_list :
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()