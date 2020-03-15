from QuoteGarden import QuoteGardenAuthor
from QuoteApi import QuoteApi
from QuoteGardenCount import QuoteGardenCount
from Quotes import Quotes

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


def give_quotes(number):


    if number == 1:
        result = QuoteApi.random_quote()
        choose = input("choose:"+ "1.presented quote" + "2.presented author")
        if choose == 1 :
            print(Quotes.get_random_quote(result))
        else:
            print(QuoteGardenAuthor.get_random_author(result))

    elif number == 2:
        result = QuoteApi.all_quotes()
        choose = input("choose:" + "1.presented quotes" + "2.presented count " + "3. presented all author")
        number_quote = QuoteGardenCount.get_number_quotes(result)
        if choose == 1:
            list = Quotes.get_all(result)
            for i in range(number_quote):
                print(list[i])
        elif choose == 2:
            print(number_quote)
        else:
            list = QuoteGardenAuthor.get_all_author(result)

    else:
        name = input("Enter author name:")
        result = QuoteApi.quotes_by_author(name)
        choose = input("choose:" + "1.presented quotes" + "2.presented count")
        number_quote = QuoteGardenCount.get_number_quotes(result)
        if choose == 1:
            list = Quotes.get_all(result)
            for i in range(number_quote):
                print(list[i])
        else:
            print(number_quote)


def get_quote(type):
    if type == 1:
        give_quotes(1)
    if type == 2:
        give_quotes(3)
    if type == 3:
        give_quotes(2)

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
