#!/usr/bin/env python3

import  sys
import logging

from GlobalExamBot.helpers import Helpers
from GlobalExamBot.database import create_table_sheets

from GlobalExamBot.driver import Driver
from GlobalExamBot.bot import Bot

def main():
    """
    Main function
    """
    try:
        helpers = Helpers()

        # Load all configuration variables
        config = helpers.load_configuration()

        logging.info('Starting bot ...')

        create_table_sheets()

        profile = f'prof_{config.username}'

        logging.info(f'Username : {config.username}')

        # Initialize driver and actions
        if config.noheadless :
            driver, action = Driver(profile).setup(headless=False)
        else:
            driver, action = Driver(profile).setup()

        # Start bot actions
        Bot(driver, action, config).run()

    except KeyboardInterrupt :
        if not helpers.ask_to_exit() :
            logging.info('Restart bot ...')
            driver.quit()
            main()
        else :
            logging.info('Bye bye !')
            sys.exit(1)

if __name__ == "__main__":
    Helpers().logging_configuration()
    main()
