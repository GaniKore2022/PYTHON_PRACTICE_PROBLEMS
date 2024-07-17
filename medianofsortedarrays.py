nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
nums3=nums1+nums2
nums3.sort()
k=len(nums3)
if k%2!=0:
    median=nums3[k//2]
    print(median)
else:
    median=(nums3[k//2 - 1]+nums3[k//2])/2
    print("{:.1f}".format(median))
