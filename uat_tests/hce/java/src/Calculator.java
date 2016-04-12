package src;
public class Calculator {
   public static void main(String[] args) {
               
          Calculator cal = new Calculator();
            int result=cal.add(Integer.parseInt(args[0]),Integer.parseInt(args[1]));
  
           System.out.println(result);
                                          }



           public int add(int n1,int n2)
                {
             return n1+n2;
                }

                       }
