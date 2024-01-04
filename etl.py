import requests
from datetime import datetime
import os
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

#database credentials

username= os.getenv('db_username')
host=os.getenv('host')
password=os.getenv('password')
db_name= os.getenv('database_name')
port=os.getenv('port')



#EXTRACTION FROM WEBSITE
pages=[1,2]
dfs=[]
def extraction():
    for page in pages:
        url=f'https://afx.kwayisi.org/ngx/?page={page}'
        response= requests.get(url)
        scrapped= response.content
        soup= BeautifulSoup(scrapped, 'lxml')
        html=str(soup.find_all('table')[3])
        df=pd.read_html(html)[0]
        dfs.append(df)
        my_dfs=pd.concat(dfs)
        my_dfs.to_csv('raw_stocks_data', index=False)
        print ('Extraction sucessfull')
        # print(url)
        
#TRANSFORMATION
        #DATE COLUMN WHEN DATA WAS SCRAPPED
        #NULL VOLUME OF TRADE SHOULD BE CLEANED TO TOTAL COMPANIES MEAN VOLUME 


def transformation():
        df= pd.read_csv('raw_stocks_data')
        df['Extraction_date']= datetime.now() #to get the current time of extraction
        df['Volume']=df['Volume'].fillna(df['Volume'].mean())
        df.to_csv('transformed_stock_data', index=False)
        print('Data has been transformed successfully')

def loading():
      df=pd.read_csv('transformed_stock_data')
      engine=create_engine(f'postgresql+psycopg2://{username}:{password}@{host}: {port}/{db_name}')
      df.to_sql('stock_data', con=engine, if_exists='replace', index=False)
      print('Data successfully loaded to database')
        
        
extraction()
transformation()
loading()