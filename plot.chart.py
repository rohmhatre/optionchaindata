from matplotlib import pylab
l=[]
m=[]
n=[]
for i in range(14):
    l.append(call_otm.iat[i,1])
for i in call_otm.index:
    if i == 11250.0:
        break
    m.append(i)
for i in range(14):
    n.append(put_itm.iat[i,8]) 
import numpy as np
import matplotlib.pyplot as plt
def call_otm_plot():
    index = np.arange(14)
    #plt.bar(index, l)
    plt.bar(index, l, color = 'g', width = 0.25,label="CALL")
    plt.bar(index + 0.25, n, color = 'r', width = 0.25,label="PUT")
    plt.xlabel('Index', fontsize=10)
    plt.ylabel('Change in OI', fontsize=10)
    plt.xticks(index, m, fontsize=8, rotation=30)
    plt.title('CALL OUT OF THE MONEY CHART')
    plt.show()
call_otm_plot()

a=[]
b=[]
c=[]
for i in range(20,40):
    a.append(call_itm.iat[i,1])
for i in put_otm.index[20:40]:
    b.append(i)
for i in range(20,40):
    c.append(put_otm.iat[i,8]) 

def put_otm_plot():
    index = np.arange(20)
    #plt.bar(index, l)
    plt.bar(index, a, color = 'g', width = 0.25,label="CALL")
    plt.bar(index + 0.25, c, color = 'r', width = 0.25,label="PUT")
    plt.xlabel('Index', fontsize=10)
    plt.ylabel('Change in OI', fontsize=10)
    plt.xticks(index, b, fontsize=8, rotation=30)
    plt.title('PUT OUT OF THE MONEY CHART')
    plt.show()
put_otm_plot()
