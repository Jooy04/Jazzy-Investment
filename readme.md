## Project overview
Jazzy Investment(Name changed for privacy), one of 10Alytics clients is a stockbroking firm that deals in 
issuance and trading of stocks on behalf of its customers in the Nigeria Stock 
Exchange. For the analytics team to analyze market trends and place the best bet 
on company stocks, they require the daily stock exchange data published on here: 
https://afx.kwayisi.org/ngx/ 
As one of the data consulting team sent by 10Alytics, we are required to build a web scrapper (data pipeline) to Extract, Transform and load the 
listed companies/securities data from https://afx.kwayisi.org/ngx/ to Jazzy Investment Postgresql database. 

## Tools 
Python

Postgresql

Beautiful soup

Sqlalchemy

## Data source URL
https://afx.kwayisi.org/ngx/

## Process
Extraction:
The request library was using in connecting to the website so as to get the html data using request.get(url) while Beautiful soup was used to process parse the html content 
with the help of lxml parser. Beutiful soup was also used to get the location of the necessary needed table and pandas was used to return the list of the selected tables.
Because the table spans over two pages, data from the 2 pages were concatinated to each other and appended to a new dataframe.
The result was converted to a csv(raw stock data) using pandas.

Transformation:
The data was transformed by creating a function which filled in th emissing volume column data with the mean of all the volume. 
Another transformation was the inclusion of a column named "Extraction_date" which aided in recording the dates each data was extracted.

Loading:
The tranformed data was loaded into posgresql using sqlalchemy and pandas.

## Final postgresql snippet
![Jazzy](https://github.com/Jooy04/Jazzy-Investment/assets/141316339/9abfaa35-4e94-4614-a38b-fab8e88ff753)
