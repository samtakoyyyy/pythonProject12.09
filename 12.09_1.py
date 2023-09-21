#1. Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.
arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = []

while True:
    x = input().split()
    if "end" in x:
        break
    matrix.append([int(n) for n in x])

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()


print(matrix[::-1])
