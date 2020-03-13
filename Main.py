from QuoteGarden import QuoteGardenAuthor
from QuoteApi import QuoteApi
from QuoteGardenCount import QuoteGardenCount
from Quotes import Quotes

if __name__ == '__main__':

    number = input("choose:" + "1.random" + "2.all" + "3. by author")

    if number == 1 :
        result = QuoteApi.random_quote()
        choose = input("choose:"+ "1.presented quote" + "2.presented author")
        if choose == 1 :
            print(Quotes.get_random_quote(result))
        else:
            print(QuoteGardenAuthor.get_random_author(result))

    elif number == 2 :
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
