def animal_crackers(string):
    li=string.split(' ')
    if(li[0][0]==li[1][0]):
        return True;
    else:
        return False;

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
