"""Program to retrieve data from the database."""
import mysql.connector as con


class retrieve (object):
    """Functions for various retrievals."""
    def __init__ (self):
        self.sat = con.connect (
            host = "localhost",
            user = "root",
            passwd = "laferrar1",
            database = "satisfy"
        )
        self.cur = self.sat.cursor(buffered = True) # 'bufffered = True' was causing the MySQL errors(unread parameter and arguments missing error). If you get any such errors, check this line.

    def get_uid(self, mail):
        """Retruns uid using mail."""
        sql = 'select uid from user_mail where mail = %s'
        val = (mail, )

        self.cur.execute(sql, val)
        result = self.cur.fetchone()

        return result[0]

    def get_tot_time(self, uid):
        """Returns total time logged."""
        sql = 'select tot_time from user where uid = %s'
        val = (uid, )

        self.cur.execute(sql, val)
        result = self.cur.fetchone()

        return result[0]

    def get_tot_dist(self, uid):
        """Returns total distance coverec."""
        sql = 'select tot_dist from user where uid = %s'
        val = (uid, )

        self.cur.execute(sql, val)
        result = self.cur.fetchone()

        return result[0]

    def get_fin_speed(self, uid):
        """Retruns speed based on total distance and total time."""
        sql = 'select fin_speed from user_speed where uid = %s'
        val = (uid, )

        self.cur.execute(sql, val)
        result = self.cur.fetchone()

        return result[0]

    def get_run_num(self, uid, rdate):
        """Returns the run_num from run table for that particular day."""
        sql = 'select max(run_num) from run where uid = %s and rdate = %s'
        val = (uid, rdate)

        self.cur.execute(sql, val)
        result = self.cur.fetchone()

        return result[0]

    def get_all_runs(self, uid):
        """Retruns the run details of one user."""
        sql = 'select dist, time, rdate from run where uid = %s'
        val = (uid, )
        self.cur.execute(sql, val)
        result = self.cur.fetchall()

        return result

    def get_all_challenges(self, uid):
        """Returns the challenges of a user."""
        sql = 'select cid from participate where uid = %s'
        val = (uid, )
        self.cur.execute(sql, val)

        res = self.cur.fetchall()

        result = []
        sql = 'select dist, time, type, start, end from challenge where cid = %s'
        for i in res:
            val = (i[0], )
            self.cur.execute(sql, val)
            r = self.cur.fetchone()
            result.append(r)

        return result

    def make_commit(self):
        """Commit the changes into the database."""
        self.sat.commit()