import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 10,
}

def get_slot_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

def print_slots(cols):
    for row in range(len(cols[0])):
        for col, column in enumerate(cols):
            if col != len(cols) - 1:
                print(column[row], end=' | ')  
            else: 
                print(column[row], end='')
            
        print()
        
        
'''This function is used to get the amount the user wants to deposit. The user will be asked to enter the amount they want to deposit. If the user enters a string, the following message will be displayed: "Please enter a valid amount." If the user enters a negative number or 0, the following message will be displayed: "Please enter a valid amount greater then 0."'''
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                '''If the user enters a negative number or 0, the following message will be displayed.'''
                print("Please enter a valid amount greater then 0.")
        else:
            '''If the user enters a string, the following message will be displayed.'''
            print("Please enter a valid number.")
    
    return amount

'''This function is used to get the number of lines the user wants to bet on. The user will be asked to enter the number of lines they want to bet on. If the user enters a string, the following message will be displayed: "Please enter a number." If the user enters a number that is not between 1 and 3, the following message will be displayed: "Please enter a valid number of lines."'''
def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines you wishes to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                '''If the user enters a number that is not between 1 and 3, the following message will be displayed.'''
                print("Please enter a valid number of lines.")
        else:
            '''If the user enters a string, the following message will be displayed.'''
            print("Please enter a number.")
    
    return lines

'''This function is used to get the amount the user wants to bet on each line. The user will be asked to enter the amount they want to bet on each line. If the user enters a string, the following message will be displayed: "Please enter a number." If the user enters a number that is not between 1 and 100, the following message will be displayed: "Please enter a valid bet amount between $1 - $100."'''
def get_bet_amount():
    while True:
        bet = input("Enter the amount you wish to bet on each line (1-100): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                '''If the user enters a number that is not between 1 and 100, the following message will be displayed.'''
                print(f"Please enter a valid bet amount between ${MIN_BET} - ${MAX_BET}.")
        else:
            '''If the user enters a string, the following message will be displayed.'''
            print("Please enter a number.")
    
    return bet

def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"You do not have enough balance to bet, your balance is ${balance}.")
        else:
            break
            
    print(f'Your are betting on {lines} lines with ${bet} on each line. Your total bet is: ${total_bet}')
    
       
main()

slots = get_slot_spins(ROWS, COLS, symbol_count)
print_slots(slots)