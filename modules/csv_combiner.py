if __name__ == "__main__":
    import sys
    print("This is a module for main.py \nit should not be called by itself\nUsage\n   - python3 main.py")
    sys.exit(1)
import os, collections
import pandas as pd

# all this could definitly be done more effectively, but i'd rather get to working with the option strategies
# i will update this as nesecarry (if i notice very slow runtimes). This should only be ran once a week or so
# so i don't mind runtimes of a few minutes if it gets to that
def combine_csv():
    data_files = collections.defaultdict(list)
    for file in sorted(os.listdir("data")):
        if os.path.isfile(os.path.join("data", file)) == False:
            print("warning: dirty data folder - non-file found in data folder")
            continue
        if file[-4:] != ".csv":
            print("warning: dirty data folder - non-csv file found in data folder")
            continue

        data_files[file[:-24]].append(file)

    if not os.path.isdir("combined_csvs"):
        if os.path.isfile("combined_csvs"):
            print("expected path ./combined_csvs/ is a file, unable to proceed")
            import sys
            sys.exit(1)
        print("creating directory ./combined_csvs/")
        os.mkdir("combined_csvs")

    if not os.path.isdir(".backup_data"):
        if os.path.isfile(".backup_data"):
            print("expected path ./.backup_data/ is a file, unable to proceed")
            import sys
            sys.exit(1)
        print("creating directory ./.backup_data/")
        os.mkdir(".backup_data")

    for ticker in data_files.keys():
        print(f"Combining {ticker} data")
        temp_data = [pd.read_csv(f'data/{csv_file}',header=[0, 1], index_col=0, parse_dates=True) for csv_file in data_files[ticker]] # takes up a lot of memory, do better if noticable
        if os.path.isfile(f"combined_csvs/{ticker}.csv"):
            temp_data.append(pd.read_csv(f"combined_csvs/{ticker}.csv",header=[0, 1], index_col=0, parse_dates=True))
        combined = pd.concat(temp_data)
        combined = combined[~combined.index.duplicated(keep='first')].sort_index()
        combined.to_csv(f"combined_csvs/{ticker}.csv")
        [os.rename(f"data/{csv_file}", f".backup_data/{csv_file}") for csv_file in data_files[ticker]] # move files into backup folder after use
