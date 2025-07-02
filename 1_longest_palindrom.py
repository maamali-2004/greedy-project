def longest_palindrom(s):
    result = 0
    tedad = {}
    one = 0                 #faghat 1 done tak darim
    for i in s:
        if i in tedad:
            tedad[i] += 1
        else:
             tedad[i] = 1

    for v in tedad.values():
        if v % 2 == 0:
            result += v
        else:
            if v > 1 :
                result += v - 1
            else:
                if one < 1 :
                    result += 1
                    one += 1
    return result
                    
s = input()
print(longest_palindrom(s))
