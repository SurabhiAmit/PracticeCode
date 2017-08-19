package com.company;

public class Sorting {


    public static void main(String[] args)
    {

        //Selection sort

        int[] numbers = {2, 8, 4, 3, 5, 9, 2};
        ascend(numbers);
        System.out.println("Ascending sort");
        for (int i = 0; i < numbers.length; i++)
        {
            System.out.println(numbers[i] + "\t");
        }
        descend(numbers);
        System.out.println("Descending sort");
        for (int i = 0; i < numbers.length; i++)
        {
            System.out.println(numbers[i] + "\t");
        }

    }

    public static void ascend(int[] num) {
        int i, j, temp;
        for (i = 0; i < num.length; i++) {
            for (j = i+1; j < num.length; j++) {
                if (num[j] < num[i]) {
                    temp = num[j];
                    num[j] = num[i];
                    num[i] = temp;
                }
            }
        }
    }

    public static void descend(int[] num) {
        int i, j, temp;
        for (i = num.length - 1; i > 0; i--) {
            for (j = i-1; j >= 0; j--) {
                if (num[j] < num[i]) {
                    temp = num[j];
                    num[j] = num[i];
                    num[i] = temp;
                }
            }
        }
    }

}
OUTPUT:-

Ascending sort
2	
2	
3	
4	
5	
8	
9	
Descending sort
9	
8	
5	
4	
3	
2	
2	
