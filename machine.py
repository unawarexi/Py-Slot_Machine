import random
import main


def get_slot_machine_spin(rows, cols, symbols):
    # Create the grid and add a symbol to each slot.
    all_symbols = []
    for symbol, main.symbol_count in symbols.items():
        for _ in range(main.symbol_count):
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





def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],  end = "|")
            else:
                print(column[row], end = "")
                #"|" is for not print last col
        print()