import random
import locale

class Handkerchief:
    def __init__(self, material, design, colors, price):
        self.material = material
        self.design = design
        self.colors = colors
        self.price = price

def design_custom_handkerchief():
    
    print("Designing a custom handkerchief based on your preferences.")
    customer_name = input("Enter your name: ")
    customer_gender = input("Enter your gender: ")
    customer_age = input("Enter your age: ")
    customer_habits = input("Enter your habits: ")
    customer_hobbies = input("Enter your hobbies: ")
    customer_favorite_things = input("Enter your favorite things: ")

    print("Choose a material for your handkerchief:")
    materials = [
        "Silk",
        "Linen",
        "Cotton",
        "Cashmere",
        "Chiffon",
        "Satin",
        "Velvet",
        "Wool",
        "Bamboo",
        "Microfiber"
    ]
    for i, material in enumerate(materials, 1):
        print(f"{i}. {material}")
        
    material_choice = int(input("Enter the number corresponding to your choice: "))
    material = materials[material_choice - 1]

    design = f"Custom Design for {customer_name}"
    colors = []
    
    while True:
        color = input("Enter a color for your handkerchief (type 'done' when finished): ")
        if color.lower() == 'done':
            break
        else:
            colors.append(color)

    price = 500 + (len(colors) - 2) * 100

    return Handkerchief(material, design, colors, price)

def design_existing_handkerchief():
    
    print("Designing a handkerchief based on existing designs.")
    designs = [
        "Floral",
        "Stripes",
        "Paisley",
        "Geometric",
        "Polka Dots",
        "Plaid",
        "Checkered",
        "Herringbone",
        "Tartan",
        "Damask"
    ]
    
    for i, design in enumerate(designs, 1):
        print(f"{i}. {design}")
        
    design_choice = int(input("Enter the number corresponding to the design you want: "))
    design = designs[design_choice - 1]

    print("Choose a material for your handkerchief:")
    materials = [
        "Silk",
        "Linen",
        "Cotton",
        "Cashmere",
        "Chiffon",
        "Satin",
        "Velvet",
        "Wool",
        "Bamboo",
        "Microfiber"
    ]
    
    for i, material in enumerate(materials, 1):
        print(f"{i}. {material}")
        
    material_choice = int(input("Enter the number corresponding to your choice: "))
    material = materials[material_choice - 1]
    colors = []
    for i in range(2):
        color = input(f"Enter color {i+1}: ")
        colors.append(color)

    additional_colors = input("Do you want to add more colors? (y/n): ")
    while additional_colors.lower() == 'y':
        color = input("Enter additional color: ")
        colors.append(color)
        additional_colors = input("Do you want to add more colors? (y/n): ")

    price = 300 + (len(colors) - 2) * 100

    return Handkerchief(material, design, colors, price)

def main():
    locale.setlocale(locale.LC_ALL, '')

    orders = []

    while True:
        print("Welcome to the Luxury Handkerchief Shop")
        print("Choose a service:")
        print("1. Design a custom handkerchief")
        print("2. Design a handkerchief based on existing designs")
        print("3. Exit")

        try:
            service_choice = int(input("Enter the number corresponding to your choice: "))
            if service_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice.")
        except ValueError as e:
            print("Error:", e)
            continue

        if service_choice == 1:
            item = design_custom_handkerchief()
        elif service_choice == 2:
            item = design_existing_handkerchief()
        
        if service_choice != 3:
            orders.append(item)
        
            print(f"Handkerchief designed: {item.design} - {locale.currency(item.price, grouping=True)}")
            order_more = input("Do you want to design more handkerchiefs? (y/n): ")
            
            if order_more.lower() != 'y':
                print(' ')
                print("Thank you for shopping with us!")
                print(' ')
                total_cost = sum(item.price for item in orders)
                print("Your orders:")
                print(' ')
                for i, item in enumerate(orders, 1):
                    print(f"Product {i}:")
                    print(f"Design: {item.design}, Material: {item.material}, Price: {locale.currency(item.price, grouping=True)}")
                    if isinstance(item.colors, list):
                        print("Colors:", ", ".join(item.colors))
                    else:
                        print("Colors:", item.colors)
                    print('-' * 30)
                print(f"Total: {locale.currency(total_cost, grouping=True)}")
                break
        else:
            if orders:
                print(' ')
                print("Thank you for shopping with us!")
                print(' ')
                total_cost = sum(item.price for item in orders)
                print("Your orders:")
                print(' ')
                for i, item in enumerate(orders, 1):
                    print(f"Product {i}:")
                    print(f"Design: {item.design}, Material: {item.material}, Price: {locale.currency(item.price, grouping=True)}")
                    if isinstance(item.colors, list):
                        print("Colors:", ", ".join(item.colors))
                    else:
                        print("Colors:", item.colors)
                    print('-' * 30)
                print(f"Total: {locale.currency(total_cost, grouping=True)}")
            else:
                print("Goodbye!")
            break

if __name__ == "__main__":
    main()
