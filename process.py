import main
import machine
import won




def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(" Enter the number of line to bet on (1-" + str(main.MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= main.MAX_LINES :
                break
            else:
                print("enter a valid number of line")
        else:
            print("please enter a number.")
    return lines

def get_bet():
     while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if main.MIN_BET <= amount <= main.MAX_BET :
                break
            else:
                print(f"amount must be between ${main.MIN_BET} - ${main.MAX_BET}.")
        else:
            print("please enter a number.")
     return amount
    

def spin(balance): 
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"you do not have sufficient amount, your current balance is: ${balance}")
        else:
            break
        
    
    print(f"you're betting ${bet} on {lines} lines. total bet is equal to: ${total_bet}")
    
    slots =  machine.get_slot_machine_spin(main.ROWS, main.COLS, main.symbol_count)
    machine.print_slot_machine(slots)
    
    winnings, winning_lines = won.check_winnings(slots, lines, bet, main.symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet