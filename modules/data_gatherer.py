if __name__ == "__main__":
    import sys
    print("This is a module for main.py \nit should not be called by itself\nUsage\n   - python3 main.py")
    sys.exit(1)

import yfinance as yf
from datetime import datetime
import os
def gather_today_csv(aTickers,aPeriod="8d",aInterval="1m"):
    if not os.path.isdir("data"):
        if os.path.isfile("data"):
            print("expected path ./data/ is a file, unable to proceed")
            import sys
            sys.exit(1)
        print("creating directory ./data/")
        os.mkdir("data")

    for ticker in aTickers:
        print(f"{ticker} starting download")
        data = yf.download(  tickers=ticker
                             , period=aPeriod
                             , interval=aInterval
                           )
        data.to_csv(f"data/{ticker}_{datetime.today().strftime('%Y-%m-%d_%H:%M:%S')}.csv")
        print(f"{ticker} finished download")
