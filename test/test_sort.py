from chall import sort

def test_sort():
    assert sort("aBc123") == "abcB123"
    assert sort("zYx9876543210") == "xyzY9876543210"
    assert sort("") == "Invalid input, please enter alphanumeric characters only."
    assert sort("!@#") == "Invalid input, please enter alphanumeric characters only."
    assert sort("abcABC123") == "abcABC123"
    assert sort("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
