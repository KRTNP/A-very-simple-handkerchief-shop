# Luxury Handkerchief Shop

Welcome to the Luxury Handkerchief Shop repository! This Python script allows users to design and purchase custom handkerchiefs based on their preferences or select from existing designs.

## Features

- **Custom Handkerchief Design**: Users can create handkerchiefs by specifying material, design, and colors.
- **Existing Design Selection**: Users can choose from a list of pre-designed handkerchiefs.
- **Interactive Console**: The program interacts with users through a command-line interface.
- **Order Summary**: After designing, the program displays the order summary and the total cost.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Program

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/luxury-handkerchief-shop.git
    cd luxury-handkerchief-shop
    ```

2. **Run the script**:
    ```sh
    python handkerchief_shop.py
    ```

### Usage

When you run the program, you'll be greeted with the main menu:

```
Welcome to the Luxury Handkerchief Shop
Choose a service:

1. Design a custom handkerchief
2. Design a handkerchief based on existing designs
3. Exit
```

#### Custom Handkerchief Design

- Select option `1` to start designing a custom handkerchief.
- Follow the prompts to enter your preferences, including name, gender, age, habits, hobbies, favorite things, material, and colors.
- A base price of 500 is set, with an additional 100 for each color beyond the first two.

#### Existing Handkerchief Design

- Select option `2` to choose from existing designs.
- Follow the prompts to select a design, material, and colors.
- A base price of 300 is set, with an additional 100 for each color beyond the first two.

#### Exiting the Program

- Select option `3` to exit. If you have placed any orders, the program will display a summary of your orders and the total cost.

### Example

```
Welcome to the Luxury Handkerchief Shop
Choose a service:

Design a custom handkerchief
Design a handkerchief based on existing designs
Exit
Enter the number corresponding to your choice: 1
Designing a custom handkerchief based on your preferences.
Enter your name: John Doe
Enter your gender: Male
Enter your age: 30
Enter your habits: Reading
Enter your hobbies: Hiking
Enter your favorite things: Books
Choose a material for your handkerchief:
Silk
Linen
...
Enter the number corresponding to your choice: 3
Enter a color for your handkerchief (type 'done' when finished): Blue
Enter a color for your handkerchief (type 'done' when finished): White
Enter a color for your handkerchief (type 'done' when finished): done
Handkerchief designed: Custom Design for John Doe - $500.00
Do you want to design more handkerchiefs? (y/n): n
Thank you for shopping with us!

Your orders:

Product 1:
Design: Custom Design for John Doe, Material: Cotton, Price: $500.00
Colors: Blue, White
Total: $500.00
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, feel free to reach out.

Happy designing!
