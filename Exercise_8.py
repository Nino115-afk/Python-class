#---MENU---
#add data
#show data
#update data
#delete data
#Exit

data = []

while True:
    print("===Menu===")
    print("1. Add data")
    print("2. Show data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("/n---Add Data---")
        amount = (int(input("Enter amount of data: ")))
        for x in range(0, amount):
            input_data = input(f"Input data [{x+1}] : ")
            data.append(input_data)
        
        print("✓ Data added successfully!")
    
    elif choice == "2":
        print("\n--- SHOW DATA ---")
        
        if len(data) == 0:
            print("No data found!")
        else:
            for x in range(0, len(data)):
                print(data[x])

    elif choice == "3":
        print("\n--- UPDATE DATA ---")
        
        if len(data) == 0:
            print("No data found!")
        else:
            for x in range(len(data)):
                print(f"{x+1}. {data[x]}")
            
            try:
                number = int(input("\nInput number : "))
                
                if number < 1 or number > len(data):
                    print("Invalid number!")
                else:
                    update_data = input("Input new data : ")
                    data[number - 1] = update_data
                    print("Data updated successfully!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("/n--- DELETE DATA ---")

        if len(data) == 0:
            print("No data found!")
        else:
            for x in range(len(data)):
                print(f"{x+1}. {data[x]}")

            try:
                delete_input = input("\nInput data that you want to delete : ")
                
                if delete_input in data:
                    data.remove(delete_input)
                    print(f"✓ {delete_input} deleted successfully!")
                else:
                    print("Data not found!")
            except:
                print("Invalid input!")
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option! Please choose 1-5.")
 