def func(w,x,T):
    s=0
    for i in range(len(w)):
        s+= w[i]*x[i]
    if(len(w)==1):
        if(s<T):
            return -1
        else:
            return 1
    else:
        if(s<T):
            return 0
        else:
            return 1
while(1):
    g = input("Enter gate = ")
    if(g.upper()=='AND'):
        print("x1\tx2\t y\n------------------")
        print("0\t0\t",func([1,1],[0,0],2))
        print("0\t1\t",func([1,1],[0,1],2))
        print("1\t0\t",func([1,1],[1,0],2))
        print("1\t1\t",func([1,1],[1,1],2))
    elif(g.upper()=='OR'):
        print("x1\tx2\t y\n------------------")
        print("0\t0\t",func([1,1],[0,0],1))
        print("0\t1\t",func([1,1],[0,1],1))
        print("1\t0\t",func([1,1],[1,0],1))
        print("1\t1\t",func([1,1],[1,1],1))
    elif(g.upper()=='NOT'):
        print("x\ty")
        print(1,"\t",func([-1],[1],1))
        print(-1,"\t",func([-1],[-1],1))
    else:
        print("Wrong gate")
        break
