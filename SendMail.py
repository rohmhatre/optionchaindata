import pandas as pd
import datetime, smtplib
stklist=["nifty", "hdfc", "m&m" ,"escorts", "l&tfh","biocon","banknifty","grasim","kotakbank","techm","tcs","reliance"]

def mail_to(msg,toaddress):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rohmh.iitb@gmail.com", "sun@MOM2310")
    server.sendmail("rohmh.iitb@gmail.com",toaddress, msg)
    server.quit()

msg=""



for stname in stklist:
    
    df=pd.read_csv("/Sites/option_chain/lists/Analysis_"+stname+".csv") 

    if df.at[df.shape[0]-1,'S1'] != df.at[df.shape[0]-2,'S1'] or df.at[df.shape[0]-1,'R1'] != df.at[df.shape[0]-2,'R1']:
        if df.at[df.shape[0]-1,'S1'] != df.at[df.shape[0]-2,'S1'] and df.at[df.shape[0]-1,'R1'] != df.at[df.shape[0]-2,'R1']:
            if df.at[df.shape[0]-1,'S1'] > df.at[df.shape[0]-2,'S1'] and df.at[df.shape[0]-1,'R1'] > df.at[df.shape[0]-2,'R1']:
                print("Buy",stname," support1 and resistance1 moving up")
                msg+="Buy "+stname+" support1 and resistance1 moving up\n\n"
            elif df.at[df.shape[0]-1,'S1'] < df.at[df.shape[0]-2,'S1'] and df.at[df.shape[0]-1,'R1'] < df.at[df.shape[0]-2,'R1']:
                print("Sell",stname," support1 and resistance1 moving down")
                msg+="Sell "+stname+" support1 and resistance1 moving down\n\n"
            else:
                print(stname+" support1 and resistance1 moving But check graph for signal")
                msg+=stname+" support1 and resistance1 moving But check graph for signal\n\n"
        elif df.at[df.shape[0]-1,'S1'] != df.at[df.shape[0]-2,'S1']:
            if df.at[df.shape[0]-1,'S1'] > df.at[df.shape[0]-2,'S1']:
                print("Buy", stname,"support1 moved up")
                msg+="Buy "+stname+" support1 moved up\n\n"
            else:
                print("Sell", stname,"support1 moved down")
                msg+="Sell "+ stname+" support1 moved down\n\n"
        else:
            if df.at[df.shape[0]-1,'R1'] > df.at[df.shape[0]-2,'R1']:
                print("Buy", stname," resistance1 moved up")
                msg+="Buy "+ stname+" resistance1 moved up\n\n"
            else:
                print("Sell", stname,"resistance1 moved down")
                msg+="Sell "+ stname+"resistance1 moved down\n\n"


    elif df.at[df.shape[0]-1,'S2'] != df.at[df.shape[0]-2,'S2'] or df.at[df.shape[0]-1,'R2'] != df.at[df.shape[0]-2,'R2']:
        if df.at[df.shape[0]-1,'S2'] > df.at[df.shape[0]-2,'S2'] and df.at[df.shape[0]-1,'R2'] > df.at[df.shape[0]-2,'R2']:
                print("Buy",stname," support2 and resistance2 moving up")
                msg+="Buy "+stname+" support2 and resistance2 moving up\n\n"
        elif df.at[df.shape[0]-1,'S2'] < df.at[df.shape[0]-2,'S2'] and df.at[df.shape[0]-1,'R2'] < df.at[df.shape[0]-2,'R2']:
                print("Sell",stname," support2 and resistance2 moving down")
                msg+="Sell "+stname+" support2 and resistance2 moving down\n\n"
        elif df.at[df.shape[0]-1,'S2'] != df.at[df.shape[0]-2,'S2']:
            if df.at[df.shape[0]-1,'S2'] > df.at[df.shape[0]-2,'S2']:
                print("Buy", stname,"support2 moved up")
                msg+="Buy "+ stname+" support2 moved up\n\n"
            else:
                print("Sell", stname,"support2 moved down")
                msg+="Sell "+ stname+" support2 moved down\n\n"
        else:
            if df.at[df.shape[0]-1,'R2'] > df.at[df.shape[0]-2,'R2']:
                print("Buy", stname,"resistance2 moved up")
                msg+="Buy "+ stname+" resistance2 moved up\n\n"
            else:
                print("Sell", stname,"resistance2 moved down")
                msg+="Sell "+ stname+" resistance2 moved down\n\n"



    elif df.at[df.shape[0]-1,'S3'] != df.at[df.shape[0]-2,'S3'] or df.at[df.shape[0]-1,'R3'] != df.at[df.shape[0]-2,'R3']:
        if df.at[df.shape[0]-1,'S3'] > df.at[df.shape[0]-2,'S3'] and df.at[df.shape[0]-1,'R3'] > df.at[df.shape[0]-2,'R3']:
                print("Buy",stname," support3 and resistance3 moving up")
                msg+="Buy "+stname+" support3 and resistance3 moving up\n\n"
        elif df.at[df.shape[0]-1,'S3'] < df.at[df.shape[0]-2,'S3'] and df.at[df.shape[0]-1,'R3'] < df.at[df.shape[0]-2,'R3']:
                print("Sell",stname," support3 and resistance3 moving down")
                msg+="Sell "+stname+" support3 and resistance3 moving down\n\n"
        elif df.at[df.shape[0]-1,'S3'] != df.at[df.shape[0]-2,'S3']:
            if df.at[df.shape[0]-1,'S3'] > df.at[df.shape[0]-2,'S3']:
                print("Buy", stname,"support3 moved up")
                msg+="Buy "+ stname+" support3 moved up\n\n"

            else:
                print("Sell", stname,"support3 moved down")
                msg+="Sell "+stname+" support3 moved down\n\n"
        else:
            if df.at[df.shape[0]-1,'R3'] > df.at[df.shape[0]-2,'R3']:
                print("Buy", stname,"resistance3 moved up")
                msg+="Buy "+ stname+" resistance3 moved up\n\n"
            else:
                print("Sell", stname,"resistance3 moved down")
                msg+="Sell "+ stname+" resistance3 moved down\n\n"


    elif df.at[df.shape[0]-1,'S4'] != df.at[df.shape[0]-2,'S4'] or df.at[df.shape[0]-1,'R4'] != df.at[df.shape[0]-2,'R4']:
        if df.at[df.shape[0]-1,'S1'] > df.at[df.shape[0]-2,'S1'] and df.at[df.shape[0]-1,'R1'] > df.at[df.shape[0]-2,'R1']:
                print("Buy",stname,"support1 and resistance1 moving up")
                msg+="Buy "+ stname+" support1 and resistance1 moving up\n\n"
        elif df.at[df.shape[0]-1,'S1'] < df.at[df.shape[0]-2,'S1'] and df.at[df.shape[0]-1,'R1'] < df.at[df.shape[0]-2,'R1']:
                print("Sell",stname,"support1 and resistance1 moving down")
                msg+="Sell "+stname+" support1 and resistance1 moving down\n\n"
        elif df.at[df.shape[0]-1,'S4'] != df.at[df.shape[0]-2,'S4']:
            if df.at[df.shape[0]-1,'S4'] > df.at[df.shape[0]-2,'S4']:
                print("Buy", stname,"support4 moved up")
                msg+="Buy "+ stname+" support4 moved up\n\n"
            else:
                print("Sell", stname,"support4 moved down")
                msg+="Sell "+ stname+" support4 moved down\n\n"
        else:
            if df.at[df.shape[0]-1,'R4'] > df.at[df.shape[0]-2,'R4']:
                print("Buy", stname,"resistance4 moved up")
                msg+="Buy "+ stname+" resistance4 moved up\n\n"
            else:
                print("Sell", stname,"resistance4 moved down")
                msg+="Sell ", stname," resistance4 moved down\n\n" 
if msg!="":
    mail_to(msg,"rohanmhatre16390@gmail.com")

