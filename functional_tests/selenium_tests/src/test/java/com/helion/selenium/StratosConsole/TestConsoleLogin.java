package com.helion.selenium.StratosConsole;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.NoSuchElementException;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

import pages.GalleryviewPage;
import pages.LoginPage;

public class TestConsoleLogin {

	private static WebDriver driver = null;
	public static String consolUrl = null;
	
		@Parameters({"url"})
		@BeforeTest
	    public void setup(String url){

			consolUrl = url;
	    	//uncomment below line if you want to execute tests on firefox browser
	        //driver = new FirefoxDriver();
	    	
	    	//uncomment below lines if you want to execute tests on chrome driver browser
	    	System.setProperty("webdriver.chrome.driver", "chromedriver");
	    	driver = new ChromeDriver();
	    	
	    	//uncomment below line if you want to execute tests on HtmlUnitDriver browser
	    	//driver = new HtmlUnitDriver(true);
	    	
	        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	    }
	    
	    @AfterTest
	    public void teardown(){  	 
	 
	        driver.quit();
	    }   
	    @Parameters({ "nonadminuser", "nonadminpwd"})
	    @Test
	    public void test_auth_nonadmin_user(String username, String password){
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("",driver.getTitle());
	    		if(LoginPage.login(driver).isDisplayed()){
	    			LoginPage.loginToConsole(driver, username, password);
	    			if(GalleryviewPage.userSettings(driver).isDisplayed())
	    			{
	    				GalleryviewPage.signoutConsole(driver);
	    			}
	    		}
	    		else{
	    			System.out.println("Login Button is not displayed");
	    			}
	    		
	    	}catch(NoSuchElementException ex){
	    			System.out.println(ex.getMessage());
	    		}
	    }	    
	    @Parameters({ "adminuser", "adminpwd"})
	    @Test
	    public void test_auth_admin_user(String username, String password){
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("",driver.getTitle());
	    		if(LoginPage.login(driver).isDisplayed()){
	    			LoginPage.loginToConsole(driver, username, password);
	    			if(GalleryviewPage.userSettings(driver).isDisplayed()){
	    				GalleryviewPage.signoutConsole(driver);
	    			}
	    		}
	    		else{
	    			System.out.println("Login button is not displayed");
	    		}
	    	}catch(NoSuchElementException ex){
	    				System.out.println(ex.getMessage());
	    			}
	    	}  
		}
