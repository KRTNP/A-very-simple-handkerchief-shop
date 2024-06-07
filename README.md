# Luxury Handkerchief Shop

Welcome to the Luxury Handkerchief Shop repository! This Python script allows users to design and purchase custom handkerchiefs based on their preferences or select from existing designs.

## Overview

The script provides an interactive console application where users can design custom handkerchiefs by choosing materials, designs, and colors, or they can select from pre-existing designs. The script calculates the price based on the user's choices and displays an order summary at the end.

## Code Explanation

### Class Definition

```python
class Handkerchief:
    def __init__(self, material, design, colors, price):
        self.material = material
        self.design = design
        self.colors = colors
        self.price = price
```

The `Handkerchief` class is a blueprint for creating handkerchief objects. Each handkerchief has:

- `material`: The fabric used.
- `design`: The design or pattern.
- `colors`: A list of colors used.
- `price`: The price of the handkerchief.

### Custom Handkerchief Design Function

```python
def design_custom_handkerchief():
    ...
    return Handkerchief(material, design, colors, price)
```

This function interacts with the user to design a custom handkerchief. It does the following:

1. Collects user information (name, gender, age, habits, hobbies, favorite things).
2. Displays a list of materials for the user to choose from.
3. Prompts the user to input colors until they type 'done'.
4. Calculates the price based on the number of colors.
5. Returns a `Handkerchief` object with the specified attributes.

### Existing Handkerchief Design Function

```python
def design_existing_handkerchief():
    ...
    return Handkerchief(material, design, colors, price)
```

This function allows the user to select a handkerchief from pre-existing designs. It performs the following steps:

1. Displays a list of pre-defined designs.
2. Displays a list of materials for the user to choose from.
3. Prompts the user to input at least two colors and optionally add more.
4. Calculates the price based on the number of colors.
5. Returns a `Handkerchief` object with the specified attributes.

### Main Function

```python
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
                break
        else:
            break

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
            print("Colors:", ", ".join(item.colors))
            print('-' * 30)
        print(f"Total: {locale.currency(total_cost, grouping=True)}")
    else:
        print("Goodbye!")
```

The `main()` function is the entry point of the application. It initializes locale settings and manages the main loop of the application. Here are the steps:

1. **Locale Setting**: Sets the locale for currency formatting.
2. **Order List**: Initializes an empty list to store handkerchief orders.
3. **Main Menu**: Displays the main menu and prompts the user to choose a service.
4. **Service Choice Handling**: Based on the user's choice, it calls either `design_custom_handkerchief()` or `design_existing_handkerchief()` and adds the result to the orders list.
5. **Order Confirmation**: If the user wants to design more handkerchiefs, the loop continues. Otherwise, it breaks out of the loop.
6. **Order Summary**: If there are any orders, it prints a thank you message, the order details, and the total cost. If there are no orders, it simply says goodbye.

### Example Interaction

When you run the program, you'll be greeted with the main menu:

```
Welcome to the Luxury Handkerchief Shop
Choose a service:
1. Design a custom handkerchief
2. Design a handkerchief based on existing designs
3. Exit
```

#### Designing a Custom Handkerchief

```
Enter the number corresponding to your choice: 1
Designing a custom handkerchief based on your preferences.
Enter your name: John Doe
Enter your gender: Male
Enter your age: 30
Enter your habits: Reading
Enter your hobbies: Hiking
Enter your favorite things: Books
Choose a material for your handkerchief:
1. Silk
2. Linen
...
Enter the number corresponding to your choice: 3
Enter a color for your handkerchief (type 'done' when finished): Blue
Enter a color for your handkerchief (type 'done' when finished): White
Enter a color for your handkerchief (type 'done' when finished): done
Handkerchief designed: Custom Design for John Doe - $500.00
Do you want to design more handkerchiefs? (y/n): n
```

After designing, the program will display the order summary and total cost:

```
Thank you for shopping with us!

Your orders:

Product 1:
Design: Custom Design for John Doe, Material: Cotton, Price: $500.00
Colors: Blue, White
------------------------------
Total: $500.00
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, feel free to reach out.

Happy designing!
