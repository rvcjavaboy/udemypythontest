def master_yoda(text):
    li=text.split(' ');
    return " ".join(li[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))
