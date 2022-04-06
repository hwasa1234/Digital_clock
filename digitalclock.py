import time
import font as font


def now_date():
    return time.strftime("%H:%M:%S")#display the time in Hour,minutes and second


def clear():
    from os import system, name
    # windows terminal
    if name == 'nt':
        _ = system('cls')

    # mac,linux(OS: Posix)
    else:
        _ = system('clear')

try:
 while True: #create a loop
    date_str = now_date()
    font.draw_font(date_str)# call the function in the module font
    time.sleep(1)  # delay one second
    clear()


except:
    KeyboardInterrupt
finally:
    print("HEHEHEHE HAVE A GOOD DAY ;)")

