from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Define service, driver and options
chrome_option = Options()
chrome_option.add_argument("--disable-search-engine-choice-screen") #to disable browser suggestions
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


# Load the web-page
driver.get('https://demoqa.com/login')


# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'password')))
login_button = driver.find_element(By.ID,'login')


# Fill in the username, password and click login button
username_field.send_keys('pythoncourse')
password_field.send_keys('@Pythoncourse1234')
# login_button.click() but sometimes bcz of lots of ads it can give error by clicking on the ad.
driver.execute_script("arguments[0].click();",login_button) # script is a JAVA script


# Locate the Element dropdown and Text Box
element = (WebDriverWait(driver,10).until
           (EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]'))))
element.click()
text_box = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()


# Locate the form fields and submit button
fullname_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
email_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
permanent_address_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
submit_button = driver.find_element(By.ID,'submit')


# Fill in the form fields and click submit button
fullname_field.send_keys("John Smith")
email_field.send_keys("john@gmail.com")
current_address_field.send_keys("Piscatway,NJ, USA")
permanent_address_field.send_keys("Piscatway, NJ, USA")
driver.execute_script("arguments[0].click();",submit_button) # script is a JAVA script


input("Press Enter to close the browser")
driver.quit()
