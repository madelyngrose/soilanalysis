import pandas as pd

def calc_zscores(row):
    return(row-row.mean())/row.std()

def main():
    input_file = 'FILE_NAME' #Use pertinent file (as CSV)
    df = pd.read_csv(input_file, index_col=0)
    z_scores_df = df.apply(calc_zscores, axis = 1)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    return z_scores_df

if __name__ == "__main__":
    z_scores_df = main()
    print("Z Scores:")
    print(z_scores_df)