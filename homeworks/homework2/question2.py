# Andrew Wakefield

"""
ECE241 - Fall 2025, Homework 2, question 2.
    denote WORTH CASE asymptotic time complexity use the big-O notation
    assuming the input parameters are all arrays.
    You can use the variable name to represent the length of the input array in your solution.
    You can assume all built-in function's execution time is constant, i.e., O(1)
    In addition, when indexing in an array is always success.
    i.e., the array has sufficiently large amount of elements.
"""

from math import log, sin, tan  # assume these functions all take O(1) time


def demo(n):
    # NOTE: This is a demo for this question.
    # You DO NOT need to include the solution for this one in your submission

    total = 0
    for i in n:
        total += i
    return total
    # Let n is the input array.
    # The time complexity of this function is O(n),
    # where in this question,
    # you can use the variable name to represent the length of the input array.


def function1(n, m):
    nm = []

    for n_i in n:
        nm.append(n_i)

    for m_i in m:
        nm.append(m_i)

    return nm


def function2(n):
    lt = len(n)
    nm = []

    while lt > 1:
        nm.append(n[2025] * n[lt - 1])
        lt -= 1

    return nm


def function3(n):
    total = n[0]
    count = 0
    index = 1
    while index < len(n):
        if n[index] > 241241 or n[index] < -241241:
            n[index] += 1
        total += n[index]
        index += 1
        count += 1

    return count


def function4(n):
    nn = []
    repeats = 10
    total = 0
    for i in n:
        total += i
    avg = total / len(n)
    for j in range(repeats):
        nn.append(avg * j)

    return nn


def function5(m, n, x, y, z, t):
    my_secret_value = [val for val in y if val > x[2025]]
    if sum(my_secret_value) * len(m) + min(2025 * n[2025], 2025) < max(2025, 2025 ** x[2025]):
        return 2025 ** log(log(tan(2025 + sin(2025)))) - abs(x[2025]) + 9 * log(log(len(t)))
    else:
        return 2025 * 2025 - min(x[2025], y[2025], z[20] + z[24], -2025) + 9 * log(
            log(log(len(t) + 2025)) + log(t[2025 ** 2025]))

