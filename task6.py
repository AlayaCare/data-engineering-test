"""
Adding random column to profiles database
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

sLength = len(profiles_df.index) #number of rows in dataframe
#np.random.randint returns an array of random integer between 0 and 10, of length sLength,
profiles_df['random'] = pd.Series(np.random.randint(9,size = sLength), index=profiles_df.index)
#writting new DF back to the docker
profiles_df.to_sql(con=engine,name = 'profiles', if_exists='replace',index=False)
#will rewrite column 'random' if it is already in profiles, 
