package pages;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class GalleryviewPage {

	    private static WebElement element = null;
		 
	    public static WebElement userSettings(WebDriver driver){
	 
	         element = driver.findElement(By.cssSelector(".btn-border-less.helion-icon.helion-icon-User_settings"));
	 
	         return element;
	 
	         }
	    public static WebElement signOut(WebDriver driver){
	   	 
	         element = driver.findElement(By.cssSelector(".helion-icon.helion-icon-Logout"));
	 
	         return element;
	 
	         }
	    
}
