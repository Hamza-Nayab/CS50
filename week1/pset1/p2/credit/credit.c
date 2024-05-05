#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long a = get_long("Number = ");
    long cn = a;
    int i = 0;
    do
    {
        cn = cn / 10;
        i++;
    }
    while (cn > 0);
    if (i == 13 || i == 15 || i == 16)
    {
        long x = a;
        int sum = 0, sum1, total, rem1;
        do
        {
            //remove last digit add add to sum
            rem1 = x % 10;
            x = x / 10;
            sum += rem1;
            rem1 = x % 10;
            x = x / 10;
            rem1 = rem1 * 2;
            sum = sum + (rem1 % 10);
            sum = sum + (rem1 / 10);
        }
        while (x > 0);
        //remove second last digit and add
        //double the second last and add
        long q = a;
        if (sum % 10 == 0)
        {
            //american express 15 digits, start 34 or 37
            if (q / 10000000000000 == 34 || q / 10000000000000 == 37)
            {
                printf("AMEX\n");
            }
            //visa 13 or 16 digits starts with 4
            else if (q / 1000000000000000 == 4 || q / 1000000000000 == 4)
            {
                printf("VISA\n");
            }
            else if (50 < q / 100000000000000 && 56 > q / 100000000000000)
                //master card 16 digits, starts 51 to 55
            {
                printf("MASTERCARD\n");
            }
            // for 3rd condition
            else
            {
                printf("INVALID\n");
            }
        }
        //for second condition
        else
        {
            printf("INVALID\n");
        }

    }
    else
        //for first condition
    {
        printf("INVALID\n");
    }
}