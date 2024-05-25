#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

// Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 
// For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], 
// return [(-1, -1), (1, 1)].


const int ARRAY_LENGTH_MIN = 1;
const int ARRAY_LENGTH_MAX = 20;
const int COORDINATE_OBJECT_WIDTH = 2;

int main(int argc, char const *argv[])
{
    srand(time(0));
    int arraySize = rand() % (ARRAY_LENGTH_MAX - ARRAY_LENGTH_MIN +1) + ARRAY_LENGTH_MIN;
    printf("%d\n",arraySize);
    int ** array = malloc(arraySize * sizeof(int *));
    if (array == 0)
    {
        printf("Erreur d'initialisation du tableau\n");
        return 1;
    } else {
        for (int i = 0; i < arraySize; i++)
        {
            array[i] = malloc(COORDINATE_OBJECT_WIDTH * sizeof(int));
            if (array[i] == 0)
            {
                printf("Erreur d'initialisation du tableau\n");
                return 1;
            } else {
                array[i][0] = rand() % 10;
                array[i][1] = rand() % 10;
            }
        }
    }
    printf("[");
    for (int i = 0; i < arraySize; i++)
    {
        printf("{%d,%d},",array[i][0],array[i][1]);
    }
    printf("]\n");

    int firstPoint[2];
    int secondPoint[2];
    double distance = -1.0;
    for (int i = 0; i < arraySize; i++)
    {
        for (int j = i+1; j < arraySize; j++)
        {
            double tmp = sqrt(pow(array[i][0]-array[j][0],2) + pow(array[i][1]-array[j][1],2));
            if (tmp < distance || distance == -1.0)
            {
                distance = tmp;
                firstPoint[0] = array[i][0];
                firstPoint[1] = array[i][1];
                secondPoint[0] = array[j][0];
                secondPoint[1] = array[j][1];
            }
        }
    }
    printf("[{%d,%d},{%d,%d}]\n",firstPoint[0],firstPoint[1],secondPoint[0],secondPoint[1]);
    return 0;
}
