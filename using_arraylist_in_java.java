# Property.java file

package com.company;

public class Property
{
    private int price;
    private int bed_num;
    private int bath_num;
    private int size;
    private String type;

    public Property(int price, String type, int size)
    {
        this.price = price;
        this.type = type;
        this.size = size;

    }
    public Property(int price, String type, int size, int bed_num, int bath_num)
    {
        this(price,type,size);
        this.bed_num = bed_num;
        this.bath_num = bath_num;
    }

    public String toString()
    {
        return "\nAsking price : "+price+ "\nType of property : "+type+
                "\nLot size : "+size+"\nNumber of bedrooms : "+
                bed_num+"\nNumber of bathrooms : "+bath_num;
    }

}

# Arraylist.java file

package com.company;

        import java.util.ArrayList;

public class Arraylist {

    public static void main(String[] args){
        ArrayList<Property> myList = new ArrayList<Property>();
        Property obj1 = new Property(121000,"Land",21);
        myList.add(obj1);
        obj1 = new Property(293100,"Estate",16,3,4);
        myList.add(obj1);
        System.out.println(myList.toString());
    }
}


OUTPUT :-

[
Asking price : 121000
Type of property : Land
Lot size : 21
Number of bedrooms : 0
Number of bathrooms : 0, 
Asking price : 293100
Type of property : Estate
Lot size : 16
Number of bedrooms : 3
Number of bathrooms : 4]