from string_utils import get_lengths

def test_get_lengths():
    strings = ["apple", "cat", "hello",1]

    result = get_lengths(strings)

    assert result == [5, 3, 5]