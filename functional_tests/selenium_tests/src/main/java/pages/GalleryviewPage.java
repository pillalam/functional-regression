package pages;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class GalleryviewPage {

	    private static WebElement element = null;
		 
	    public static WebElement userSettings(WebDriver driver){
	 
	         element = driver.findElement(By.xpath(".//*[@id='navbar']/icons/avatar/i"));
	 
	         return element;
	 
	         }
	     public static WebElement signOut(WebDriver driver){
	   	 
	         element = driver.findElement(By.xpath(".//*[@id='navbar']/icons/avatar/div/div[2]/account-actions/div/div[2]/span[3]/a/i"));
	 
	         return element;
	 
	         }
	     
	     public static WebElement accountSettings(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//*[@id='navbar']/icons/avatar/div/div[2]/account-actions/div/div[2]/span[1]/a/i"));
	 
	         return element;
	 
	         }
	     
	     public static WebElement applicationcard(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//span[contains(text(),'ace')]"));
	 
	         return element;
	 
	         }
	     public static void signoutConsole(WebDriver driver)
	     {
	    	 userSettings(driver).click();
	     	 signOut(driver).click();
	     }
	    
}
