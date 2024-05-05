// Implements a dictionary's functionality
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
//copied from stack overflow because strcasecmp was giving error despite adding the header

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int total = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *cursor = table[hash(word)];
    while (cursor != NULL)
    {
        //true if word is there
        //case insensitive
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    //false if it is not
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int sum = 0;
    unsigned int size = strlen(word);
    for (int i = 0; i < size; i += 3)
    {
        sum = sum + tolower(word[1]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open file and read
    FILE *f = fopen(dictionary, "r");
    //bool value for memory error
    if (f == NULL)
    {
        return false;
    }
    char word0[LENGTH + 1];
    //read strings from file
    //loop through every data
    while (fscanf(f, "%s", word0) != EOF)
    {
        //malloc data for new memory
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        //hash the string and add to corresponding bucket OF LINKED LIST
        int index = hash(word0);
        strcpy(n->word, word0);
        //insert
        n->next = table[index];
        table[index] = n;
        total++;
    }
    fclose(f);
    return true;
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return total;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{

    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *temp = table[i]->next;
            free(table[i]);
            table[i] = temp;
        }
    }
    return true;
}