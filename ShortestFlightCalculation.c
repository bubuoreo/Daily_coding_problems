#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// You are given a huge list of airline ticket prices between different cities around the world on a given day.
// These are all direct flights. Each element in the list has the format (source_city, destination, price).

// Consider a user who is willing to take up to k connections from their origin city A to their destination B.
// Find the cheapest fare possible for this journey and print the itinerary for that journey.

// For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are 
// as follows:
// [
//     ('JFK', 'ATL', 150),
//     ('ATL', 'SFO', 400),
//     ('ORD', 'LAX', 200),
//     ('LAX', 'DFW', 80),
//     ('JFK', 'HKG', 800),
//     ('ATL', 'ORD', 90),
//     ('JFK', 'LAX', 500),
// ]
// Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.

const int DESCRIPTION_ELEMENT_SIZE = 3;

// void displayList(char* array[][DESCRIPTION_ELEMENT_SIZE], int arrayLength) {
//     for (int i = 0; i < arrayLength; i++) {
//         for (int j = 0; j < DESCRIPTION_ELEMENT_SIZE; j++) {
//             printf("%s, ", array[i][j]);
//         }
//         printf("\n");
//     }
// }

void displayList(char* array[][DESCRIPTION_ELEMENT_SIZE], int arrayLength) {
    for (int i = 0; i < arrayLength; i++) {
        printf("%s->%s %s$", array[i][0], array[i][1], array[i][2]);
        printf("\n");
    }
}

char* recursiveHelper(char* array[][DESCRIPTION_ELEMENT_SIZE], char* startingPoint, int currentFlightsPlanned, int maxFlightsAllowed, int arrayLength) {
    char* ret = (char*)malloc(100);
    if (currentFlightsPlanned >= maxFlightsAllowed)
    {
        return "";
    }
    for (int i = 0; i < arrayLength; i++)
    {
        if (strncmp(array[i][0],startingPoint,3) == 0)
        {
            printf("%s c'est ok\n",array[i][0]);
        }
    }
    return ret;
}

void findTrip(char* array[][DESCRIPTION_ELEMENT_SIZE], char* A, char* B, int k, int arrayLength) {
    printf("Le client souhaite effectuer le voyage : %s -> %s.\n", A, B);
    printf("Trouvons le meilleur prix en effectuant au maximum %d changements.\n",k);
    char* result = recursiveHelper(array,A,0,k+1,arrayLength);
    free(result);
}

int main(int argc, char const *argv[]) {
    char* flightTickets[7][DESCRIPTION_ELEMENT_SIZE] = {
        {"JFK", "ATL", "150"},
        {"ATL", "SFO", "400"},
        {"ORD", "LAX", "200"},
        {"LAX", "DFW", "80"},
        {"JFK", "HKG", "800"},
        {"ATL", "ORD", "90"},
        {"JFK", "LAX", "500"}
    };
    int maxConnectionNbAllowed = 3;
    char origin[] = "JFK";
    char destination[] = "LAX";
    // displayList(flightTickets, sizeof(flightTickets) / sizeof(flightTickets[0]));
    findTrip(flightTickets, origin, destination, maxConnectionNbAllowed, sizeof(flightTickets) / sizeof(flightTickets[0]));
    return 0;
}

