package com.company;

import java.util.Scanner;

public class Arrays
{

    public static void main(String[] args)
    {
        Scanner get = new Scanner(System.in);
        double prices[][] = new double[4][2];
        for(int i=0;i<4;i++)
        {
        System.out.println("Enter the original price");
        prices[i][0]= get.nextDouble();
        prices[i][1] = .7* prices[i][0];

        }
        for (int i=0;i<4;i++)
        {
            System.out.println("Original Price is $"+prices[i][0]+"\t Discounted price is $"+prices[i][1]);
        }

        }
        }

OUTPUT:-

Enter the original price
20
Enter the original price
30
Enter the original price
40
Enter the original price
65
Original Price is $20.0	 Discounted price is $14.0
Original Price is $30.0	 Discounted price is $21.0
Original Price is $40.0	 Discounted price is $28.0
Original Price is $65.0	 Discounted price is $45.5