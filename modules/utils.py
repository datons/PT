import yfinance as yf

def calculate_yearly_returns(
    stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'META', 'TSLA'],
    start='2010-01-01', end='2020-12-31'
):
    
    df_base = yf.download(stocks, start, end)
    df = df_base['Adj Close']

    df = (df
        .loc['2010':]
        .groupby(df.index.year).pct_change().add(1)
        .groupby(df.index.year).cumprod().sub(1)
        .resample('1Y').last()
        .mul(100)
    )
    
    return df