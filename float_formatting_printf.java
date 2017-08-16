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
        /* in %a.bf, a is number of total digits in that decimal number (ie,n) including decimal point,
        b is number of digits after decimal point(padding zeroes to right of it).
        so if %10.2f is used for a double with 3 digits and no digit after decimal point,
        2 zeroes will be padded to right of decimal point
        rest 10-2-decimal point-3 digits = 4 spaces would be present at its front,
        if just %10f then extra space will be as padding zeroes after decimal point*/
        System.out.printf(" You spent $%5.2f at %s",total,place);
        System.out.printf(" \n You spent $%10.2f at %s",total,place);
        System.out.printf(" \n You spent $%5f at %s",total,place);
        System.out.printf(" \n You spent $%f at %s",total,place);

    }
}

OUTPUT

Input the price of 3 items : 
3
2.9
4.50
Enter shopping place
Keller
 You spent $10.40 at Keller 
 You spent $     10.40 at Keller 
 You spent $10.400000 at Keller 
 You spent $10.400000 at Keller
