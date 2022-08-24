import os
import sys
import termios
import tty

from platform import system


format_prefix = "\033["
position_suffix = "H"

def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def getch_unix(char_width=1):
    '''get a fixed number of typed characters from the terminal. 
    Linux / Mac only'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(char_width)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getch_():
    if system().lower().startswith('win'):
        from msvcrt import getch
        return getch()
    else:
        return getch_unix()

def clear_screen():
    """
    Clears the terminal screen.
    """
    
    # Clear screen command as function of OS
    command = 'cls' if system().lower().startswith('win') else 'clear'

    # Action
    os.system(command)

def print_menu(menu: list[tuple[str,  callable]], title: str = ""):
    pointer = "\033[5m←\033[0m"
    pointer_pos = 1
    y_offset = 0
    
    clear_screen()

    if title != "":
        print(title)
        y_offset = 1

    # Print text menu
    for i in range(len(menu)):
        printAt(0, i+1+y_offset, menu[i][0])

    show_menu = True

    while show_menu:
        # Print pointer at current position
        printAt(len(menu[pointer_pos-1][0])+2, pointer_pos + y_offset, pointer)

        # Hide old pointer
        for i in range(len(menu)):
            if i == pointer_pos -1:
                continue
            printAt(len(menu[i][0])+1, i+1 + y_offset, "   ")

        # Get input
        command = ord(getch_())

        # 13 is the enter key
        if command == 13:
            clear_screen()
            show_menu = False
            return menu[pointer_pos-1][1]()

        # 65 is the up key
        elif command == 65:
            if pointer_pos == 1:
                continue
            else:
                pointer_pos -= 1

        # 66 is the down key
        elif command == 66:
            if pointer_pos == len(menu):
                continue
            else:
                pointer_pos += 1
                
        # 81 is the q key
        elif command == 81:
            print("\nExiting...")
            show_menu = False
            
        # 273 is the escape key
        elif command == 273:
            quit()

if __name__ == "__main__":
    print_menu([("Menu 1", lambda: print("Test"))])