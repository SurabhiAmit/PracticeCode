package com.company;

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;


public class Fileread {

    public static void main(String[] args) {
        File input = new File("/Users/amit/IdeaProjects/TestApp/src/com/company/trial.txt");
        Scanner get = null;

        try {
            get = new Scanner(input);
        }
        catch (Exception e) {
            e.toString();
        }

        ArrayList<String>  replies = new ArrayList<String>();
        String answer;

        try {
            while (get.hasNextLine()) {
                answer = get.nextLine();
                replies.add(answer);

            }
        }
           catch(Exception e)
            {
                System.out.println("The input file \"trial.txt\" is not found");
                System.out.println(e.toString());
            }
            System.out.println("The fortune teller is ready. Ask any question and then press enter");
            Scanner in = new Scanner(System.in);
            in.nextLine();
            Random num = new Random();
            System.out.println("The answer is : "+replies.get(num.nextInt(replies.size())));

        }
    }


trial.txt file :- 

I don't know
I won't say
Don't ask me
Yes, no doubt
Never ever
Certainly yes
Absolutely no
Hell yeah!


OUTPUT :-

The fortune teller is ready. Ask any question and then press enter

The answer is : I won't say
