from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_cambridge_login_reachable():
    url = "https://www.cambridge.org/signin?referrer=/"

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/125.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    os.makedirs("screenshots", exist_ok=True)

    try:
        driver.get(url)

        # print iframe info for debugging
        frames = driver.find_elements(By.TAG_NAME, "iframe")
        print("🧩 Found iframes:", len(frames))
        for idx, f in enumerate(frames):
            print(f"iframe[{idx}] src:", f.get_attribute("src"))

        # try switching into first iframe if present
        if frames:
            driver.switch_to.frame(frames[0])

        # wait for username field or fail gracefully
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )

        print("✅ Login page reachable")

    except Exception as e:
        driver.save_screenshot("screenshots/error_ci.png")
        print(f"❌ Error: {e}")
        raise e

    finally:
        driver.quit()
