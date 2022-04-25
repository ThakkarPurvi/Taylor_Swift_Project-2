import mysql.connector
import sys


class DatabaseManager(): 

    def __init__(self, connection):
        self.connection = connection
        #self.cur = self.connection.cursor()

    def read_all_table_items(self, table_name):
        if self.__ensure_table_exist(table_name) is True:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM %s" % table_name)
            result = cur.fetchall()
            for row in result:
                print(row)

    def __ensure_table_exist(self, table_name):
        cur = self.connection.cursor()
        cur.execute("SHOW TABLES")
        tables = []
        for table in cur:
            tables.append(table[0])
        if table_name in tables:
            return True
        else:
            return False


