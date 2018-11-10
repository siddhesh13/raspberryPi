# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.ticker as mticker
from matplotlib import style
import numpy as np
import csv
import matplotlib.dates as mdates
import urllib

#style
style.use('fivethirtyeight')
print(plt.style.available)
print(plt.__file__)

#basic demo sketch
'''
x=np.linspace(0,2,100)
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubuc')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Basic plot')
plt.legend()
plt.show()
'''
#sin wave
'''
x=np.arange(0,10,0.2)
y=np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()
'''

#legends titles and lables
'''
x=[1,2,3,4]
y=[9,8,7,6]
x2=[1,2,3,4]
y2=[10,14,23,11]
plt.plot(x,y, label='first line')
plt.plot(x2,y2, label='second line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Basic Graph')
plt.legend()
plt.show()
'''

#bar charts and histograms
'''
x=[2,4,6,8,10]
y=[1,3,5,7,9]
x2=[3,5,7,9]
y2=[99,88,77,66]
population_ages = [12,42,13,65,34,23,76,44,66,44,25,87,3,21,65,32,45,21,74,82,75,21,53,65,43,81,95,27,71]
bins = [0,10,20,30,40,50,60,70,80,90]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.5)
plt.bar(x,y,label='bar 2',color='r')
plt.bar(x2,y2,label='bar 1',color='g')
plt.xlabel('x line')
plt.ylabel('y label')
plt.title('bar chart and histograms')
plt.legend()
plt.show()
'''

#scatter plots
'''
x=[1,2,3,4,5,6,7,8]
y=[3,4,3,2,8,4,2,7]
plt.scatter(x,y,label='skitscat',color='k',marker='*',s=50)
plt.xlabel('x line')
plt.ylabel('y label')
plt.title('scatter plots')
plt.legend()
plt.show()
'''

#stack plots
'''
days=[1,2,3,4,5,6,7]
sleeping=[7,6,8,9,5,7,8]
eating=[2,4,3,1,2,4,3]
working=[9,7,6,8,9,10,8]
playing=[4,5,3,6,2,1,4]
plt.plot([],[],color='b',label='Sleeping',linewidth=5)
plt.plot([],[],color='r',label='Eating',linewidth=5)
plt.plot([],[],color='k',label='Working',linewidth=5)
plt.plot([],[],color='g',label='Playing',linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing, colors=['b','r','k','g']) 
plt.xlabel('x line')
plt.ylabel('y label')
plt.title('stack plots')
plt.legend()
plt.show()
'''

#pie charts
'''
days=[1,2,3,4,5,6,7]
sleeping=[7,6,8,9,5,7,8]
eating=[2,4,3,1,2,4,3]
working=[9,7,6,8,9,10,8]
playing=[4,5,3,6,2,1,4]
slices=[7,2,2,5]
cols=['b','r','c','g']
activities=['sleeping','eating','working','playing']
plt.pie(slices,labels=activities,
        colors=cols,startangle=90,
        shadow=True,explode=(0,0,0.1,0),
        autopct='%1.1f%%')
plt.title('Pie chart')
plt.show()
'''

#loading data from files
'''
x=[]
y=[]
with open('example','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='loaded from file')          


x,y =np.loadtxt('example',delimiter=',',unpack=True)
plt.plot(x,y,label='loaded from file')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('loading dat from files')
plt.legend()
plt.show()
'''

#moving average function
MA1= 10
MA2 = 30
def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas
def high_minus_low(highs, lows):
    return highs-lows



#getting data from internet, customization.
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter(s)
    return bytesconverter
def graph_data():

    fig = plt.figure()
    #ax1 = plt.subplot2grid((1,1),(0,0))
    ax1=plt.subplot2grid((6,1),(0,0), rowspan=2, colspan=1)
    ax2=plt.subplot2grid((6,1),(2,0), rowspan=2, colspan=1)
    ax3=plt.subplot2grid((6,1),(4,0), rowspan=2, colspan=1)
    
    
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})


    
    #customization
    '''
    ax1.plot_date(date,closep,'-',label='Price')
    ax1.plot([],[],linewidth=5,color='g',label='Gain')

    ax1.plot([],[],linewidth=5,color='r',label='Loss')
    ax1.axhline(closep[0],color='k',linewidth=5)
    ax1.fill_between(date,closep,closep[0],where=closep > closep[0],facecolor='g',alpha=0.3)
    ax1.fill_between(date,closep,closep[0],where=closep < closep[0],facecolor='r',alpha=0.3)
    ax1.grid(True,color='g')
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([200,400,600,800])
    ax1.spines['left'].set_color('c')
    ax1.spines['left'].set_linewidth(5)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.tick_params(axis='x',colors='#f06215')
    '''
    #candlestick OHLC graph
    '''
    x=0
    y=len(date)
    ohlc=[]
    while x<y:
        append_me=date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
        ohlc.append(append_me)
        x+=1
    candlestick_ohlc(ax1,ohlc)
    '''
    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2 -1:])
    h_1 = list(map(high_minus_low, highp, lowp))
    ax2.plot_date(date, h_1, '-')
    #annotation
    '''
    #anotation example with arrow
    ax1.annotate('bad news',(date[11],closep[11]),
                 xytext=(0.8,0.9), textcoords='axes fraction',
                 arrowprops = dict(facecolor='grey',color='grey'))
    #font dict example
    font_dict = {'family':'serif',
                 'color':'darkred',
                 'size':15}
    #hard coded text
    ax1.text(date[10], closep[1], 'Text Example', fontdict=font_dict)
    '''
    bbox_props= dict(boxstyle='larrow',fc='w',ec='k',lw=1)
    ax1.annotate(str(closep[-1]),(date[-1],closep[-1]),
                 xytext = (date[-1]+4,closep[-1]), bbox=bbox_props)
    ax1.plot(date,closep)
    #print(len(date),len(ma1))
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    ax3.plot(date[-start:], ma1[-start:],linewidth=1)
    ax3.plot(date[-start:], ma2[-start:],linewidth=1)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r', edgecolor='g', alpha=0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='r', edgecolor='g', alpha=0.5)
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.xlabel('dates')
    plt.ylabel('price')
    #plt.title('loading data from files')
    #plt.legend()
    plt.show()   

graph_data()
