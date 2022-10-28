# O(nlog(n)) time | O(1) space
def nonConstructibleChange(coins):
    coins.sort()
    running_total = 0

    for coin in coins:
        if coin > running_total + 1:
            return running_total + 1

        running_total += coin

    return running_total + 1
