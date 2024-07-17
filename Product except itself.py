nums=[1,2,3,4]
x=[]
prod=1
for i in nums:
    x.append(prod)
    prod*=i
prod=1
for j in reversed(range(len(nums))):
    x[j] *=prod
    prod*=nums[j]
print(x)