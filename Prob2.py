##################################################
# Name:
# Collaborators:
# Estimate of time spent (hr):
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    x = len(array)
    s = sum(array[0])
    
    for r in array:
        if len(r) != x or sum(r) != s:
            return False
    
    for i in range(x):
        s2 = 0
        for r in array:
            s2 += r[i]
        if s2 != s:
            return False
    s3 = 0
    for i in range(x):
        s3 += array[i][i]
    if s3 != s:
        return False
    s4 = 0
    for i in range(x):
        s4 += array[i][x-i-1]
    if s4 != s:
        return False
        

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

