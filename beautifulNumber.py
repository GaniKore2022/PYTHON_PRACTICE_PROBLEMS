# class Solution:
#     def beautifulNumber(self, n : int) -> bool:
#         # code here
#         n=str(n)
#         if len(n)==1:
#             if (int(n))**2==1:
#                 return True
#             else:
#                 return False
#         else:
#             s=0
#             for i in n:
#                 s=s + int(i)**2
#             obj.beautifulNumber(s)
# 
# 
# #{ 
#  # Driver Code Starts
# if __name__=="__main__":
#     t = int(input())
#     for _ in range(t):
#         
#         n = int(input())
#         
#         obj = Solution()
#         res = obj.beautifulNumber(n)
# 
#         
#         result_val = "Yes" if res else "No"
#         print(result_val)
#
def square_sum_of_digits(n):
    sum_of_squares = 0
    while n > 0:
        digit = n % 10
        sum_of_squares += digit ** 2
        n //= 10
    return sum_of_squares

def is_beautiful_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = square_sum_of_digits(n)
    
    return n == 1

# Read input from the user
num = int(input("Enter a number: "))

# Check if the number is beautiful
if is_beautiful_number(num):
    print(f"{num} is a beautiful number!")
else:
    print(f"{num} is not a beautiful number.")
