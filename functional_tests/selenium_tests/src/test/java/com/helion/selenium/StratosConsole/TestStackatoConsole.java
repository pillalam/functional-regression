package com.helion.selenium.StratosConsole;
import java.util.Random;
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
import pages.SummaryPage;
import pages.SettingsPage;
import pages.EndpointsPage;
import pages.ClustersPage;
import pages.HcePage;

public class TestStackatoConsole {

	private static WebDriver driver = null;
	public static String consolUrl = null;
	public static String clusterName = null;
	public static String hceName = null;
	public static String appName = null;
	public static Random random = null;
	
		@Parameters({"url"})
		@BeforeTest
	    public void setup(String url){

			consolUrl = url;
	    	//uncomment below line if you want to execute tests on firefox browser
	        //driver = new FirefoxDriver();
	    	
	    	//uncomment below lines if you want to execute tests on chrome driver browser
	    	//System.setProperty("webdriver.chrome.driver", "chromedriver");
	    	driver = new ChromeDriver();
	    	
	    	//uncomment below line if you want to execute tests on HtmlUnitDriver browser
	    	//driver = new HtmlUnitDriver(true);
	        random = new Random();
	        clusterName = "Cluster"+random.nextInt(1000);
	        hceName = "endPoint"+random.nextInt(1000);
	        appName = "testApp"+random.nextInt(1000);
	        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	       
	    }
	    
	    @AfterTest
	    public void teardown(){  	 
	 
	        driver.quit();
	    }  
	    
	    @Parameters({ "nonadminuser", "nonadminpwd"})
	    @Test(priority=1)
	    public void test_auth_nonadmin_user(String username, String password){
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("Helion Stackato",driver.getTitle());
	    		//Login and Logout
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
	    @Test(priority=2)
	    public void test_auth_admin_user(String username, String password){
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("Helion Stackato",driver.getTitle());
	    		//Login and Logout
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
	    
	    @Parameters({ "adminuser", "adminpwd", "clusterurl", "clusteruser", "clusterpwd"})
	    @Test(priority=3)
	    public void test_cluster_register(String username, String password, String clusterurl, String clusteruser, String clusterpwd ){
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("Helion Stackato",driver.getTitle());
	    		//Login
	    		if(LoginPage.login(driver).isDisplayed()){
	    			LoginPage.loginToConsole(driver, username, password);
	    		}
	    		else{
	    			System.out.println("Login button is not displayed");
	    		}
	    		//register cluster
	    		GalleryviewPage.endPoints(driver).click();
	    		driver.navigate().refresh();
	    		if(EndpointsPage.cfRegistration(driver).isDisplayed()){
	    			EndpointsPage.registerCloudFoundry(driver, clusterurl, clusterName);
	    		}
	    		//connect cluster
	    		EndpointsPage.cfClusterChart(driver).click();
	    		if(ClustersPage.clusterActionsMenu(driver, clusterName).isDisplayed())
	    		{
	    			ClustersPage.connectCluster(driver, clusterName, clusteruser, clusterpwd);
	    		}
	    		//disconnect cluster
	    		if(ClustersPage.clusterActionsMenu(driver, clusterName).isDisplayed())
	    		{
	    			ClustersPage.disConnectCluster(driver, clusterName);
	    		}
	    		//Logout
	    		if(GalleryviewPage.userSettings(driver).isDisplayed())
    			{
    				GalleryviewPage.signoutConsole(driver);
    			}
	    		
	    	}catch(NoSuchElementException ex){
	    				System.out.println(ex.getMessage());
	    			}
	    	}  
	    
	    
	    @Parameters({ "adminuser", "adminpwd", "hceurl", "hceuser", "hcepwd"})
	    @Test(priority=4)
	    public void test_endpoint_register(String username, String password, String hceurl, String hceuser, String hcepwd ) {
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("Helion Stackato",driver.getTitle());
	    		//Login
	    		if(LoginPage.login(driver).isDisplayed()){
	    			LoginPage.loginToConsole(driver, username, password);
	    		}
	    		else{
	    			System.out.println("Login button is not displayed");
	    		}
	    		//register endPoint
	    		GalleryviewPage.endPoints(driver).click();
	    		driver.navigate().refresh();
	    		if(EndpointsPage.ceRegistration(driver).isDisplayed()){
	    			EndpointsPage.registerCodeEngine(driver, hceName, hceurl);
	    		}
	    		//connect EndPoint
	    		EndpointsPage.hceChart(driver).click();
	    		if(HcePage.hceActionsMenu(driver, hceName).isDisplayed())
	    		{
	    			HcePage.connectEndPoint(driver, hceurl, hceuser, hcepwd);
	    		}
	    		//disconnect EndPoint
	    		if(HcePage.hceActionsMenu(driver, hceName).isDisplayed())
	    		{
	    			HcePage.disConnectEndPoint(driver, hceName);
	    		}
	    		//Logout
	    		if(GalleryviewPage.userSettings(driver).isDisplayed())
    			{
    				GalleryviewPage.signoutConsole(driver);
    			}
	    	}catch(NoSuchElementException ex){
	    				System.out.println(ex.getMessage());
	    			}
	    	}  
	    
	    
	    @Parameters({ "adminuser", "adminpwd"})
	    @Test(priority=5)
	    public void test_add_delete_app(String username, String password) throws InterruptedException{
	    try{
	    		driver.get(consolUrl);
	    		Assert.assertEquals("Helion Stackato",driver.getTitle());
	    		//Login
	    		if(LoginPage.login(driver).isDisplayed()){
	    			LoginPage.loginToConsole(driver, username, password);
	    			
	    		}
	    		else{
	    			System.out.println("Login button is not displayed");
	    		}
	    		//Add Application
	    		if(GalleryviewPage.addApp(driver).isDisplayed())
	    		{
	    			GalleryviewPage.addApplication(driver, appName);
	    		}
	    		else{
	    			System.out.println("Add Application button is not displayed");
	    		}
	    		//Delete Application
	    		if(GalleryviewPage.appNameCheck(driver, appName).isDisplayed()){
	    		SummaryPage.deleteApplication(driver, appName);
	    		}
	    		//Logout
	    		if(GalleryviewPage.userSettings(driver).isDisplayed())
    			{
    				GalleryviewPage.signoutConsole(driver);
    			}
	    	}catch(NoSuchElementException ex){
	    				System.out.println(ex.getMessage());
	    		
	    }
	    }   
		}
