import os


def save_df(df, file_name, destination):
    if os.path.exists(destination):
        file_path = f'{destination}/{file_name}.csv'
        df.to_csv(file_path, index=False)
    else:
        print("Failed to save csv.")