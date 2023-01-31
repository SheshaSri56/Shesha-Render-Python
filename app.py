from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
Charting_Link = "https://chartink.com/screener/"
Charting_url = 'https://chartink.com/screener/process'

#-shesha-bulloong1



 
Condition = "( {33489} ( weekly high > 1 week ago high and latest high > 1 day ago high and ( {33489} ( latest rsi( 5 ) > 1 day ago rsi( 5 ) and 1 day ago  rsi( 5 ) <= 2 day ago  rsi( 5 ) and weekly rsi( 14 ) > 2 weeks ago rsi( 14 ) and 1 week ago  rsi( 14 ) <= 3 weeks ago  rsi( 14 ) and weekly rsi( 9 ) > 3 weeks ago rsi( 9 ) and 1 week ago  rsi( 9 ) <= 4 weeks ago  rsi( 9 ) and weekly rsi( 14 ) > 5 weeks ago rsi( 14 ) and 1 week ago  rsi( 14 ) <= 6 weeks ago  rsi( 14 ) ) ) ) )  "

#shesha-bulloong1


def GetDataFromChartink1(payload):
    payload = {'scan_clause': payload}
    
    with requests.Session() as s:
        r = s.get(Charting_Link)
        soup = BeautifulSoup(r.text, "html.parser")
        csrf = soup.select_one("[name='csrf-token']")['content']
        s.headers['x-csrf-token'] = csrf
        r = s.post(Charting_url, data=payload)

        df1 = pd.DataFrame()
      
        for item in r.json()['data']:
            df1 = df1.append(item, ignore_index=True)
           
    return df1

data = GetDataFromChartink(Condition)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('sheshadri-python-test-9a0984512950.json', scope)
client = gspread.authorize(creds)
if(len(data.index) != 0):
    data = data.sort_values(by = 'per_chg', ascending=False)
    sheshadri1_test=client.open("SheshaGoldenHand").worksheet("bulloong3" )
    sheshadri1_test.clear()
    #sheshadri1_test.update_title("AGP-SERVICES-BULLISH")
    #sheshadri1_test.update_cell(1,1,"shesha thunai potri")
    sheshadri1_test.update([data.columns.values.tolist()] + data.values.tolist())
    sheshadri1_test.format('A1:G1', {'textFormat': {'bold': True}})
else :
    sheshadri1_test=client.open("SheshaGoldenHand").worksheet("bulloong3")
    
    sheshadri1_test.clear()
    #sheshadri1_test.update_title("BUY POSITIONAL - 95% ACCURACY")
    sheshadri1_test.update_cell(1,1,"shesha thunai potri- data yet to available/no data")




    
    
    
    




if __name__ == '__main__':
    app.run()