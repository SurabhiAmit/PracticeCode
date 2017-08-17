Create 2 java files under same package, each saved with their respective class names.


Movie.java:-

package com.company;

 public class Movie
 {
     private String movieName;
     private String rating;
     private int year;
     private int runTime;

     public Movie(String movieName,String rating,int year,int runTime)
     {
         this.movieName = movieName;
         this.rating = rating;
         this.year = year;
         this.runTime = runTime;
     }

      public String toString()
     {
          return "Movie name :" +movieName +"\nMovie rating : "+rating
                  + "\nYear of release : "+year+" \nMovie runtime in minutes : " + runTime;
     }

     }

Main.java:-


package com.company;

import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner get = new Scanner(System.in);
        System.out.println("Please enter the movie name : ");
        String movieName = get.nextLine();
        System.out.println("Please enter the movie rating : ");
        String rating = get.next();
        System.out.println("Please enter the year in which movie was released : ");
        int year = get.nextInt();
        System.out.println("Please enter the runtime of movie in minutes : ");
        int runTime = get.nextInt();
        Movie film = new Movie(movieName,rating,year,runTime);
        //String result = film.toString();
        System.out.println(film.toString());

    }
}


OUTPUT:-

Please enter the movie name : 
Love is the new sunshine
Please enter the movie rating : 
PG
Please enter the year in which movie was released : 
2014
Please enter the runtime of movie in minutes : 
130
Movie name :Love is the new sunshine
Movie rating : PG
Year of release : 2014 
Movie runtime in minutes : 130