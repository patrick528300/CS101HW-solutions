"""
    this is the homework of iteration
    In some problem, iteration might not be the best solution!
    ***YOU DONT HAVE TO FILL IN ALL BLANKS IF YOUR CODE IS GOOD ENOUGH***
"""

def gcd(m,n):
    """
    find the greatest common divisor between two numbers using iteration
    definition of gcd: gcd is the greatest number that can divide the two numbers

    hint: the builtin function min(m,n) returns the smaller one of the two numbers

    Sample output:
    >>> gcd(1,2)
    1
    >>> gcd(100,50)
    50
    >>> gcd(86,92)
    2
    >>> gcd(1001,70)
    7
    """
    assert m > 0 and n > 0; "only receive positive numbers"
    sln = min(m,n)
    while sln > 1:
        if m%sln == 0 and n%sln == 0:
            return sln
        sln = sln - 1
    return 1


def lcm(m,n):
    """
    find the least common multiplier between two numbers using iteration
    definition of lcm: lcm is the least number that can be divided by the two numbers

    hint: the builtin function max(m,n) returns the bigger one of the two numbers
    Sample output:
    >>> lcm(1,1)
    1
    >>> lcm(1,2)
    2
    >>> lcm(100,50)
    100
    >>> lcm(78,12)
    156
    >>> lcm(89,56)
    4984
    """
    assert m > 0 and n > 0; "only receive positive numbers"
    a, sln = m*n,1
    while a >= max(m,n):
        if a%m == 0 and a%n == 0:
            sln = a
        a = a - 1
    return sln

def collatz(x):
    """
    find how many steps are needed to narrow down the number to 1 in a collatz conjecture using iteration

    >>> collatz(1)
    1
    >>> collatz(100)
    25
    """
    sln = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        sln = sln + 1
    return sln

def is_prime(x):
    """
    determine if a number is prime using iteration. A prime number can only be divided by 1 and itself
    >>> is_prime(2)
    True
    >>> is_prime(0)
    False
    >>> is_prime(103)
    False
    >>> is_prime(1001)
    True
    """
    assert x >= 0, "only receive positive numbers"
    if x == 0:
        return False
    a = x - 1
    while a > 1:
        if x%a == 0:
            return False
        a = a - 1
    return True
    
    
def get_digit(x):
    """return how many digits in a number """
    if abs(x) == 0:
        return 0
    else:
        return get_digit(x//10) + 1

def all_prime(x):
    """
    only keep prime digits. 

    hint: use the is_prime() function and get_digit() function
    use pow() function -> pow(2,10) == 2^10

    >>> all_prime(666)
    0
    >>> all_prime(101300)
    113
    >>> all_prime(9257708662)
    25772
    >>> all_prime(9256851230)
    255123
    """
    sln = 0
    while x > 0:
        b = x % 10
        if is_prime(b):
            sln = b * pow(10,get_digit(sln)) + sln
        x = x // 10
    return sln