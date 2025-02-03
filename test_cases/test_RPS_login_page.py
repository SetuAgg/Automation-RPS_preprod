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
    username = 'kapoor@mailinator.com'
    password = 'Test@123'
    invalid_username = 'kapoor1@mailinator.com'
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
        exp_title = "Sign in to lxp-rps-preprod"
        if act_title == exp_title:
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Page Title Visibility", attachment_type=AttachmentType.PNG)
            message05 = "Title of page i.e, 'Sign in to lxp-rps-preprod' is visible successfully.."
            allure.attach(message05, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Title Visibility", attachment_type=AttachmentType.PNG)
            message06 = "Page Title i.e, 'Sign in to lxp-rps-preprod' is not visible.."
            allure.attach(message06, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(3)
        # HEADER TEXT VERIFICATION
        element1 = self.driver.find_element(By.XPATH, '//header[@class="login-pf-header"]')
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
        # EYE PATCH VERIFICATION
        self.admin_lp = RPS_Login_Page(self.driver)
        self.admin_lp.enter_password(self.password)
        element2 = self.driver.find_element(By.XPATH, '//i[@class="fa fa-eye-slash"]')
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
        element3 = self.driver.find_element(By.XPATH, '//input[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]')
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
        # FORGOT PASSWORD TEXT VISIBILITY
        element4 = self.driver.find_element(By.XPATH, "//a[text()='Forgot Password?']")
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
        element5 = self.driver.find_element(By.XPATH, '//div[@class="card-pf card-pf col-md-4 col-md-offset-2"]')
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
        # BACK TO LOG BUTTON
        element6 = self.driver.find_element(By.XPATH,"//a[text()='« Back to Login']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element6)
        time.sleep(2)
        self.admin_lp.click_back_to_login()
        time.sleep(3)
        # LOGO VISIBILITY
        element6 = self.driver.find_element(By.XPATH, '//div[@class="logo"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element6)
        time.sleep(2)
        if element6.is_displayed():
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
        element7 = self.driver.find_element(By.XPATH, "//h1[text()='GET CERTIFIED IN THE']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element7)
        time.sleep(3)
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
        # TEXT VISIBILITY
        element8 = self.driver.find_element(By.XPATH, "//h4[text()='EVER-GROWING FIELD OF TECHNOLOGY']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element8)
        time.sleep(3)
        if element8.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Welcome text Visibility", attachment_type=AttachmentType.PNG)
            message22 = "Welcome text is visible and highlighted successfully.."
            allure.attach(message22, name="Welcome text Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Welcome text Visibility", attachment_type=AttachmentType.PNG)
            message23 = "Welcome text is not visible and not highlighted.."
            allure.attach(message23, name="Welcome text Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FOOTER VISIBILITY
        element10 = self.driver.find_element(By.XPATH, '//div[@class="container footerBgClolro"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element10)
        time.sleep(3)
        if element10.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility", attachment_type=AttachmentType.PNG)
            message24 = "Footer is visible and highlighted successfully.."
            allure.attach(message24, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility", attachment_type=AttachmentType.PNG)
            message25 = "Footer is not visible and not highlighted.."
            allure.attach(message25, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(3)
        # FOOTER TEXT VISIBILITY
        element11 = self.driver.find_element(By.XPATH, "//p[text()='COPYRIGHT © NIIT ']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element11)
        element12 = self.driver.find_element(By.XPATH,"//span[text()='2025']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element12)
        element12 = self.driver.find_element(By.XPATH,"//p[text()='. ALL RIGHTS RESERVED.']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element12)
        allure.attach(self.driver.get_screenshot_as_png(), name="Footer Text Visibility", attachment_type=AttachmentType.PNG)
        message25 = "Footer Text is visible and highlighted successfully.."
        allure.attach(message25, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
        time.sleep(2)
        # FORGOT PASSWORD IN-DETAIL
        element15 = self.driver.find_element(By.XPATH, "//a[text()='Forgot Password?']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element15)
        time.sleep(2)
        self.admin_lp.click_forgot_password()
        time.sleep(2)
        self.admin_lp.enter_username(self.username)
        element13 = self.driver.find_element(By.XPATH,'//input[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element13)
        time.sleep(2)
        self.admin_lp.click_forgot_password_submit()
        time.sleep(2)
        element14 = self.driver.find_element(By.XPATH,'//div[@class="alert-success pf-c-alert pf-m-inline pf-m-success"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element14)
        allure.attach(self.driver.get_screenshot_as_png(), name="Forgot Password In-detail", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.driver.close()






