import pandas  as pd
import os
###
srcol=['Name','Curprice','RH1','RH2','RL1','RL2','SH1','SH2','SL1','SL2']
###
stklist=open('/Sites/option_chain/lists/stlist.txt')

def create_analysis(stname,filename):
    df=pd.DataFrame(columns=srcol)
    sh1,sh2,sl1,sl2=[],[],[],[]
    rh1,rh2,rl1,rl2=[],[],[],[]
    datelist=[]
    datedata=0
    cur_val=[]    
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
    itm_call=call_val[call_val.index[0]:itm_val].sort_values('CallChnginOI',ascending=False)
    otm_call=call_val[otm_val:call_val.index[-1]].sort_values('CallChnginOI',ascending=False)
    itm_put=put_val[otm_val:call_val.index[-1]].sort_values('PutChnginOI',ascending=False)
    otm_put=put_val[call_val.index[0]:itm_val].sort_values('PutChnginOI',ascending=False)
    rh1.append(otm_call.index[0])
    rh2.append(otm_call.index[1])
    rl1.append(otm_call.index[-1])
    rl2.append(otm_call.index[-2])
    sh1.append(otm_put.index[0])
    sh2.append(otm_put.index[1])
    sl1.append(otm_put.index[-1])
    sl2.append(otm_put.index[-2])
    datelist.append(filename.strip('.csv\n'))
    cur_val.append(csvdata.CurrentVal.iat[0])
    ####
    df['Name']=datelist
    df['Curprice']=cur_val
    df['RH1']=rh1
    df['RH2']=rh2
    df['RL1']=rl1
    df['RL2']=rl2
    df['SH1']=sh1
    df['SH2']=sh2
    df['SL1']=sl1
    df['SL2']=sl2
    
    if os.path.isfile('/Sites/option_chain/lists/Analysis_COI_'+stname+'.csv'):
        analysis_csv=pd.read_csv('/Sites/option_chain/lists/Analysis_COI_'+stname+'.csv')
        print(">>>##",stname)
        analysis_csv=analysis_csv[srcol]
        NewCsvData=analysis_csv.append(df,ignore_index=True)
        df=NewCsvData[srcol]
        if analysis_csv.at[analysis_csv.shape[0]-1,"Name"].lower()!=df.at[df.shape[0]-1,'Name'].lower():
            print(">>>",stname)
            NewCsvData.to_csv('/Sites/option_chain/lists/Analysis_COI_'+stname+'.csv')
    else:
        analysis_csv=pd.DataFrame(columns=srcol)
        NewCsvData=analysis_csv.append(df,ignore_index=True)
        NewCsvData=NewCsvData[srcol]
        NewCsvData.to_csv('/Sites/option_chain/lists/Analysis_COI_'+stname+'.csv')

for stname in stklist:
    stname=stname.strip('\n')
    stname=stname.lower()
    msg=""
    filename=''
    listofnames=open('/Sites/option_chain/lists/'+stname+'.txt')
    for name in listofnames:
        create_analysis(stname,name)
