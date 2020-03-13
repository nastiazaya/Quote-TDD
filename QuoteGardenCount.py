from QuoteApi import QuoteApi


class QuoteGardenCount:

    @staticmethod
    def get_number_quotes_author(result):
        return result['count']

    @staticmethod
    def get_number_quotes(result):
        return result['count']