from selenium import webdriver
import os


def startBot(username, password, url):
    path = "C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps\\chromedriver"

    driver = webdriver.Chrome(path)

    driver.get(url)

    driver.find_element_by_name(
        "id/class/email").send_keys(username)

    driver.find_element_by_name(
        "id/class/password").send_keys(password)

    driver.find_element_by_name(
        "id/class/name/submit").click()


if __name__ == "__main__":
    username = "sohail "
    password = "sohail"
    # Replace with the actual URL
    url = "https://crunchify.com/wp-content/uploads/code/Crunchify-LoginPage.html"
    startBot(username, password, url)
