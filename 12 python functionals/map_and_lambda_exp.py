cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lis=[]
    i=0
    n1,n2=0,1
    if n==0:
        return []
    elif n==1:
        lis.append(n1)
       
    else:
        while i<n:
            lis.append(n1)
            nextn=n1+n2
            n1=n2
            n2=nextn
    
            i=i+1
    return lis        


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))