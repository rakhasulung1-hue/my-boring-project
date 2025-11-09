import time
import os
from art import text2art

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def delay_animation1():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", 
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
                 "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        clear()
        print("Loading Kalaja...")
        print(animation[i])
        time.sleep(0.30)
    clear()

def delay_animation2():
    animation = ["[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", 
                 "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for a in range(len(animation)):
        clear()
        print("Initializing Kalaja...")
        print(animation[a])
        time.sleep(0.15)
    clear()

def kallaja_info():
    print(" -v  kalaja Version, For showing Kallaja Version"
          "\n -h  kalaja Help, For showing Kallaja Help"
          "\n -c  kalaja Creator, For showing Kallaja Creator"
          "\n exit/quit  To Exit Kalaja"
          "\n Type exit, quit, ex, or q to exit Kalaja."
          "\n Type call to Open Callculator."
          "\n Type print"
          "\n Type print-s for more Better than print"
          "\n Type kallaja For Showing Something cool i think")

def thred_art():
    print(text2art("Kalaja", font="block", chr_ignore=True))
    print(text2art("by Rakha Projects - Version 0.0.1.25", font="small", chr_ignore=True))

delay_animation1()
#delay_animation2()



while True:
    usr_input = input("kallaja~# ").strip()
    if usr_input == "kallaja -v":
        print("Kalaja Version: 0.0.1.25")
    elif usr_input == "kallaja -h":
        kallaja_info()
    elif usr_input == "kallaja -c": # Creator Info Command
        print("Kalaja Creator: Rakha Projects")
    elif usr_input in ["exit", "quit", "ex", "q"]:
        clear()
        time.sleep(1)
        print("Exiting Kalaja...")
        time.sleep(3)
        clear()
        break
    elif usr_input == "clear": #clear Screen Command
        clear()
    elif usr_input == "call": # Kalkulator Fitur
        print("Opening Callculator...")
        time.sleep(2)
        clear()
        print("Type -h for Information about Callculator.")

        # helper to read a number with validation; returns None if user wants to cancel
        def get_number(prompt):
            while True:
                s = input(prompt).strip()
                if s in ["exit", "quit", "ex", "q"]:
                    return None
                try:
                    return float(s)
                except ValueError:
                    print("Invalid number. Type 'exit' to cancel or try again.")

        while True:
            kalku = input("Callculator~# ").strip()
            if kalku == "-h":
                print("""Welcome to This Future Callculator.
Ketik + Untuk Penjumlahan
Ketik - Untuk Pengurangan
Ketik * Untuk Perkalian
Ketik / Untuk Pembagian
Ketik % Untuk Modulus
Type exit, quit, ex, or q to exit Callculator.""")
            elif kalku == "+":                                      # Penjumlahan Fitur
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Cancelled operation.")
                    continue
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Cancelled operation.")
                    continue
                print(f"Result: {num1 + num2}")
            elif kalku == "-":                                # Pengurangan Fitur       
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Cancelled operation.")
                    continue
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Cancelled operation.")
                    continue
                print(f"Result: {num1 - num2}")
            elif kalku == "*":                              # Perkalian Fitur       
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Cancelled operation.")
                    continue
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Cancelled operation.")
                    continue
                print(f"Result: {num1 * num2}")
            elif kalku == "/":                            # Pembagian Fitur
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Cancelled operation.")
                    continue
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Cancelled operation.")
                    continue
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero.")
            elif kalku == "%":                          # Modulus Fitur
                num1 = get_number("Enter first number: ")
                if num1 is None:
                    print("Cancelled operation.")
                    continue
                num2 = get_number("Enter second number: ")
                if num2 is None:
                    print("Cancelled operation.")
                    continue
                if num2 != 0:
                    print(f"Result: {num1 % num2}")
                else:
                    print("Error: Modulus by zero.")
            elif kalku in ["exit", "quit", "ex", "q"]:
                print("Exiting Callculator...")
                time.sleep(2)
                clear()
                break
            elif kalku == "clear":                      # Clear Screen Fitur
                clear()
            elif kalku == "print":
                print("Unknown command in Callculator. Command 'print' Only in kalla mode.")
            elif kalku == "":
                continue
            elif kalku == "-c":
                print("Callculator Creator: Rakha Projects")
            else:
                print("Unknown command in Callculator. Type -h for help.") 
    elif usr_input.startswith("print "): # Print Fitur Code
         to_print = usr_input[6:]  # Mengambil teks setelah "print "
         print(to_print)
    elif usr_input == "":
        continue
    elif usr_input == "Call" or usr_input == "cal" :
        print("Did you mean 'call'? Type 'call' to open Callculator.")
    elif usr_input == "sh -c" or usr_input == "show command":
        print("print = for showing text"
              "\n kallaja -v = for showing kallaja version"
              "\n kallaja -h = for showing kallaja help"
              "\n kallaja -c = for showing kallaja creator"
              "\n exit/quit = to exit kallaja"
              "\n call = to open callculator"
              "\n sh c / show command = for showing this command"
              "\n clear = for clearing the screen")
    elif usr_input == "kallaja":
        clear()
        thred_art()
    elif usr_input.startswith("print-s "):
         p = usr_input[8:]  # ambil setelah "print-s "
         if p.strip() == "":
            pass  # tidak lakukan apa-apa kalau kosong
         else:
            print(text2art(p, font="small", chr_ignore=True))

    else:
        print(usr_input + " Unknown command. Type 'kallaja -h' for help.")



