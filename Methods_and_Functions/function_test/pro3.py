def makes_twenty(n1,n2):
    if n1 ==20 or n2==20:
        return True
    elif n1+n2==20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))
