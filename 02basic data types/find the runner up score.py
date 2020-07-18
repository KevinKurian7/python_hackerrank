#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().strip().split()))

for i in range(0,len(arr)):
    arr[i]=int(arr[i])
arr.sort()

arr2=set(arr)    
arr2.remove(max(arr2))
print(max(arr2))
