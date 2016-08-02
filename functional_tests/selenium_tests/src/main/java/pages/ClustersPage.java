package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class ClustersPage {
	
	
	private static WebElement element = null;


	public static WebElement clusterActionsMenu(WebDriver driver, String clusterName){

		element = driver.findElement(By.xpath("//div[span[contains(text(),"+clusterName+")] and actions-menu]/actions-menu"));

		return element;

     }
	
	public static WebElement connect(WebDriver driver,  String clusterName){

	     element = driver.findElement(By.xpath("//div[span[contains(text(),"+clusterName+")] and actions-menu]/actions-menu/div/ul/li[1]"));

	     return element;

	     }
	
	public static WebElement disConnect(WebDriver driver,  String clusterName){

	     element = driver.findElement(By.xpath("//div[span[contains(text(),"+clusterName+")] and actions-menu]/actions-menu/div/ul/li[1]"));

	     return element;

	     }
		
	public static WebElement unRegister(WebDriver driver, String clusterName){

	     element = driver.findElement(By.xpath("//div[span[contains(text(),"+clusterName+")] and actions-menu]/actions-menu/div/ul/li[2]"));

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
	public static void connectCluster(WebDriver driver, String clusterName, String clusterUser, String clusterPWD)
    {
		clusterActionsMenu(driver, clusterName).click();
		connect(driver, clusterName).click();
		userName(driver).sendKeys(clusterName);
		password(driver).sendKeys(clusterPWD);
		connectConfirm(driver).click();
    }
	
	public static void disConnectCluster(WebDriver driver, String clusterName)
    {
		clusterActionsMenu(driver, clusterName).click();
		disConnect(driver, clusterName).click();
    }

}
