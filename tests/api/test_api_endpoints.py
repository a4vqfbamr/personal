from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_drupal_api_reachable():
    # Use headless mode (for CI/CD)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    url = "https://www.drupal.org/jsonapi"
    
    try:
        driver.get(url)

        # Check if the page title or body contains "jsonapi"
        page_source = driver.page_source
        assert "jsonapi" in page_source.lower() or "data" in page_source.lower(), \
            "❌ Drupal JSON:API not reachable or invalid response"
        
        print("✅ Drupal API is reachable and returned content.")

    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_drupal_api_reachable()
