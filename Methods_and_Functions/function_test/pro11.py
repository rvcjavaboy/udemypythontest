def spy_game(li):
    stack=[0,0,7,'x'];

    for num in li:

        #print(stack.pop())
        if num==stack[0]:
            stack.remove(num)

    return len(stack)==1


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
