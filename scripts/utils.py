
import pandas as pd

def check_nulls(df, name):
    """Return null count for each column."""
    print(f"\n{name} — null count")
    return df.isna().sum()

def check_duplicates(df, name):
    """Return number of duplicate rows."""
    dup = df.duplicated().sum()
    print(f"{name} — duplicates: {dup}")
    return dup

def check_dtypes(df, name):
    """Return data types of dataframe columns."""
    print(f"\nDtypes in {name}:")
    return df.dtypes

def convert_to_datetime(df, cols):
    """Convert list of columns to datetime."""
    df[cols] = df[cols].apply(pd.to_datetime, errors="coerce")
    return df

def ensure_str(df, cols):
    """Convert list of columns to string."""
    for col in cols:
        df[col] = df[col].astype(str)
    return df
