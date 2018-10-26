import pandas  as pd
stk = pd.read_csv("NIFTY.csv",index_col="StrikePrice")
stock=stk.replace("-",0).convert_objects(convert_numeric=True)
del stock["Unnamed: 0"]

call_list=['CallOI', 'CallChnginOI', 'CallVolume', 'CallIV', 'CallLTP',
       'CallNetChng', 'CallBidQty', 'CallBidPrice', 'CallAskPrice',
       'CallAskQty','CurrentVal']
put_list=['PutBidQty', 'PutBidPrice', 'PutAskPrice', 'PutAskQty',
       'PutNetChng', 'PutLTP', 'PutIV', 'PutVolume', 'PutChnginOI', 'PutOI','CurrentVal']
current_val=stock["CurrentVal"].values[0]
c_itm_list=[]
c_otm_list=[]
for i in stock.index.values:
    if i < current_val:
        c_itm_list.append(i)
    else:
        c_otm_list.append(i)
call_val=stock[call_list]
put_val=stock[put_list]

call_itm=call_val.loc[c_itm_list]
call_otm=call_val.loc[c_otm_list]
put_itm=put_val.loc[c_otm_list]
put_otm=put_val.loc[c_itm_list]


print(call_itm.to_string())
print(call_otm.to_string())
print(put_otm.to_string())
print(put_itm.to_string())

