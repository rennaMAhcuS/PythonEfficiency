#include <chrono>
#include <iostream>

long long fib(int n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);
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
    fib(n);
    auto init_end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> init_duration = init_end - init_start;
    std::cout << init_duration.count() << std::endl;

    double total_duration = 0;
    for (int i = 0; i < runs; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        fib(n);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        total_duration += duration.count();
    }
    double average_duration = total_duration / runs;

    std::cout << average_duration << std::endl;

    return 0;
}
