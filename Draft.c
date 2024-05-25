#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

float random_float() {
    // Générer un nombre entier aléatoire dans la plage complète des valeurs possibles de int
    int random_int = rand();

    // Normaliser le nombre entier pour obtenir un nombre flottant dans l'intervalle [0, 1)
    float random_float = (float)random_int / (RAND_MAX + 1);

    return random_float;
}

int main() {
    // Initialiser la graine aléatoire
    srand(time(NULL));
    printf("%d\n",RAND_MAX);

    // Générer et imprimer un nombre flottant aléatoire entre 0 et 1
    float random_number = random_float();
    printf("Random number: %f\n", random_number);

    return 0;
}