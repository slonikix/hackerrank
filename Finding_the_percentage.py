if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        
        scores.append(sum(scores) / len(scores))
        student_marks[name] = scores
        
        
    query_name = input()
    result = student_marks[query_name][3]
print(f'{result:.2f}')
