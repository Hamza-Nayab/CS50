#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //prompt for name
    string name = get_string("What's your name? ");
    //get the name and say hello to it
    printf("hello, %s\n", name);
}