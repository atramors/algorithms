# GREEDY ALGORITHM

from typing import Dict, List

# Let's asume you are buying something in a shop and it costs 113
# coins, in your wallet you have one coin with denomination of 500
# and you want to have as less as possible of coins
# denominations of coins which are exist: 1, 2, 5, 10, 20, 50, 100, 500

money_you_have = 500
cost_of_goods = 113


def greedy_coin_change_problem(money: int, price: int) -> Dict[int, int]:
    """Solving coin change problem"""

    wallet = {500: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    change = money - price

    for nominal in wallet.keys():
        while (change - nominal) >= 0:
            change = change - nominal
            wallet[nominal] += 1

    return wallet


def greedy_coin_change_problem_optional(
        money: int, coin_types: List) -> List[int]:
    """Solving coin change problem"""

    index = len(coin_types) - 1
    wallet = []
    while money:
        if coin_types[index] <= money:
            wallet.append(coin_types[index])
            money -= coin_types[index]
        else:
            index -= 1

    return wallet
