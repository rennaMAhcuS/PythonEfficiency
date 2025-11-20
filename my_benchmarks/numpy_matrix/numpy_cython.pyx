import numpy as np
cimport numpy as np

def matmul(int n):
    cdef np.ndarray[np.int64_t, ndim=2] A = np.fromfunction(lambda i, j: i + j, (n, n), dtype=np.int64)
    cdef np.ndarray[np.int64_t, ndim=2] B = np.fromfunction(lambda i, j: i - j, (n, n), dtype=np.int64)
    cdef np.ndarray[np.int64_t, ndim=2] C = np.dot(A, B)
    return C[0, 0]  # avoid optimization away
