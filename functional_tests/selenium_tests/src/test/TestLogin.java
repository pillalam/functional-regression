package test;
 
import java.util.concurrent.TimeUnit;


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.firefox.FirefoxDriver;
//import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.LoginPage;
import pages.DashboardPage;

 
public class TestLogin {
 
    WebDriver driver;
    LoginPage objLoginPage;
    HomePage objHomePage;
    DashboardPage dbPage;
     
    @BeforeTest
    public void setup(){
 
    	//uncomment below line if you want to execute tests on firefox browser
        //driver = new FirefoxDriver();
    	
    	//uncomment below lines if you want to execute tests on chrome driver browser
    	System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");
    	driver = new ChromeDriver();
    	
    	//uncomment below line if you want to execute tests on HtmlUnitDriver browser
    	//driver = new HtmlUnitDriver(true);
    	
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        //System.out.println(driver.getTitle());
    }
    
    @AfterTest
    public void teardown(){  	 
 
        driver.close();
    }
 
    @Parameters({ "username", "password", "url" })
    @Test
    public void test_Login_Logout(String username, String password, String url){
 
        objHomePage = new HomePage(driver);
        objHomePage.getHomePage(url);
        
        objLoginPage = new LoginPage(driver);
        objLoginPage.loginTo(username, password);
        
        dbPage = new DashboardPage(driver);
        dbPage.Logout();

    }
    }