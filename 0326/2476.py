N=int(input())
arr=[]
for i in range(N):
    a,b,c= map(int,input().split())
    if(a==b==c):
       arr.append(10000+(a*1000))
    elif(a==b or a==c):
        arr.append(1000+(100*a))
    elif(b==c):
        arr.append(1000+(b*100))
    else:
        arr.append(max(a,b,c)*100)
print(max(arr))