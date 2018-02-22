def old_macdonald(name):
    result=""
    for c in range(0,len(name)-1):
        if c==0 or c==3:
            result+=name[c].upper()
        else:
            result+=name[c]
    return result
print(old_macdonald('macdonald'))
