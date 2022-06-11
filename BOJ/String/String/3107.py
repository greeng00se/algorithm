import sys

input = sys.stdin.readline

def solve():
    data = list(input().rstrip().split(':'))        
    result = []
    
    if len(data) > 8: data.remove('')
    for i in range(len(data), 8):
        data.insert(data.index(''), '')
        
    for i in range(len(data)):
        result.append('0' * (4 - len(data[i])) + data[i])

    print(':'.join(result))
    
solve()