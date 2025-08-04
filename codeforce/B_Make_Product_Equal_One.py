test = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

count = 0
non_negative = []
negative = []

for i in nums:
    if i > 0:
        non_negative.append(i)
    elif i==0:
        count+=1
    else:
        negative.append(i)


total = 0

if  len(negative) % 2 == 0: #even -ve
    for i in non_negative:
        total += (i + 1)
    for j in negative:
        total += (1 - j)
else: # odd -ve
    for i in non_negative:
        total += (i + 1)
    if len(negative) > 0:
        total += negative[0] + 1
        for j in negative[1:]:
            total += (1 - j)
if count>0:
    total+=count
print(total)
