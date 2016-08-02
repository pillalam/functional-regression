package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class EndpointsPage {
	
private static WebElement element = null;


    public static WebElement registration(WebDriver driver){
 
         element = driver.findElement(By.xpath("//service-tile[1]/div/div[1]/a/span/span"));
 
         return element;
 
         }

	public static WebElement clusterUrl(WebDriver driver){
	 
		element = driver.findElement(By.xpath("//form/div[1]/input"));

		return element;

    }

	public static WebElement clusterName(WebDriver driver){
	 
		element = driver.findElement(By.xpath("//form/div[2]/input"));

		return element;

    }

	public static WebElement registerCluster(WebDriver driver){
	 
		element = driver.findElement(By.xpath("//form/div[3]/button[2]"));

		return element;

    }

	public static WebElement cfClusterChart(WebDriver driver){
	 
		element = driver.findElement(By.xpath("//service-tile[1]/div/div[2]/ring-chart/div/div[2]/ul/li[3]/span[2]"));

		return element;

    }
	
	 public static void registerCluster(WebDriver driver, String clusterUrl, String clusterName)
	    {
		 clusterUrl(driver).sendKeys(clusterUrl);
		 clusterName(driver).sendKeys(clusterName);
		 registerCluster(driver).click();
	    }
}
