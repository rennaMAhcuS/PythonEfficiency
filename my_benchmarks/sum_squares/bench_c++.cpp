#include <chrono>
#include <cstdlib>
#include <iostream>

// Sum of squares: sum_{i=0}^{n-1} i*i
long long sum_squares(int n) {
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += static_cast<long long>(i) * i;
    }
    return total;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <n>\n";
        return 1;
    }
    int n = std::stoi(argv[1]);
    int runs = 5;

    // Warm-up (keeps consistency with Python benchmarks)
    auto init_start = std::chrono::high_resolution_clock::now();
    sum_squares(n);
    auto init_end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> init_duration = init_end - init_start;
    std::cout << init_duration.count() << std::endl;

    double total_duration = 0;
    for (int i = 0; i < runs; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        sum_squares(n);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        total_duration += duration.count();
    }
    double average_duration = total_duration / runs;

    std::cout << average_duration << std::endl;

    return 0;
}
