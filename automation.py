import random, time, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit

chrome_path = r'C:\Users\swami\AppData\Local\Google\Chrome\User Data\Profile 2'


def chrome(url):
    global driver
    options = Options()
    USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3"
    ]

    user_data_dir = chrome_path
    options.add_argument(f"user-agent={random.choice(USER_AGENT_LIST)}")
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-blink-features=UseEmojiCharacters')
    options.add_argument('--enable-features=UseEmojiCharacters')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--headless=new")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    return None


def youtube(query):
    if query is None:
        url = "https://www.youtube.com/"
        chrome(url)
    else:
        url = (f"https://www.youtube.com/results?search_query={query}")
        pywhatkit.playonyt(url)


def spotify(query):
    if query is None:
        url = "https://open.spotify.com/?flow_ctx=1682b429-fe09-48b5-a2ab-b5ea3c9740d2%3A1716737132"
        chrome(url)
    else:
        url = (f"https://open.spotify.com/search/{query}")
        chrome(url)
        wait = WebDriverWait(driver, 10)
        select = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ouEZqTcvcvMfvezimm_J')))
        select.click()
        play_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="play-button"]')))
        driver.execute_script("arguments[0].click();", play_button)
