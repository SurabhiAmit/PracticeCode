package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
      System.out.println("Please enter the limit:");
      Scanner get = new Scanner(System.in);
      int limit = get.nextInt();
      int count=0;

      //do-while loop
      do{
          count++;
      }while(count<limit);

      System.out.println("The result of do-while loop with limit "+limit+" is "+count);
        count=0;

      //while loop
        while(count<limit)
        {
            count++;
        }

        System.out.println("The result of while loop with limit "+limit+" is "+count);
        count=0;

      //for loop
        for(int i=0;i<limit;i++)
        {
            count++;
        }
        System.out.println("The result of for loop with limit "+limit+" is "+count);
    }
}

OUTPUT:-

Please enter the limit:
12
The result of do-while loop with limit 12 is 12
The result of while loop with limit 12 is 12
The result of for loop with limit 12 is 12