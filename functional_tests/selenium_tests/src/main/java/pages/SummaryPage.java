package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class SummaryPage {

	private static WebElement element = null;
	 
	
    public static WebElement delete(WebDriver driver){
 
         element = driver.findElement(By.xpath("html/body/console-view/div/div/div/div/ul/li[4]/button"));
 
         return element;
 
         }
    
    public static WebElement confirmDelete(WebDriver driver){
    	 
        element = driver.findElement(By.xpath("html/body/div[1]/div/div/div[3]/button[2]"));

        return element;

        }
    public static WebElement appHeader(WebDriver driver){
   	 
        element = driver.findElement(By.cssSelector(".application-header.font-semi-bold.text-uppercase"));
       
        return element;

        }
    
}
