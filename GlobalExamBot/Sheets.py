import logging
from math import floor

from GlobalExamBot.helpers import wait_between
from GlobalExamBot.database import Database

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class Sheets:
    def __init__(self, driver, action, configuration):
        self.driver = driver
        self.actions = action
        self.configuration = configuration
        self.pagecard_xpath = '//a[@class="mb-4 w-full lg:w-auto lg:mb-0 button-solid-primary-small"]'
        self.Sheetscard_xpath = '//div[@class="container py-8 lg:pt-12 lg:pb-12"]'
        self.manageSheets = Database()

    def search(self):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.XPATH, self.pagecard_xpath)))
        page_cards = self.driver.find_elements(by=By.XPATH, value=self.pagecard_xpath)
        card_list = []
        for card in page_cards :
            if not self.manageSheets.link_exist(card.get_attribute('href')):
                card_list.append(card)
        return card_list

    def watch(self, Sheets_el):
        self.actions.move_to_element(Sheets_el).click(Sheets_el).perform()
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.XPATH, self.Sheetscard_xpath)))
        max_height = self.driver.execute_script("return document.body.scrollHeight")
        for height in range(0, max_height, floor(max_height/10)) :
            self.driver.execute_script(f"window.scrollTo(0, { height })")
            logging.info(f'Position : { height } | MaxPosition: { max_height }')
            wait_between(25,30)
        logging.info(f'Add new url in database: { self.driver.current_url }')
        self.manageSheets.add_link(self.driver.current_url)
