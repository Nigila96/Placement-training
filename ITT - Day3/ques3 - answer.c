#include <stdio.h>

int main() {
    int num;
    int count = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    // 0 has no 1's, so it is invalid
    if (num <= 0) {
        printf("Invalid input.\n");
        return 0;
    }

    printf("Binary digits (reversed): ");
    while (num > 0) {
        int remainder = num % 2;
        printf("%d", remainder);
        
        if (remainder == 1) {
            count++;
        }
        num = num / 2;
    }
    printf("\n");

    printf("Count of 1's: %d\n", count);

    return 0;
}
