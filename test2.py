from morse import decode
import pytest


@pytest.mark.parametrize(
    "morse_message,decoded_message",
    [
        ('... --- ...', 'SOS'),
        ('... - ..- -.. . -. -', 'STUDENT'),
        ('-.-.-.', ';')  # не сработает, тк нет кодировки для ';'
    ]
)
def test_decode(morse_message: str, decoded_message: str) -> None:
    assert decode(morse_message) == decoded_message
