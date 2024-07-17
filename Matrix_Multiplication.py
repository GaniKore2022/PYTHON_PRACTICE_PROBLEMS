def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Matrix dimensions not matched for multiplication"
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [eval(x) for x in input(f"Enter space-separated elements for row {i+1}: ").split()]
        if len(row) != cols:
            print("Number of elements in the row does not match the number of columns.")
            return None
        matrix.append(row)
    return matrix

rows_A, cols_A = map(int, input("Enter no of rows & columns for mat A: ").split())
rows_B, cols_B = map(int, input("Enter no of rows and columns for mat B: ").split())

if cols_A != rows_B:
    print("Matrix dimensions not matched for multiplication")
else:
    print("elements for matrix A:")
    A = input_matrix(rows_A, cols_A)

    print("elements for matrix B:")
    B = input_matrix(rows_B, cols_B)

    result = matrix_multiply(A, B)
    if result:
        print("Resultant Matrix:")
        for row in result:
            print(row)
