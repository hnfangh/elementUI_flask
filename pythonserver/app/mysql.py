import pymysql

_host = '47.106.133.253'
_port = 3306
_user = 'root'
_password = '123456'
_charset = 'utf8'

class DataBase:

    def __init__(self):
        self.db = pymysql.connect(host=_host, port=_port, user=_user, password=_password, charset=_charset)
        self._cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def insertSQL(self,sql):
        self._cursor.execute(sql)
        self.db.commit()
        self.db.close()

    def updateSQL(self,sql):
        self._cursor.execute(sql)
        self.db.commit()
        self.db.close()

    def selectSQL(self,sql):
        self._cursor.execute(sql)
        self.db.close()
        return (self._cursor.fetchall())

    def deleteSQL(self,sql):
        self._cursor.execute(sql)
        self.db.commit()
        self.db.close()
