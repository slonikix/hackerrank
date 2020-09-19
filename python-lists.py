# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    li = list()
    for _ in range(N):
        command = input().strip().split()
        if command[0] == 'print':
            print(li)
        else:
            getattr(li, command[0])(*(map(int, command[1:])))
