# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:36:42 2018

@author: liamc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

members = pd.read_csv(r'C:\Users\liamc\OneDrive\Desktop\Data Science\KKbox\members_v3.csv')
members =members.loc[(members['bd']>2) & (members['bd']<99)]
train = pd.read_csv(r'C:\Users\liamc\OneDrive\Desktop\Data Science\KKbox\train.csv')
df = pd.merge(members,train,how='inner',on=['msno'])
df = df.iloc[0:50000]
msnos = df['msno']

#transactions = pd.read_csv(r'C:\Users\liamc\OneDrive\Desktop\Data Science\KKbox\transactions.csv')
#transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'],format='%Y%m%d')
#relevant_transactions = transactions.loc[transactions['msno'].isin(msnos)]
#relevant_transactions['membership_expire_date'] = pd.to_datetime(relevant_transactions['membership_expire_date'],format='%Y%m%d')
#relevant_transactions = relevant_transactions.loc[relevant_transactions['membership_expire_date']>'2017-02-28']


user_logs= pd.read_csv(r'C:\Users\liamc\OneDrive\Desktop\Data Science\KKbox\user_logs.csv',nrows=40000000)
user_logs['date'] = pd.to_datetime(user_logs['date'],format='%Y%m%d')
relevant_user_logs = user_logs.loc[user_logs['msno'].isin(msnos)]
relevant_user_logs =relevant_user_logs.loc[relevant_user_logs['date']>'2017-01-29']

#relevant_transactions.to_csv('relevant_transactions.csv',index=False)
relevant_user_logs.to_csv('relevant_user_logs.csv',index=False)

#
#rel_transactions_userlogs = pd.merge(relevant_transactions,relevant_user_logs,how='inner',on='msno')
#rel_transactions_userlogs.to_csv('rel_tansactions_userlogs.csv',index=False)

#transactions_userlogs = pd.read_csv('rel_tansactions_userlogs.csv')
#pivoted_transactions_userlogs = pd.pivot_table(transactions_userlogs,index=['msno'],columns=['transaction_date','date'])
#pivoted_transactions_userlogs.reset_index(level=0,inplace=True)
#df=pd.merge(pivoted_transactions_userlogs,df,how='inner',on='msno')

#df = pd.read_csv('sample_df.df.to_csv('wrangled_sample_df.csv',index=False)csv') ?????

#transactions = pd.read_csv('relevant_transactions.csv')
#user_logs= pd.read_csv('relevant_user_logs.csv')
#pivoted_transactions = pd.pivot_table(transactions, index=['msno'], columns=['transaction_date'])
#pivoted_transactions.reset_index(level=0, inplace=True)
#df = pd.merge(pivoted_transactions,df,how='inner',on='msno')
#pivoted_user_logs= pd.pivot_table(user_logs, index=['msno'],columns =['date'])
#pivoted_user_logs.reset_index(level=0, inplace=True)
#df = pd.merge(pivoted_user_logs,df,how='inner',on='msno')
#
#churners = df.loc[df['is_churn']==1]
#nonchurners = df.loc[df['is_churn']==0]
#churners = churners.sample(n=1000)
#nonchurners = nonchurners.sample(n=4000)
#df2= pd.concat([nonchurners,churners])
