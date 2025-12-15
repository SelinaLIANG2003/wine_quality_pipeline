import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data shape:", df.shape)
    return df

if __name__ == "__main__":
    print("load_data module ready")
