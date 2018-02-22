def count_primt(num):
    li=[]
    if num<2:
        return 0;
    else:
        for n in range(2,num):
            #print("N{}\tJ{}".format(n,0))
            for j in range(2,int(n/2)):
                print("N{}\tJ{}".format(n,j))
                if n%j==0:
                    break;
                else:
                    li.append(n)
                    break
    print(li)
    return len(li);


print(count_primt(100))
