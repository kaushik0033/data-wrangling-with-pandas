# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
data=pd.read_csv(path,delimiter=";")
data.shape
print(data.head(2))
data.describe()
data.replace('unknown',np.nan,inplace=True)
data.dropna(inplace=True)
data.isnull().sum()
data.rename({'loan':'previous_loan_status','y':'loan_status'},axis=1,inplace=True)
print(data.job.describe())
data.job.value_counts()
data.groupby(['job'])['loan_status'].value_counts(normalize=True).round(3)*100
data[data['loan_status']=='yes']['education'].value_counts(normalize=True).round(2)*100
data[data['loan_status']=='yes']['previous_loan_status'].value_counts(normalize=True).round(2)*100
pd.pivot_table(data,index='loan_status',columns='marital',values='age')
data[data['marital']=='married']['loan_status'].value_counts()
df_branch_1=pd.DataFrame({'customer_id':['101','102'],'first_name':['Ajay','Vijay'],'last_name':['Kaushik','Patel']})
df_branch_2=pd.DataFrame({'customer_id':['201','202'],'first_name':['Avya','Hezal'],'last_name':['Sharma','Shah']})
df_credit_score =pd.DataFrame({'customer_id':['201','101'],'score':[20,30]})
df_new=pd.concat([df_branch_1,df_branch_2],ignore_index=True)
pd.merge(df_new,df_branch_1,on='customer_id')
# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 

# Find out the information of the `job` column.

# Check the `loan_status`  approval rate by `job`

# Check the percentage of loan approved by `education`

# Check the percentage of loan approved by `previous loan status`

# Create a pivot table between `loan_status` and `marital ` with values form `age`

# Loan status based on marital status whose status is married

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key



