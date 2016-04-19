package tests;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.PageFactory;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import pages.DashboardPage;
import pages.LoginPage;

public class TestLogin {

	static WebDriver driver;
	DashboardPage dashboardPage;
	LoginPage loginPage;
	
	    @BeforeTest
	    public void setup(){
	    	

	    	//uncomment below line if you want to execute tests on firefox browser
	        //driver = new FirefoxDriver();
	    	
	    	//uncomment below lines if you want to execute tests on chrome driver browser
	    	System.setProperty("webdriver.chrome.driver", "chromedriver");
	    	driver = new ChromeDriver();
	    	
	    	loginPage = PageFactory.initElements(driver, LoginPage.class);
	    	dashboardPage = PageFactory.initElements(driver, DashboardPage.class);
	    	
	    	//uncomment below line if you want to execute tests on HtmlUnitDriver browser
	    	//driver = new HtmlUnitDriver(true);
	    	
	        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
	        //System.out.println(driver.getTitle());
	        //driver.get("http://10.241.127.17/");
	    }
	    
	    @AfterTest
	    public void teardown(){  	 
	 
	        driver.close();
	    }
	    
	    @Parameters({ "username", "password", "url" })
	    @Test
	    public void test_Login_Logout(String username, String password, String url){
	    	
	    	driver.get(url);
  	
	    	loginPage.userName.sendKeys(username);
	    	loginPage.password.sendKeys(password);
	    	loginPage.login.click();
	    	
	    	dashboardPage.profileEditor.click();
	    	dashboardPage.logoutlink.click();
	    	

	    }
	 
	
}
