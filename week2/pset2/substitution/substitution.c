#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

//Function to encipher
void encipher(string key, string text);

int main(int argc, string argv[])
{
    //to check if they provided key
    if (argc != 2)
    {
        printf("usage: ./substitution KEY\n");
        return 1;
    }
    //to see if the key is long enough
    int n = strlen(argv[1]);
    if (n != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        //to validate all the alphabets
        if (!isalpha(argv[1][i]))
        {
            printf("Key must only contain alphabetic characters\n");
            return 1;
        }
        //to check repetation
        for (int j = i + 1; j < n; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Key must not contain repeated characters\n");
                return 1;
            }
        }
    }
    //get user input
    string pt = get_string("plaintext: ");
    printf("ciphertext: ");
    //a function to encipher the given text
    encipher(argv[1], pt);
    return 0;
}

void encipher(string key, string text)
{
    //to get the length
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        //if the text is upper
        if (isupper(text[i]))
        {
            //print should also be in upper case
            printf("%c", toupper(key[text[i] - 65]));
        }
        //if the text is in lower
        else if (islower(text[i]))
        {
            //then the print should also be in lower case
            printf("%c", tolower(key[text[i] - 97]));
        }
        //else print as it is
        else
        {
            printf("%c", text[i]);
        }
    }
    //newline as the enciphering ended
    printf("\n");
}