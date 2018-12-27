def coin_changes(amount, coins):
    combinations = [0] * (amount + 1)
    combinations[0] = 1
    for coin in coins:
        for value in range(amount + 1):
            if value >= coin:
                combinations[value] += combinations[value - coin]
    return combinations[amount]


