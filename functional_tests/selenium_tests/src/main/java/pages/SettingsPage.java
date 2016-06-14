package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class SettingsPage {
	private static WebElement element = null;
	 
	
    public static WebElement connect(WebDriver driver){
 
         element = driver.findElement(By.xpath("html/body/console-view/div/div/service-registration/div/div/div/table/tbody/tr[1]/td[6]/a/span/span"));
 
         return element;
 
         }
    
    public static WebElement form(WebDriver driver){
 
         element = driver.findElement(By.xpath("html/body/console-view/div/div/service-registration/flyout/div[2]/div/ng-transclude/credentials-form"));
 
         return element;
 
         }
    public static WebElement serviceUsername(WebDriver driver)
    {
    	element = driver.findElement(By.id("credentials-form-username"));
    	return element;
    }
    
    public static WebElement servicePassword(WebDriver driver)
    {
    	element = driver.findElement(By.id("credentials-form-password"));
    	return element;
    }
    
    public static WebElement Register(WebDriver driver)
    {
    	element = driver.findElement(By.xpath("html/body/console-view/div/div/service-registration/flyout/div[2]/div/ng-transclude/credentials-form/div/form/div[5]/button[2]"));
    	return element;
    }
}
