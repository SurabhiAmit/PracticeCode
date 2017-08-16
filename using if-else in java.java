package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
      System.out.println("Please enter the total cost:");
      Scanner get = new Scanner(System.in);
      double totalcost = get.nextDouble();
      if (totalcost < 30)
      {
            totalcost+=5;
                            }
      else if (totalcost<60)
      {
          totalcost += 10;
                            }
      else if (totalcost<90)
      {
          totalcost+=15;
      }
      System.out.printf("The total cost including shipping is $%5.2f.",totalcost);

    }
}

OUTPUT :-

Please enter the total cost:
57
The total cost including shipping is $67.00.