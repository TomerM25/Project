import pymysql
from datetime import datetime

db_host = 'sql7.freemysqlhosting.net'
db_user = 'sql7620888'
db_pass = 'r3b4L5FbeQ'
db_schema_name = 'sql7620888'


class ConnectionDb:
    def __init__(self):
        self._conn = pymysql.connect(host=db_host, port=3306, user=db_user, passwd=db_pass, db=db_schema_name)
        self._conn.autocommit(True)
        self.cursor = self._conn.cursor()

    def create_db(self):
        """
        Create the 'users' table in the specified database schema.

        :return:
        """
        try:
            statement_to_execute = f"CREATE TABLE `{db_schema_name}`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL, `creation_date` VARCHAR(50) NOT NULL, PRIMARY KEY (`user_id`));"
            self.cursor.execute(statement_to_execute)

        except pymysql.Error as e:
            print(f'error in connection to DB:\n', e)

    def get_user(self, user_id: str):
        """
        Retrieve a user from the 'users' table by user ID.

        :param user_id: user id to get from the table
        :return: the string representation of the given user id
        """
        try:
            # Getting data from table “users”
            self.cursor.execute(f"SELECT * FROM users WHERE user_id={user_id};")

            # Check if data received from Database
            if self.cursor.rowcount == 0:
                return ''
            else:
                return self.cursor.fetchone()

        except pymysql.Error as e:
            print(f'error in connection to DB:\n', e)

    def add_user(self, user_id: str, user_name: str):
        """
        Add a user to the 'users' table with the specified user ID and name.

        :param user_id: user id to insert the table
        :param user_name: user name to insert the table
        :return:
        """
        try:
            timestamp_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # Inserting data into table
            self.cursor.execute(
                f"INSERT into users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', '{timestamp_str}')")

        except pymysql.Error as e:
            print(f'error in connection to DB:\n', e)

    def update_user(self, user_id: str, user_name: str):
        """
        Update the name of a user in the 'users' table by user ID.

        :param user_id: user id of the user name to update in table
        :param user_name: new user name to update in table
        :return:
        """
        try:
            # Updating <user_name> data inside the table according to <user_id>
            self.cursor.execute(f"UPDATE users SET user_name = '{user_name}' WHERE user_id = {user_id}")

        except pymysql.Error as e:
            print(f'error in connection to DB:\n', e)

    def delete_user(self, user_id: str):
        """
        Delete a user from the 'users' table by user ID.

        :param user_id:
        :return:
        """
        try:
            # Deleting data into table according to <user_id>
            self.cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")

        except pymysql.Error as e:
            print(f'error in connection to DB:\n', e)
