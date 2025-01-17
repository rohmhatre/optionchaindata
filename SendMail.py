import pandas as pd
import datetime, smtplib
import math
from scipy.stats import norm

def mail_to(msg,toaddress):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rohmh.iitb@gmail.com", "sun@MOM2310")
    server.sendmail("rohmh.iitb@gmail.com",toaddress, msg)
    server.quit()

msg=""

def IVCALCULATOR(stname,R,S):
    msg=""
    Days= datetime.date(2019, 2, 28) - datetime.date.today()
    stlist=open('/Sites/option_chain/lists/'+stname+'.txt')
    analisisnifty=pd.read_csv('/Sites/option_chain/lists/Analysis_'+stname+'.csv')
    csvdata=pd.read_csv('/Sites/option_chain/'+stname.upper()+'/'+stlist.readlines()[-1].strip('\n'),index_col='StrikePrice')
    csvdata=csvdata.replace('-',0)
    CurrentPrice=csvdata.CurrentVal.iloc[0]
    CallIV=float(csvdata.CallIV.loc[R])
    PutIV=float(csvdata.PutIV.loc[S])
    NoDays=Days.days
    if CallIV!=0:
        CallNormDist=math.log(R/CurrentPrice)/(CallIV*math.sqrt(NoDays/365))
        msg+='Probability to hit '+ str(R)+' :  '+str(norm.cdf(CallNormDist*100)*100)+'\n'
    if PutIV!=0:
        PutNormDist=math.log(S/CurrentPrice)/(PutIV*math.sqrt(NoDays/365))
        msg+='Probability to hit '+str(S)+' :  '+str((1-norm.cdf(PutNormDist*100))*100)+'\n'
    msg+='-------------------------------------------------------------------------\n'
    return msg

def findSR(level,oldS,newS,oldR,newR):
    msg=""
    if newS != oldS and oldR != newR:
        if newS > oldS and newR > oldR:
            msg+="Buy...support"+level+" Moved up from "+str(oldS)+" to "+str(newS)+" and Resistance"+level+" Moved from Up "+str(oldR)+" to "+str(newR)+"\n"
        elif newS < oldS and newR < oldR:
            msg+="Sell...support"+level+" Moved Down from "+str(oldS)+ " to "+str(newS)+" and Resistance"+level+" Moved from Down "+str(oldR)+" to "+str(newR)+"\n"
        else:
            msg+=stname +" Support "+level+" Moved from "+str(oldS)+ " to "+str(newS)+" and Resistance"+level+" Moved from "+str(oldR)+" to "+str(newR)+"\n"

    elif newS != oldS:
        if newS > oldS:
            msg+="Buy...Support "+level+" Moved Up from "+str(oldS)+ " to "+str(newS)+"\n"
        else:
            msg+="Sell...Support "+level+" Moved Down from "+str(oldS)+ " to "+str(newS)+"\n"

    elif newR != oldR:
        if newR > oldR:
            msg+="Buy...Resistance "+level+" Moved from Up "+str(oldR)+" to "+str(newR)+"\n"
        else:
            msg+="Sell...Resistance "+level+" Moved from Down "+str(oldR)+" to "+str(newR)+"\n"

    else:
        pass
    return msg

stklist=open('/Sites/option_chain/lists/stlist.txt')

for stname in stklist:
    stname=stname.strip("\n")
    stname=stname.lower()
    msg+=stname.upper()+'\n'
    df=pd.read_csv("/Sites/option_chain/lists/Analysis_"+stname+".csv")
    if df.shape[0]>1:
        print(stname)
        msg+=findSR("1",df.at[df.shape[0]-2,'S1'],df.at[df.shape[0]-1,'S1'],df.at[df.shape[0]-2,'R1'],df.at[df.shape[0]-1,'R1'])
        msg+=IVCALCULATOR(stname,df.at[df.shape[0]-1,'R1'],df.at[df.shape[0]-1,'S1'])
        msg+=findSR("2",df.at[df.shape[0]-2,'S2'],df.at[df.shape[0]-1,'S2'],df.at[df.shape[0]-2,'R2'],df.at[df.shape[0]-1,'R2'])
        msg+=IVCALCULATOR(stname,df.at[df.shape[0]-1,'R2'],df.at[df.shape[0]-1,'S2'])
        msg+=findSR("3",df.at[df.shape[0]-2,'S3'],df.at[df.shape[0]-1,'S3'],df.at[df.shape[0]-2,'R3'],df.at[df.shape[0]-1,'R3'])
        msg+=findSR("4",df.at[df.shape[0]-2,'S4'],df.at[df.shape[0]-1,'S4'],df.at[df.shape[0]-2,'R4'],df.at[df.shape[0]-1,'R4'])
        msg+='#########################################################################################\n'

if msg!="":
    mail_to(msg,"rohanmhatre16390@gmail.com")
