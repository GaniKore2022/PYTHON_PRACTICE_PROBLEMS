##Task1
# ip=list(map(int,input().split(',')))
# op=[]
# for i in ip:
#     if i not in op:
#         op.append(i)
# print(*op)
# Task2
# a=int(input())
# n=a//100
# s=(a%100)*(n+1)
# s=s+(((n*(n+1))/2)*100)
# print(s)
# Task3
# total_seconds=int(input())
# h=total_seconds//(3600)
# m=(total_seconds%(3600))//60
# s=(total_seconds%(3600))%60
# print(f"h:{h} m:{m} s:{s}")
# Task4
# s=input()
# s1=""
# for i in range(len(s)-1):
#     if s[i]!=s[i+1]:
#             s1+=s[i]
# s1=s1+s[-1]
# print(s1)
# Task5
# ip:"khoor"
# n:3
# op:"hello"
# ip:"bvec"
# n:4
# op:"xray"
# a=input()
# n=int(input())
# for i in a:
#     if(ord(i)-n <97):
#         print(chr(ord(i)-n+26),end="")
#     else:
#         print(chr(ord(i)-n),end="")
# Task6
# l=list(map(int,input().split()))
# c=m=0
# for i in l:
#     if i%2==0:
#         c+=1
#     else:
#         if c>m:
#             m=c
#         c=0
# if c>m:
#     m=c
# print(m)
# Task7
# x=input()
# c=1
# m=[]
# for i in range(len(x)-1):
#     if ord(x[i])+1 == ord(x[i+1]):
#         c+=1
#     else:
#         if c!=1:
#             m.append(c)
#         c=1
# if c!=1:
#     m.append(c)
# print(*m)
# a=input().split(",")
# b=""
# for i in a:
#     i=i.split(":")
#     if(str(len(i[0])) in i[1]):
#         b=b+i[0][-1]
#     else:
#         d=0;c=0
#         for j in i[1]:
#             if(int(j)<len(i[0])):
#                 c=1
#                 if(int(j)>d):
#                     d=int(j)
#         if(c==1):
#             
#         else:
#             b=b+"x"
# print(b)
# a=input()
# b=[]
# for i in a:
#     if(i.isalpha()):
#         b.append(i)
# b=b[::-1]
# for i in range(len(a)):
#     if(not a[i].isalpha()):
#         b.insert(i,a[i])
# print("".join(b))
a=list(map(int,input().split()))
n=int(input())
b=a.copy()
b.sort()
# print(abs(a.index(n)-b.index(n)))
# s=0
# for i in a:
#     s=s+(i*abs(a.index(i)-b.index(i)))
# print(s)
print(b[-n])
