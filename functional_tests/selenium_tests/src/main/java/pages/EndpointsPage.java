package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class EndpointsPage {
	
private static WebElement element = null;


    public static WebElement cfRegistration(WebDriver driver){
 
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
	
	 public static WebElement ceRegistration(WebDriver driver){
    	 
	        element = driver.findElement(By.xpath("//service-tile[2]/div/div[1]/a/span/span"));

	        return element;

	        }
	    public static WebElement endpointAddress(WebDriver driver){
	   	 
	        element = driver.findElement(By.xpath("//form/div[1]/input"));

	        return element;

	        }
	    public static WebElement endpointName(WebDriver driver){
	   	 
	        element = driver.findElement(By.xpath("//form/div[2]/input"));

	        return element;

	        }
	    public static WebElement registerHCE(WebDriver driver){
	   	 
	        element = driver.findElement(By.xpath("//div[2]/button[2]"));

	        return element;

	        }

	    public static WebElement hceChart(WebDriver driver){
	      	 
	        element = driver.findElement(By.xpath("//service-tile[2]/div/div[2]/ring-chart/div/div[2]/ul/li[3]/span[2]/span"));

	        return element;

	    }
	
	
	 public static void registerCloudFoundry(WebDriver driver, String clusterUrl, String clusterName)
	    {
		 clusterUrl(driver).sendKeys(clusterUrl);
		 clusterName(driver).sendKeys(clusterName);
		 registerCluster(driver).click();
	    }
	 
	 public static void registerCodeEngine(WebDriver driver, String hceUrl, String hceName)
	    {
		 endpointAddress(driver).sendKeys(hceUrl);
		 endpointName(driver).sendKeys(hceName);
		 registerHCE(driver).click();
	    }
}
