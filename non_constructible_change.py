# Non-Constructible Change
# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1.

# Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]
# [1, 1, 2, 3, 5, 7, 22]
# Sample Output
# 20

def non_constructible_change(array):
    # sort array
    array.sort() # nlog(n)
    # [1, 1, 2, 3, 5, 7, 22]
    change = 0
    for num in array:
        if num > change + 1:
            return change + 1
        change = change + num
    return change + 1

print(non_constructible_change(coins))
coins = [5, 7, 1, 1, 2, 3, 20] # 40
print(non_constructible_change(coins))