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
	   	 
	         element = driver.findElement(By.xpath(".//*[@id='navbar']/icons/avatar/div/div[2]/account-actions/div/div[2]/span[2]/a"));
	 
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
	     
	     public static WebElement endPoints(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//*[@id='navbar']/navigation/ul/li[2]/a"));
	 
	         return element;
	 
	         }	     
	     
		 public static WebElement addApp(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//button[@class='btn btn-primary']"));
	 
	         return element;
	 
	         }
	     
	     public static WebElement appName(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//*[@id='add-app-workflow-application-name']"));
	 
	         return element;
	 
	         }
	     public static WebElement hostName(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath(".//*[@id='add-app-workflow-application-host']"));
	 
	         return element;
	 
	         }
	     public static WebElement deliveryMethod(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath("//ng-include/ul/li[2]/div[1]/radio-input/div/div[1]"));
	 
	         return element;
	 
	         }
	     
	     public static WebElement continueButton(WebDriver driver){
		   	 
	         element = driver.findElement(By.xpath("//button[@class='btn btn-primary next']"));
	 
	         return element;
	 
	         }
	     public static WebElement appNameCheck(WebDriver driver, String appName){
		   	 
	         element = driver.findElement(By.xpath("//div/span[contains(text(),"+appName+")]"));
	 
	         return element;
	 
	         }
	     
	     
	     
	     public static void addApplication(WebDriver driver, String appName) throws InterruptedException
	     {
	    		addApp(driver).click();
	    		//Unable to find the locators.It is intermittent. temporarily fixing the issue by thread.sleep
	    		Thread.sleep(2000);
 			appName(driver).sendKeys(appName);
 			hostName(driver).sendKeys(appName);
 			continueButton(driver).click();
 			Thread.sleep(2000);
 			continueButton(driver).click();
 			//deliveryMethod(driver).click();
 			Thread.sleep(2000);
 			continueButton(driver).click();
 	     }
	     
	     public static void signoutConsole(WebDriver driver)
	     {
	    	 userSettings(driver).click();
	     	 signOut(driver).click();
	     }
	     
	    
}
