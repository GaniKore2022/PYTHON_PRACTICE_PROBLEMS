import sys

MAX_SIZE = 3

def main():
    A = []
    B = []
    C = []

    print("Enter the number of rows and columns of matrix A: ")
    r1, c1 = map(int, input().split())

    print("Enter the number of rows and columns of matrix B: ")
    r2, c2 = map(int, input().split())

    if c1 != r2:
        print("Matrix multiplication is not possible because the number of columns in matrix A is not equal to the number of rows in matrix B.")
        sys.exit(1)

    if r1 > MAX_SIZE or c1 > MAX_SIZE or r2 > MAX_SIZE or c2 > MAX_SIZE:
        print(f"Matrix size exceeds the maximum allowed size of {MAX_SIZE}.")
        sys.exit(1)

    print("Enter elements of matrix A:")
    for i in range(r1):
        row = list(map(float, input().split()))
        if max(row) > (sys.maxsize // (r1 * c1)):
            print("Value of element in matrix A is too large.")
            sys.exit(1)
        A.append(row)

    print("Enter elements of matrix B:")
    for i in range(r2):
        row = list(map(float, input().split()))
        if max(row) > (sys.maxsize // (r2 * c2)):
            print("Value of element in matrix B is too large.")
            sys.exit(1)
        B.append(row)

    for i in range(r1):
        C.append([0] * c2)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("Resultant matrix:")
    for row in C:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
