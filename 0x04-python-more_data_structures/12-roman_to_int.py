#!/usr/bin/python
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    return sum(romans[c] if romans[c] >= romans.get(p, 0) else -romans[c] for c, p in zip(roman_string, roman_string[1:] + "0"))
