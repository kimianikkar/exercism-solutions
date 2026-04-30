""" Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    """
    parameters:
    budget: float(The amount of money you are planning to exchange.)
    exchange_rate: float (The amount of domestic currency equal to 1 unit of foreign currency.)

    returns:
    float (The value of the exchanged currency.)

    """
    return budget / exchange_rate

def get_change (budget, exchanging_value):
    """
    parameters:
    budget: float (Amount of money before exchange.)
    exchanging_value: float (The amount of your money you want to get back in the foreign currency.)

    returns:
    float (The amount of money that is left from the budget.)
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """
    parameters:
    denomination: int (The value of a single bill.)
    number_of_bills: int (Total number of bills.)

    returns:
    int (The total value of all of your bills.)
    """
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """
    parameters:
    amount: float (The total starting value.)
    denomination: int (The value of a single bill.)

    returns:
    int (The number of currency bills that you can receive within the given amount)
    """
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    """
    parameters:
    amount: float (The total starting value.)
    denomination: int (The value of a single bill.)

    returns:
    int (The leftover amount that cannot be given in bills.)
    """
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    parameters:
    budget: float (The amount of your money you are planning to exchange.
    exchange_rate: float (The unit value of the foreign currency.)
    denomination: int (The value of a single bill.)
    spread: int (The percentage that is taken as an exchange fee.

    returns:
    int (The maximum value you can get.)
    """
    spread_decimal = spread / 100
    actual_exchange_rate = exchange_rate * ( 1 +spread_decimal)
    foreign_currency = budget / actual_exchange_rate
    number_of_bills  = foreign_currency // denomination

    return int (number_of_bills * denomination)

