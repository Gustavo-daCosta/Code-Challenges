#include <iostream>

int main() {
    double continuosFraction = 1 / (1 + 1);

    int n = 2;

    double pn;
    for (int i = 0; i < n; i++) {
        continuosFraction = 1 / (1 + continuosFraction);
    }

    printf("Pn = %f", pn);
}