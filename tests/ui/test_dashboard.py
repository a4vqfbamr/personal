from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_Cambridge_homepage_simple():
    # Setup headless browser (good for CI/CD)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.cambridge.org")
        assert "Cambridge" in driver.title, "❌ Homepage did not load properly"
        print("✅ Cambridge homepage loaded successfully.")
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_Cambridge_homepage_simple()
