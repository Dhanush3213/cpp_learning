#include <iostream>
#include <set>

int main() {
    std::set<int> mySet = {1, 2, 3, 4, 5};

    int target = 3;

    // Perform binary search
    auto found = mySet.find(target) != mySet.end();

    std::cout << "Target found: " << (found ? "Yes" : "No") << std::endl;

    return 0;
}
