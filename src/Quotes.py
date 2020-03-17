from QuoteApi import QuoteApi


class Quotes:
    @staticmethod
    def get_number_quotes(result):
        return result['count']

    @staticmethod
    def get_list(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]['quoteText'])
        return result_list

    @staticmethod
    def get_all(result):
        number_quote = result['count']
        print(number_quote)
        list_result = Quotes.get_list(result)
        # for i in range(number_quote):
        # print(result['results'][i]['quoteText'])
        return list_result

    @staticmethod
    def get_by_author(result):
        list_result = Quotes.get_list(result)
        return list_result

    @staticmethod
    def get_random_quote(result):
        return [result["quoteText"]]

    @staticmethod
    def get_list_author(result):
        result_list = []
        number = result['count']
        for i in range(number):
            if not result['results'][i]["quoteAuthor"] in result_list:
                result_list.append(result['results'][i]["quoteAuthor"])
        return result_list

    @staticmethod
    def get_all_author(result):
        list_result = Quotes.get_list_author(result)
        return list_result

    @staticmethod
    def get_random_author(result):
        return result["quoteAuthor"]

    @staticmethod
    def get_random():
        result = QuoteApi.random_quote()
        return Quotes.get_random_quote(result), Quotes.get_random_author(result)

    @staticmethod
    def get_all_quote():
        result = QuoteApi.all_quotes()
        return Quotes.get_number_quotes(result), Quotes.get_all(result), Quotes.get_all_author(result)

    @staticmethod
    def get_quote_by_author(name):
        result = QuoteApi.quotes_by_author(name)
        return Quotes.get_number_quotes(result), Quotes.get_by_author(result)
