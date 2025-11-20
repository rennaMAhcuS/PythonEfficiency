#include <chrono>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <n>\n";
        return 1;
    }

    int n = std::stoi(argv[1]);
    std::string text;
    std::string word = "lorem ipsum ";
    while ((int)text.size() < n) text += word;
    if ((int)text.size() > n) text.resize(n);

    auto count_words = [](const std::string& data) {
        std::unordered_map<std::string, int> word_count;
        std::istringstream iss(data);
        std::string word;
        while (iss >> word) {
            ++word_count[word];
        }
        return word_count;
    };

    int runs = 5;

    // Warm-up (keeps consistency with Python benchmarks)
    auto init_start = std::chrono::high_resolution_clock::now();
    count_words(text);
    auto init_end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> init_duration = init_end - init_start;
    std::cout << init_duration.count() << std::endl;

    double total_duration = 0;
    for (int i = 0; i < runs; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        count_words(text);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        total_duration += duration.count();
    }
    double average_duration = total_duration / runs;

    std::cout << average_duration << std::endl;

    return 0;
}
