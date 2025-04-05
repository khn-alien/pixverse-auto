from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
username = 'voweye4994@movfull.com'
password = '14169191khnalien'
login_url = 'https://app.pixverse.ai/login'
home_url = 'https://app.pixverse.ai/home'

# Browser options
options = Options()
options.headless = False
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(login_url)
    time.sleep(6)
    driver.execute_script("window.stop();")

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Username"))).send_keys(username)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Navigate to home
    WebDriverWait(driver, 20).until(EC.url_contains("/home"))
    driver.get(home_url)

    # Wait for balance span using FULL XPATH
    span_xpath = '/html/body/div[1]/div/div/div[2]/header[2]/div/div[5]/div[1]/span'
    balance_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, span_xpath))
    )

    balance = balance_element.text
    print(f"✅ Credit Balance: {balance}")

except Exception as e:
    print(f"❌ Error: {e}")
    print("🔍 DEBUG: Listing all spans with 'text-text-warning' class...")
    spans = driver.find_elements(By.CLASS_NAME, 'text-text-warning')
    for idx, span in enumerate(spans):
        print(f"[{idx}] → {span.text}")

    print("🧾 Partial Page Source:")
    print(driver.page_source[:1000])

    input("⏳ Press Enter to keep browser open and inspect...")

finally:
    pass  # Do not close browser

