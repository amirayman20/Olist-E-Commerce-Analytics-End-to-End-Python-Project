import matplotlib.pyplot as plt
import seaborn as sns

def plot_order_status(df, save_path="images/order_status_bar_chart.png"):
    status_counts = df["order_status"].value_counts().reset_index()
    status_counts.columns = ["order_status", "count"]

    plt.figure(figsize=(14,6))
    sns.barplot(data=status_counts, x="order_status", y="count", color="#1D7CF2")
    plt.title("Order Status Distribution — Olist")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_daily_pattern(df, save_path="images/daily_pattern_line_chart.png"):
    plt.figure(figsize=(14,6))
    sns.lineplot(data=df, x="day_in_month", y="avg_orders_per_day", color="#1D7CF2")
    plt.title("Average Orders per Day Number")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_monthly_orders(df, save_path="images/monthly_orders_line_chart.png"):
    plt.figure(figsize=(14,6))
    sns.lineplot(data=df, x="month", y="orders_count", color="#1D7CF2")
    plt.title("Monthly Orders Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_order_value(df, save_path="images/order_value_histogram.png"):
    plt.figure(figsize=(14,6))
    sns.histplot(df["payment_value"], bins=50, kde=True, color="#1D7CF2")
    plt.title("Order Value Distribution")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_freight_value(df, save_path="images/freight_value_distribution.png"):
    filtered = df[df["freight_value"] <= 200]
    plt.figure(figsize=(14,6))
    sns.histplot(filtered["freight_value"], bins=50, kde=True, color="#1D7CF2")
    plt.title("Freight Value Distribution")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_payment_type(df, save_path="images/payment_type_pie.png"):
    payment_percent = df["payment_type"].value_counts(normalize=True) * 100

    plt.figure(figsize=(8,8))
    plt.pie(
        payment_percent.values,
        labels=payment_percent.index,
        autopct=lambda p: f"{p:.2f}%",
        startangle=140,
        pctdistance=0.85,
        labeldistance=1.1,
        colors=sns.color_palette("Blues", len(payment_percent))
    )
    plt.title("Payment Type Distribution")
    plt.savefig(save_path)
    plt.close()
