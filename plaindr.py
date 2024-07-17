# def palindrome(s):
#     a=s[::-1]
#     if s==a:
#         print("palindrome")
#     else:
#         print("not")
# s=input()
# palindrome(s)
# s=input()
# m=input()
# flag=0
# for i in s:
#     if i in m:
#         falg=0
#     else:
#         flag=1
#         break
# if(flag==0):
#     print("Anagram")
# else:
#     print("Not")
# if sorted(s)==sorted(m):
#     print("yes")
# else:
#     print("no")
# n=int(input())
# p=1
# for i in range(2,n+1):
#     p=p*i
# print(p)
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input())
# print(fact(n))
# # 0 1 1 2 3 5 8 13 21
# n=int(input())
# a=0
# b=1
# if n==1:
#     print(a)
# elif n==2:
#     print(a,b)
# else:
#     print(a,b,end=" ")
#     for i in range(n):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# def fib(n,l):
#     print(l[0],l[1],end=" ")
#     for i in range(2,n):
#         a=l[-1]+l[-2]
#         print(a,end=" ")
#         l.append(a)
# n=int(input())
# l=[0,1]
# fib(n,l)
