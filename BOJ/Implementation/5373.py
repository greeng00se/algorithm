
U = [['w'] * 3 for _ in range(3)]
D = [['y'] * 3 for _ in range(3)]
F = [['r'] * 3 for _ in range(3)]
B = [['o'] * 3 for _ in range(3)]
L = [['g'] * 3 for _ in range(3)]
R = [['b'] * 3 for _ in range(3)]

def top(idx):
    cube = [U, D, F, B, L, R]
    a = [[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]]
    b = [[0, 1], [1, 2], [2, 1], [1, 0], [0, 1]]
    
    t1, t2 = cube[idx][0][0], cube[idx][0][1]
    cube[idx][0][0], cube[idx][0][1] = cube[idx][2][0], cube[idx][1][0]
    cube[idx][2][0], cube[idx][1][0] = cube[idx][2][2], cube[idx][2][1]
    cube[idx][2][2], cube[idx][2][1] = cube[idx][0][2], cube[idx][1][2]
    cube[idx][0][2], cube[idx][1][2] = t1, t2
        
def spinU(f):
    for i in range(f):
        top(0)

        t1, t2, t3 = F[0][0], F[0][1], F[0][2]

        F[0][0], F[0][1], F[0][2] = R[0][0], R[0][1], R[0][2]
        R[0][0], R[0][1], R[0][2] = B[0][0], B[0][1], B[0][2]
        B[0][0], B[0][1], B[0][2] = L[0][0], L[0][1], L[0][2]
        L[0][0], L[0][1], L[0][2] = t1, t2, t3

def spinD(f):
    for i in range(f):
        top(1)

        t1, t2, t3 = F[2][0], F[2][1], F[2][2]

        F[2][0], F[2][1], F[2][2] = L[2][0], L[2][1], L[2][2]
        L[2][0], L[2][1], L[2][2] = B[2][0], B[2][1], B[2][2]
        B[2][0], B[2][1], B[2][2] = R[2][0], R[2][1], R[2][2]
        R[2][0], R[2][1], R[2][2] = t1, t2, t3
            
def spinF(f):
    for i in range(f):
        top(2)

        t1, t2, t3 = U[2][0], U[2][1], U[2][2]

        U[2][2], U[2][1], U[2][0] = L[0][2], L[1][2], L[2][2]
        L[0][2], L[1][2], L[2][2] = D[0][0], D[0][1], D[0][2]
        D[0][0], D[0][1], D[0][2] = R[2][0], R[1][0], R[0][0]
        R[0][0], R[1][0], R[2][0] = t1, t2, t3
        
        
def spinB(f):
    for i in range(f):
        top(3)

        t1, t2, t3 = U[0][0], U[0][1], U[0][2]

        U[0][0], U[0][1], U[0][2] = R[0][2], R[1][2], R[2][2]
        R[0][2], R[1][2], R[2][2] = D[2][2], D[2][1], D[2][0]
        D[2][0], D[2][1], D[2][2] = L[0][0], L[1][0], L[2][0]
        L[0][0], L[1][0], L[2][0] = t3, t2, t1
        
def spinL(f):
    for i in range(f):
        top(4)

        t1, t2, t3 = U[0][0], U[1][0], U[2][0]

        U[0][0], U[1][0], U[2][0] = B[2][2], B[1][2], B[0][2]
        B[0][2], B[1][2], B[2][2] = D[2][0], D[1][0], D[0][0]
        D[0][0], D[1][0], D[2][0] = F[0][0], F[1][0], F[2][0]
        F[0][0], F[1][0], F[2][0] = t1, t2, t3
        
def spinR(f):
    for i in range(f):
        top(5)

        t1, t2, t3 = U[0][2], U[1][2], U[2][2]

        U[0][2], U[1][2], U[2][2] = F[0][2], F[1][2], F[2][2]
        F[0][2], F[1][2], F[2][2] = D[0][2], D[1][2], D[2][2]
        D[0][2], D[1][2], D[2][2] = B[2][0], B[1][0], B[0][0]
        B[2][0], B[1][0], B[0][0] = t1, t2, t3
        
n = int(input())

for i in range(n):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    num = int(input())
    data = list(input().split())
    for j in range(len(data)):
        run = 1
        if data[j][1] == '-':
            run = 3
        if data[j][0] == 'U':
            spinU(run)
        if data[j][0] == 'D':
            spinD(run)
        if data[j][0] == 'F':
            spinF(run)
        if data[j][0] == 'B':
            spinB(run)
        if data[j][0] == 'L':
            spinL(run)
        if data[j][0] == 'R':
            spinR(run)
            
    for ff in U:
        print(*ff, sep='')
        
        