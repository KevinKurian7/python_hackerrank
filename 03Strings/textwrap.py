import textwrap
#https://www.hackerrank.com/challenges/text-wrap/problem
def wrap(string, max_width):
    #k=0
    #j=max_width
    #a=""
    #for i in range(len(string)//2):
        #a=a+string[k:j]+"\n"
        #k=k+max_width
        #j=j+max_width

    #above code is correct too
    #comment out the below line to use the above code    
    a=textwrap.fill(string,max_width)
    return  a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)