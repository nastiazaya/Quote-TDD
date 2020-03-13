import unittest
from unittest.mock import Mock, patch

from QuoteApi import QuoteApi
from QuoteGardenCount import QuoteGardenCount
from Quotes import Quotes
from QuoteGarden import QuoteGardenAuthor


class TestQuote(unittest.TestCase):

    @patch('QuoteGarden.requests.get')
    def test_random_quote(self, mock_get):
        random_quote_response = {
            "_id": "5d91b45d9980192a317c9a26",
            "quoteText": "A man who doesn't trust himself can never really trust anyone else.",
            "quoteAuthor": "Cardinal Retz"
        }

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = random_quote_response

        result = QuoteApi.random_quote()
        expected = "A man who doesn't trust himself can never really trust anyone else."
        random_quote_result = Quotes.get_random_quote(result)
        print(random_quote_result)
        self.assertEqual(random_quote_result, expected)


    @patch('QuoteGarden.requests.get')
    def test_all_quote(self,mock_get):
        all_quote_response = {
            "count":2 ,
            "results":
                [
                    {
                        "_id":"5d91b45d9980192a317c87f3",
                        "quoteText":"Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor":"Lao Tzu"
                    },
                    {
                        "_id":"5d91b45d9980192a317c87fa",
                        "quoteText":"Work out your own salvation. Do not depend on others.",
                        "quoteAuthor":"Buddha"
                    }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response

        result = QuoteApi.all_quotes()
        expected = ["Doing nothing is better than being busy doing nothing.","Work out your own salvation. Do not depend on others."]

        all_quote_result = Quotes.get_all(result)
        #print(all_quote_result)
        self.assertEqual(all_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_author_quote(self, mock_get):
        author_quote_response = {
            "count": 2,
            "results":
                [
                    {
                        "_id": "5d91b45d9980192a317c87f3",
                        "quoteText": "Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor": "Lao Tzu"
                    },
                    {
                        "_id": "5d91b45d9980192a317c87ed",
                        "quoteText": "To lead people walk behind them.",
                        "quoteAuthor": "Lao Tzu"
                    }
                ]
        }
        name = "Lao Tzu"
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = author_quote_response
        result = QuoteApi.quotes_by_author(name)
        expected = ["Doing nothing is better than being busy doing nothing.", "To lead people walk behind them."]
        author_quote_result = Quotes.get_by_author(result)
        self.assertEqual(author_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_author_quote_number(self, mock_get):
        author_quote_response = {
            "count": 2,
            "results":
                [
                    {
                        "_id": "5d91b45d9980192a317c87f3",
                        "quoteText": "Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor": "Lao Tzu"
                    },
                    {
                        "_id": "5d91b45d9980192a317c87ed",
                        "quoteText": "To lead people walk behind them.",
                        "quoteAuthor": "Lao Tzu"
                    }
                ]
        }
        name = "Lao Tzu"
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = author_quote_response
        result = QuoteApi.quotes_by_author(name)
        expected = 2
        author_quote_result = QuoteGardenCount.get_number_quotes_author(result)
        self.assertEqual(author_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_random_quote_author(self, mock_get):
        random_quote_response = {
            "_id": "5d91b45d9980192a317c9a26",
            "quoteText": "A man who doesn't trust himself can never really trust anyone else.",
            "quoteAuthor": "Cardinal Retz"
        }

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = random_quote_response

        result = QuoteApi.random_quote()
        expected = "Cardinal Retz"
        random_quote_result = QuoteGardenAuthor.get_random_author(result)
        self.assertEqual(random_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_all_author(self,mock_get):
        all_quote_response = {
            "count": 2
            , "results":
                [
                    {
                        "_id": "5d91b45d9980192a317c87f3",
                        "quoteText": "Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor": "Lao Tzu"},
                        {
                            "_id": "5d91b45d9980192a317c87fa",
                            "quoteText": "Work out your own salvation. Do not depend on others.",
                            "quoteAuthor": "Buddha"
                        }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        result = QuoteApi.all_quotes()
        expected = ["Lao Tzu","Buddha"]
        random_quote_result = QuoteGardenAuthor.get_all_author(result)
        self.assertEqual(random_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_author_not_found(self,mock_get):
        all_quote_response =  {
            "count": 0,
            "results": []
        }
        name = "Lao "
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        result = QuoteApi.quotes_by_author(name)
        expected = 0
        author_quote_result = QuoteGardenCount.get_number_quotes_author(result)
        self.assertEqual(author_quote_result, expected)

    @patch('QuoteGarden.requests.get')
    def test_quote_number(self,mock_get):
        all_quote_response = {
            "count": 2,
            "results":
                [
                    {
                        "_id": "5d91b45d9980192a317c87f3",
                        "quoteText": "Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor": "Lao Tzu"
                    },
                    {
                        "_id": "5d91b45d9980192a317c87ed",
                        "quoteText": "To lead people walk behind them.",
                        "quoteAuthor": "Lao Tzu"
                    }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        result = QuoteApi.all_quotes()
        expected = 2
        author_quote_result = QuoteGardenCount.get_number_quotes(result)
        self.assertEqual(author_quote_result, expected)


if __name__ == '__main__':
    unittest.main()

