import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data shape:", df.shape)
    print(df.head())   
    return df

if __name__ == "__main__":
    df = load_data("../data/winequality-red.csv")
