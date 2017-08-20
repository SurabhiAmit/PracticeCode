Grocery class:-

package com.company;

import java.util.Scanner;
import java.util.ArrayList;

public class Grocery
{
    public static void main(String[] args)
    {
        Scanner get = new Scanner(System.in);
        ArrayList<String> checklist = new ArrayList<String>();
        checklist.add("Tomato");
        checklist.add("Brinjal");
        checklist.add("Potato");
        checklist.add("Watermelon");
        checklist.add("Papaya");
        System.out.println("Now, the grocery items in the checklist is : "+checklist.toString());
        String next = "quit";
       do{
            System.out.println("Enter another item or enter quit : ");
            next = get.nextLine();
            if (!next.equalsIgnoreCase("quit"))
            {
            search(checklist,next);
            }
       }while(!next.equalsIgnoreCase("quit"));
            System.out.println("Now, the grocery items in the checklist are:");
            for(int i=0;i<checklist.size();i++)
            {
                System.out.println(checklist.get(i));
            }
    }

    public static void search(ArrayList<String> checklist, String item)
    {   Boolean found = false;
        for (int i=0;i < checklist.size() ;i++)
        {
           if (item.equalsIgnoreCase(checklist.get(i)))
           {
               System.out.println("This item is already in the checklist!");
               found=true;
               break;
           }
        }

        if (!found)
        {
            System.out.println("The item is not found in the checklist, hence adding it now!");
            checklist.add(item);
        }
    }


}

Item.java file :-

package com.company;

public class Item {
    private int name;
}


OUTPUT :-

Now, the grocery items in the checklist is : [Tomato, Brinjal, Potato, Watermelon, Papaya]
Enter another item or enter quit : 
potato
This item is already in the checklist!
Enter another item or enter quit : 
banana
The item is not found in the checklist, hence adding it now!
Enter another item or enter quit : 
quit
Now, the grocery items in the checklist are:
Tomato
Brinjal
Potato
Watermelon
Papaya
banana
