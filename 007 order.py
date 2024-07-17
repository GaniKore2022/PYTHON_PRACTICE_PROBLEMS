# l=list(map(int,input().split()))
# def order(l):
#     if 0 in l and 7 in l:
#         x=l.index(0)
#         y=l.index(7)
#         for i in range(x+1,y+1):
#             if l[i]==0:
#                 return True
#         return False
#     else:
#         return False
# print(order(l))
def spy(nums):
    code=[0,0,7,'x']
    for i in nums:
        if i==code[0]:
            code.pop(0)
    return len(code)==1
nums=list(map(int,input().split()))
print(spy(nums))