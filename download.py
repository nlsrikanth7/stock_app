import yfinance

df = yfinance.download('AMZN', start='2022-01-01', end='2022-12-30')
df.to_csv('AMZN.csv')

