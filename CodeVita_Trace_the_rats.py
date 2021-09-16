
A = []
X = []
Y = []
d = []

cor = []
zeroes = []
flag = 0


N = int(input("Enter the size of the maze:"))

for i in range(0, N):
    t = []
    for j in range(0, N):
        t.append(input())
    A.append(t)
    

R = int(input("Enter the number of rats:"))


# co-ordinates are stored in a 2d-list

for i in range(0, R):
    X, Y = map(int, input("Enter the coordinates of the rats:").split())
    d.append(X-1)
    d.append(Y-1)
    cor.append(d)
    d = []
    
    
# Dummy matrix (with all zero values)
for i in range(0, N):
    t1 = []
    for j in range(0, N):
        t1.append(0)
    zeroes.append(t1)
    
    
# print(cor)
# print(zeroes)

for i in range(0, len(cor)):
    e = len(cor[i])
    for j in range(0, e-1):
        zeroes[cor[i][j]][cor[i][j+1]] = 1
        
        
# print(zeroes)

for i in range(0, len(A)):
    q = len(A[i])
    for j in range(0, q):
        if A[i][j] == 'X':
            zeroes[i][j] = -1
            
# print(zeroes)

def ways(row, col):
    
    if row < 0 or row > (N-1) or col < 0 or col > (N-1):
        return
    
    elif zeroes[row][col] == -1:
        return
    
    elif zeroes[row][col] == 2:
        return
    
    else:
        zeroes[row][col] = 2
        
    ways(row+1, col)
    ways(row-1, col)
    ways(row, col+1)
    ways(row, col-1)
    
    


ways(cor[0][0],cor[0][1])

# print(zeroes)


# If there is 1 in my resulatant zeroes 2d list, it says that one mice is stuck between walls.

for i in range(0, len(zeroes)):
    w = len(zeroes[i])
    for j in range(0, w):
        if zeroes[i][j] == 1:
            flag = 1
            
            
if flag == 1:
    print("No")
else:
    print("Yes")
    
    
