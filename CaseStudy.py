import pandas as pd
import re

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

newline = re.compile(r"\n")
semicolon = re.compile(r";")

arr = newline.split(data)
df = []

for i in range(1,len(arr)-1):
    df.append(semicolon.split(arr[i]))
    
table = pd.DataFrame(df, columns = semicolon.split(arr[0]))

#Transforming FlightCodes column
table['FlightCodes'] = pd.to_numeric(table['FlightCodes']).astype('Int64')
table['FlightCodes'] = table['FlightCodes'].fillna(10+table['FlightCodes'].shift(1))


#Splitting To_From into two columns and fixing capitalization 
table[['To','From']] = table['To_From'].str.split('_', expand = True)
del table['To_From']

table['To'] = table['To'].str.capitalize()
table['From'] = table['From'].str.capitalize()

#Getting rid of punctuation in Airline Code column

table['Airline Code'] = table['Airline Code'].str.replace('[^a-zA-Z\s]','')
