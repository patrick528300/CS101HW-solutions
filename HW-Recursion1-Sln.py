"""

in the following questions, recursion might not be the best solution,
but still good to apply recursive leap of faith to find out the aggregation method.

***YOU DONT HAVE TO FILL IN ALL BLANKS IF YOUR SOLUTION IS GOOD ENOUGH***

"""

def twoTothePowerOf(x):
    """
    use recursion to find another method to do 2^x
    Sample output:
    >>> twoTothePowerOf(5)
    32
    >>> twoTothePowerOf(10)
    1024
    """
    if x <= 0:
        return 1
    else:
        return 2 * twoTothePowerOf(x-1)

def reverse(x):
    """
    Reverse the order of the digits, and replace odd numbers with 0
    >>> reverse(123456)
    604020
    >>> reverse(13546)
    64000
    >>> reverse(23546)
    64002
    """
    sub = x
    n = 0   # get how many digits in x
    while sub > 0:
        n += 1
        sub = sub // 10
    def helper(x,n):
        if x == 0:
            return 0
        elif x%2 == 0:
            return (x%10) * (pow(10,n-1)//1) + helper(x//10,n-1)
        else:
            return helper(x//10,n-1)
    return helper(x,n)
    
        
        
def collatz(x):
    """
    Calculate how many steps to let the input number 
    narrow down to hit 1. Check out Lec04 to get what 
    collatz conjecture is
    Sample output:
    >>> collatz(100)
    25
    >>> collatz(1)
    0
    """
    assert x >= 0; "only receive positive input"
    if x <= 1:
        return 0
    elif x% 2 == 0:
        return 1 + collatz(x//2)
    else:
        return 1 + collatz(3*x+1)
        
        

    
def btod(b):
    """
    convert binary to decimal.
    
    hint:
    catch the digit place whose digit is 1
    for exmaple, if b = 1010, the target digit places are 2 and 4
    then decimal = 2^(4-1) + 2^(2-1)
    
    Plz use the twoTothePowerOf() instead of pow()

    >>> btod(1010)
    10
    >>> btod(0)
    0
    >>> btod(10100101)
    165
    """
    def helper(b,n):
        if b == 0:
            return 0
        elif b%10 == 1:
            return twoTothePowerOf(n) + helper(b//10, n+1)
        else:
            return helper(b//10,n+1)
    return helper(b,0)
    
    
        
        
def gcd(m,n):
    """
    to find out the greatest common divisor between two numbers
    
    hint: if m > n, and m % n == r, then gcd(m,n) == gcd(n,r)
    
    sample output:
    >>> gcd(100,50)
    50
    >>> gcd(86,92)
    2
    >>> gcd(1001,70)
    7
    >>> gcd(5,2)
    1
    """
    assert m > 0 and n > 0; "only receive positive input"
    if m == 1 or n == 1:
        return 1
    elif m == n:
        return m
    elif m > n:
        if m % n == 0:
            return n
        return gcd(n,m%n)
    else:
        if n%m == 0:
            return m
        return gcd(m,n%m)
