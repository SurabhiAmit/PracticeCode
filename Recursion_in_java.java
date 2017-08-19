package com.company;

import java.util.Scanner;

public class Recursive {
    public static void main(String[] args) {
        Scanner get = new Scanner(System.in);
        System.out.println("Enter the countdown limit : ");
        int num = get.nextInt();
        countdown(num);
    }

    public static void countdown(int number) {
        if (number == 0)
            System.out.println("Blast Off!!");
        else {
            System.out.println(number);
            countdown(number - 1);
        }
    }
}

OUTPUT :-

Enter the countdown limit : 
10
10
9
8
7
6
5
4
3
2
1
Blast Off!!
