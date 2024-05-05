#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


int main(void)
{
    //getting input
    string s = get_string("Text: ");
    //ints decleration
    int let = 0, word = 1, sen = 0;
    //loop to check each char of string
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        //to check if they're alphabets
        if (isalpha(s[i]))
        {
            let++;
        }
        //to check if it's a word
        else if (isspace(s[i]))
        {
            word++;
        }
        //to check if it's a sentence
        else if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            sen++;
        }
    }
    //applying colemen liau index
    int grade = round((0.0588 * let / word * 100) - (0.296 * sen / word * 100) - 15.8);
    //checking if it's smaller than 1
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    //checking if it's larger than 16
    else if (grade > 15)
    {
        printf("Grade 16+\n");
    }
    //declearing grade
    else
    {
        printf("Grade %i\n", grade);
    }
    return 0;
}