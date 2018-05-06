

import numpy as np
import pandas as pd
#train = pd.read_csv('train.csv')
#print(train.shape)
#print(train.head())
#print(train.info(memory_usage='deep'))

#types={'msno':object,'payment_method_id':np.int8, 'payment_plan_days':np.int8, 'plan_list_price':np.int16\
      # ,'actual_amount_paid':np.int16,'is_auto_renew':bool,'transaction_date':np.int64,\
       #'membership_expire_date':np.int64,'is_cancel':bool}
#transactions = pd.read_csv('transactions.csv',nrows=10000000,dtype=types)
#transactions = pd.read_csv('transactions.csv')       
#print(transactions.shape)
#print(transactions.head())
#print(transactions.info(memory_usage='deep'))

members = pd.read_csv('members_v3.csv')
print(members.shape)
print(members.head())
print(members.info(memory_usage='deep'))

user_logs= pd.read_csv('user_logs.csv',nrows=20000000)
print(user_logs.shape)
print(user_logs.head())
print(user_logs.info(memory_usage='deep'))


#print(members.gender.isnull().sum())
#print(members.gender.value_counts())
#print(members.describe())
#print(members.iloc[0:100, 2])
#print(members.bd.value_counts())

#uniqueusers= user_logs.msno.nunique()
#print(uniqueusers)

merged = pd.merge(members,user_logs,how='inner', on=['msno'])
print(merged.info(memory_usage='deep'))