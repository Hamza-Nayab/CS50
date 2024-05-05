#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h > 8 || h < 1);
    // to get desired info


    //first iteration for main loop
    for (int i = 1; i <= h; i++)
    {
        //for spaces
        for (int j = 0; j < h - i; j++)
        {
            printf(" ");
        }
        //for main blocks
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        //new line after completion
        printf("\n");
    }
}