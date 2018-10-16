"""
Rewritting
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import numpy as np
#data frame loading code from task 3:
# grabbing the database, 172.18.0.2 is ip address of docker container,
# 3306 is the port
engine = create_engine('mysql+pymysql://root:root@172.18.0.2:3306/test')
# hard coded solution
# assigning database to dataframes
profiles_df = pd.read_sql_query('SELECT * FROM profiles', engine)
#updating column to new value
profiles_df['value'] = 'fifth row'
#writting updated dataframe back to the database in docker
profiles_df.to_sql(con=engine,name = 'profiles', if_exists='replace',index=False)
#will rewrite column 'random' if it is already in profiles,
