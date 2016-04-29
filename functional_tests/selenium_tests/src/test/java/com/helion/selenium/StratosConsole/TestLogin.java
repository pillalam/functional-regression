package test.java.com.helion.selenium.StratosConsole;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import pages.GalleryviewPage;
import pages.LoginPage;

public class TestLogin {

	private static WebDriver driver = null;
	
	    @BeforeTest
	    public void setup(){
	    	

	    	//uncomment below line if you want to execute tests on firefox browser
	        //driver = new FirefoxDriver();
	    	
	    	//uncomment below lines if you want to execute tests on chrome driver browser
	    	System.setProperty("webdriver.chrome.driver", "chromedriver");
	    	driver = new ChromeDriver();
	    	
	    	//uncomment below line if you want to execute tests on HtmlUnitDriver browser
	    	//driver = new HtmlUnitDriver(true);
	    	
	        driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
	    }
	    
	    @AfterTest
	    public void teardown(){  	 
	 
	        driver.quit();
	    }
	    
	    @Parameters({ "username", "password", "url" })
	    @Test
	    public void test_Login_Logout(String username, String password, String url){
	    	
	    	driver.get(url);
  	
	    	LoginPage.userName(driver).sendKeys(username);
	    	LoginPage.password(driver).sendKeys(password);
	    	LoginPage.login(driver).click();
	    	
	    	GalleryviewPage.userSettings(driver).click();
	    	GalleryviewPage.signOut(driver).click();

	    }
	 
}
