#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* transformToBinary(int number, int* len) {
    int ret[100 + 1] = {0};
    int count = 0;
    while (number)
    {
        if (number % 2 == 0) {
            ret[count] = 0;
        } else {
            number--;
            ret[count] = 1;
        }
        number = number / 2;
        count++;
    }
    *len = count;
    return ret;
}

void displayBinary(int* array, int len) {
    for (int i = 0; i < len; i++)
    {
        printf("%d",array[(len-1)-i]);
    }
    printf("\n");
}



int countOnes(int* array, int len) {
    int ret = 0;
    for (int i = 0; i < len; i++)
    {
        if (array[i] == 1) {
            ret++;
        }
    }
    return ret;
}

int increaseUntilSameOnesNumber(int x, int nbOnes) {
    int ret = 0;
    int len = 0;
    int tmp = 0;
    while (1)
    {
        x++;
        int* array = transformToBinary(x, &len);
        tmp = countOnes(array, len);
        if (tmp == nbOnes) {
            displayBinary(array, len);
            ret = x;
            break;
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    char* p;
    int x = 0;
    long conv = strtol(argv[1], &p, 10);
    if (*p != '\0' || conv > INT64_MAX || conv < INT64_MIN) {
        printf("Le nombre donné n'a pas été reconnu\n");
        return 1;
    } else {
        x = conv;
    }
    int len;
    int* array = transformToBinary(x, &len);
    displayBinary(array, len);
    int nbOnes = countOnes(array, len);
    int ret = increaseUntilSameOnesNumber(x,nbOnes);
    printf("%d\n",ret);
    return 0;
}
