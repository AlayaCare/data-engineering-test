"""
Reading database from docker container and merging tables into single dataframe
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine

# grabbing the database, 172.18.0.2 is ip address of docker container,
# 3306 is the port
engine = create_engine('mysql+pymysql://root:root@172.18.0.2:3306/test')

# hard coded solution that works here
# assigning database to dataframes
profiles_df = pd.read_sql_query('SELECT * FROM profiles', engine)
clients_df = pd.read_sql_query('SELECT * FROM clients', engine)

# merging dataframes
merged_df = clients_df.merge(
    profiles_df, 'outer', left_on='idprofile', right_on='contact_id')

"""
# ideally somehting like this would be better, but the condition got hard coded regardless:

for table in engine.table_names():
    sql_query = 'SELECT * FROM '+str(table)
    new_df =  pd.read_sql_query(sql_query, engine)
    final_df = final_df.merge(new_df, 'outer', left_on=condition_old_table, right_on=condition_new_table)
"""
