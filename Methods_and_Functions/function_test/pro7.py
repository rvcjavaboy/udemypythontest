def has_33(li):
    for l in range(0,len(li)-1):
        if li[l]==3 and li[l+1]==3:
                return True

    else:
        return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#print(has_33([1, 3, 3]))
