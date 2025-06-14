from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Step 2: Locate the username and password fields and enter credentials
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("Admin")
password_input.send_keys("admin123")

# Step 3: Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Step 4: Verify login successful and take screenshot
dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
print("✅ Login successful. Dashboard is visible.")

#  Step 5: Save screenshot
driver.save_screenshot("dashboard.png")
print("📸 Screenshot saved as 'dashboard.png'")

# Step 6: Wait to see dashboard
time.sleep(1000)

# Step 7: Close browser
driver.quit()
