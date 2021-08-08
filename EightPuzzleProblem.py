def display(cur):
    for i in range(9):
        if(i==3 or i==6):
            print()
        if(cur[i]==9):
            print('-',end=' ')
            continue
        print(cur[i],end=' ')
def findheuristic(cur):
    l  =[1,2,3,8,9,4,7,6,5]
    c=0
    for i in range(9):
        if(cur[i]==9):
            continue
        elif(l[i]!=cur[i]):
            c+=1
    return c
cur=list(map(int,input("Welcome to 8 puzzle problem\nEnter the puzzle\n").split()))
res=findheuristic(cur)
print()
display(cur)
print("\nh(n) =",res,"\n")
while(res!=0):
    ind = cur.index(9)
    if(ind+3<9):
        cur1=cur.copy()
        cur1[ind],cur1[ind+3] = cur1[ind+3],cur1[ind]
        res=findheuristic(cur1)
        nxt=cur1
        s="Move down"
    if(ind-3>=0):
        cur2=cur.copy()
        cur2[ind],cur2[ind-3] = cur2[ind-3],cur2[ind]
        up =findheuristic(cur2)
        if(up<res):
            res=up
            nxt=cur2
            s="Move up"
    if(ind-1>=0):
        cur3=cur.copy()
        cur3[ind],cur3[ind-1] = cur3[ind-1],cur3[ind]
        left = findheuristic(cur3)
        if(left<res):
            res=left
            nxt=cur3
            s="Move left"
    if(ind+1<9):
        cur4=cur.copy()
        cur4[ind],cur4[ind+1] = cur4[ind+1],cur4[ind]
        right = findheuristic(cur4)
        if(right<res):
            res=right
            nxt=cur4
            s="Move right"
    cur=nxt
    print(s)
    display(cur)
    print("\nh(n) =",res,"\n")
print("8 puzzle problem solved!")
