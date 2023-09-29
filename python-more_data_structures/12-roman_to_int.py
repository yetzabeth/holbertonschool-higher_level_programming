#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        sum = 0
    # I put a final 0 to avoid conflics when len(roman_string) == 1
        roman_string += "0"
        for i in range(0, len(roman_string) - 1):
            if roman_string[i] == "I":
                if roman_string[i + 1] == "V" or roman_string[i + 1] == "X":
                    sum -= 1
                else:
                    sum += 1

            if roman_string[i] == "V":
                sum += 5
            if roman_string[i] == "X":
                if roman_string[i + 1] == "L" or roman_string[i + 1] == "C":
                    sum -= 10
                else:
                    sum += 10

            if roman_string[i] == "L":
                sum += 50

            if roman_string[i] == "C":
                if roman_string[i + 1] == "D" or roman_string[i + 1] == "M":
                    sum -= 100
                else:
                    sum += 100

            if roman_string[i] == "D":
                sum += 500

            if roman_string[i] == "M":
                sum += 1000
        return sum
    return 0
