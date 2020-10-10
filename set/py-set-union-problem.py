#https://www.hackerrank.com/challenges/py-set-union/problem
n=int(input())
english=set(map(int,input().split()))
b=int(input())
french=set(map(int,input().split()))
a=english.union(french)
print(len(a))