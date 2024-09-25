from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Define service, driver and options
        chrome_option = Options()
        chrome_option.add_argument("--disable-search-engine-choice-screen")  # to disable browser suggestions

        # to download in the project directory
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_option.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_option, service=service)

    def login(self,username, password):
        # Load the web-page
        self.driver.get('https://demoqa.com/login')

        # Locate username, password and login button
        username_field = (WebDriverWait(self.driver, 10).
                          until(EC.visibility_of_element_located((By.ID, 'userName'))))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in the username, password and click login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        # login_button.click() but sometimes bcz of lots of ads it can give error by clicking on the ad.
        self.driver.execute_script("arguments[0].click();", login_button)  # script is a JAVA script

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Element dropdown and Text Box
        element = (WebDriverWait(self.driver, 10).until
                   (EC.visibility_of_element_located((By.XPATH,
                                                      '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]'))))
        element.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields and click submit button
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)  # script is a JAVA script

    def download(self):
        # Locate the Upload & Download section and Download Button
        upload_download = self.driver.find_element(By.ID, 'item-7')
        self.driver.execute_script("arguments[0].click();",upload_download)
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login("pythoncourse","@Pythoncourse1234")
    webautomation.fill_form("John","john@gmail.com","Piscatway, NJ", "Piscatway, NJ, USA")
    webautomation.download()
    webautomation.close()