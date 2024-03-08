"""
***Tree Recursion HW***

*** YOU DONT HAVE TO FILL IN ALL BLANKS IF YOUR CODE IS GOOD ENOUGH***

"""
    

def ferry_arrange(ppl):
    """
    Suppose there are some certain amount of people on a bank of a river
    and there is a boat who capacity is 3 people
    Find how many ways to ferry people to the opposite bank

    hint: the boat can also take 1 or 2 person(s) at a time
    warning: order of arrangement DOES matter!
    >>> ferry_arrange(2)
    2
    >>> ferry_arrange(3)
    4
    >>> ferry_arrange(5)
    13
    >>> ferry_arrange(10)
    274
    """
    if ________:
        _________
    elif ________:
        ________
    else ________:
        ________
    


def count_notes(n):
    """
    find how many ways to get 25 dollars by having arbitrary amount of 1 dollar , 5 dollars, 
    10 dollars and 20 dollars notes. 
    
    Hint: there will be three recursive calls with different input arguments. 

    order of arrangements DOES NOT matter!
    >>> count_notes(5)
    2
    >>> count_notes(10)
    4
    >>> count_notes(25)
    23
    """
    if ________:
        ________
    elif ________:
        ________
    else:
        ________
    

def tradeForDrinks(stamp_amount):
    """
    Suppose you have some certain amount of stamps, and you can trade them for drinks.
    You can trade 2 stamps for a can of Sprite, 3 stamps for a can of Sunkist,
    and 5 stamps for a can of Pepsi.
    How many ways can you trade until you have only 0 or 1 stamps left?
    warning: order of arrangement DOES NOT matter!
    >>> tradeForDrinks(1)
    0
    >>> tradeForDrinks(5) 
    3
    >>> tradeForDrinks(7) #(5+2 3+2+2 2+2+2)
    4
    """
    if ________:
        _______
    def trade_assist(________):
        if ________:
            ________
        elif ________:
            ________
        else:
            ________
    return trade_assist(________)


def add_all_digits(number):
    """
    Use recursion and memorization to add all digits of the number and return the sum
    >>> add_all_digits(10)
    1
    >>> add_all_digits(5201314)
    16
    >>> add_all_digits(666)
    18
    """
    def helper(_______,_______):
        if ________:
            ________
        else:
            ________
    return helper(____ , ___)