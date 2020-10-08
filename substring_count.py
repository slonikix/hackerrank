# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    score = 0
    for i in range(len(string)):
        if string[i:len(sub_string) + i] == sub_string:
            score += 1
    return score

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
