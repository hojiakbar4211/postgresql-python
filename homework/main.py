import datetime
from natficatsion import natficatsion
from postgresConnect import PostgresConnector

class Clock:
    def __init__(self, create_date, create_time, send_message):
        self.create_date = create_date
        self.create_time = create_time
        self.send_message = send_message

    def insert(self):
        with PostgresConnector(password='adgjmptw', db_name='g4') as con:
            self.cur = con.cursor()
            self.sql = """INSERT INTO clock(create_date, create_time, send_message)
                         VALUES(%s, %s, %s);"""
            self.cur.execute(self.sql, (self.create_date, self.create_time, self.send_message))
            con.commit()

    def start(self):
        with PostgresConnector(password='adgjmptw', db_name='g4') as con:
            self.cur = con.cursor()
            self.cur.execute('SELECT * FROM clock')
            res = self.cur.fetchall()
            while True:
                for i in res:
                    today = datetime.datetime.now()
                    time = datetime.time(hour=today.hour, minute=today.minute, second=today.second)
                    day = datetime.date(year=today.year, month=today.month, day=today.day)
                    if i[2] == time and i[1] == day:
                        natficatsion('radar.mp3', i[3])
                    else:
                        pass


clock = Clock('2021-12-11', '18:41:10', 'uy ishi')
clock.insert()
clock.start()
