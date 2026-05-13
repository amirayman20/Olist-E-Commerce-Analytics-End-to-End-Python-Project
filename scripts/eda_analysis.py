
import pandas as pd

def monthly_orders(df):
    """Return monthly order counts."""
    df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M")
    return df.groupby("order_month")["order_id"].count().reset_index()

def daily_order_pattern(df):
    """Return average orders per day number."""
    df["day_in_month"] = df["order_purchase_timestamp"].dt.day
    daily = df.groupby("day_in_month")["order_id"].count().reset_index()
    months_count = df["order_purchase_timestamp"].dt.to_period("M").nunique()
    daily["avg_orders_per_day"] = daily["order_id"] / months_count
    return daily

def order_value_stats(df):
    """Return descriptive statistics for payment_value."""
    stats = df["payment_value"].describe()
    quantiles = df["payment_value"].quantile([0.25, 0.50, 0.75, 0.90, 0.95])
    zero_value = (df["payment_value"] == 0).sum()
    high_value = (df["payment_value"] > 500).sum()

    return {
        "describe": stats,
        "quantiles": quantiles,
        "zero_value_orders": zero_value,
        "high_value_orders": high_value
    }

def freight_stats(df):
    """Return descriptive statistics for freight_value."""
    stats = df["freight_value"].describe()
    zero_freight = (df["freight_value"] == 0).sum()
    high_freight = (df["freight_value"] > 200).sum()

    return {
        "describe": stats,
        "zero_freight": zero_freight,
        "high_freight": high_freight
    }

def payment_type_distribution(df):
    """Return count and percentage of payment types."""
    counts = df["payment_type"].value_counts()
    percent = df["payment_type"].value_counts(normalize=True) * 100
    return counts, percent
