package com.company;

import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner get = new Scanner(System.in);
        boolean repeat=false;
        do
            {
                System.out.println("Are you admitted for an overnight stay? Enter true or false ");
                boolean reply = get.nextBoolean();
                if(reply==true)
                {
                    System.out.println("Please enter the hospital overnight charges, medication charges and lab service charges : ");
                    double overnight = get.nextDouble();
                    double medication = get.nextDouble();
                    double lab = get.nextDouble();
                    double total_charges = overnight+medication+lab;
                    System.out.printf("The total expenses amount to $%7.2f",total_charges);
                }
                else if(reply==false)
                {
                    System.out.println("Please enter the medication charges and lab service charges : ");
                    double medication = get.nextDouble();
                    double lab = get.nextDouble();
                    double total_charges = medication+lab;
                    System.out.printf("The total expenses amount to $%7.2f",total_charges);
                }

            System.out.println("\n Do you want to compute expenses for another patient? Enter true or false .");
            repeat = get.nextBoolean();
            } while (repeat);
    }
}

OUTPUT:-

Are you admitted for an overnight stay? Enter true or false 
true
Please enter the hospital overnight charges, medication charges and lab service charges : 
123.87
786.43
987.32
The total expenses amount to $1897.62
 Do you want to compute expenses for another patient? Enter true or false .
true
Are you admitted for an overnight stay? Enter true or false 
false
Please enter the medication charges and lab service charges : 
897.32
789.21
The total expenses amount to $1686.53
 Do you want to compute expenses for another patient? Enter true or false .
false
