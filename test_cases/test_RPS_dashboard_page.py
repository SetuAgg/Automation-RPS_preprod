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
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility", attachment_type=AttachmentType.PNG)
            message31 = "Footer is Visible and highlighted successfully.."
            allure.attach(message31, name="Footer Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Footer Visibility", attachment_type=AttachmentType.PNG)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="Feedback Button Visibility", attachment_type=AttachmentType.PNG)
            message33 = "Feedback Button is Visible and highlighted successfully.."
            allure.attach(message33, name="Feedback Button Visibility Message", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Feedback Button Visibility", attachment_type=AttachmentType.PNG)
            message34 = "Feedback Button is not Visible and not highlighted.."
            allure.attach(message34, name="Feedback Button Visibility Message", attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        # BATCH NAME BOX VERIFICATIONS AND CLICKS
        element1 = self.driver.find_element(By.XPATH,'//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element1)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element1)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element2 = self.driver.find_element(By.XPATH,"//a[text()='MS Teams Test Batch']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element2)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name Box Visibility", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_batch_text_1()
        time.sleep(2)
        element3 = self.driver.find_element(By.XPATH,'//div[@class="dashboard-course-main-inner"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element3)
        time.sleep(2)
        element4 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element4)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element5 = self.driver.find_element(By.XPATH,"//a[text()='RPS MS TEAMS QA BATCH']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element5)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name Box Visibility", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_batch_text_2()
        time.sleep(2)
        element6 = self.driver.find_element(By.XPATH,'//div[@class="dashboard-program-left animate fadeInLeft three"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element6)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element6)
        time.sleep(2)
        element7 = self.driver.find_element(By.XPATH,'//img[@alt="Chatbot"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element7)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name Box Visibility", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element8 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element8)
        time.sleep(2)
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element8)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element9 = self.driver.find_element(By.XPATH,"//a[text()='module with vilt']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element9)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name Box Visibility", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_batch_text_3()
        time.sleep(2)
        element10 = self.driver.find_element(By.XPATH,'//div[@class="dashboard-program-left animate fadeInLeft three"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element10)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Batch Name Box Visibility", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        # FEEDBACK BUTTON VERIFICATION AND CLICK
        element11 = self.driver.find_element(By.XPATH,'//div[@class="feedback--button contentDesktopView"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element11)
        time.sleep(2)
        self.admin_lp.click_feedback_btn()
        time.sleep(2)
        element12 = self.driver.find_element(By.XPATH,'//div[@class="modal-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element12)
        allure.attach(self.driver.get_screenshot_as_png(), name="Feedback_Btn click", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        # SKIP BUTTON VERIFICATION AND CLICK
        element13 = self.driver.find_element(By.XPATH,'//button[@class="skipBtn btn btn-primary"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element13)
        allure.attach(self.driver.get_screenshot_as_png(), name="Skip_Btn click", attachment_type=AttachmentType.PNG)
        self.admin_lp.click_skip_btn()
        time.sleep(2)
        # PROGRAMS TAB VERIFICATION AND CLICK
        element14 = self.driver.find_element(By.XPATH,"//a[text()='Programs']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element14)
        time.sleep(2)
        self.admin_lp.click_programs_tab()
        time.sleep(2)
        # MY PROGRAMS TAB IN PROGRAMS TAB
        element15 = self.driver.find_element(By.XPATH,"//a[text()='My Programs']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element15)
        time.sleep(2)
        # MY COURSES TAB IN PROGRAMS TAB
        element16 = self.driver.find_element(By.XPATH,"//a[text()='My Courses']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element16)
        time.sleep(2)
        # PROGRAMS TAB MAIN HEAD
        element17 = self.driver.find_element(By.XPATH,'//div[@class="title"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element17)
        time.sleep(2)
        # PROGRAMS TAB LEFT CONTENT
        element18 = self.driver.find_element(By.XPATH,'//div[@class="left-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element18)
        time.sleep(2)
        # PROGRAMS TAB RIGHT CONTENT
        element19 = self.driver.find_element(By.XPATH, '//div[@class="session_my_events_first"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element19)
        time.sleep(2)
        # PROGRAMS TAB RIGHT BOTTOM CONTENT
        element20 = self.driver.find_element(By.XPATH, '//div[@class="session_my_events"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element20)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Programs_Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        # MY COURSES TAB CLICK AND ELEMENT VERIFICATION
        element21 = self.driver.find_element(By.XPATH, "//a[text()='My Courses']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element21)
        time.sleep(2)
        self.admin_lp.click_my_courses_tab()
        time.sleep(2)
        element22 = self.driver.find_element(By.XPATH,'//div[@class="title"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element22)
        time.sleep(2)
        element23 = self.driver.find_element(By.XPATH, '//div[@class="session_my_events_first"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element23)
        time.sleep(2)
        element24 = self.driver.find_element(By.XPATH, '//div[@class="session_my_events"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element24)
        time.sleep(2)
        element25 = self.driver.find_element(By.XPATH,'//div[@class="dropdown false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element25)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Courses Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_my_courses_dropdown()
        time.sleep(2)
        element26 = self.driver.find_element(By.XPATH, "//li[text()='All']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element26)
        time.sleep(2)
        self.admin_lp.click_all_text_tab()
        time.sleep(2)
        element27 = self.driver.find_element(By.XPATH, '//div[@class="course-accordin"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element27)
        time.sleep(2)
        self.admin_lp.click_ms_courses_tab()
        time.sleep(2)
        element28 = self.driver.find_element(By.XPATH, '//div[@class="course-text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element28)
        time.sleep(2)
        # MY PROGRAMS TAB VERIFICATION AND CLICK
        element29 = self.driver.find_element(By.XPATH, "//a[text()='My Programs']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element29)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Courses Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_my_programs_tab()
        time.sleep(2)
        element30 = self.driver.find_element(By.XPATH,'//div[@class="column3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element30)
        time.sleep(2)
        self.admin_lp.click_slick_track_1()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element31 = self.driver.find_element(By.XPATH, '//div[@class="title-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element31)
        time.sleep(2)
        element32 = self.driver.find_element(By.XPATH, '//div[@class="left-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element32)
        time.sleep(2)
        element33 = self.driver.find_element(By.XPATH, '//div[@class="right-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element33)
        time.sleep(2)
        element34 = self.driver.find_element(By.XPATH, '//div[@class="module-left"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element34)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_module_1()
        time.sleep(2)
        element35 = self.driver.find_element(By.XPATH, '//div[@class="title-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element35)
        time.sleep(2)
        element36 = self.driver.find_element(By.XPATH, '//div[@class="left-section1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element36)
        time.sleep(2)
        element37 = self.driver.find_element(By.XPATH, '//div[@class="right-section1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element37)
        time.sleep(2)
        element38 = self.driver.find_element(By.XPATH, '//img[@class="maximize-button-image"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element38)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_maximize_btn_1()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element40 = self.driver.find_element(By.XPATH, '//button[@class="close-button"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element40)
        time.sleep(2)
        self.admin_lp.click_close_btn()
        time.sleep(2)
        element41 = self.driver.find_element(By.XPATH, '//img[@alt="Course Progress"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element41)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_course_progress_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element42 = self.driver.find_element(By.XPATH, '//div[@class=" module-detail-header progress-complete1"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element42)
        time.sleep(2)
        self.admin_lp.click_module_2()
        time.sleep(2)
        element43 = self.driver.find_element(By.XPATH,'//img[@class="maximize-button-image"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element43)
        time.sleep(2)
        self.admin_lp.click_maximize_btn_2()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_close_btn_2()
        time.sleep(2)
        element44 = self.driver.find_element(By.XPATH, '//a[@class="back"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element44)
        time.sleep(2)
        self.admin_lp.click_back_btn_1()
        time.sleep(2)
        element46 = self.driver.find_element(By.XPATH, "//a[text()='Dashboard']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element46)
        time.sleep(2)
        self.admin_lp.click_dashboard_tab()
        time.sleep(2)
        element47 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element47)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element48 = self.driver.find_element(By.XPATH, "//a[text()='MS Teams Test Batch']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element48)
        time.sleep(2)
        self.admin_lp.click_batch_text_1()
        time.sleep(2)
        element49 = self.driver.find_element(By.XPATH, "//a[text()='Programs']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element49)
        time.sleep(2)
        self.admin_lp.click_programs_tab()
        time.sleep(2)
        element50 = self.driver.find_element(By.XPATH, '//div[@class="column3"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element50)
        time.sleep(2)
        self.admin_lp.click_slick_track_1()
        time.sleep(2)
        element51 = self.driver.find_element(By.XPATH, '//div[@class="title-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element51)
        time.sleep(2)
        element52 = self.driver.find_element(By.XPATH, '//div[@class="course-introduction-accordin-single"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element52)
        time.sleep(2)
        element53 = self.driver.find_element(By.XPATH, '//div[@class="right-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element53)
        time.sleep(2)
        element61 = self.driver.find_element(By.XPATH,"//a[text()='Dashboard']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element61)
        time.sleep(2)
        self.admin_lp.click_dashboard_tab()
        time.sleep(2)
        element62 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element62)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element63 = self.driver.find_element(By.XPATH, "//a[text()='RPS MS TEAMS QA BATCH']")
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element63)
        time.sleep(2)
        self.admin_lp.click_batch_text_2()
        time.sleep(2)
        element64 = self.driver.find_element(By.XPATH,"//a[text()='Programs']" )
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element64)
        time.sleep(2)
        self.admin_lp.click_programs_tab()
        time.sleep(2)
        self.admin_lp.click_slick_track_1()
        time.sleep(2)
        element65 = self.driver.find_element(By.XPATH, '//div[@class="title-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element65)
        time.sleep(2)
        element66 = self.driver.find_element(By.XPATH, '//div[@class="course-introduction-accordin-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element66)
        time.sleep(2)
        element67 = self.driver.find_element(By.XPATH, '//div[@class="right-section"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element67)
        time.sleep(2)
        element68 = self.driver.find_element(By.XPATH, '//img[@alt="Chatbot"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element68)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="My Programs Tab Inside", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_dashboard_tab()
        time.sleep(2)
        # SESSIONS TAB ELEMENT VERIFICATION AND CLICKS
        element69 = self.driver.find_element(By.XPATH,  "//a[text()='Sessions']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element69)
        time.sleep(2)
        self.admin_lp.click_sessions_tab()
        time.sleep(2)
        element54 = self.driver.find_element(By.XPATH, "//div[text()='Calendar']")
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element54)
        time.sleep(2)
        element55 = self.driver.find_element(By.XPATH,'//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element55)
        time.sleep(2)
        element56 = self.driver.find_element(By.XPATH, '//div[@class="select-box"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element56)
        time.sleep(2)
        element57 = self.driver.find_element(By.XPATH, '//div[@class="d-flex"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element57)
        time.sleep(2)
        element58 = self.driver.find_element(By.XPATH, '//label[@class="calendar-label-title"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element58)
        time.sleep(2)
        element59 = self.driver.find_element(By.XPATH, '//div[@class="d-flex button-filteralignment"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element59)
        time.sleep(2)
        element60 = self.driver.find_element(By.XPATH, '//div[@class="rbc-month-view"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element60)
        time.sleep(2)
        element70 = self.driver.find_element(By.XPATH, '//div[@class="react-calendar"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element70)
        time.sleep(2)
        element71 = self.driver.find_element(By.XPATH, '//div[@class="session_my_events"]')
        self.driver.execute_script("arguments[0].style.border='5px solid green'", element71)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element72 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element72)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element73 = self.driver.find_element(By.XPATH, "//a[text()='MS Teams Test Batch']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element73)
        time.sleep(2)
        self.admin_lp.click_batch_text_1()
        time.sleep(2)
        self.admin_lp.click_day_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_month_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_week_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element74 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element74)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element75 = self.driver.find_element(By.XPATH, "//a[text()='RPS MS TEAMS QA BATCH']")
        self.driver.execute_script("arguments[0].style.border='5px solid pink'", element75)
        time.sleep(2)
        self.admin_lp.click_batch_text_2()
        time.sleep(2)
        self.admin_lp.click_day_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_month_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_week_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element76 = self.driver.find_element(By.XPATH, '//div[@class="select-box false"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element76)
        time.sleep(2)
        self.admin_lp.click_batch_name_box()
        time.sleep(2)
        element77 = self.driver.find_element(By.XPATH, "//a[text()='module with vilt']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element77)
        time.sleep(2)
        self.admin_lp.click_batch_text_3()
        time.sleep(2)
        self.admin_lp.click_day_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_month_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_week_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        element78 = self.driver.find_element(By.XPATH, "//a[text()='Dashboard']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element78)
        time.sleep(2)
        self.admin_lp.click_dashboard_tab()
        time.sleep(2)
        element87 = self.driver.find_element(By.XPATH, '//img[@alt="Calendar"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element87)
        time.sleep(2)
        self.admin_lp.click_calender_img()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        element88 = self.driver.find_element(By.XPATH,'//div[@class="row calendar-content main-container session-calendar-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element88)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sessions Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_dashboard_tab()
        time.sleep(2)
        # LOGOUT FINAL
        element79 = self.driver.find_element(By.XPATH,"//span[text()='Zeyan']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element79)
        time.sleep(2)
        self.admin_lp.click_profile_tab()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_my_profile_sub_tab()
        time.sleep(2)
        element80 = self.driver.find_element(By.XPATH, '//div[@class="left-profile"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element80)
        time.sleep(2)
        element81 = self.driver.find_element(By.XPATH, '//div[@class="right-profile"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element81)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_profile_tab()
        time.sleep(2)
        element82 = self.driver.find_element(By.XPATH, "//a[text()='Learning Points']")
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element82)
        time.sleep(2)
        self.admin_lp.click_learning_point_tab()
        time.sleep(2)
        element83 = self.driver.find_element(By.XPATH, '//div[@class="main-container"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element83)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_profile_tab()
        time.sleep(2)
        element84 = self.driver.find_element(By.XPATH, '//img[@alt="Change Password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element84)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_change_password_tab()
        time.sleep(2)
        element85 = self.driver.find_element(By.XPATH, '//div[@class="change-password-form"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element85)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Profile Tab", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        self.admin_lp.click_profile_tab()
        time.sleep(2)
        element86 = self.driver.find_element(By.XPATH, '//button[@class="logout-btn"]')
        self.driver.execute_script("arguments[0].style.border='5px solid blue'", element86)
        time.sleep(2)
        self.admin_lp.click_logout_btn()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Logout Success", attachment_type=AttachmentType.PNG)
        self.driver.close()






































































































































































        





















