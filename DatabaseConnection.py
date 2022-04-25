import mysql.connector
import sys
from config import USER, PASSWORD, HOST


"""
A Class to create connection between Python code and MySQL database.
See module mysql.connector.

Attributes
     ----------
    database_name : str
        name of the local MySQL

Methods
    -------
    __connect_to_database():
        Private method to establish connection to MySQL.

"""


class DatabaseConnectionError(Exception):
    pass


class DatabaseConnection(): # DatabaseManger or ConnectionDatabaseFactory

    """
    Constructs all the necessary attributes for the DatabaseConnection object.

            Parameters
            ----------
                database_name : str
                name of the local MySQL

    """

    def __init__(self, database_name):
        self.database_name = database_name

    def __connect_to_database(self):
        """
        Creates connection btw Python code and MySQL.

        Returns
        -------
        XX
        """
        connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database= self.database_name
                                        )
        return connection

    def _ensure_database_connection(self):
        connection = None
        try:
            if self.__ensure_database_exist() is True:
                connection = self.__connect_to_database()
            else:
                sys.exit("Database does not exist \nExit Program")  
        except Exception:
            raise DatabaseConnectionError("Failed to read data from DB")
        finally:
            if connection:
                print("Connected to DB: %s" % self.database_name )
                return connection
            else:
                sys.exit("Failed to read data from DB \nExit Program")  

    def create_connect(self):
        connection = self._ensure_database_connection()
        return connection

    def __ensure_database_exist(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                                                host=HOST,
                                                user=USER,
                                                password=PASSWORD,
                                                auth_plugin='mysql_native_password'
                                                )
            cur = connection.cursor()
            cur.execute("SHOW DATABASES")
        except Exception:
            raise DatabaseConnectionError("Failed to read data from DB")
        finally:
            if connection:
                databases = []
                for database in cur:
                    databases.append(database[0])
                connection.close()
                if self.database_name in databases:
                    return True
                else:
                    return False
            else:
                sys.exit("Failed to read data from DB \nExit Program")  
