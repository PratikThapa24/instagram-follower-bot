from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = Options()
option.add_experimental_option("detach", True)

#Variables
SIMILAR_ACCOUNT ="lebron"
USER_NAME = "your username"
PASSWORD = "your password"
FOLLOWER_AMOUNT = 10
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        #Enters USERNAME
        username = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username.send_keys(USER_NAME)
        #Enters PASSWORD
        password = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        #Clicks login
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
        time.sleep(3)
    def find_followers(self):
        #Clicks Search
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div').click()
        search = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        #Clicks the follower
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/a/div/div/div/div[2]/div/div').click()
        time.sleep(4)
        #Clicks the follower element
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        follower_list = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div')
        for user in follower_list:
            user.click()
            time.sleep(1)
follower_bot = InstaFollower()
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
# driver.quit()
