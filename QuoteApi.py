import requests

class QuoteApi:

    @staticmethod
    def random_quote():
        api_result = requests.get('https://quote-garden.herokuapp.com/quotes/random')

        api_response = api_result.json()

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
