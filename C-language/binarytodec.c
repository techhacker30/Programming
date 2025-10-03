#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>  // for true/false

int main() {
    char bno[100];
    int decno, lenno;

    printf("\n===================================================");
    printf("\n           Binary to Decimal Converter             ");
    printf("\n===================================================\n");

    while (true) {
        printf("\nEnter Binary Number: ");
        scanf("%s", bno);

        if (strlen(bno) == 0) {
            printf("\nEnter a Valid Number!\n");
            break;
        }

        lenno = strlen(bno);
        decno = 0;

        // Convert binary to decimal
        for (int i = 0; i < lenno; i++) {
            if (bno[i] != '0' && bno[i] != '1') {
                printf("\nInvalid binary digit found!\n");
                decno = -1;
                break;
            }
            decno = decno * 2 + (bno[i] - '0');
        }

        if (decno != -1) {
            printf("Decimal Number is: %d\n", decno);
        }
        break;  // stop after one conversion (remove this if you want loop)
    }
    return 0;
}

