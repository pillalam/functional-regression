package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

public class Login_Page {
	
	
	final WebDriver driver;
	 
	@FindBy(how = How.ID, using = "id_username")
	public WebElement userName;
 
	@FindBy(how = How.ID, using = "id_password")
	public WebElement password;
	
	@FindBy(how = How.ID, using="loginBtn")
	public WebElement login;
 
	// This is a constructor, as every page need a base driver to find web elements
 
	public Login_Page(WebDriver driver)
 
	{
 
		this.driver = driver;
 
	}
}
