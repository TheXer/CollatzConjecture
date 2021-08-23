import mysql.connector


class MySQLWrapper:
    def __init__(self):
        self.database = None
        self.cursor = None

    def __enter__(self):
        self.database = mysql.connector.connect(user="root", password="xxx", database="Collatz")
        self.cursor = self.database.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.cursor.close()
            self.database.close()

        except AttributeError:
            print('Not closable.')
            return True

    def query(self, query: str, val=None):
        self.cursor.execute(query, val or ())
        return self.cursor.fetchone()

    def execute(self, query, val=None, commit=False):
        self.cursor.execute(query, val or ())
        if commit:
            self.database.commit()
