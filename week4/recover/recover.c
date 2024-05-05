#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //to check for invalid input
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    //loading file to infile
    FILE *input = fopen(argv[1], "r");
    //file counter for name
    int filec = 0;
    FILE *pic;
    //to check for the first jpeg
    bool jpeg = false;
    //size of a buffer
    BYTE buffer[512];
    //reading from input into the buffer
    while (fread(&buffer, 512, 1, input) == 1)
    {
        //checking if the jpeg is found or not
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //closing the previous file
            if (jpeg == true)
            {
                fclose(pic);
            }
            //for name
            char filen[8];
            sprintf(filen, "%03i.jpg", filec);
            pic = fopen(filen, "a");
            filec++;
            //indicating that the file is found
            jpeg = true;
        }
        if (jpeg == true)
        {
            //writing after the file is found
            fwrite(&buffer, 512, 1, pic);
        }
    }
    fclose(input);
    fclose(pic);
}