def paper_doll(text):
    result=""
    for i in range(0,len(text)):
        for j in range(3):
            result+=text[i]

    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
