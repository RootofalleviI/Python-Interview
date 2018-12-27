def coin_changes(amount, coins):
    combinations = [0] * (amount + 1)
    combinations[0] = 1
    for coin in coins:
        for i in range(amount + 1):
            if i >= coin:
                combinations[i] += combinations[i - coin]
    return combinations[amount]

coins = [1, 2, 5]
amount = 12
print(coin_changes(amount, coins))