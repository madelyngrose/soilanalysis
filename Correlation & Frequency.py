import pandas as pd
def calc_corr(data_file):
    df = pd.read_csv(data_file, index_col = 0)
    corr_matrix = df.corr()
    return corr_matrix

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    data_file = '/Users/madelynrose/Desktop/FreqUPDATED.csv'
    try:
        corr_matrix = calc_corr(data_file)
        print ("Correlation Matrix:")
        print(corr_matrix)
    except FileNotFoundError:
        print ("Error: File not Found")
    except Exception as e:
        print("Error e")