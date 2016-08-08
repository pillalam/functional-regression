package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class SummaryPage {

	private static WebElement element = null;
	 
	
    public static WebElement appStop(WebDriver driver){
 
         element = driver.findElement(By.xpath("//button/i[@class='helion-icon helion-icon-lg helion-icon-Halt-stop']"));
 
         return element;
 
         }
    
    public static WebElement appDelete(WebDriver driver){
    	 
        element = driver.findElement(By.xpath("//button/i[@class='helion-icon helion-icon-lg helion-icon-Trash']"));

        return element;

    }
    public static WebElement appState(WebDriver driver){
	   	 
        element = driver.findElement(By.xpath("//div/span[contains(text(),'Incomplete')]"));

        return element;

        }
    
    public static void deleteApplication(WebDriver driver, String appName)
    {
			GalleryviewPage.appNameCheck(driver, appName).click();
			if(appState(driver).isDisplayed())
			{
				appDelete(driver).click();
			}
			else
			{
				appStop(driver).click();
				appDelete(driver).click();
			}
     }
    
}
