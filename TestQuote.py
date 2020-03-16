import unittest
from unittest.mock import Mock, patch

from QuoteApi import QuoteApi
from Quotes import Quotes


class TestAllQuote(unittest.TestCase):

    @patch('QuoteApi.requests.get')
    def test_all_quote(self, mock_get):
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
                        "_id": "5d91b45d9980192a317c87fa",
                        "quoteText": "Work out your own salvation. Do not depend on others.",
                        "quoteAuthor": "Buddha"
                    }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response

        expected = ["Doing nothing is better than being busy doing nothing.",
                    "Work out your own salvation. Do not depend on others."]

        all_quote_result_count,  all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(all_quote_result, expected)

    @patch('QuoteApi.requests.get')
    def test_all_author(self, mock_get):
        all_quote_response = {
            "count": 2,
            "results":
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
        expected = ["Lao Tzu", "Buddha"]
        all_quote_result_count, all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(all_quote_result_author, expected)

    @patch('QuoteApi.requests.get')
    def test_quote_number(self, mock_get):
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
        expected = 2
        all_quote_result_count, all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(all_quote_result_count, expected)

    @patch('QuoteApi.requests.get')
    def test_all_count_quote(self, mock_get):
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
                        "_id": "5d91b45d9980192a317c87fa",
                        "quoteText": "Work out your own salvation. Do not depend on others.",
                        "quoteAuthor": "Buddha"
                    }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response

        all_quote_result_count, all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(len(all_quote_result), all_quote_result_count)

    @patch('QuoteApi.requests.get')
    def test_all_number_author(self, mock_get):
        all_quote_response = {
            "count": 3,
            "results":
                [
                    {
                        "_id": "5d91b45d9980192a317c87f3",
                        "quoteText": "Doing nothing is better than being busy doing nothing.",
                        "quoteAuthor": "Lao Tzu"
                    },
                    {
                        "_id": "5d91b45d9980192a317c87fa",
                        "quoteText": "Work out your own salvation. Do not depend on others.",
                        "quoteAuthor": "Buddha"
                    },
                    {
                        "_id": "5d91b45d9980192a317c93ce",
                        "quoteText": "What matters is the value we've created in our lives,"
                                     "the people we've made happy and how much we've grown as people.",
                        "quoteAuthor": "Daisaku Ikeda"
                     }
                ]
        }
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        expected = 3
        all_quote_result_count, all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(len(all_quote_result_author), expected)

    @patch('QuoteApi.requests.get')
    def test_author_number_all(self, mock_get):
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
        expected = 1
        all_quote_result_count, all_quote_result, all_quote_result_author = Quotes.get_all_quote()
        self.assertEqual(len(all_quote_result_author), expected)



