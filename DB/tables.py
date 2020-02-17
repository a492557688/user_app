from DB.mysql_db import MysqlDb
class Domain(MysqlDb):
    def __init__(self):
        self._db_name='app'
        self.table = 'tb_domain '
        MysqlDb.__init__(self,self._db_name)


    #下面是 这个表的操作 函数
    def query(self,checkfield='*',**kwargs):
        sql=f'select {checkfield} from {self.table} where 1=1 '
        parms=''
        for k,v in kwargs.items(): parms+=f' and {k}={v}  '
        sql = sql+parms
        return self.getDb().query(sql)

    def insert_data(self,db_list):
        # uuid, domain, server_ip, t_mobile, company, dns_delay, dns_suc, Tcpbulddelay, tcp_suc_rate
        db_list=[tuple(d for d in obj) for obj in db_list ]
        sql=f'INSERT INTO {self.table}(uuid,domain,ip,t_mobile,company,dnsreplydelay,tcpbuilddelay,dns_suc_rate,tcp_suc_rate) values(?,?,?,?,?,?,?,?,?)'
        self.getDb().update(sql,db_list)


