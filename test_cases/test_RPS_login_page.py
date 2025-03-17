from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from configurations.config import setup
from base_pages.RPS_Login_Page import RPS_Login_Page

class Test01_RPS_Login_Page:
    page_url = 'https://auth-lxp-qa.stackroute.in/auth/realms/lxp-rps-preprod/protocol/openid-connect/auth?client_id=lxp-rps-client&redirect_uri=https%3A%2F%2Frpsapp-preprod.niit.com%3Flogin%3Dsuccess%26company_id%3D531&response_type=code&scope=openid+profile+email '
    username = 'zeyan@mailinator.com'
    password = 'Test@123'
    invalid_username = 'zeyan12@mailinator.com'
    invalid_password = 'Test@1234'
    success_login_Xpath = '//div[@class="top-title dasboard-batch"]'
    unsuccessful_login_Xpath = '//span[@class="pf-c-form__helper-text pf-m-error required kc-feedback-text"]'


    @allure.title("Testing Elements Visibility of B2B Login Page")
    def test_visibility_of_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = RPS_Login_Page(self.driver)
        # TITLE VERIFICATION
        act_title = self.driver.title
        exp_title = "Sign in to Spark LMS"
        if act_title == exp_title:
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Title Visibility", attachment_type=AttachmentType.PNG)
            message05 = "Title of page i.e, 'Sign in to Spark LMS' is visible successfully.."
            allure.attach(message05, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Title Visibility", attachment_type=AttachmentType.PNG)
            message06 = "Page Title i.e, 'Sign in to Spark LMS' is not visible.."
            allure.attach(message06, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(3)
        # HEADER TEXT VERIFICATION
        element1 = self.driver.find_element(By.XPATH, '//h2[@class="card-title"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element1)
        time.sleep(2)
        if element1.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Header Text Visibility", attachment_type=AttachmentType.PNG)
            message07 = "Page Header i.e, 'Sign in to your account' is visible and highlighted successfully.."
            allure.attach(message07, name="Header Text Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Header Visibility", attachment_type=AttachmentType.PNG)
            message08 = "Page Header i.e, 'Sign in to your account' is not Visible and not highlighted.."
            allure.attach(message08, name="Header Text Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(3)
        # TEXT BELOW HEADER TEXT
        element82 = self.driver.find_element(By.XPATH,'//div[@class="info-box"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element82)
        time.sleep(2)
        if element82.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Header Text Visibility", attachment_type=AttachmentType.PNG)
            message07 = "Header i.e, 'Learner/Trainer Login' is visible and highlighted successfully.."
            allure.attach(message07, name="Header Text Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Header Visibility", attachment_type=AttachmentType.PNG)
            message08 = "Header i.e, 'Learner/Trainer Login' is not Visible and not highlighted.."
            allure.attach(message08, name="Header Text Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # EYE PATCH VERIFICATION
        self.admin_lp = RPS_Login_Page(self.driver)
        self.admin_lp.enter_password(self.password)
        element2 = self.driver.find_element(By.XPATH, '//img[@id="toggle-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element2)
        time.sleep(2)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Eye Patch Visibility", attachment_type=AttachmentType.PNG)
            message09 = "Eye patch field is visible and highlighted successfully.."
            allure.attach(message09, name="Eye Patch Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Eye Patch Visibility", attachment_type=AttachmentType.PNG)
            message10 = "Eye patch field is not visible and not highlighted.."
            allure.attach(message10, name="Eye Patch Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        # EYE PATCH CLICK
        time.sleep(2)
        self.admin_lp = RPS_Login_Page(self.driver)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_eye_patch()
        time.sleep(2)
        assert True
        allure.attach(self.driver.get_screenshot_as_png(), name="Eye Patch Click", attachment_type=AttachmentType.PNG)
        message11 = "Eye patch field is visible and clicked and successfully.."
        allure.attach(message11, name="Eye Patch Visibility Message", attachment_type=AttachmentType.TEXT)
        time.sleep(2)
        # LOGIN BUTTON VISIBILITY
        element3 = self.driver.find_element(By.XPATH, '//button[@class="sign-in-btn"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element3)
        time.sleep(2)
        if element3.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Button Visibility", attachment_type=AttachmentType.PNG)
            message12 = "Login button is visible and highlighted successfully.."
            allure.attach(message12, name="Login Button Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Button Visibility", attachment_type=AttachmentType.PNG)
            message13 = "Login button is not visible and not highlighted.."
            allure.attach(message13, name="Login Button Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # PROVIDER SESSION VISIBILITY
        element84 = self.driver.find_element(By.XPATH,'//div[@class="provider-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element84)
        time.sleep(2)
        if element84.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Provider Session Visibility", attachment_type=AttachmentType.PNG)
            message12 = "Provider Session is visible and highlighted successfully.."
            allure.attach(message12, name="Provider Session Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Provider Session Visibility", attachment_type=AttachmentType.PNG)
            message13 = "Provider Session  is not visible and not highlighted.."
            allure.attach(message13, name="Provider Session Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # REMEMBER ME VISIBILITY
        element83 = self.driver.find_element(By.XPATH,'//div[@class="checkbox"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element83)
        time.sleep(2)
        if element83.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Remember Me Tab", attachment_type=AttachmentType.PNG)
            message12 = "Remember Me Tab is visible and highlighted successfully.."
            allure.attach(message12, name="Remember Me Tab Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Remember Me Tab", attachment_type=AttachmentType.PNG)
            message13 = "Remember Me Tab is not visible and not highlighted.."
            allure.attach(message13, name="Remember Me Tab Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FORGOT PASSWORD TEXT VISIBILITY
        element4 = self.driver.find_element(By.XPATH, "//a[text()='FORGOT PASSWORD?']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element4)
        time.sleep(2)
        if element4.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Text_Message Visibility", attachment_type=AttachmentType.PNG)
            message14 = "Text message i.e, 'Forgot Password?' field is visible and highlighted successfully.."
            allure.attach(message14, name="Text_Message Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Text_Message Visibility", attachment_type=AttachmentType.PNG)
            message15 = "Text message i.e,'Forgot Password?'  field is not visible and not highlighted.."
            allure.attach(message15, name="Text_Message Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FORGOT PASSWORD TEXT CLICK
        self.admin_lp.click_forgot_password()
        time.sleep(2)
        # FORGOT PASSWORD TEXT DIALOG SCREEN
        element5 = self.driver.find_element(By.XPATH, '//div[@class="form-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element5)
        time.sleep(2)
        if element5.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Forgot Password Screeen Visibility", attachment_type=AttachmentType.PNG)
            message15 = "Forgot Password screen is visible and highlighted successfully.."
            allure.attach(message15, name="Forgot Password Screeen Visibility", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Forgot Password Screeen Visibility", attachment_type=AttachmentType.PNG)
            message15 = "Forgot Password screen is not visible and highlighted successfully.."
            allure.attach(message15, name="Forgot Password Screeen Visibility", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FORGOT PASSWORD HEAD
        element80 = self.driver.find_element(By.XPATH,'//h2[@class="card-title"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element80)
        time.sleep(2)
        # FORGOT PASSWORD INFO TEXT
        element16 = self.driver.find_element(By.XPATH,'//div[@class="info-box"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element16)
        time.sleep(2)
        # ENTER FORGOT PASSWORD EMAIL
        self.admin_lp = RPS_Login_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        time.sleep(2)
        # BACK TO LOG BUTTON CLICK
        element6 = self.driver.find_element(By.XPATH,"//a[text()='« Back to Login']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element6)
        time.sleep(2)
        self.admin_lp.click_back_to_login()
        time.sleep(3)
        # LOGO VISIBILITY
        element61 = self.driver.find_element(By.XPATH, '//div[@class="niit-logo"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element61)
        time.sleep(2)
        if element61.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Logo Visibility", attachment_type=AttachmentType.PNG)
            message18 = "Logo is visible and highlighted successfully.."
            allure.attach(message18, name="Logo Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Logo Visibility", attachment_type=AttachmentType.PNG)
            message19 = "Logo is not visible and not highlighted.."
            allure.attach(message19, name="Logo Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # TEXT VISIBILITY
        element7 = self.driver.find_element(By.XPATH, '//div[@class="cert-header"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element7)
        time.sleep(2)
        if element7.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Welcome Text Visibility", attachment_type=AttachmentType.PNG)
            message20 = "Welcome text is visible and highlighted successfully.."
            allure.attach(message20, name="Welcome text Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Welcome text Visibility", attachment_type=AttachmentType.PNG)
            message21 = "Welcome text is not visible and not highlighted.."
            allure.attach(message21, name="Welcome text Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FOOTER TEXT VISIBILITY
        element9 = self.driver.find_element(By.XPATH, '//div[@class="footer-copyright"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element9)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Footer Text Visibility", attachment_type=AttachmentType.PNG)
        message25 = "Footer Text is visible and highlighted successfully.."
        allure.attach(message25, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
        time.sleep(2)
        # FORGOT PASSWORD IN-DETAIL
        element15 = self.driver.find_element(By.XPATH, "//a[text()='FORGOT PASSWORD?']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element15)
        time.sleep(2)
        self.admin_lp.click_forgot_password()
        time.sleep(2)
        self.admin_lp.enter_username(self.username)
        element13 = self.driver.find_element(By.XPATH,'//button[@class="sign-in-btn"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element13)
        time.sleep(2)
        self.admin_lp.click_forgot_password_submit()
        time.sleep(2)
        element14 = self.driver.find_element(By.XPATH,'//div[@class="alert-success  pf-m-success"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element14)
        allure.attach(self.driver.get_screenshot_as_png(), name="Forgot Password In-detail", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.driver.close()

    def test_login_creds(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = RPS_Login_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        time.sleep(3)
        # SUCCESSFUL LOGIN ELEMENT
        element1 = self.driver.find_element(By.XPATH,'//div[@class="container1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", element1)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Success", attachment_type=AttachmentType.PNG)
        message01 = "Successful Login Text i.e,'Dashboard' is visible and highlighted successfully.."
        allure.attach(message01, name="Login Success Message", attachment_type=AttachmentType.TEXT)
        time.sleep(2)
        # PROFILE TAB VERIFICATION AND CLICK
        element2 = self.driver.find_element(By.XPATH,'//span[@aria-label="Zeyan"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", element2)
        time.sleep(2)
        self.admin_lp.click_profile_tab()
        time.sleep(2)
        # LOGOUT BUTTON VERIFICATION AND CLICK
        element3 = self.driver.find_element(By.XPATH,'//button[@class="logout-btn"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", element3)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        message01 = "Profile Tab is visible and highlighted successfully.."
        allure.attach(message01, name="Profile Tab", attachment_type=AttachmentType.TEXT)
        self.admin_lp.click_logout_button()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="LogOut", attachment_type=AttachmentType.PNG)
        message01 = "Logout is successful.."
        allure.attach(message01, name="LogOut", attachment_type=AttachmentType.TEXT)
        time.sleep(3)
        # INVALID LOGIN VERIFICATION
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.invalid_password)
        time.sleep(2)
        self.admin_lp.click_login_button()
        time.sleep(2)
        element4 = self.driver.find_element(By.XPATH,'//span[@class="error-message"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", element4)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Invalid_Login", attachment_type=AttachmentType.PNG)
        message01 = "Invalid Login is verified and message is highlighted successfully.."
        allure.attach(message01, name="Invalid_Login Message", attachment_type=AttachmentType.TEXT)
        self.driver.close()























