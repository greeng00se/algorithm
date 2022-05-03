import sys
import heapq

input = sys.stdin.readline

def solve(gas_station, destination, current_gas):
    gas_station.sort(reverse = True)
    result = 0
    hq = []
    
    while current_gas < destination:
        while gas_station and gas_station[-1][0] <= current_gas:
            station, fuel = gas_station.pop()
            heapq.heappush(hq, -fuel)

        if not hq: break
        
        current_gas -= heapq.heappop(hq)
        result += 1

    return result if destination <= current_gas else -1

n = int(input())
gas_station = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

print(solve(gas_station, l, p))