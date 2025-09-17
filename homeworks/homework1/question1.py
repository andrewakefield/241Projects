"""
ECE241 Fall 2025 - Homework1 Question1
Andrew Wakefield
"""

# Use the following constants if you need
below_20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty','fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ['', 'thousand', 'million']


def stringify(number):
    """Convert an integer into its english equivalent.

    Args:
        number: the integer to convert.

    Returns:
        str: The english equivalent number

    Raises:
        RuntimeException: If the number is out of range
    """
    # Check for valid input
    if number > 999999999 or number < 1: 
        raise RuntimeError("Number must be an integer larger than 0 and less than 999,999,999")
    
    # 0 pad number needed for `three_digits` to funtion properly
    reversed_number = str(number)[::-1]
    while len(reversed_number) < 9: reversed_number += ("0")
    number = reversed_number[::-1]

    # Fill name array
    result = []
    if number[0:3] != "000":
        result.append(three_digits(number[0:3]))
        if number[3:9] != "000000": result.append(thousands[2] + ",") # include ',' where applicable
        else: result.append(thousands[2])
    if number[3:6] != "000":
        result.append(three_digits(number[3:6]))
        if number[6:9] != "000": result.append(thousands[1] + ",")
        else: result.append(thousands[1])
    if number[6:9] != "000": result.append(three_digits(number[6:9]))

    return " ".join(r for r in result if r) # join words with spaces only if they are not empty string


def three_digits(value):
    """Convert 3 integer string to english. Used to reduce redundancy

    Args:
        value: the 3 integer string to be converted

    Returns:
        str: the english equivalent number
    """
    name = []
    hundreds, ten, ones = value
    name .append(below_20[int(hundreds)])
    if hundreds != "0":
        name.append("hundred")
        if tens != "0" or ones != "0": name.append("and")
    if ten == "1":
        name.append(below_20[int(value[1:3])])
    else:
        if tens != "0":
            name.append(tens[int(ten)])
        if ones != "0":
            name.append(below_20[int(ones)])
        
    return " ".join(n for n in name if n) # join words with spaces only if they are not empty string


if __name__ == "__main__":
    print(stringify(1))         # excepted: one
    print(stringify(10))        # excepted: ten
    print(stringify(2024))      # excepted: two thousand, twenty four
    # excepted: twenty million, two hundred and forty two thousand, twenty four
    print(stringify(20242024))
    print(stringify(119210))