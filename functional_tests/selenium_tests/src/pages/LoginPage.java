package pages;

import org.openqa.selenium.By;
 
import org.openqa.selenium.WebDriver;
 
public class LoginPage {
 
    WebDriver driver;
 
    By userName = By.id("id_username");
 
    By password = By.id("id_password");

    By login = By.id("loginBtn");
     
    public LoginPage(WebDriver driver){
 
        this.driver = driver;
 
    }
 
    public void setUserName(String strUserName){
 
        driver.findElement(userName).sendKeys(strUserName);;
 
    }

    public void setPassword(String strPassword){
 
         driver.findElement(password).sendKeys(strPassword);
 
    }
 
    public void clickLogin(){
 
            driver.findElement(login).click();
 
    }
 
    public void loginTo(String strUserName,String strPasword){
 
        this.setUserName(strUserName);

        this.setPassword(strPasword);

        this.clickLogin();              
 
    }
 
}