def matmul(int n):
    cdef int i, j, k
    cdef long long sum_val
    A = [[0] * n for _ in range(n)]
    B = [[0] * n for _ in range(n)]
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            A[i][j] = i + j
            B[i][j] = i - j

    for i in range(n):
        for j in range(n):
            sum_val = 0
            for k in range(n):
                sum_val += A[i][k] * B[k][j]
            C[i][j] = sum_val

    return C[0][0]
