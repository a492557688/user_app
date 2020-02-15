from DB.mysql_db import MysqlDb
class domain(MysqlDb):
    def __init__(self):
        self._db_name='app'
        self.table = 'tb_domain '
        MysqlDb.__init__(self,self._db_name)


    #下面是 这个表的操作 函数
    def query_all(self,**kwargs):
        sql=f'select * from {self.table} where 1=1 '
        parms=''
        for k,v in kwargs.items(): parms+=f' and {k}={v}  '
        sql = sql+parms
        return self.getDb().query(sql)

    # def insert_data(self,data):


