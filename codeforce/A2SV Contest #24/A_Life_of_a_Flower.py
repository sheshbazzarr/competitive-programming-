test=int(input())

for _ in range(test):
  n=int(input())
  nums=list(map(int,input().split()))

  prev=-1
  dead=False
  total=1
  for cur in nums:
    if cur==1:
      if prev==1:
        total+=5
      else:
        total+=1
    else:
      if prev==0:
        dead=True
        break
    prev=cur
  if dead:
    print(-1)
  else:
    print(total)




