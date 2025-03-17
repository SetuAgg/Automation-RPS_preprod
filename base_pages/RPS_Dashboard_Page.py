from selenium.webdriver.common.by import By

class RPS_Dashboard_Page:
    textbox_username_id = "username"
    textbox_password_id = "password"
    login_button_Xpath = '//button[@class="sign-in-btn"]'
    dashboard_tab_xpath = "//a[text()='Dashboard']"
    programs_tab_xpath = "//a[text()='Programs']"
    sessions_tab_xpath = "//a[text()='Sessions']"
    batch_name_box = '//div[@class="select-box false"]'
    batch_text_1 = "//a[text()='MS Teams Test Batch']"
    batch_text_2 = "//a[text()='RPS MS TEAMS QA BATCH']"
    batch_text_3 = "//a[text()='module with vilt']"
    feedback_btn = '//div[@class="feedback--button contentDesktopView"]'
    skip_btn = '//button[@class="skipBtn btn btn-primary"]'
    my_courses_tab = "//a[text()='My Courses']"
    my_courses_dropdown = '//div[@class="dropdown false"]'
    all_text_tab = "//li[text()='All']"
    ms_courses_tab = '//div[@class="course-accordin"]'
    my_programs_tab = "//a[text()='My Programs']"
    slick_track_1 = '//div[@class="column3"]'
    module_1 = '//div[@class="module-single"]'
    maximize_btn_1 = '//img[@class="maximize-button-image"]'
    close_btn = '//button[@class="close-button"]'
    course_progress_btn = '//img[@alt="Course Progress"]'
    module_2 = '//div[@class=" module-detail-header progress-complete1"]'
    maximize_btn_2 = '//img[@class="maximize-button-image"]'
    close_btn_2 = '//button[@class="close-button"]'
    back_btn_1 = '//a[@class="back"]'
    module_3 = 'class="module-left'
    maximize_btn_3 = '//img[@class="maximize-button-image"]'
    close_btn_3 = '//button[@class="close-button"]'
    day_btn = "//button[text()='Day']"
    month_btn = "//button[text()='Month']"
    week_btn = "//button[text()='Week']"
    profile_tab = "//span[text()='Zeyan']"
    my_profile_sub_tab = '//img[@alt="My Profile"]'
    learning_point_tab = "//a[text()='Learning Points']"
    change_password_tab = '//img[@alt="Change Password"]'
    logout_btn_final = '//button[@class="logout-btn"]'
    calender_img = '//img[@alt="Calendar"]'








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

    def click_batch_name_box(self):
        self.driver.find_element(By.XPATH,self.batch_name_box).click()

    def click_batch_text_1(self):
        self.driver.find_element(By.XPATH,self.batch_text_1).click()

    def click_batch_text_2(self):
        self.driver.find_element(By.XPATH,self.batch_text_2).click()

    def click_batch_text_3(self):
        self.driver.find_element(By.XPATH,self.batch_text_3).click()

    def click_feedback_btn(self):
        self.driver.find_element(By.XPATH,self.feedback_btn).click()

    def click_skip_btn(self):
        self.driver.find_element(By.XPATH,self.skip_btn).click()

    def click_programs_tab(self):
        self.driver.find_element(By.XPATH,self.programs_tab_xpath).click()

    def click_my_courses_tab(self):
        self.driver.find_element(By.XPATH,self.my_courses_tab).click()

    def click_my_courses_dropdown(self):
        self.driver.find_element(By.XPATH,self.my_courses_dropdown).click()

    def click_all_text_tab(self):
        self.driver.find_element(By.XPATH,self.all_text_tab).click()

    def click_ms_courses_tab(self):
        self.driver.find_element(By.XPATH, self.ms_courses_tab).click()

    def click_my_programs_tab(self):
        self.driver.find_element(By.XPATH, self.my_programs_tab).click()

    def click_slick_track_1(self):
        self.driver.find_element(By.XPATH, self.slick_track_1).click()

    def click_module_1(self):
        self.driver.find_element(By.XPATH, self.module_1).click()

    def click_maximize_btn_1(self):
        self.driver.find_element(By.XPATH, self.maximize_btn_1).click()

    def click_close_btn(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def click_course_progress_btn(self):
        self.driver.find_element(By.XPATH,self.course_progress_btn).click()

    def click_module_2(self):
        self.driver.find_element(By.XPATH,self.module_2).click()

    def click_maximize_btn_2(self):
        self.driver.find_element(By.XPATH, self.maximize_btn_2).click()

    def click_close_btn_2(self):
        self.driver.find_element(By.XPATH, self.close_btn_2).click()

    def click_back_btn_1(self):
        self.driver.find_element(By.XPATH, self.back_btn_1).click()

    def click_sessions_tab(self):
        self.driver.find_element(By.XPATH, self.sessions_tab_xpath).click()

    def click_day_btn(self):
        self.driver.find_element(By.XPATH, self.day_btn).click()

    def click_month_btn(self):
        self.driver.find_element(By.XPATH, self.month_btn).click()

    def click_week_btn(self):
        self.driver.find_element(By.XPATH, self.week_btn).click()

    def click_profile_tab(self):
        self.driver.find_element(By.XPATH, self.profile_tab).click()

    def click_my_profile_sub_tab(self):
        self.driver.find_element(By.XPATH,self.my_profile_sub_tab).click()

    def click_learning_point_tab(self):
        self.driver.find_element(By.XPATH,self.learning_point_tab).click()

    def click_change_password_tab(self):
        self.driver.find_element(By.XPATH,self.change_password_tab).click()

    def click_logout_btn(self):
        self.driver.find_element(By.XPATH, self.logout_btn_final).click()

    def click_calender_img(self):
        self.driver.find_element(By.XPATH, self.calender_img).click()


















































