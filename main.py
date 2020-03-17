
from src.quotes import Quotes

import os
from time import sleep

#def clear():
#    sleep(3)
#    os.system('clear')


def close():
#    clear()
    print("program has been closed")
    sleep(1)
    exit(0)

def get_quote(type):
    if type == 1:
        quotes, author = Quotes.get_random()
        print(quotes)
    if type == 2:
        name = input("enter authore name")
        count, quotes = Quotes.get_quote_by_author(name)
        for i in range(count):
            print(quotes[i])
    if type == 3:
        count, quotes, author = Quotes.get_all_quote()
        for i in range(count):
            print(quotes[i])

def main():
    while True:
        print("""
        1. get Random
        2. get Specific author
        3. get all
        4.exit
        """)

        menu = input()
    #    clear()  # clear the screen
        switcher = {
            1: lambda x: get_quote(1),
            2: lambda x: get_quote(2),
            3: lambda x: get_quote(3), #only nerdy and explicit catagories
            4: lambda x: close(),
        }
        switcher.get(int(menu))(0)




if __name__ == "__main__":
    main()
