package com.company;
import java.util.Scanner;
import java.util.Random;
public class Main{

    public static void main(String[] args){
        System.out.println("Enter number of throws you want to perform on this die : ");
        Scanner obtain = new Scanner(System.in);
        int num=obtain.nextInt();
        Random rand=new Random();
        int countdoubles=0,prev=0,die;

        for(int i=0;i<num;i++){
            die = rand.nextInt(5)+1;
            if (prev==die)
            {
                countdoubles++;
            }
            prev= die ;
        }
        System.out.println("I got " +countdoubles+ " number of doubles in "+num +" throws!!");
    }
}

OUTPUT:-

Enter number of throws you want to perform on this die : 
54
I got 11 number of doubles in 54 throws!!


