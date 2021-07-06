import time
import csv
import pandas as pd
import psycopg2 as conn
from PostgreSQL_Config import config

#creating connection and configuration
DBconnect = conn.connect(**config)
#init the cursor
cursor = DBconnect.cursor()
#check if connection established!
print(f'[🔥] Connecting to Database ... \n{DBconnect}\
      \n[✔] Connected Successfully!\n')

def UserInput():
    #declaring user information
    print('[🔥] Getting User Details ...')
    DBname = input("Enter New Database Name: ")
    DBtable= input("Enter New Table Name: ")
    DBuser = input("Enter New Database Username: ")
    DBpass = input("Enter New User Password: ")
    print('[✔] All Details Stored Successfully!\n')

def CreateDBUser():
    #create new database user
    startCreateDBUser = time.time()
    print('\n[🔥] Creating New database user ...')
    dbqueryCreateUser = "CREATE USER DBuser WITH PASSWORD 'DBpass';"
    dbqueryGrantUser  = "GRANT ALL PRIVILEGES ON DATABASE DBname TO DBuser;"
    cursor.execute(dbqueryCreateUser, dbqueryGrantUser)
    endCreateDBUser   = time.time()
    print(f'[✔] Finished creating database user!\nTime to create database user: {round(endCreateDBUser-startCreateDBUser, 2)} sec\n')

def CreateDB():
    #create new database
    startCreateDB = time.time()
    print('[🔥] Checking if database exists or creating new one ...')
    dbqueryCreate = "CREATE DATABASE DBname;"
    cursor.execute(dbqueryCreate)
    endCreateDB   = time.time()
    print(f'[✔] Finished creating database!\nTime to create database: {round(endCreateDB-startCreateDB, 2)} sec\n')    

def TableInsertDB():
    #creating database table and calc time of excution
    startCreate = time.time()
    print('[🔥] Checking if table exists or creating one ...')
    dbquery = "CREATE TABLE IF NOT EXISTS DBtable (iso_code text, continent text, location text, date DATE, total_cases decimal NULL, new_cases decimal NULL, total_deaths decimal NULL, new_deaths decimal NULL, icu_patients decimal NULL, new_tests decimal NULL, total_tests decimal NULL, positive_rate real NULL, total_vaccinations decimal NULL, people_vaccinated decimal NULL, people_fully_vaccinated decimal NULL, new_vaccinations decimal NULL, population decimal NULL, median_age decimal NULL, aged_65_older decimal NULL, aged_70_older decimal NULL, female_smokers decimal NULL, male_smokers decimal NULL, human_development_index decimal NULL);"
    cursor.execute(dbquery)
    endCreate   = time.time()
    print(f'[✔] Finished checking/creating Table!\nTime to create/check Table: {round(endCreate-startCreate, 2)} sec\n')
    #Inserting to the table
    csv_data = csv.reader(open('../datasets/gulf.csv'))
    header = next(csv_data)
    print('[🔥] Inserting in Process ...!')
    startInsert = time.time()
    for row in csv_data:
        print(row)
        cursor.execute(
            "INSERT INTO DBtable (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population,median_age,aged_65_older,aged_70_older,female_smokers,male_smokers,human_development_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
    endInsert  = time.time()
    print(f'[✔] Finished inserting!\nTime to insert all data: {round(endInsert-startInsert, 2)} sec\n')

    #Outputing the results
    DBconnect.commit()
    cursor.close()
    DBconnect.close()
    print('[✔] Process Done!')

#excuting all function
UserInput(),CreateDBUser(),CreateDB(),TableInsertDB()