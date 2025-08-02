from chall import sort

def test_sort():
    assert sort("aBc123") == "acB132"
    assert sort("zYx9876543210") == "xzY9753108642"
    assert sort("") == "Invalid input, please enter alphanumeric characters only."
    assert sort("!@#") == "Invalid input, please enter alphanumeric characters only."
    assert sort("abcABC123") == "abcABC132"
    assert sort("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"