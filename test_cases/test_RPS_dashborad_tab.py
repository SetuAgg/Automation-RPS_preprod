from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from configurations.config import setup
from base_pages.RPS_Dashboard_Page import RPS_Dashboard_Page

class Test02_RPS_Dashboard_Tab:
    page_url = 'https://auth-lxp-qa.stackroute.in/auth/realms/lxp-rps-preprod/protocol/openid-connect/auth?client_id=lxp-rps-client&redirect_uri=https%3A%2F%2Frpsapp-preprod.niit.com%3Flogin%3Dsuccess%26company_id%3D531&response_type=code&scope=openid+profile+email '
    username = 'zeyan@mailinator.com'
    password = 'Test@123'

    @allure.title("Testing Dashboard Tab Elements Visibility of RPS Dashboard Page")
    def test_dashboard_tab(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.admin_lp = RPS_Dashboard_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        time.sleep(3)
        # LOGO VISIBILITY
        logo = self.driver.find_element(By.XPATH, '//div[@class="logo"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", logo)
        time.sleep(2)
        if logo.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Logo Visibility", attachment_type=AttachmentType.PNG)
            message07 = "Logo is Visible and highlighted successfully.."
            allure.attach(message07, name="Logo Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Logo Visibility", attachment_type=AttachmentType.PNG)
            message08 = "Logo is not Visible and not highlighted.."
            allure.attach(message08, name="Logo Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # DASHBOARD TAB VISIBILITY
        dashboard_tab = self.driver.find_element(By.XPATH,"//a[text()='Dashboard']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", dashboard_tab)
        time.sleep(2)
        if dashboard_tab.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard Tab Visibility", attachment_type=AttachmentType.PNG)
            message01 = "Dashboard Tab is Visible and highlighted successfully.."
            allure.attach(message01, name="Dashboard Tab Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard Tab Visibility", attachment_type=AttachmentType.PNG)
            message02 = "Dashboard Tab is not Visible and not highlighted.."
            allure.attach(message02, name="Dashboard Tab Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # PROGRAMS TAB VISIBILITY
        programs_tab = self.driver.find_element(By.XPATH, "//a[text()='Programs']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", programs_tab)
        time.sleep(2)
        if programs_tab.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Programs Tab Visibility", attachment_type=AttachmentType.PNG)
            message03 = "Programs Tab is Visible and highlighted successfully.."
            allure.attach(message03, name="Programs Tab Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Programs Tab Visibility", attachment_type=AttachmentType.PNG)
            message04 = "Programs Tab is not Visible and not highlighted.."
            allure.attach(message04, name="Programs Tab Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # SESSIONS TAB VISIBILITY
        sessions_tab = self.driver.find_element(By.XPATH, "//a[text()='Sessions']")
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", sessions_tab)
        time.sleep(2)
        if sessions_tab.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab Visibility",
                          attachment_type=AttachmentType.PNG)
            message05 = "Sessions Tab is Visible and highlighted successfully.."
            allure.attach(message05, name="Sessions Tab Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab Visibility",
                          attachment_type=AttachmentType.PNG)
            message06 = "Sessions Tab is not Visible and not highlighted.."
            allure.attach(message06, name="Sessions Tab Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # PROFILE HEADER VISIBILITY
        right_header = self.driver.find_element(By.XPATH, '//div[@class="right-header"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", right_header)
        time.sleep(2)
        if right_header.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Right Header Visibility", attachment_type=AttachmentType.PNG)
            message09 = "Right Header is Visible and highlighted successfully.."
            allure.attach(message09, name="Right Header Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Right Header Visibility", attachment_type=AttachmentType.PNG)
            message10 = "Right Header is not Visible and not highlighted.."
            allure.attach(message10, name="Right Header Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # PAGE MAIN HEAD VISIBILITY
        title = self.driver.find_element(By.XPATH, '//div[@class="title1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", title)
        time.sleep(2)
        if title.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Title text Visibility", attachment_type=AttachmentType.PNG)
            message11 = "Title text is Visible and highlighted successfully.."
            allure.attach(message11, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Title text Visibility", attachment_type=AttachmentType.PNG)
            message12 = "Title text is not Visible and not highlighted.."
            allure.attach(message12, name="Title Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # BATCH NAME BOX VISIBILITY
        batch_name_box = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", batch_name_box)
        time.sleep(2)
        if batch_name_box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name box Visibility", attachment_type=AttachmentType.PNG)
            message13 = "Batch Name box is Visible and highlighted successfully.."
            allure.attach(message13, name="Batch Name box Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name box Visibility", attachment_type=AttachmentType.PNG)
            message14 = "Batch Name box is not Visible and not highlighted.."
            allure.attach(message14, name="Batch Name box Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # BATCH DATE BOX VISIBILITY
        batch_date_box = self.driver.find_element(By.XPATH, '//div[@class="select-box"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", batch_date_box)
        time.sleep(2)
        if batch_date_box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Batch Date box Visibility", attachment_type=AttachmentType.PNG)
            message15 = "Batch Date box is Visible and highlighted successfully.."
            allure.attach(message15, name="Batch Date box Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Batch Date box Visibility", attachment_type=AttachmentType.PNG)
            message16 = "Batch Date box is not Visible and not highlighted.."
            allure.attach(message16, name="Batch Date box Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # COURSES BAR VISIBILITY
        courses_bar = self.driver.find_element(By.XPATH, '//div[@class="course-stats-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", courses_bar)
        time.sleep(2)
        if courses_bar.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Courses bar Visibility", attachment_type=AttachmentType.PNG)
            message17 = "Courses bar is Visible and highlighted successfully.."
            allure.attach(message17, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Courses bar Visibility", attachment_type=AttachmentType.PNG)
            message18 = "Courses bar is not Visible and not highlighted.."
            allure.attach(message18, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        programs_bar = self.driver.find_element(By.XPATH, '//div[@class="dashboard-program-row"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", programs_bar)
        time.sleep(2)
        if programs_bar.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Courses bar Visibility", attachment_type=AttachmentType.PNG)
            message17 = "Courses bar is Visible and highlighted successfully.."
            allure.attach(message17, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Courses bar Visibility", attachment_type=AttachmentType.PNG)
            message18 = "Courses bar is not Visible and not highlighted.."
            allure.attach(message18, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        leaderboard_box = self.driver.find_element(By.XPATH, '//div[@class="dashboard-program-right animate fadeInRight three"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", leaderboard_box)
        time.sleep(2)
        if leaderboard_box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Leaderboard_Box Visibility",
                          attachment_type=AttachmentType.PNG)
            message17 = "Courses bar is Visible and highlighted successfully.."
            allure.attach(message17, name="Leaderboard_Box Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Leaderboard_Box Visibility",
                          attachment_type=AttachmentType.PNG)
            message18 = "Leaderboard_Box is not Visible and not highlighted.."
            allure.attach(message18, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        my_courses_bar = self.driver.find_element(By.XPATH, '//div[@class="dashboard-course-main box animate fadeInDown four"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", my_courses_bar)
        time.sleep(2)
        if my_courses_bar.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="My_courses_Bar Visibility",
                          attachment_type=AttachmentType.PNG)
            message17 = "Courses bar is Visible and highlighted successfully.."
            allure.attach(message17, name="My_courses_Bar Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="My_courses_Box Visibility",
                          attachment_type=AttachmentType.PNG)
            message18 = "My_courses_Bar is not Visible and not highlighted.."
            allure.attach(message18, name="Courses bar Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FOOTER VISIBILITY
        footer = self.driver.find_element(By.XPATH, '//div[@class="container"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", footer)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", footer)
        time.sleep(2)
        if footer.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility",
                          attachment_type=AttachmentType.PNG)
            message31 = "Footer is Visible and highlighted successfully.."
            allure.attach(message31, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility",
                          attachment_type=AttachmentType.PNG)
            message32 = "Footer is not Visible and not highlighted.."
            allure.attach(message32, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # FEEDBACK BUTTON
        feedback_btn = self.driver.find_element(By.XPATH, '//div[@class="feedback--button contentDesktopView"]')
        self.driver.execute_script("arguments[0].style.border='5px solid yellow'", feedback_btn)
        time.sleep(2)
        if feedback_btn.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Feedback Button Visibility",
                          attachment_type=AttachmentType.PNG)
            message33 = "Feedback Button is Visible and highlighted successfully.."
            allure.attach(message33, name="Feedback Button Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Feedback Button Visibility",
                          attachment_type=AttachmentType.PNG)
            message34 = "Feedback Button is not Visible and not highlighted.."
            allure.attach(message34, name="Feedback Button Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False




















