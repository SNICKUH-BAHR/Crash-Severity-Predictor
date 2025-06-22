import pandas as pd


def filter_data(file_path, include_cols=None, exclude_vals=None, substitute=None):
    df = pd.read_csv(file_path)
    if include_cols is not None:
        df.drop(columns=[col for col in df.columns if col not in include_cols], inplace=True)


    if exclude_vals is not None:
        for col, vals in exclude_vals.items():
            idxs = df[df[col].isin(vals)].index
            df.drop(idxs, inplace=True)

    df.dropna(inplace=True)
    if substitute is not None:
        for sub_col, vals in substitute.items():
            df[sub_col] = df[sub_col].map(vals)
            df.dropna(subset=[sub_col], inplace=True)
            df[sub_col] = df[sub_col].astype(int)
    return df
