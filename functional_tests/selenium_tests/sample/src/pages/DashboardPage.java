package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

public class DashboardPage {

	  final WebDriver driver;
	
	  @FindBy(how = How.XPATH, using = ".//*[@id='profile_editor_switcher']/button")
	  public WebElement  profileEditor;
	  
	  @FindBy(how = How.XPATH, using = ".//*[@id='editor_list']/li[4]/a")
	  public WebElement logoutlink;
	  
	  public DashboardPage(WebDriver driver)
	  {
		  this.driver = driver;
	  }
}
