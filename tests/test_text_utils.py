from toolbox.text_utils import is_palindrome, word_frequency


def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue actuellement, voir issues/001


def test_is_palindrome_false():
    assert is_palindrome("python") is False


def test_word_frequency_basic():
    result = word_frequency("le chat et le chien")
    assert result == {"le": 2, "chat": 1, "et": 1, "chien": 1}


def test_word_frequency_case_insensitive():
    result = word_frequency("Le LE le")
    assert result == {"le": 3}


def test_word_frequency_no_punctuation():
    result = word_frequency("hello, world! hello.")
    assert result == {"hello": 2, "world": 1}


def test_word_frequency_empty():
    result = word_frequency("")
    assert result == {}


def test_word_frequency_single_word():
    result = word_frequency("python")
    assert result == {"python": 1}


def test_word_frequency_no_spaces_between_words():
    result = word_frequency("le:chat")
    expected = word_frequency("le chat")
    assert result == expected
