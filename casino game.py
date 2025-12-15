import random
import time
import os

# █ ▓ ▒ ░

# ━ ┏ ┓ ┗ ┛ ┳ ┻ ┣ ┫ ╋ ┃ ━ ┏━┓ ┗━┛  (potential characters you could use to decorate,
#                                                               you could add more)


YELLOW  = "\033[33m"
BLUE    = "\033[34m"
RED     = "\033[31m"
GREEN   = "\033[32m"

RESET   = "\033[0m"


def main():
    clear_screen()

    opening_cutscene()

    
















def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



def opening_cutscene():

    title_art = """




               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒         ▒▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
               ▓▓                       ▒▒  ▒▒           ▒▒                          ▒▒             ▒▒ ▒▒       ▒▒       ▓▓          ▓▓
               ▓▓                      ▒▒    ▒▒          ▒▒                          ▒▒             ▒▒  ▒▒      ▒▒       ▓▓          ▓▓
               ▓▓                     ▒▒      ▒▒         ▒▒                          ▒▒             ▒▒   ▒▒     ▒▒       ▓▓          ▓▓
               ▓▓                    ▒▒        ▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒              ▒▒             ▒▒    ▒▒    ▒▒       ▓▓          ▓▓
               ▓▓                   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                   ▒▒              ▒▒             ▒▒     ▒▒   ▒▒       ▓▓          ▓▓
               ▓▓                  ▒▒            ▒▒                  ▒▒              ▒▒             ▒▒      ▒▒  ▒▒       ▓▓          ▓▓
               ▓▓                  ▒▒            ▒▒                  ▒▒              ▒▒             ▒▒       ▒▒ ▒▒       ▓▓          ▓▓
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▒▒            ▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒         ▒▒▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓







                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              ▒▒▒▒              ▒▒▒               ▒▒▒        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                             ▓▓            ▓▓             ▒▒  ▒▒             ▒▒ ▒             ▒ ▒▒        ▓▓
                             ▓▓            ▓▓            ▒▒    ▒▒            ▒▒  ▒           ▒  ▒▒        ▓▓
                             ▓▓            ▓▓           ▒▒      ▒▒           ▒▒   ▒         ▒   ▒▒        ▓▓
                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▒▒        ▒▒          ▒▒    ▒       ▒    ▒▒        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                           ▓▓         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒         ▒▒     ▒     ▒     ▒▒        ▓▓
                                           ▓▓        ▒▒            ▒▒        ▒▒      ▒   ▒      ▒▒        ▓▓
                                           ▓▓        ▒▒            ▒▒        ▒▒       ▒ ▒       ▒▒        ▓▓
                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▒▒            ▒▒        ▒▒        ▒        ▒▒        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓





"""

    lst = title_art.split("\n")


    total_line = 36
    gap_line = 23
    top_printed = 6
    bottom_printed = -7

    for i in range(9):
        clear_screen()
        print('\n'.join(lst[:top_printed + i]))
        print("\n" * (gap_line - ((i + 1) * 2)))
        print('\n'.join(lst[bottom_printed - i:]))
        time.sleep(0.18)








    










main()