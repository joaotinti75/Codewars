'''
The function must return the truncated version of the given string up to the given limit followed or concatenated by "..." if the result is shorter than the original. Return the same string if nothing was truncated.

Example:

solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'
'''

def solution(st, limit): 
    if len(st) > limit:
        return st[:limit]+'...'
    else:
        return st


print(solution('Testing String', 3))
print(solution('Testing String', 8))
print(solution('Test', 8))