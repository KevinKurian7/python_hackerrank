#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    people=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        people.append([name,score])

    #j=min(people,key= lambda x: x[1])
    minimum=min(people,key= lambda x: x[1])
    
    f=[x for x in people if x[1]!=minimum[1]]
    
    #print(f)

    minimum=min(f,key= lambda x: x[1])
    a=[]
    
    minimum=minimum[1]
    
    for i in f:
        if i[1]==minimum:
            a.append(i[0])
    a.sort()
    for i in a:
        print(i)           
    
