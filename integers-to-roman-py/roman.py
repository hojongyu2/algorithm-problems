def to_roman(num):
    # Creates String that will contain Roman-numbers and assigned as empty
    # Creates a dicts that have Roman numbers as key and Arabian numbers as value so that when we iterate through,
    # we can compare with a given number
    # creates while loop that run until given number meets certain condition
    # creates for loop inside of the while loop that iterates created dics
    # start from the biggest roman number, compare with given number and if the given number is bigger than the given numnber
    # divide given number by the arabian number and assign given number as remainder
    # insert key to the created string and
    roman_integer = ""
    romanObj = {
        "M":  1000,
        "CM": 900,
        "D":  500,
        "CD": 400,
        "C":  100,
        "XC": 90,
        "L":  50,
        "XL": 40,
        "X":  10,
        "IX": 9,
        "V":  5,
        "IV": 4,
        "I":  1,
    }
    while num > 0:
        for roman_number in romanObj:
            if (num / romanObj[roman_number]) >= 1:
                roman_integer += roman_number
                num = num - romanObj[roman_number]
                break;
    return roman_integer
