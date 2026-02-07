import curses
import time
import random

MACHINE = [
    "╔═════════════════════════════════════════╗",
    "║       ******  SLOT MACHINE  ******      ║",
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



symbols = ["C", "L", "W", "D", "|", "7"]

machine_height = 11
machine_width = 43



def play_slot(stdscr):
    curses.curs_set(0)

    # center machine#
    scr_h, scr_w = stdscr.getmaxyx()  #screen height, screen width

    top = (scr_h - machine_height) // 2 - 4  #first row the machine art starts to print
    left = (scr_w - machine_width) // 2 - 2  #first column the machine art starts to print

    # draw machine frame
    for i, line in enumerate(MACHINE):
        stdscr.addstr(top + i, left, line)

    # instruction
    stdscr.addstr(top + 13, left, "      SPACE = spin          Q = quit")


    # handle input
    while True:
        ch = stdscr.getch()
        if ch == ord('q'):
            break

        delay = 0.1
        if ch == ord(' '):  # spin animation

            last_reel = [None, None, None]            
            for i in range(20):
                reels = []
                for j in range(3):
                    new_sym = random.choice(symbols)
                    while new_sym == last_reel[j]:
                        new_sym = random.choice(symbols)
                    reels.append(new_sym)

                last_reel = reels[:]

                stdscr.addstr(top + 4, left + 7, reels[0])
                stdscr.addstr(top + 4, left + 21, reels[1])
                stdscr.addstr(top + 4, left + 35, reels[2])
                stdscr.refresh()
                time.sleep(delay)
                delay *= 1.1

                curses.flushinp()
        stdscr.refresh()
    

curses.wrapper(play_slot)




def slot_cutscene():
    pass






def options():
    pass








    
    














