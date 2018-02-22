def blackjack(li):
    sum=0
    for i in li:
        sum+=i;
    if sum<=21:
        return sum

    elif sum<=31 and 11 in li :

        return sum-10
    else:
        return 'BUST'


print(blackjack([5,6,7]))
print(blackjack([9,9,9]))
print(blackjack([9,9,11]))
