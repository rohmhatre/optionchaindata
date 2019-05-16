import requests
import pandas as pd
from bs4 import BeautifulSoup
import os,glob
from datetime import datetime
import pandasql as ps

global stock_price

def getoptionchain(i,expiry):
# for i in ListOfStock.readlines():
    i=i.strip('\n')
    if '&' in i:
        i=i.replace('&','%26')
    cur_date=datetime.now().strftime("%d-%m-%Y_%H:%M")
    Base_url =("https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?instrument=OPTIDX&symbol="+i+"&date="+expiry)

    page = 0
    page = requests.get(Base_url,headers={'Cache-Control': 'no-cache'})
    page.status_code
    page.content

    soup = BeautifulSoup(page.content,"html.parser")
    table_cls_1 = soup.find_all(id="octable")
    stock_name=i

#find table header
    col_list = []
    for mytable in table_cls_1:
        table_head = mytable.find('thead')
        try:
            rows = table_head.find_all('tr')
            for tr in rows:
                flag=0
                cols = tr.find_all('th')
                for th in cols:
                    er = th.text
                    if er=="Strike Price":
                        flag=1
                    if flag==0:
                        ee ='Call'+er.replace(' ','')
                    else:
                        if er == "Strike Price":
                            ee=er.replace(' ','')
                        else:
                            ee ='Put'+er.replace(' ','')
                    col_list.append(ee)
        except:
            print("no thead")
    col_list_fnl = [e for e in col_list if e not in ('CallCALLS','CallPUTS','CallChart','Call\xc2\xa0','Call\xa0','PutChart')]

    #find table body values
    table_cls_2 = soup.find(id="octable")
    all_trs = table_cls_2.find_all('tr')
    req_row = table_cls_2.find_all('tr')
    new_table = pd.DataFrame(index=range(0,len(req_row)-3), columns=col_list_fnl)
    row_marker = 0
    for row_number, tr_nos in enumerate(req_row):
        if row_number <=1 or row_number == len(req_row)-1:
            continue
        td_columns = tr_nos.find_all('td')
        select_cols = td_columns[1:22]
        cols_horizontal = range(0,len(select_cols))
        for nu, column in enumerate(select_cols):
            utf_string = column.get_text()
            utf_string = utf_string.strip('\n\r\t": ')
            tr = utf_string#.encode('utf8')
            tr = tr.replace(',' ,'')
            new_table.ix[row_marker,[nu]]=tr

        row_marker+=1
##find name
    stock_info = soup.find_all(style="font-size:1.2em;")
    print(stock_info)
    if stock_info != []:
        stock_price=float(stock_info[0].text.split()[1])
        print(stock_name,stock_price)
        #print(new_table)
        new_table["CurrentVal"]=stock_price

    if not os.path.exists(stock_name+"/"+expiry):
        os.makedirs(stock_name+"/"+expiry)
    new_table.to_csv(stock_name+"/"+expiry+"/"+stock_name+"_"+cur_date+".csv")
    print(stock_name+"/"+expiry+"/"+stock_name+"_"+cur_date+".csv")

indexlist=['NIFTY','BANKNIFTY','NIFTYIT']
lastfile = glob.glob("/Sites/Stock_Watch/tmp/fo*")
lastfile.sort(key=os.path.getmtime)
CsvData = pd.read_csv(lastfile[-1])
for index in indexlist:
    IndexEx="select DISTINCT EXPIRY_DT from CsvData where INSTRUMENT='OPTIDX' and SYMBOL='"+index+"';"
    IndexOpEx=ps.sqldf(IndexEx, locals())
    IndexOpExpiry=list(IndexOpEx["EXPIRY_DT"])
    #print(IndexOpExpiry)
    a=5
    if index == 'NIFTYIT':
        a=3
    for expiry in IndexOpExpiry[:a]:
        expiry=expiry.upper()
        expiry=expiry.replace('-','')
        expiry=expiry.strip('0')
        print(index,expiry)
        getoptionchain(index,expiry)
        
