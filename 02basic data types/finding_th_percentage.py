#https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        sum=0
        for i in range(len(student_marks[query_name])):
            sum=sum+student_marks[query_name][i]
    value=(sum/3.00)
    print("{0:.2f}".format(value))    