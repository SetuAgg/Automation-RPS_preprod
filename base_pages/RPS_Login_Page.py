from selenium.webdriver.common.by import By

class RPS_Login_Page:
    textbox_username_id = "username"
    textbox_password_id = "password"
    login_button_Xpath = '//input[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]'
    eye_patch_xpath = '//i[@class="fa fa-eye-slash"]'
    profile_tab_xpath = '//span[@aria-label="automation"]'
    logout_btn_xpath = '//button[@class="logout-btn"]'
    forgot_password_xpath = "//a[text()='Forgot Password?']"
    back_to_login_btn_xpath = "//a[text()='« Back to Login']"
    forgot_password_submit_btn = '//input[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]'



    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_Xpath).click()

    def click_eye_patch(self):
        self.driver.find_element(By.XPATH, self.eye_patch_xpath).click()

    def click_profile_tab(self):
        self.driver.find_element(By.XPATH, self.profile_tab_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath).click()

    def click_forgot_password(self):
        self.driver.find_element(By.XPATH, self.forgot_password_xpath).click()

    def click_back_to_login(self):
        self.driver.find_element(By.XPATH, self.back_to_login_btn_xpath).click()

    def click_forgot_password_submit(self):
        self.driver.find_element(By.XPATH, self.forgot_password_submit_btn).click()



