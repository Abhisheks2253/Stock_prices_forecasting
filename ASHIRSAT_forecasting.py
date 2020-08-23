#HW 8 - Forecasting -- ashirsat


import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import quandl
import numpy as np


# Q1 - Import data using tickerSymbol, startDate, endDate

def importQuotes(ticker, date1, date2):
    quandl.ApiConfig.api_key = "rrimPiVuct_rMkHAGXC-"
    dataSource = "WIKI/%s" % (ticker).lower().title()
    quotes1 = quandl.get(dataSource, start_date=date1, end_date=date2, returns="numpy")
    closing_prices = quotes1['Close']
    return closing_prices
    
# importQuotes(tickerSymbol, startDate, endDate)
# cp = importQuotes(tickerSymbol, startDate, endDate)

# tau = 3

# Q2 - Moving average method 
# NOTE: The tau here wont affect the result - We are getting value for next time period

def forecastMA(n,cp,tau):
    ft_array = cp[-n:]
    ft = np.sum(ft_array)/n
    return ft



# Q3 - Forecast using Linear Regression

def forecastLR(tau, cp):
#     di = importQuotes('tsLA','2017-09-01','2017-10-30')
    i_mat = np.arange(1,(len(cp)+1))
    idi = np.multiply(cp,i_mat)
    sum_idi = np.sum(idi)
    sum_di = np.sum(cp)
    Sxy = (len(cp)*sum_idi) - ((len(cp)*(len(cp)+1)*sum_di))/2
    Sxx_1 = ((len(cp)*len(cp))*(len(cp)+1)*((2*len(cp))+1))/6
    Sxx_2 = ((len(cp)*len(cp))*((len(cp)+1)*(len(cp)+1)))/4
    Sxx = Sxx_1 - Sxx_2
    D_avg = sum_di/len(cp)
    slope = round((Sxy/Sxx),2)    #SLOPE 'b'
    intercept = (D_avg) - (slope*(len(cp)+1))/2   #INTERCEPT 'a'
#     tau = len(cp) + a
    T = len(cp) + tau
    LR_forecast = round((intercept + (slope*T)),2)
    mylist = [LR_forecast, slope, intercept]
    return mylist

# forecastLR(tau, closing_prices)

# Q3 - Forecast using Holt's method

def forecastHolt(tau, alpha, beta, closing_prices):
#     di = importQuotes('tsLA','2017-09-01','2017-10-30')
    i_mat = np.arange(1,(len(closing_prices)+1))
    idi = np.multiply(closing_prices,i_mat)
    sum_idi = np.sum(idi)
    sum_di = np.sum(closing_prices)
    Sxy = (len(closing_prices)*sum_idi) - ((len(closing_prices)*(len(closing_prices)+1)*sum_di))/2
    Sxx_1 = ((len(closing_prices)*len(closing_prices))*(len(closing_prices)+1)*((2*len(closing_prices))+1))/6
    Sxx_2 = ((len(closing_prices)*len(closing_prices))*((len(closing_prices)+1)*(len(closing_prices)+1)))/4
    Sxx = Sxx_1 - Sxx_2
    D_avg = sum_di/len(closing_prices)
    slope = Sxy/Sxx    #SLOPE 'b'
    intercept = (D_avg) - (slope*(len(closing_prices)+1))/2   #INTERCEPT 'a'
#     tau = len(closing_prices) + a
    Dt = intercept + (slope*tau)
    
#St = αDt +(1−α)(St−1 +Gt−1) 
#Gt = β(St − St−1) + (1 − β)Gt−1,
    G = slope
    S = intercept
    for i in range(0,len(closing_prices)):
        S0 = S
        S = alpha*(closing_prices[i]) + ((1-alpha)*(S + G))
        G = beta*(S - S0) + (1-beta)*G
        Ft = round((S + (tau*G)),2)
    return Ft
        


