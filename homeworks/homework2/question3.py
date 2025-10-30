# Andrew Wakefield
"""
ECE 241 - Fall 2025, Homework 2 question 3.
"""

def condition_higher_than_65(temp):
    return temp > 65

def condition_lower_than_75(temp):
    return temp < 75


def nth_highest(alist, n):
    """Finds the nth highest temperature by sorting the array,
    then calculating this temperatures' position

    Args:
        alist: the array of temperatures
        n: the nth highest temperature to retrieve

    Returns:
        int: the nth highest temperature
    """
    length = len(alist)
    if n > length: return None # check to make sure the request element is within range
    alist.sort() # sort the list into ascending order
    return alist[length - n] # return the nth highest indice
    

def nth_lowest(alist, n):
    """Finds the nth lowest temperature by sorting the array,
    then calculating this temperatures' position

    Args:
        alist: the array of temperatures
        n: the nth lowest temperature to retrieve

    Returns:
        int: the nth lowest temperature
    """
    length = len(alist)
    if n > length: return None # check to make sure the request element is within range
    alist.sort() # sort the list into ascending order
    return alist[n - 1] # return the nth lowest indice


def average_if(alist, condition):
    """Finds the average of the numbers in an array that meet
    conditions that the user specifies

    Args:
        alist: the array of numbers
        conditon: the function that determines which numbers are valid

    Returns:
        int: the average of #s that meet the condition
    """
    sum = 0 # initialize the sum counter
    total = 0 # initialize the total # of valid inputs
    for item in alist: # iterate through the list
        if condition(item): # ensure the indice meets the condition
            sum += item # add the current indice to the sum
            total += 1 # incrememnt the total # of valid numbers 
    return sum / total # calculate and return the average



def range_if(alist, condition):
    """Finds the difference between the largest and smallest numbers 
    that meet the conditions that the user specifies

    Args:
        alist: the array of numbers
        conditon: the function that determines which numbers are valid

    Returns:
        int: the difference between the min and max #s that meet the condition
    """
    # initialize the min and max numbers
    min = None 
    max = None

    for item in alist: # iterate through the list
        if condition(item): # ensure the indice meets the condition
            # if min is None, so is max; set them both to first valid element
            if min == None:
                min = item
                max = item

            # if item is less than current min, update this min
            if item < min: min = item
            
            # if item is more than current max, update this max
            if item > max: max = item

    return 0 if min == None else max - min # check that an element was valid, else return difference
            

if __name__ == '__main__':
    N = 3
    temperatures = [72.4, 65.1, 58.6, 81.3, 44.8, 90.2, 68.9, 79.5, 53.7, 87.1]

    highest = nth_highest(temperatures, N)
    lowest = nth_lowest(temperatures, N)
    average = average_if(temperatures, condition_higher_than_65)
    temperature_range = range_if(temperatures, condition_lower_than_75)

    print("The " + str(N) + "th highest temperature is: " + str(highest))
    print("The " + str(N) + "th lowest temperature is: " + str(lowest))
    print("The average temperatures (given the temperature is higher than 65) is: " + str(average))
    print("The range of temperatures (given the temperature is lower than 75) is: " + str(temperature_range))

