import sqlite3

class Database_akun:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, nama text, password text, job text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Users")
        rows = self.cur.fetchall()
        return rows

    def insert(self,nama,password,job):
        self.cur.execute("INSERT INTO Users VALUES (NULL, ?, ?, ?)",
        (nama,password,job))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Users WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,nama,password,job):
        self.cur.execute("UPDATE Users SET nama = ?, password = ?, job = ? WHERE id = ?" , (nama,password,job,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

