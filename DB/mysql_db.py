import pymysql
from DB.log import logger1_mysql as  log
from DB.env import getMysqlCfg
import time


class Mysql:
    def __init__(self, dbname=None, day=None):
        if dbname is None:
            raise  ValueError("sql DB 必须选择否则创建失败")
        self._db_name = dbname
        self._db_host, self._db_port, self._db_user, self._db_pass = getMysqlCfg()
        self._db_connect_flag = False
        log.debug(f'connect mysql: {self._db_user}@tcp({self._db_host}):{self._db_port}')
        self._connect()

    # 释放数据库的连接
    def __del__(self):
        if self._db_connect_flag:
            self._db.close()

    # 打开数据库连接
    def _connect(self):
        from warnings import filterwarnings
        filterwarnings('error', category=pymysql.Warning)
        self._db = pymysql.connect(
            host=self._db_host,
            user=self._db_user,
            password=self._db_pass,
            port=self._db_port,
            # db = self._db_name,
            charset = "GBK",
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self._db.cursor()

        if not self.databaseExists():
            self.createDatabase()
        self.useDatabase()
        self._db_connect_flag = True

    def databaseExists(self):
        sql = f"SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME='{self._db_name}';"
        dbs = self.query(sql)
        if len(dbs) == 1:
            return True
        else:
            return False

    def createDatabase(self):
        self.query("CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET utf8mb4" % (self._db_name))

    def useDatabase(self):
        sql = f"USE {self._db_name}"
        self.query(sql)

    def close(self):
        if self._db_connect_flag:
            self._db.close()

    def query(self, sql):
        try:
            # log.info("MYSQL查询：%s" % sql)
            self._cursor.execute(sql)
            results = self._cursor.fetchall()
        except Exception as e:
            log.exception('FAILED sql=%s, exception:%s' % (sql, e))
            results = ()
        return results

    # 执行多条语句的插入、删除或更新
    def update(self, sql, args):
        try:
            sql = sql.replace('?', '%s')
            self._cursor.executemany(sql, args)
            self.commit()
            return True
        except Exception as e:
            log.exception('exception:%s [rollback] sql:%s' % (e, sql))
            log.error(args)
            self.rollback()
            return False

    # 执行多条语句（不带参数，带参数时使用update）
    def script(self, sqls):
        try:
            start = time.time()
            sql_list = sqls.split(';')
            for sql in sql_list:
                if len(str.strip(sql)) == 0:
                    continue
                self._cursor.execute(sql)
            self._db.commit()
            end = time.time()
            log.debug('[script] spent time: %.02f' % (end - start))
        except Exception as e:
            log.exception('exception:%s [rollback] %s ' % (e, sql))
            self._db.rollback()

    def insert(self, sqls, data):
        try:
            log.debug("!!! 插入语句：%s,带插入数据%s" % (sqls, data))
            self._cursor.execute(sqls, data)
            insert_id = self._cursor.lastrowid
            return insert_id
        except Exception as e:
            log.exception("@@@ 插入错误：%s  \n 语句%s 参数：%s" % (e, sqls, data))
            self.rollback()
            return 0

    def replace(self, sql):
        log.debug("!!! SQL替换：%s" % sql)
        try:
            self._cursor.execute(sql)
            self.commit()
            return True
        except Exception as e:
            log.exception("@@@ SQL替换错误：%s \n 语句%s" % (e, sql))
            self.rollback()
            return False

    def delete(self, sql):
        try:
            self._cursor.execute(sql)
            self.commit()
            return True
        except Exception as e:
            log.exception(f"@@@ SQL删除错误：{e}")
            self.rollback()
            return False

    def commit(self):
        self._db.commit()

    def rollback(self):
        self._db.rollback()

import  sys
from tools.config import  *
from DB.log import logger1_mysql as  log
class MysqlDb():
    def __init__(self, dbname=None, daily=None):
        try:
            self._db = Mysql(dbname=dbname, day=daily)
            if len(self._db.query("SHOW TABLES")) == 0:
                #这个db下啥也没有有创一些表
                sqls = readConfig('app.sql')
                log.info(f"\n{'-'*20} 初始化SQL数据库 {'-'*20}\n{sqls}")
                self._db.script(sqls)
        except Exception as e:
            log.exception(f"初始化MYSQL错误：{e}")
            sys.exit(100)

    def getDb(self):
        return self._db
