import logging
import os
import sys

from GlobalExamBot.helpers import TypeInField, element_exists, wait_between
from GlobalExamBot.Sheets import Sheets


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Bot:
    
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.email_xpath = '//input[@name="email"]'
        self.password_xpath = '//input[@name="password"]'
        self.index = 0
        self.catindex = 0
        self.categories = ['https://exam.global-exam.com/library/study-sheets/categories/grammar',
                             'https://exam.global-exam.com/library/study-sheets/categories/language-functions',
                             'https://exam.global-exam.com/library/study-sheets/categories/vocabulary']
    
    def login(self):
        """
        Actions for the login form
        """
        email_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.email_xpath)))
        self.actions.move_to_element(email_el).click(email_el).perform()
        TypeInField(self.driver, self.email_xpath, self.configuration.username)
        password_el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, self.password_xpath)))
        self.actions.move_to_element(password_el).click(password_el).perform()
        TypeInField(self.driver, self.password_xpath, self.configuration.password)
        password_el.send_keys(Keys.RETURN)

    def run(self):
        
        profile = f'prof_{self.configuration.username}'

        if not os.path.exists(f'./Profiles/{profile}'):
            self.driver.get('https://auth.global-exam.com/login')
            self.login()
        else :
            self.driver.get('https://exam.global-exam.com/library/study-sheets/categories/grammar')
            if element_exists('//input[@name="email"]', self.driver) :
                self.login()

        logging.info('Logged in')

        sheets_actions = Sheets(self.driver, self.actions, self.configuration)

        while True:
            self.driver.get(self.categories[self.catindex])
            sheets_list = sheets_actions.search()
            if sheets_list :
                logging.info(f'Sheets n??{ self.index }')
                sheets_actions.watch(sheets_list[0])
                self.index +=1
                wait_between(3,10)
            else:
                if self.catindex != len(self.categories) - 1 :
                    logging.info('All visible Sheets have already been read. Use of the next category.')
                    self.catindex += 1
                else:
                    logging.info('No category available.')
                    sys.exit(1)
