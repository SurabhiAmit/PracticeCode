package com.company;
import java.util.Scanner;
public class Scanning {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        double[] prices =new double[3];
        System.out.println("Input the price of 3 items : ");
        prices[0]=in.nextDouble();
        prices[1]=in.nextDouble();
        prices[2]=in.nextDouble();
        System.out.println("Enter shopping place");
        String place = in.next();
        double total=prices[0]+prices[1]+prices[2];
        /* in %xs, x is number of total characters in that string (ie,n), 
        so if %10s is used for a string with 3 characters, 
        7 spaces would be present at its front, if x is less than or equal to n, 
        then no difference to string(no spaces added)*/
        System.out.printf(" You spent $%5.2f at %10s",total,place);
        System.out.printf(" \n You spent $%5.2f at %1s",total,place);
        System.out.printf(" \n You spent $%5.2f at %6s",total,place);
        System.out.printf(" \n You spent $%5.2f at %s",total,place);

    }
}


OUTPUT

Input the price of 3 items : 
43
23.65
9.99
Enter shopping place
Dubai
 You spent $76.64 at      Dubai 
 You spent $76.64 at Dubai 
 You spent $76.64 at  Dubai 
 You spent $76.64 at Dubai