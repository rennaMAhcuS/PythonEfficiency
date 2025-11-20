#include <chrono>
#include <cstdlib>
#include <iostream>
#include <vector>

using Matrix = std::vector<std::vector<long long>>;

Matrix matmul(const Matrix& A, const Matrix& B, int n) {
    Matrix C(n, std::vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            long long aik = A[i][k];
            for (int j = 0; j < n; ++j) {
                C[i][j] += aik * B[k][j];
            }
        }
    }
    return C;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <n>\n";
        return 1;
    }
    int n = std::stoi(argv[1]);
    int runs = 5;

    Matrix A(n, std::vector<long long>(n));
    Matrix B(n, std::vector<long long>(n));
    // Fill matrices with some values
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            A[i][j] = i + j;
            B[i][j] = i - j;
        }
    }

    // Warm-up (keeps consistency with Python benchmarks)
    auto init_start = std::chrono::high_resolution_clock::now();
    matmul(A, B, n);
    auto init_end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> init_duration = init_end - init_start;
    std::cout << init_duration.count() << std::endl;

    double total_duration = 0;
    for (int i = 0; i < runs; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        matmul(A, B, n);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        total_duration += duration.count();
    }
    double average_duration = total_duration / runs;

    std::cout << average_duration << std::endl;

    return 0;
}
