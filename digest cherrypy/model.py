from sqlobject import *
import os.path

dbfile = 'enzyme.db3'

# Magic formatting for database URI
conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:'+ conn_str

sqlhub.processConnection = connectionForURI(conn_str)

class enzyme_list(SQLObject):
    name = StringCol()
    amount = IntCol()
    digest = StringCol()
    start_pos = StringCol()

class enzymes():
    enzyme = []
    def __init__(self):
        for e in enzyme_list.select():
            self.enzyme.append((e.name,e.amount,e.digest,e.start_pos))
