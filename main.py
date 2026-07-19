if __name__ != "__main__":
    print("main.py may not be called as a module")
    import sys
    sys.exit(1)

# global variables
tickers = ["MSFT","AMZN","HD","DIS","AAPL"
          ,"XOM","SLB","JNJ","GE","BA","BRK-B"
          ,"V","KO","^IXIC","^GSPC"
          ]

# data collection
from modules.data_gatherer import gather_today_csv
from modules.csv_combiner import combine_csv

# data postprocessing


# Interface
print("Welcome to the data gathering tool")
print("Note that this should only be used in")
print("the directory in which the file resides")
print("                                  -Marcus")
while True:
    print("\n   1 - gather data from last 8 days\n   2 - combine csvs\n   3 - custom data gathering\n   0 - exit\n")
    user_input = input()
    if user_input == "0":
        import sys
        sys.exit()
    elif user_input == "1":
        gather_today_csv(tickers)
    elif user_input == "2":
        combine_csv()
    elif user_input == "3":
        print("Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max")
        aPeriod = input("Period: ")
        print("Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo\nIntraday data cannot extend last 60 days")
        aInterval = input("Interval: ")
        gather_today_csv(tickers,aPeriod,aInterval)
