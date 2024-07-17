# def quicksort(a, first, last):
#     if first < last:
#         pivot = first
#         i = first
#         j = last
#         while i < j:
#             while a[i] <= a[pivot] and i < last:
#                 i += 1
#             while a[j] > a[pivot]:
#                 j -= 1
#             if i < j:
#                 a[i],a[j] = a[j],a[i]
#         a[pivot],a[j]= a[j],a[pivot]
#         quicksort(a, first, j-1)
#         quicksort(a, j+1, last)
# n = int(input("Enter the total Number of Elements: "))
# a = []
# print("Enter elements: ")
# for i in range(n):
#     a.append(int(input()))
# quicksort(a, 0, n-1)
# print("Order of Sorted elements: ")
# print(*a,sep=" ")
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left_arr=[i for i in arr if i<pivot]
    right_arr=[i for i in arr if i>pivot]
    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)
arr=list(map(int,input("Input list: ").split()))
print(f"Orignal list: {arr}")
print(f"Sorted list: {quick_sort(arr)}")