import requests


class QuoteGarden:

    @staticmethod
    def random_quote():

        api_result = requests.get('https://quote-garden.herokuapp.com/quotes/random')

        api_response = api_result.json()
        print(api_response)
        return api_response

    @staticmethod
    def quotes_by_author(author_name):

        api_result = requests.get('https://quote-garden.herokuapp.com/quotes/author/' + author_name)

        api_response = api_result.json()

        return api_response

    @staticmethod
    def all_quotes():
        api_result = requests.get('https://quote-garden.herokuapp.com/quotes/all')

        api_response = api_result.json()

        return api_response

    @staticmethod
    def get_list(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]['quoteText'])
        return result_list

    def get_list_author(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]["quoteAuthor"])
        return result_list

    @staticmethod
    def get_by_author(name):
       # name = input("Enter author name:")
        result = QuoteGarden.quotes_by_author(name)
        #number_quote = result['count']
        #print(number_quote)
        listResult = QuoteGarden.get_list(result)
        #for i in range(number_quote):
           # print(result['results'][i]['quoteText'])
        return listResult

    @staticmethod
    def get_number_quotes_author(name):
        result = QuoteGarden.quotes_by_author(name)
        return result['count']

    @staticmethod
    def get_number_quotes():
        result = QuoteGarden.all_quotes()
        return result['count']

    @staticmethod
    def get_all():
        result = QuoteGarden.all_quotes()
        number_quote = result['count']
        print(number_quote)
        listResult = QuoteGarden.get_list(result)
        #for i in range(number_quote):
            #print(result['results'][i]['quoteText'])
        return listResult

    @staticmethod
    def get_all_author():
        result = QuoteGarden.all_quotes()
        number_quote = result['count']
        listResult = QuoteGarden.get_list_author(result)
        return listResult

    @staticmethod
    def get_random_quote():
        result= QuoteGarden.random_quote()
        return result["quoteText"]

    @staticmethod
    def get_random_author():
        result = QuoteGarden.random_quote()
        return result["quoteAuthor"]


z = QuoteGarden()
z.random_quote()