from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


episode_number = input("enter episode number ")


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
browser = driver.get("https://animepahe.ru/")




WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "input-search"))
)
search_bar = driver.find_element(By.CLASS_NAME, "input-search")
search_bar.send_keys("one piece")

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, "One Piece"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "One Piece")
link.click()

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, f"Watch - {episode_number} Online"))
)
episode = driver.find_element(By.PARTIAL_LINK_TEXT, f"Watch - {episode_number} Online")
episode.click()

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.ID, "downloadMenu"))
)
download_button = driver.find_element(By.ID, "downloadMenu")
download_button.click()

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "dropdown-item"))
)
download_link = driver.find_element(By.PARTIAL_LINK_TEXT, "SubsPlease · 720p")
redirect_link = download_link.get_dom_attribute("href")

driver.get(redirect_link)

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Continue"))
)
listss = driver.find_element(By.PARTIAL_LINK_TEXT, "Continue")
driver.get(listss.get_dom_attribute("href"))

WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "button"))
)
download_button_2 = driver.find_element(By.CLASS_NAME, "button")
download_button_2.click()

time.sleep(30)
driver.quit()