#include <algorithm>
#include <array>
#include <charconv>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <omp.h>
#include <vector>

int main()
{
    uint64_t min_loc = ~0U;

    std::ifstream file{"data.txt"};
    file.seekg(0, std::ios::end);
    std::string data(file.tellg(), 0);
    file.seekg(0, std::ios::beg);
    file.read(data.data(), data.size());

    std::vector<uint64_t> seeds;
    size_t c = 0;

    while (data[c] != ':')
        ++c;
    ++c;

    while (data[c] != '\n')
    {
        size_t i = ++c;
        while (std::isdigit(data[c]))
            ++c;

        std::from_chars(&data[i], &data[c], seeds.emplace_back());
    }
    seeds.shrink_to_fit();

    std::array<std::vector<std::array<uint64_t, 3>>, 7> tables;

    for (size_t i = 0; i < tables.size(); ++i)
    {
        size_t j;

        c += 2;
        while (data[c] != '\n')
            ++c;

        do
        {
            tables[i].emplace_back();

            j = ++c;
            while (std::isdigit(data[c]))
                ++c;
            std::from_chars(&data[j], &data[c], tables[i].back()[0]);

            j = ++c;
            while (std::isdigit(data[c]))
                ++c;
            std::from_chars(&data[j], &data[c], tables[i].back()[1]);

            j = ++c;
            while (std::isdigit(data[c]))
                ++c;
            std::from_chars(&data[j], &data[c], tables[i].back()[2]);
        } while (data[c + 1] != '\n');
    }

    for (auto &&seed : seeds)
    {
        uint64_t loc = seed;

        for (auto &&table : tables)
            for (auto &&[d, s, r] : table)
                if (s <= loc && loc < s + r)
                {
                    loc = d + loc - s;
                    break;
                }

        if (loc < min_loc)
            min_loc = loc;
    }

    std::cout << "Best location = " << min_loc << '\n';

    int num_threads = seeds.size() >> 1;
    omp_set_num_threads(num_threads);
    std::vector<uint64_t> min_locs(num_threads, ~0U);

#pragma omp parallel
    {
        int i = omp_get_thread_num();
        uint64_t start = seeds[2 * i];
        uint64_t n = seeds[2 * i + 1];
        uint64_t per = 0;
        std::string prefix;
        std::string suffix;

        for (size_t j = 0; j < i; ++j)
            prefix += "     ";

        for (size_t j = i + 1; j < num_threads; ++j)
            suffix += "     ";

        for (uint64_t seed = start; seed < start + n; ++seed)
        {
            uint64_t loc = seed;

            for (auto &&table : tables)
                for (auto &&[d, s, r] : table)
                    if (s <= loc && loc < s + r)
                    {
                        loc = d + loc - s;
                        break;
                    }

            if (loc < min_locs[i])
                min_locs[i] = loc;
            if ((seed + 1 - start) * 100 / n > per)
            {
                ++per;
#pragma omp critical
                {
                    std::cout << prefix << std::setw(3) << per << "% " << suffix << '\n';
                    std::cout.flush();
                }
            }
        }
    }
    std::cout << '\n';

    min_loc = *std::ranges::min_element(min_locs);

    std::cout << "Best location = " << min_loc << '\n';

    return 0;
}
