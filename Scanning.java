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
        System.out.printf(" You spent $%5.2f at %s",total,place);
       

    }
}

OUTPUT:

Input the price of 3 items : 
32.9
4.65
2
Enter shopping place
Kroger
 You spent $39.55 at Kroger