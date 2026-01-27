import curses
import time
import random

MACHINE = [
    "╔═════════════════════════════════════════╗",
    "║            🎰 SLOT MACHINE 🎰          ║",
    "╠═════════════════════════════════════════╣",
    "║   ┌─────┐       ┌─────┐       ┌─────┐   ║",
    "║   │  C  │       │  W  │       │  S  │   ║",
    "║   └─────┘       └─────┘       └─────┘   ║",
    "╠═════════════════════════════════════════╣",
    "║    ┌────────────┐     ┌────────────┐    ║",
    "║    │    SPIN    │     │    QUIT    │    ║",
    "║    └────────────┘     └────────────┘    ║",
    "╚═════════════════════════════════════════╝",
]



SYMS = ["C", "L", "W", "S", "B", "D"]

machine_height = 11
machine_width = 43



def play_slot(stdscr):
    curses.curs_set(0)



    #center machine#
    scr_h, scr_w = stdscr.getmaxyx()  #screen height, screen width

    top = (scr_h - machine_height) // 2  #first row the machine art starts to print
    left = (scr_w - machine_width) // 2  #first column the machine art starts to print

    for i, line in enumerate(MACHINE):
        stdscr.addstr(top + i, left, line)


    stdscr.refresh()
    ch = stdscr.getch()


    curses.wrapper(play_slot)





def slot_cutscene():
    pass






def options():
    pass








    
    














