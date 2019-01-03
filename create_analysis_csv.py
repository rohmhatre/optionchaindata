import pandas  as pd
###
srcol=['Name','Curprice','R1','R2','R3','R4','S1','S2','S3','S4']
###
stklist=["nifty", "hdfc", "m&m" ,"escorts", "l&tfh","biocon","banknifty","grasim","kotakbank","techm","tcs","reliance"]

for stname in stklist:
    msg=""
    filename=''
    df=pd.DataFrame(columns=srcol)
    listofnames=open('/Sites/option_chain/lists/'+stname+'.txt')
    s1,s2,s3,s4=[],[],[],[]
    r1,r2,r3,r4=[],[],[],[]
    datelist=[]
    datedata=0
    cur_val=[]
    for name in listofnames:
        filename=name 
    csvdata=pd.read_csv('/Sites/option_chain/'+stname.upper()+'/'+filename.strip('\n'),index_col="StrikePrice")
    csvdata=csvdata.replace("-",0).convert_objects(convert_numeric=True)
    call_list=['CallOI', 'CallChnginOI','CallLTP']
    put_list=['PutOI', 'PutChnginOI','PutLTP']
    call_val=csvdata[call_list]
    put_val=csvdata[put_list]
    itm_val=0
    datedata+=1
    for i in call_val.index:
        if i < csvdata.CurrentVal.iat[0]:
            itm_val=i
        else:
            otm_val=i
            break
    itm_call=call_val[call_val.index[0]:itm_val].sort_values('CallOI',ascending=False)
    otm_call=call_val[otm_val:call_val.index[-1]].sort_values('CallOI',ascending=False)
    itm_put=put_val[otm_val:call_val.index[-1]].sort_values('PutOI',ascending=False)
    otm_put=put_val[call_val.index[0]:itm_val].sort_values('PutOI',ascending=False)
    r1.append(otm_call.index[0])
    r2.append(otm_call.index[1])
    r3.append(otm_call.index[2])
    r4.append(otm_call.index[3])
    s1.append(otm_put.index[0])
    s2.append(otm_put.index[1])
    s3.append(otm_put.index[2])
    s4.append(otm_put.index[3])
    datelist.append(filename.strip('.csv\n'))
    cur_val.append(csvdata.CurrentVal.iat[0])
    ####
    df['Name']=datelist
    df['Curprice']=cur_val
    df['R1']=r1
    df['R2']=r2
    df['R3']=r3
    df['R4']=r4
    df['S1']=s1
    df['S2']=s2
    df['S3']=s3
    df['S4']=s4
    
    analysis_csv=pd.read_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
    analysis_csv=analysis_csv[srcol]
    NewCsvData=analysis_csv.append(df,ignore_index=True)
    df=NewCsvData[srcol]
    if analysis_csv.at[analysis_csv.shape[0]-1,"Name"].lower()!=df.at[0,'Name'].lower():
        NewCsvData.to_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
