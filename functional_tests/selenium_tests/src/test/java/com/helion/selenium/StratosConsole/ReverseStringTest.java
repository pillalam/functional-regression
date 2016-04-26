package com.helion.selenium.StratosConsole;
public class ReverseStringTest {
  
 public static void main (String[] args) {
    String str = "What is going on";
    int len =str.length();
    System.out.println("Before Reverse: "+str);
    System.out.println("String Length : "+len);

    StringBuffer dest = new StringBuffer(len);

      for (int i=(len-1); i>=0 ; i--) 
       dest.append(str.charAt(i));
        
       System.out.println(dest);

				         }

}
