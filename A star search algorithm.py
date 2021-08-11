n=int(input("Enter number of vertices = "))
d={}
m={}
for i in range(n):
    a,b=input("Enter vertex and corresponding h(n) = ").split()
    d[a] = int(b)
    m[a] = {}
e = int(input("Enter number of edges = "))
for i in range(e):
    a,b,c = input("Enter edge and corresponding cost = ").split()
    m[a][b] = int(c)
    m[b][a] = int(c)
S = input("Enter initial state = ")
D = input("Enter final state = ")
dct={}
visited={}
cur = S 
val = d[cur]
print("X = ",cur,val)
while(cur!=D):
    for i in m[cur]:
        if (i not in dct and i not in visited):
            dct[i] = m[cur][i]+d[i]
    visited[cur] = val
    dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
    print("OPEN = ",dct)
    print("CLOSE = ",visited,"\n")
    cur =min(dct, key=dct.get)
    val = dct[cur]
    print("X = ",cur,val)
    del dct[cur]
visited[cur] = val
print("OPEN = ",dct)
print("CLOSE = ",visited,"\n")
print("Path = ",end='')
for i in visited:
    if(i==D):
        print(i)
    else:
        print(i,end='-')
print("Cost = ",end='')
lst=list(visited.keys())
j=lst[0]
print(j,end='-')
for i in lst[1:]:
    print(m[j][i],end="-")
    if(i==D):
        print(i)
    else:
        print(i,end='-')
    j=i
