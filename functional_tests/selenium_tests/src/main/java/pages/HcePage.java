package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class HcePage {
	
	private static WebElement element = null;

	public static WebElement hceActionsMenu(WebDriver driver, String hceName){

		element = driver.findElement(By.xpath("//table/tbody/tr[td[contains(text(),"+hceName+")]]/td/actions-menu/div/i"));

		return element;

     }
	
	public static WebElement connect(WebDriver driver,  String hceName){

	     element = driver.findElement(By.xpath("//table/tbody/tr[td[contains(text(),"+hceName+")]]/td/actions-menu/div/ul/li[1]"));

	     return element;

	     }
	
	public static WebElement disConnect(WebDriver driver,  String hceName){

	     element = driver.findElement(By.xpath("//table/tbody/tr[td[contains(text(),"+hceName+")]]/td/actions-menu/div/ul/li[1]"));

	     return element;

	     }
	
	public static WebElement unRegister(WebDriver driver, String hceName){

	     element = driver.findElement(By.xpath("//table/tbody/tr[td[contains(text(),"+hceName+")]]/td/actions-menu/div/ul/li[2]"));

	     return element;

	     }
	
	public static WebElement confirmUnregister(WebDriver driver){

	     element = driver.findElement(By.xpath("//div/button[2]"));

	     return element;

	     }
	
	public static WebElement userName(WebDriver driver){

	     element = driver.findElement(By.xpath(".//*[@id='credentials-form-username']"));

	     return element;

	     }
		
	public static WebElement password(WebDriver driver){

	     element = driver.findElement(By.xpath(".//*[@id='credentials-form-password']"));

	     return element;

	     }
	
	public static WebElement connectConfirm(WebDriver driver){

	     element = driver.findElement(By.xpath("//credentials-form/div/form/div[5]/button[2]"));

	     return element;

	     }
	
	public static void connectEndPoint(WebDriver driver, String hceName, String hceUser, String hcePWD)
    {
		hceActionsMenu(driver, hceName).click();
		connect(driver, hceName).click();
		userName(driver).sendKeys(hceName);
		password(driver).sendKeys(hcePWD);
		connectConfirm(driver).click();
    }
	
	public static void disConnectEndPoint(WebDriver driver, String hceName)
    {
		hceActionsMenu(driver, hceName).click();
		disConnect(driver, hceName).click();
    }

}
