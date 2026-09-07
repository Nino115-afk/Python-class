#---MENU---
#add product
#show product
#update product
#delete product
#Exit

product = []


def add_product(product):
    print("\n---Add product---")
    try:
        size = int(input("Enter size of product: "))
        if size <= 0:
            print("Please enter a positive number!")
            return
        
        for x in range(0, size):
            input_product = input(f"Input product [{x+1}]: ")
            product.append(input_product)
        
        print("Product added successfully!")
    except ValueError:
        print("Please enter a valid number!")


def show_product(product):
    print("\n---Show product---")
    if len(product) == 0:
        print("No product found!")
    else:
        for x in range(0, len(product)):
            print(f"{x+1}. {product[x]}")


def update_product(product):
    print("\n---Update product---")
    
    if len(product) == 0:
        print("No product found!")
    else:
        for x in range(len(product)):
            print(f"{x+1}. {product[x]}")
        
        try:
            number = int(input("\nInput number: "))
            
            if number < 1 or number > len(product):
                print("Invalid number!")
            else:
                update_product_name = input("Input new product: ")
                product[number - 1] = update_product_name
                print("Product updated successfully!")
        except ValueError:
            print("Please enter a valid number!")


def delete_product(product):
    print("\n---Delete product---")
    
    if len(product) == 0:
        print("No product found!")
    else:
        for x in range(len(product)):
            print(f"{x+1}. {product[x]}")
        
        try:
            number = int(input("\nInput number: "))
            
            if number < 1 or number > len(product):
                print("Invalid number!")
            else:
                product.pop(number - 1)
                print("Product deleted successfully!")
        except ValueError:
            print("Please enter a valid number!")


def main():
    while True:
        print("\n===Menu===")
        print("1. Add product")
        print("2. Show product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_product(product)
        elif choice == "2":
            show_product(product)
        elif choice == "3":
            update_product(product)
        elif choice == "4":
            delete_product(product)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()