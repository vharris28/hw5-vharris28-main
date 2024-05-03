# TODO: Your solutions here...
def zip(s, t):
    min_length = min(len(s), len(t))
    result = []
    for i in range(min_length):
        result.append((s[i], t[i]))
    
    return result


def find_period(s):
    n = len(s)
    if n == 0:
        return -1 

    for p in range(1, n // 2 + 1):
        if n % p == 0:  
            if s[:p] * (n // p) == s:  
                return p  
    return -1 



