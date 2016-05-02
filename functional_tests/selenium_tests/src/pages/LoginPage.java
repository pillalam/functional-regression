package pages;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class LoginPage {
	
	private static WebElement element = null;
	 
    public static WebElement userName(WebDriver driver){
 
         element = driver.findElement(By.id("login-form-username"));
 
         return element;
 
         }
    public static WebElement password(WebDriver driver){
    	 
        element = driver.findElement(By.id("login-form-password"));

        return element;

        }
    public static WebElement login(WebDriver driver){
    	 
        element = driver.findElement(By.xpath(".//*[@id='section-login-panel']/login-form/form/button"));

        return element;

        } 
}
