# selenium-login-test
Automated login test using Selenium and Python
This is a simple Selenium automation project created by a fresher to demonstrate the ability to write and run test cases using **Python and Selenium WebDriver**.  
The project tests a **successful login** functionality on the [OrangeHRM demo website](https://opensource-demo.orangehrmlive.com/).

---

## 📌 Project Objectives

- ✅ Automate the login process
- ✅ Verify successful login by checking for the Dashboard
- ✅ Use waits to handle dynamic elements
- ✅ Take screenshots based on test result
- ✅ Print clear PASS/FAIL status in the console

---

## 🧰 Technologies & Tools

- 🐍 Python 3.x
- 🌐 Selenium WebDriver
- 📦 WebDriver Manager
- 💻 Google Chrome + ChromeDriver
- 💡 Visual Studio Code (VS Code)

---

## 🚀 How to Run

### 1. Clone this repository or download the code
```bash
git clone https://github.com/yourusername/selenium-login-test.git
cd selenium-login-test

2. Install the required packages
bash
Copy
Edit
pip install selenium webdriver-manager
3. Run the script
bash
Copy
Edit
python test_successful_login.py
🧪 Test Case Used
✅ Successful Login Test
Step	Action	Expected Result
1	Open OrangeHRM login page	Login page loads successfully
2	Enter valid username and password	Fields accept input
3	Click on Login button	Page navigates to Dashboard
4	Check for "Dashboard" heading	If found, login is successful
5	Capture screenshot	Save with appropriate filename

📸 Screenshots
successful_login.png – Screenshot of dashboard after successful login

failed_login.png – Screenshot in case of error or failure

✅ Output Example
bash
Copy
Edit
✅ TEST CASE PASSED: Successfully logged in.
# OR
❌ TEST CASE FAILED: Login unsuccessful.
✍️ Author
Iswarya N
Fresher | Software Testing Enthusiast
📍 India

📌 License
This project is for educational purposes only.
