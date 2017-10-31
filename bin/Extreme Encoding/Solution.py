for j in range(int(input())):
    ne=int(input())
    a=[]
    b=[]
    for i in range(ne):
        x=int(input())
        b.append(x>>16)
        a.append(x-(b[i]<<16))
    print("Case "+str(j+1)+":")
    print(*a)
    print(*b)
