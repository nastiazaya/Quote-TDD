import unittest
from unittest.mock import Mock, patch

from src.quote_api import QuoteApi
from src.quotes import Quotes


class TestQuoteByAuthor(unittest.TestCase):

    @patch('src.quote_api.requests.get')
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
        expected = ["Doing nothing is better than being busy doing nothing.", "To lead people walk behind them."]
        author_quote_result_count, author_quote_result = Quotes.get_quote_by_author(name)
        self.assertEqual(author_quote_result, expected)

    @patch('src.quote_api.requests.get')
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
        expected = 2
        author_quote_result_count, author_quote_result = Quotes.get_quote_by_author(name)
        self.assertEqual(author_quote_result_count, expected)

    @patch('src.quote_api.requests.get')
    def test_author_not_found(self, mock_get):
        all_quote_response = {
            "count": 0,
            "results": []
        }
        name = "Lao "
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        expected = 0
        author_quote_result_count, author_quote_result = Quotes.get_quote_by_author(name)
        self.assertEqual(author_quote_result_count, expected)

    @patch('src.quote_api.requests.get')
    def test_author_not_found_zero_quote(self, mock_get):
        all_quote_response = {
            "count": 0,
            "results": []
        }
        name = "Lao "
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = all_quote_response
        expected = []
        author_quote_result_count, author_quote_result = Quotes.get_quote_by_author(name)
        self.assertEqual(author_quote_result, expected)

    @patch('src.quote_api.requests.get')
    def test_all_count_quote(self, mock_get):
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
        all_quote_result_count, all_quote_result = Quotes.get_quote_by_author(name)
        self.assertEqual(len(all_quote_result), all_quote_result_count)