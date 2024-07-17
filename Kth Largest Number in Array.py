nums=[3,2,1,5,6,4]
k=2
maxi=float('-inf')
while(k!=0):
    for i in nums:
        maxi=max(maxi,i)
    if maxi==float('-inf'):
        print(0)
        break
    elif maxi in nums:
        nums.remove(maxi)
        maxi=float('-inf')
        k-=1
print(max(nums))