#include <stdio.h>
#include <math.h>

int main() {
    int N;
    int K;

    scanf("%d", &N);
    scanf("%d", &K);

    N = N / 2;
    printf("%d", N);
    printf("%d", floor(N));

    return 0;
}
