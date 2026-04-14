matrix = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)