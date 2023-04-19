import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def main():
    stock()


def stock():
    # stocks: 'AAPL', 'WMT', 'IBM', 'MU', 'BA', 'FB' , 'AMZN' , 'NFLX',
    tickers_list = ['NFLX', 'IBM']
    # Fetch the data
    data = yf.download(tickers_list, start='2022-9-12',
                       end='2023-3-12')['Adj Close']
    # print(data)
    # Print first 5 rows of the data
    print(data.head(2))
    #returns = data.pct_change()
    returns = np.log(data).diff()

    returns.tail()

    # Generate Var-Cov matrix
    cov_matrix = returns.cov()
    cov_matrix

    # Calculate mean returns for each stock
    avg_rets = returns.mean()
    avg_rets

    # Plot returns
    returns.plot()
    plt.show()

    return


if __name__ == "__main__":
    main()
