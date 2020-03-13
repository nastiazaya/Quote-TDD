import requests

from QuoteApi import QuoteApi


class QuoteGardenAuthor:

    @staticmethod
    def get_list_author(result):
        result_list = []
        number = result['count']
        for i in range(number):
            result_list.append(result['results'][i]["quoteAuthor"])
        return result_list


    @staticmethod
    def get_all_author(result):
        list_result = QuoteGardenAuthor.get_list_author(result)
        return list_result

    @staticmethod
    def get_random_author(result):
        return result["quoteAuthor"]