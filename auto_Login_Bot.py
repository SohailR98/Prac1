from selenium import webdriver
import os


def startBot(username, password, url):
    path = "C:\\Users\\User\\Desktop\\chromedriver"

    driver = webdriver.Chrome(path)

    driver.get(url)

    driver.find_element_by_name(
        "id/class/email").send_keys(username)

    driver.find_element_by_name(
        "id/class/password").send_keys(password)

    driver.find_element_by_name(
        "id/class/name/Login").click()

    username = "sohail"
    password = "sohail"

    url = "https://my.account.sony.com/central/signin/?duid=0000000700090100c714e9aace8c7808ce0244efd6a947bdcebdcb53bbd06c0924698b4994e68cc0&response_type=code&client_id=e4a62faf-4b87-4fea-8565-caaabb3ac918&scope=web%3Acore&access_type=offline&state=f8bb1416e4844d0c881a802dbff8711cb7390ee8718c97e81c91c9f04236125a&service_entity=urn%3Aservice-entity%3Apsn&ui=pr&smcid=web%3Apdc&redirect_uri=https%3A%2F%2Fweb.np.playstation.com%2Fapi%2Fsession%2Fv1%2Fsession%3Fredirect_uri%3Dhttps%253A%252F%252Fio.playstation.com%252Fcentral%252Fauth%252Flogin%253Flocale%253Den_AE%2526postSignInURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Fen-ae%25252Fplaystation-network%25252F%2526cancelURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Fen-ae%25252Fplaystation-network%25252F%26x-psn-app-ver%3D%2540sie-ppr-web-session%252Fsession%252Fv5.30.1-hotfix.1&auth_ver=v3&error=login_required&error_code=4165&error_description=User+is+not+authenticated&no_captcha=false&cid=7e3b2cbb-7aa3-4dbf-92b1-a8fb1c5bb161#/signin/ca?entry=ca"

    startBot(username, password, url)
