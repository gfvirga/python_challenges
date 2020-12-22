import re
def get_duplicates(s):
    N = len(s)
    for i in range(1, N//2+1):
        if N % i == 0 and s[:i]* (N//i) == s:
            print("True")
            return True
    print("False")
    return False

string = "aba"
get_duplicates(string)