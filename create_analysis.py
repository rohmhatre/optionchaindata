import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import datetime
from scipy.stats import norm
import math


def IVCALCULATOR(CurPrice,S,R,PutIV,CallIV):
    prob=[]
    Days= datetime.date(2019, 4, 4) - datetime.date.today()
    NoDays=Days.days+1


    CallNormDist=math.log(R/CurPrice)/(CallIV*math.sqrt(NoDays/365))
    PutNormDist=math.log(S/CurPrice)/(PutIV*math.sqrt(NoDays/365))
    
    prob.append(round(norm.cdf(CallNormDist*100)*100,2))
    prob.append(round((1-norm.cdf(PutNormDist*100))*100,2))
    return prob

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

def create_analysis(csvdata):
    OptionAnalysis=dict()
    OptionAnalysis["curprice"]=csvdata.CurrentVal[0]
    datelist=[]
    datedata=0
    cur_val=[]
    csvdata=csvdata.replace("-",0).convert_objects(convert_numeric=True,)
    csvdata=csvdata.set_index("StrikePrice")
   
    call_list=['CallOI', 'CallChnginOI','CallLTP','CallNetChng','CallIV','CallBidPrice','CallAskPrice']
    put_list=['PutOI', 'PutChnginOI','PutLTP','PutNetChng','PutIV','PutBidPrice','PutAskPrice']
    call_val=csvdata[call_list].convert_objects(convert_numeric=True,)
    put_val=csvdata[put_list].convert_objects(convert_numeric=True,)

    itm_val=0
    datedata+=1  
    for i in list(call_val.index):
        i=float(i)
        if i < csvdata.CurrentVal.iat[0]:
            itm_val=i
        else:
            otm_val=i
            break

    itm_call=call_val[call_val.index[0]:itm_val].sort_values('CallOI',ascending=False)
    otm_call=call_val[otm_val:call_val.index[-1]].sort_values('CallOI',ascending=False)
    itm_put=put_val[otm_val:call_val.index[-1]].sort_values('PutOI',ascending=False)
    otm_put=put_val[call_val.index[0]:itm_val].sort_values('PutOI',ascending=False)
    OptionAnalysis["support"]=list(otm_put.index)[:4]
    OptionAnalysis["resistance"]=list(otm_call.index)[:4]    
    OptionAnalysis["callprob"]=[]
    OptionAnalysis["putprob"]=[]
    OptionAnalysis["CallChngInLTP"]=[]
    OptionAnalysis["PutChngInLTP"]=[]
    OptionAnalysis["CoiMaxAdd"]=[]
    OptionAnalysis["CoiMaxExit"]=[]
    OptionAnalysis["pcr"]=0
    
   
    
    
    for i in range(4):
    ###IV Calculation
        s=OptionAnalysis['support'][i]
        r=OptionAnalysis['resistance'][i]
        #print(OptionAnalysis['curprice'],s,r,otm_call.CallIV[r],otm_put.PutIV[s])
        prob=IVCALCULATOR(OptionAnalysis['curprice'],s,r,otm_put.PutIV[s],otm_call.CallIV[r])
        OptionAnalysis["callprob"].append(prob[0])
        OptionAnalysis["putprob"].append(prob[1])

    ###PREMIUM DECAY
        #print(otm_put)
        callltp=otm_call.CallLTP[r]
        callchngltp=otm_call.CallNetChng[r]
        putltp=otm_put.PutLTP[s]
        putchngltp=otm_put.PutNetChng[s]
        OptionAnalysis["CallChngInLTP"].append(round(callchngltp*100/callltp,2))
        OptionAnalysis["PutChngInLTP"].append(round(putchngltp*100/putltp,2)) 
        
    ###Max COI
    for j in list(call_val.sort_values('CallChnginOI',ascending=False).index)[:2]:
        OptionAnalysis["CoiMaxAdd"].append(j)
    for j in list(put_val.sort_values('PutChnginOI',ascending=False).index)[:2]:
        OptionAnalysis["CoiMaxAdd"].append(j)
    for j in list(call_val.sort_values('CallChnginOI').index)[:2]:
        OptionAnalysis["CoiMaxExit"].append(j)
    for j in list(put_val.sort_values('PutChnginOI').index)[:2]:
        OptionAnalysis["CoiMaxExit"].append(j)
        
    ###PCR Ratio
    OptionAnalysis["pcr"]=csvdata['PutOI'].sum()/csvdata['CallOI'].sum()
    
    return OptionAnalysis



analysiscol=['name','curprice','pcr','resistance','support','CallChngInLTP','PutChngInLTP','CoiMaxAdd','CoiMaxExit','callprob','putprob']
stlist=open('/Sites/option_chain/lists/stlist.txt')
for stname in stlist:
    stname=stname.strip('\n')
    print(">>>",stname)
    csvd=pd.DataFrame(columns=analysiscol)    
    filenmlist=open('/Sites/option_chain/lists/'+stname.lower()+'.txt')
    filenm=filenmlist.readlines()[-1].strip('\n')
    optionchain=pd.read_csv('/Sites/option_chain/'+stname+'/'+filenm)
    srvalues=create_analysis(optionchain)
    for key in srvalues:
        strval=''
        if key in ['resistance','support','CallChngInLTP','PutChngInLTP','CoiMaxAdd','CoiMaxExit','callprob','putprob']:
            for j in range(len(srvalues[key])):
                strval=strval+str(srvalues[key][j])+','
            srvalues[key]=strval
    srvalues['name']=filenm
    if os.path.isfile('/Sites/option_chain/lists/Analysis_'+stname+'.csv'):
        analysis_csv=pd.read_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
        print("file found",stname)
        analysis_csv=analysis_csv[analysiscol]
        NewCsvData=analysis_csv.append(srvalues,ignore_index=True)
        df=NewCsvData[analysiscol]
        if analysis_csv.at[analysis_csv.shape[0]-1,"name"].lower()!=df.at[df.shape[0]-1,'name'].lower():
            print("New data wrriten",stname)
            NewCsvData.to_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
    else:
        analysis_csv=pd.DataFrame(columns=analysiscol)
        NewCsvData=analysis_csv.append(srvalues,ignore_index=True)
        NewCsvData=NewCsvData[analysiscol]
        NewCsvData.to_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
        print("new file created")


