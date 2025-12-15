import os 
import time
import sys
import requests
import keyboard
from art import text2art
from urllib.parse import urlparse
from colorama import init, Fore, Style

init(autoreset=True)

def clear():  # clear Function
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    try:
        # // Loading Bar
        for i in range(0, 101):
            bar = "#" * (i // 2)
            sys.stdout.write(f"\r[{bar:<50}] {i}%")
            sys.stdout.flush()
            time.sleep(0.05)  # delay Loading
        clear()
    except KeyboardInterrupt:
        print("\nLoading interrupted. Exiting...")
        loading2()
        sys.exit(0)

def loading2():
    try:
        # // Loading Bar 2
        for i in range(0, 101):
            bar = "#" * (i // 2)
            sys.stdout.write(f"\r[{bar:<50}] {i}%")
            sys.stdout.flush()
            time.sleep(0.05)  # delay Loading
            clear()
        clear()
        time.sleep(2) 
        print("\nSee You later my sweet :)")
        time.sleep(1)
        clear()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)


 
# // Reset auto color
def Reset():
    print(Style.RESET_ALL, end='')

# --- added helper functions to safely handle Ctrl+C and Ctrl+X ---
def _ctrl_x_pressed():
    try:
        return keyboard.is_pressed("ctrl+x")
    except Exception:
        # keyboard may raise if not permitted; treat as not pressed
        return False

# // Detection Keyboard Input (ctrl + x)
def safe_input(prompt):
    # quick non-blocking check for Ctrl+X before asking input
    if _ctrl_x_pressed():
        print("\nCTRL+X detected. Exiting.")
        loading2()
        sys.exit(0)
    try:
        return input(prompt)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nKeyboard interrupt (Ctrl+C) detected.")
        while True:
            try:
                resp = input("Exit program? (y/n): ").strip().lower()
            except KeyboardInterrupt:
                # if user keeps pressing Ctrl+C, keep looping until valid answer
                continue
            if resp in ("y", "yes"):
                loading2()
                sys.exit(0)
            elif resp in ("n", "no"):
                clear()
                return ""
            else:
                print("Please answer y or n.")
# --- end added helpers ---

def command():
    print("\n JUNKMODE COMMAND LIST ")   

# Cool Loading 
def art():
    try:
        clear()
        print(Fore.LIGHTGREEN_EX + (text2art("WELLCOME")))
        time.sleep(1)
        clear()
        print(text2art( "KALLAJA", font='block', chr_ignore=True))
        time.sleep(1)
        loading()
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + (text2art(" KALLAJA HACKING VERSION ", font='small')))
        time.sleep(2)
        clear()
        print(Fore.LIGHTRED_EX + text2art("CREATE BY : huxstar", font='small'))
        time.sleep(2)
        clear()
        print("Starting Program")
        time.sleep(2)
        clear()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)

# // Menu
def menu1():
    print(Fore.LIGHTGREEN_EX + (text2art("KALLAJA", font='small')))
    


# // Loading system \\
art()

while True: 
    menu1()
    a = safe_input("Menu~# :").strip()
    Reset()
    if a == "1":
        clear()
        time.sleep(1)
        while True:
            usr = safe_input("Type 'mode -t': ").strip()
            if usr == "":
                continue
            elif usr == "mode -t":
                while True:
                    a = safe_input("Tools~!# ").strip()
                    if a == "sh -t":
                        clear()
                        time.sleep(2)
                        print(Fore.LIGHTYELLOW_EX + "2.HTTP CHEKING HEADER")
                        Reset()
                    elif a == "2" or a == "HTTP CHEKING HEADER":
                        clear()
                        #feature HTTP CHEKING HEADER
                        while True:
                            link = safe_input("Paste URL here > ").strip()
                            if not link:
                                continue
                            elif link == "exit":
                                break
                            parsed = urlparse(link)
                            if parsed.scheme.lower() not in ("http", "https") or not parsed.netloc:
                                print("Your input is not Valid,  Paste URL from your browsure (Only can Start with http:// or https://)")
                                continue
                            try:

                                # ------------------------------------------------------------------------------#
                                # You Can Deleted This Code if you want to using this tools without Loading     #
                                clear()                                                                         #
                                print(Fore.LIGHTBLUE_EX+ (text2art("Wait For a second")))                       #
                                time.sleep(2)                                                                   #
                                clear()                                                                         #
                                print(Fore.LIGHTGREEN_EX + (text2art("Tools by : kibong")))                     #
                                print(Fore.LIGHTRED_EX + (text2art("Version Tools: hx-00-01-25", font='smal'))) #
                                #------------------------------------------------------------------------------ #
                                r = requests.get(link, timeout=5)
                                print(r.text)
                                print("\n ")
                                print("\n")
                                print(Fore.LIGHTGREEN_EX + f"Succesfull gett request from {link}")
                                break
                                # If failed to get requsts from link

                            except requests.RequestException as e:
                                print(Fore.RED + f"Failed to connect from {link}", e) 
                                break
                    elif a == "clear":
                        clear()
                    elif a == "exit" or a == "ex":
                        clear()
                        break
                    elif a.startswith ("print "):
                        p = a[6:]
                        if p.strip():
                            print(text2art(p, font='small', chr_ignore=True))
                        else:
                            pass
                    else:
                        print("Invalid tools Type sh -t for showing tools")    
            elif usr == "exit":
                time.sleep(0.10)
                clear()
                break
            else:
                print(Fore.RED + "Invalid input, Please Try valid input")
    elif a == "":
        clear()
        continue
    elif a == "3" or a == "exit" or a == "ex":
        while True:
            # // Give user Quetion Before Exit
            choice = safe_input("Are you sure Want to exit this program? (Yes) or (No): ").strip().lower()
            if choice in ("yes", "y"):
                sys.exit(0)
            elif choice in ("no", "n"):
                clear()
                break
    elif a == "clear" or a == "cls":
        clear()
    else:
        clear() 
        print( a + " Unexpected Command")
        time.sleep(2)
        clear()