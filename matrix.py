#Write python program to multiply matrices

X = [[2,17,3],
    [4 ,5,36],
    [17 ,8,9]]

Y = [[5,8,3,2],
    [6,9,3,0],
    [4,1,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
