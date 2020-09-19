if __name__ == '__main__':
   
    n = int(input())
    markList =  [[input(), float(input())] for _ in range(n)]

    markList.sort(key = lambda x : x[1])
    scorelist = [score for name, score in markList ]

    scores = sorted(set(scorelist))[1]

    result = sorted([name for name, score in markList if score == scores ])

    print ('\n'.join(result))
