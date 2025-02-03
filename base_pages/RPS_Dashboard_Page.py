from selenium.webdriver.common.by import By

class RPS_Dashboard_Page:
    textbox_username_id = "username"
    textbox_password_id = "password"
    login_button_Xpath = '//input[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]'
    dashboard_tab_xpath = "//a[text()='Dashboard']"
    programs_tab_xpath = "//a[text()='Programs']"
    sessions_tab_xpath = "//a[text()='Sessions']"




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

    def click_dashboard_tab(self):
        self.driver.find_element(By.XPATH, self.dashboard_tab_xpath).click()


