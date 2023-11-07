from what_is_year_now import what_is_year_now
from unittest.mock import patch
import io


def test_first_format():  # тестируем формат YYYY-MM-DD
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO(
                   '{"currentDateTime": "2023-11-06T16:57Z"}'
               )):
        assert what_is_year_now() == 2023


def test_second_format():  # тестируем формат DD.MM.YYYY
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO(
                   '{"currentDateTime": "06.11.2023T16:57Z"}'
               )):
        assert what_is_year_now() == 2023


def test_error():
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=io.StringIO(
                   '{"currentDateTime": "06/11/2023T16:57Z"}'
               )):
        try:
            what_is_year_now()
        except ValueError:
            pass
