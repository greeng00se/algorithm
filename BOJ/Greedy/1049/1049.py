import sys 
import math

input = sys.stdin.readline

n, m = map(int, input().split())
bundle = []
piece = []

for _ in range(m):
    bundlePrice, piecePrice = map(int, input().split())
    bundle.append(bundlePrice)
    piece.append(piecePrice)

minBundle = min(bundle)
minPiece = min(piece)

result = min(math.ceil(n / 6) * minBundle, n * minPiece, n // 6 * minBundle + n % 6 * minPiece)
print(result)