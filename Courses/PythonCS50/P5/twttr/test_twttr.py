import twttr

from twttr import shorten

def main():
    test_words()
    test_words_with_numbers()
    test_no_words()

def test_words():
    assert shorten('twitter') == 'twttr'

def test_words_with_numbers():
    assert shorten('Gagan13846Gagan') == 'Ggn13846Ggn'

def test_no_words():
    assert shorten('') == ''