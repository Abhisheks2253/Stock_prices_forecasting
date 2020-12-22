## Stock_prices_forecasting

#### The importQuotes function accepts 3 string inputs - (1) Stock Ticker Symbol, (2) Start date and (3) End Date to return the Stock's closing prices between given date range as numpy object; used quandl.get function from Quandl

#### The forecastMA function accepts 3 inputs - (1) Desired number of periods to use for moving average method (int), (2) numpy object- o/p from importQuotes function and (3) number of periods into future for which forecast should be provided (int) to return the moving average forecast

#### forecastLR function accepts 2 inputs - (1) Number of periods for which forecast should be provided and (2) numpy object- o/p from importQuotes function to return a list with - 1. The forecasted closing price of the stock, 2. The slope of the linear regression line 3. The y-intercept of the linear regression line

#### forecastHolt function accepts 4 inputs - (1) Number of periods for which forecast should be provided (2) alpha parameter (3) beta parameter (4) numpy object- o/p from importQuotes function to return Holts's forecast 
