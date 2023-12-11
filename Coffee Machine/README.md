# Coffee Machine
This code represents a simple console-based coffee machine simulator. Users can interact with the program to make coffee selections, check the current resources, and simulate the purchase of drinks.

## Files
```bash
coffee_machine.py
```

This file contains the main code for the coffee machine simulation.

## Functions:
- clear_screen(): Clears the console screen.
- return_resources(): Returns the current state of available resources.
- format_resource(account): Formats and returns the resource information.
- process_coins(): Processes user input for coin insertion and returns the total amount.
- check_resources(choice): Checks if there are enough resources to make the selected coffee.
- status(number): Prints status messages based on the availability of resources.
- process_customer_request(choice): Processes the user's coffee request, handles payment, and updates resources accordingly.

Main Loop: The program runs an infinite loop, prompting the user to make a coffee selection or check the report. Users can choose from 'espresso', 'latte', 'cappuccino', or request a 'report' of the current resources.

The program calculates and returns change based on the user's input.

The file 'coffee_data.py' contains data about the coffee menu and available resources.

## Menu:
Contains information about different coffee types, including their ingredients and cost.

## Resources:
Represents the initial available resources, including water, milk, and coffee.

## How to Use:
- Run the coffee_machine.py file in a Python environment.
- Follow the prompts to select a coffee type or check the current resource report.
- Insert coins when prompted to make a purchase.


## Coffee Menu:
- Espresso: Water (50ml), Milk (0ml), Coffee (18g) - Cost: $1.5
- Latte: Water (200ml), Milk (150ml), Coffee (24g) - Cost: $2.5
- Cappuccino: Water (250ml), Milk (100ml), Coffee (24g) - Cost: $3.0

Initial Resources:
- Water: 300ml
- Milk: 200ml
- Coffee: 100g

Feel free to explore and modify the code to enhance or customize the coffee machine simulation.
## Dependencies
This game requires the following dependencies:

- Python 3.x

## Running the Game

```bash
python coffee_machine.py
```


*Enjoy your coffee! ☕*