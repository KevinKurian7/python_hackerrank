#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character

    
    
    ns="".join(l)
    return ns

if __name__ == '__main__':