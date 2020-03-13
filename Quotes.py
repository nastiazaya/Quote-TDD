
class Quotes:

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
        return result["quoteText"]