from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path='C:\driver\chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        time.sleep(2)

    def follow(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys("maraqli.tv")
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]').click()
        time.sleep(4)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').click()
        time.sleep(2)

        for i in range(1, 5):
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/ul/div/li[' + str(i)+']/div/div[3]/button').click()
            time.sleep(1)


object = InstaBot("botmytest", "rasimqazwsxedc")
object.login()
object.follow()
