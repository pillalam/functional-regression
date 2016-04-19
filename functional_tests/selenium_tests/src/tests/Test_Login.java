package tests;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.PageFactory;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import pages.Dashboard_Page;
import pages.Login_Page;

public class Test_Login {

	static WebDriver driver;
	Dashboard_Page dashboard_Page;
	Login_Page login_Page;
	
	    @BeforeTest
	    public void setup(){
	    	

	    	//uncomment below line if you want to execute tests on firefox browser
	        //driver = new FirefoxDriver();
	    	
	    	//uncomment below lines if you want to execute tests on chrome driver browser
	    	System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");
	    	driver = new ChromeDriver();
	    	
	    	login_Page = PageFactory.initElements(driver, Login_Page.class);
	    	dashboard_Page = PageFactory.initElements(driver, Dashboard_Page.class);
	    	
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
  	
	    	login_Page.userName.sendKeys(username);
	    	login_Page.password.sendKeys(password);
	    	login_Page.login.click();
	    	
	    	dashboard_Page.profileEditor.click();
	    	dashboard_Page.logoutlink.click();
	    	

	    }
	 
	
}
