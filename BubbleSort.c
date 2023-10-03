#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], char * s, int arrSize);
int * bubbleSort(int arr[], int arrSize);
int userInput(void);

int main(int argc, char * argv[])
{
    if (argc != 2)
    {
        printf("Error: Array size needed\n");
        printf("Usage: ./bubbleSort arraySize\n");
        return 1;
    }


    int arraySize = atoi(argv[1]);
    int array[arraySize];

    printf("Thank you for selecting to sort an array of length %i.\n", arraySize);
    printf("Please enter %i integers to add to your array.\n", arraySize);

    for (int i = 0; i < arraySize; i++)
    {
        array[i] = userInput();
    }

    printArray(array, "Unsorted: ", arraySize);

    bubbleSort(array, arraySize);

    printArray(array, "Bubble sorted: ", arraySize);
}

int * bubbleSort(int arr[], int length)
{
    int swap;
    for (int i = 0; i < length - 1; i++)
    {
        for (int j = 0; j < length - i - 1; j++)
        {
            if(arr[j] > arr[j + 1])
            {
                swap = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = swap;
            }
        }
    }
    return arr;
}

int userInput(void)
{
    int myNum;
    printf("Append to array, an int: ");
    scanf("%d", &myNum);
    return myNum;
}

void printArray(int arr[], char * s, int arraySize)
{
    printf("%s", s);
    for (int k = 0; k < arraySize; k++)
    {
        printf("%i,", arr[k]);
    }
    printf("\n");
}

