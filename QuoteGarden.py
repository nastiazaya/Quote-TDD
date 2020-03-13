import requests

from QuoteApi import QuoteApi


class QuoteGarden:


    @staticmethod
    def get_list(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]['quoteText'])
        return result_list

    @staticmethod
    def get_list_author(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]["quoteAuthor"])
        return result_list

    @staticmethod
    def get_by_author(name):
       # name = input("Enter author name:")
        result = QuoteApi.quotes_by_author(name)
        #number_quote = result['count']
        #print(number_quote)
        list_result = QuoteGarden.get_list(result)
        #for i in range(number_quote):
           # print(result['results'][i]['quoteText'])
        return list_result

    @staticmethod
    def get_number_quotes_author(name):
        result = QuoteApi.quotes_by_author(name)
        return result['count']

    @staticmethod
    def get_number_quotes():
        result = QuoteApi.all_quotes()
        return result['count']

    @staticmethod
    def get_all():
        result = QuoteApi.all_quotes()
        number_quote = result['count']
        print(number_quote)
        list_result = QuoteGarden.get_list(result)
        #for i in range(number_quote):
            #print(result['results'][i]['quoteText'])
        return list_result

    @staticmethod
    def get_all_author():
        result = QuoteApi.all_quotes()
        number_quote = result['count']
        list_result = QuoteGarden.get_list_author(result)
        return list_result

    @staticmethod
    def get_random_quote():
        result = QuoteApi.random_quote()
        return result["quoteText"]

    @staticmethod
    def get_random_author():
        result = QuoteApi.random_quote()
        return result["quoteAuthor"]