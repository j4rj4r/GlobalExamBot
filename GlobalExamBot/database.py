import sqlite3

class Database:
    """
    Database management
    """
    def __init__(self, database_link='./data/data.db'):
        """
        Database constructor
        """
        self.database_link = database_link

    def add_link(self, link):
        """
        Add a link to the database

        :param link String: link of a sheet
        """
        connection = sqlite3.connect(self.database_link)
        c = connection.cursor()
        c.execute('''INSERT INTO sheet_links (link) VALUES (:link);''', (link,))
        c.close()
        connection.commit()

    def link_exist(self, link):
        """
        Returns true if the link exists in the database.

        :param link String: Link of a sheet
        """
        connection = sqlite3.connect(self.database_link)
        c = connection.cursor()
        c.execute('''SELECT * FROM sheet_links WHERE link = ?;''', (link,))
        data = c.fetchall()
        # If this link exist or not
        if len(data) == 0:
            return False
        else:
            return True

def create_table_sheets():
    """
    Create new tables to save the sheets links.

    """
    connection = sqlite3.connect('./data/data.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sheet_links
        (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, link text);''')
    c.close()
    connection.commit()
