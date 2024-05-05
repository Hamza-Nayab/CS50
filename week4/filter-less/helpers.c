#include "helpers.h"
#include "math.h"
#include "string.h"


//to check if everything is in limit
int max(int a)
{
    if (a > 255)
    {
        return 255;
    }
    else
    {
        return a;
    }
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // to calculate avg
    float avg;
    for (int i = 0; i < height; i++)
    {
        // to go through every pixel
        for (int j = 0; j < width; j++)
        {
            //to take sum and then avg
            avg = round(((float)image[i][j].rgbtRed + (float)image[i][j].rgbtBlue + (float)image[i][j].rgbtGreen) / 3);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // applying sepia formula
            int sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            //applying max fuction to act as upper limit
            image[i][j].rgbtRed = max(sepiaRed);
            image[i][j].rgbtGreen = max(sepiaGreen);
            image[i][j].rgbtBlue = max(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            //using temp to swap opposite values
            RGBTRIPLE temp;
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    //to make a copy
    memcpy(temp, image, sizeof(RGBTRIPLE) * height * width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //for the counting of sums
            float sumR, sumG, sumB, count;
            sumR = sumG = sumB = count = 0;
            //to check 3 x 3 values and taking avg
            for (int x = - 1; x <  2; x++)
            {
                for (int y = - 1; y < 2; y++)
                {
                    // for corner cases and sides
                    if (i + x < 0 || i + x >= height || j + y < 0 || j + y >= width)
                    {
                        continue;
                    }
                    sumR += temp[i + x][j + y].rgbtRed;
                    sumG += temp[i + x][j + y].rgbtGreen;
                    sumB += temp[i + x][j + y].rgbtBlue;
                    count++;
                }
            }
            image[i][j].rgbtRed = round(sumR / count);
            image[i][j].rgbtGreen = round(sumG / count);
            image[i][j].rgbtBlue = round(sumB / count);
        }
    }
    return;
}
