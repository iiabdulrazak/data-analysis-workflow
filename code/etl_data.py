try:
    import pandas as pd
except Exception as e:
    print(f"error while importing packages! \n\n{e}")

try:
    #import datasets from data.gov.sa
    startExtracting = time.time() #starting time of Extracting data from github repo
    data = pd.read_excel('./datasets/original/all_job_seekers2021.xlsx') #transfaring data to pandas dataframe
    endExtracting = time.time() #ending time of the Extracting proccess
    print(f'Time to Extract Data: {round(endExtracting-startExtracting,2)} sec')
except Exception as e: #if the proccess of Extracting the data didn't work, will print error message
    print(f'Error while Extracting data!\n\n{e}')

try:
    data.drop(data.index[[0]], inplace=True) #droping first row
    #renaming columns to be in regex format
    data.columns = ['id','gender','region','city','age','edu_degree','major','gpa','gpa_from','inistitute','inserted_date','grad_date','record_from']
    #droping unwanted columns
    data.drop(['record_from','grad_date','inserted_date','gpa_from','gpa'], axis=1, inplace=True)
    
    data.replace('انثى','أنثى', inplace=True) #replacing names to clean missed female count
    data.fillna('لا يوجد', inplace=True) #filling nan with 'لا يوجد' because we need it
    
    #cleaning data to be ready for reporting and dashboards
    un_wanted = data[(data['gender'] == 'لا يوجد') | (data['edu_degree'] == 'لا يوجد') | (data['major'] == 'لا يوجد') | (data['inistitute'] == 'لا يوجد')].index #cleaning 'لايوجد' from importing columns
    data.drop(un_wanted , inplace=True) #droping it
    
    #now we extracting all males and females between age 22 to 30 and graduated
    male_grad_dbmd = data.loc[(data['gender'] == 'ذكر') & (data['age'] > 22) & (data['age'] <=30) & (data['inistitute'].str.startswith("جامعة"))]
    female_grad_dbmd = data.loc[(data['gender'] == 'أنثى') & (data['age'] > 22) & (data['age'] <=30) & (data['inistitute'].str.startswith("جامعة"))]
    #concating two datas
    males_females_with_dbmd = pd.concat([male_grad_dbmd,female_grad_dbmd])
except Exception as e: #if the wrangling proccess didn't work, will print error message
    print(f'Error while wrangling the data!\n\n{e}')

#checking if the folder exists to overwrite or create new
data.to_csv('../datasets/created/seekers.csv', index=False)
males_females_with_dbmd.to_csv('./datasets/created/males_and_females_with_dbmd.csv', index=False)
print('Dataset File Saved!')
