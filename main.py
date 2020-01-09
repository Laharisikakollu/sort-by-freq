n=int(input())
lis=[]
for i in range(n):
  l=list(map(int,input().split()))
  lis.append(l)
lis.sort(key=len)
print(lis)