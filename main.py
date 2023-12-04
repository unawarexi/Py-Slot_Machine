import process

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "c": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "c": 3,
    "D": 2,
}

    
    

def main():
    balance = process.deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += process.spin(balance)
        
    print(f"you left with ${balance}")
        
    
    
main()