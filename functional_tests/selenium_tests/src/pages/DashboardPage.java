package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class DashboardPage {

	  WebDriver driver;  
	  By profileEditor = By.xpath(".//*[@id='profile_editor_switcher']/button");
	  By logoutlink = By.xpath(".//*[@id='editor_list']/li[4]/a");
	  
	    public DashboardPage(WebDriver driver){

	        this.driver = driver;
	    }
	
	    public void Logout(){
	    	
	    	driver.findElement(profileEditor).click(); 
            driver.findElement(logoutlink).click();
    }
}
