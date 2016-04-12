package test;
import junit.framework.TestCase;
import src.Calculator;
public class TestCalculator extends TestCase {
       public static void main(String[] args) {
          testAdd();             
                   
                                              }
          public static void testAdd() {
            Calculator cal = new Calculator() ;
            double result = cal.add(10,60);
            assertEquals(70,result,0);
}
}
