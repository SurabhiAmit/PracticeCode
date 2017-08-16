package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        double req_area,total_windows_size,total_door_size,length,breadth,height;
        int windows_num,doors_num;
        System.out.println("Enter the length,breadth,height of house to be painted, in metres : ");
        Scanner in= new Scanner(System.in);
        length=in.nextDouble();
        breadth=in.nextDouble();
        height=in.nextDouble();
        double total_area=(2*length*height)+(2*breadth*height);
        System.out.println("Enter the number, height and width of windows in metres : ");
        windows_num=in.nextInt();
        double window_height=in.nextDouble();
        double window_width=in.nextDouble();
        double total_window_area= windows_num * window_height * window_width;
        System.out.println("Enter the number, height and width of doors in metres : ");
        doors_num=in.nextInt();
        double door_height=in.nextDouble();
        double door_width=in.nextDouble();
        double total_door_area=doors_num * door_height * door_width;
        req_area=total_area-total_window_area-total_door_area;
        System.out.println("The total surface area to be painted is "+req_area+ " sq.metres");
        System.out.println("Enter the coverage area in sq.metres of one gallon of paint : ");
        double coverage_area=in.nextDouble();
        double req_paint=req_area/coverage_area;
        System.out.println("Amount of paint required is "+req_paint+" gallons");

    }
}

OUTPUT:-

Enter the length,breadth,height of house to be painted, in metres : 
47
43
12
Enter the number, height and width of windows in metres : 
4
6
7
Enter the number, height and width of doors in metres : 
2
8
4
The total surface area to be painted is 1928.0 sq.metres
Enter the coverage area in sq.metres of one gallon of paint : 
54
Amount of paint required is 35.7037037037037 gallons
