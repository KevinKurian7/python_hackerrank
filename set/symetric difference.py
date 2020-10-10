#https://www.hackerrank.com/challenges/symmetric-difference/problem
m=int(input())
m1=set(map(int,input().split()))
n=int(input())
n2=set(map(int,input().split()))

a=m1.difference(n2)
b=n2.difference(m1)
c=a.union(b)
c=sorted(list(c))
for _ in c:
    print(_)
