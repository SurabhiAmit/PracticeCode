USING DESIGN PATTERNS
SINGLETON

There are two java files as there are two classes:-


// Main.java file with Main class

package com.company;


public class Main
{
    public static void main(String[] args)
    {
       Mysingleton single = Mysingleton.getInstance();
       System.out.println(single.status());

       //  the below one line can replace the above two lines
       System.out.println(Mysingleton.getInstance().status());

    }
}

// Mysingleton.java file with Mysingleton class

package com.company;

public class Mysingleton{

    //place-holder for the single object and has to be static, 
    // so as to be used by the static method coming later
    private static Mysingleton me;

    //constructor for single object
    private Mysingleton(){ }

    //lazy initiation - initiating(creating object) only after first customer comes in,
    // not keeping it ready before the first one asks
    //but for second customer onwards, this single object is ready to use prior to them asking for it.

    //make this method static so that it can be called without creating an object of this class
    // as no objects of this class can be created outside this class
    // (this class cannot have more than one object and 
    //this single object will be created inside this class using private constructor)

    public static Mysingleton getInstance(){
        if (me==null)
            me=new Mysingleton();
        return me;
    }
    public String status(){
        return"Hurray!! I got my Singleton!";
    }
}


OUTPUT:-

Hurray!! I got my Singleton!
Hurray!! I got my Singleton!
