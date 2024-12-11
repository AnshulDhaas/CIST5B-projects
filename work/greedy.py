def calculate_change(amount_due, amount_paid):
    change = amount_paid - amount_due
    coins = [100, 50, 25, 10, 5, 1]
    coin_change = {}

    for coin in coins:
        if change == 0:
            break

        count = change // coin
        if count > 0:
            coin_change[coin] = count
            change -= count * coin

    print(coin_change)

calculate_change(1234, 2000)