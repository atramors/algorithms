# GREEDY ALGORITHM

from typing import Dict

# Let's asume you are buying something in a shop and it costs 113
# coins, in your wallet you have one coin with denomination of 500
# and you want to have as less as possible of coins
# denominations of coins which are exist: 1, 2, 5, 10, 20, 50, 100, 500

money_you_have = 500
cost_of_goods = 113


def greedy_algorithm(money: int, price: int) -> Dict[int, int]:
    """Solving coin change problem"""

    wallet = {500: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    change = money - price

    for nominal in wallet.keys():
        while (change - nominal) >= 0:
            change = change - nominal
            wallet[nominal] += 1

    return wallet


print(greedy_algorithm(money_you_have, cost_of_goods))
