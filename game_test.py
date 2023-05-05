import unittest
from time import sleep
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class game_test(unittest.TestCase):

    # Setting up the chrome browser and maximising the browser window
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

    # Test Scenario 1
    def testing_scenarios_1(self):
        self.driver.get('https://www.saucedemo.com/')    #Navigating to the URL

        self.driver.find_element(By.ID, 'user-name').send_keys("standard_user")  #Locating and typing the username
        self.driver.find_element(By.NAME, 'password').send_keys("secret_sauce")  #Locating and typing the password
        self.driver.find_element(By.ID, 'login-button').click()  #Locating and clicking the login button

        time.sleep(5)  #Sleep time to load the page
        element = self.driver.find_element(By.CSS_SELECTOR,"#header_container > div.primary_header > div.header_label > div")  #Locating the Logo
        logo_text=element.is_displayed()  #This function is to check whether logo present or not

        # Condition to check that logo_text is either true or false
        if logo_text == True:
            print("Logo found. Test Scenario 1 is Passed")
        else:
            print("Logo not found")

    # Test Scenario 2
    def testing_scenarios_2(self):
        self.driver.get('https://www.saucedemo.com/')

        self.driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
        self.driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(5)

        #Getting the text of the error message
        error_text=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3').text
        actual_text="Sorry, this user has been banned. "  #Error text to check whether it display as same as in the login screen

        #This method is to check both error_text and actual_text are same. If not same, it will throw an error
        self.assertEqual(error_text, actual_text)

        print("Test Scenario 2 is Passed")


    # Test Scenario 3
    def testing_scenarios_3(self):
        self.driver.get('https://www.saucedemo.com/')
        self.driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        self.driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(5)

        #Filtering products by price low to high
        drop_locate=self.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select')
        #Clicking the dropdown
        drop_list=Select(drop_locate)
        #Selecting the filter - price low to high
        drop_list.select_by_visible_text('Price (low to high)')
        sleep(5)

        #clicking the lowest priced product
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
        #Clicking add to cart
        self.driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        #Clicking the checkout button
        self.driver.find_element(By.ID,'checkout').click()
        #Typing first_name, last_name and postal code in the screen after clicking checkout
        self.driver.find_element(By.ID, 'first-name').send_keys("John")
        self.driver.find_element(By.ID, 'last-name').send_keys("Doe")
        self.driver.find_element(By.ID, 'postal-code').send_keys("123")
        #Clicking continue button
        self.driver.find_element(By.NAME, 'continue').click()
        time.sleep(3)

        #Getting total price of the product on the screen
        price=self.driver.find_element(By.CSS_SELECTOR,'#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label').text
        time.sleep(5)
        #Orginal price of the product as given
        orginal_price='Total: $8.63'
        sleep(5)

        #Method to check price and orginal_price is same or not
        self.assertEqual(price,orginal_price)

        #Clicking finish button
        self.driver.find_element(By.ID, 'finish').click()
        time.sleep(5)
        #Getting the text of "Thank you" message from the screen"
        message = self.driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2').text
        #Actual message as given
        display="Thank you for your order!"
        #Checking whether message and display is same or not
        self.assertEqual(message, display)
        print("Test Scenario 3 is Passed")



    def tearDown(self):
        #Close the browser.
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
