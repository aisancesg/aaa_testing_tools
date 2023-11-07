from morse import encode


def test_encode(message: str) -> str:
    r"""
    >>> encode('SOS')
    '... --- ...'
    >>> encode(';') # Будет ошибка, тк нет кодировки для ';'
    '-.-.-.'
    """
    return encode(message)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
