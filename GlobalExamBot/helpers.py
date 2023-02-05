# Standard libraries
import sys
import logging
from time import sleep
from random import uniform
import argparse

from selenium.webdriver.common.by import By

import GlobalExamBot.constants as const


class Helpers:
    def __init__(self):
        """
        Helpers class constructor
        """

    def ask_to_exit(self):
        """
        The user is asked if he wants to leave

        :return: Boolean
        """
        try:
            user_input = input('Type "STOP" to stop the application:\n')

            # Continue
            if user_input.upper() == "STOP":
                return True
            # Exit
            else:
                print('/!\\ Please type "STOP" to exit the bot execution /!\\')
                return False
        except Exception:
            return False

    def load_configuration(self):
        """
        this method allows you to load arguments.
        :return: args 
        """
        header()
        # Load all configuration variables
        parser = argparse.ArgumentParser()
        parser.add_argument('-p','--password', help='Set GlobalExam password', type=str, required=True)
        parser.add_argument('-u','--username',help='Set GlobalExam username', type=str, required=True)
        parser.add_argument('--noheadless',help='Desactivate Chrome headless mode', required=False, action='store_true')
        args = parser.parse_args()
        return args

    def logging_configuration(self, logging_level=logging.INFO, filename='data/logs/bot_globalexam.log'):
        logging.basicConfig(filename=filename,
                            level=logging_level,
                            format='%(asctime)s - %(levelname)s - %(message)s')
                
        root_logger = logging.getLogger()
        root_logger.setLevel(logging_level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

# Utilities methods
def header():
    """
    This function display an header when the script start
    """
    const.init()
    logging.info('==\t=============================================================\t==')
    logging.info('==\t                   ' + const.APP_NAME + '                            \t==')
    logging.info('==\t                   version : ' + const.VERSION + '                         \t==')
    logging.info('==\t=============================================================\t==')

def wait_between( min, max):
    """
    Wait random time in second beetween min and max seconds, to have an not linear behavior and be more human.
    """
    rand=uniform(min, max)
    sleep(rand)

def TypeInField(element, xpath, myValue):
    """Type in a field"""
    val = myValue
    elem = element.find_element(by=By.XPATH, value=xpath)
    for i in range(len(val)):
        elem.send_keys(val[i])
        wait_between(0.2, 0.4)
    wait_between(0.4, 0.7)

def element_exists(xpath, element, by=By.XPATH):
    """
    Check if an element exist
    
    :return: Boolean
    """
    try:
        wait_between(2,3)
        element.find_element(by=by, value=xpath)
    except:
        return False
    return True