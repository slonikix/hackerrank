https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    sList = list(map(str, (arr[::-1])))
    print(" ".join(sList))
