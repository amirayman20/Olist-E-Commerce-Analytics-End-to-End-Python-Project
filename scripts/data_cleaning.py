# ================================
# 🔍 Quick Null Check
# ================================
def check_nulls(df, name):
    print(f"\n{name} — null count")
    print(df.isna().sum())

check_nulls(orders, "orders")
check_nulls(order_items, "order_items")
check_nulls(products, "products")
check_nulls(customers, "customers")
check_nulls(payments, "payments")
check_nulls(reviews, "reviews")
check_nulls(sellers, "sellers")
check_nulls(geolocation, "geolocation")


# ================================
# 🧹 Clean Product Table
# ================================
# fill missing category
products["product_category_name"].fillna("unknown", inplace=True)

# drop rows with missing dimensions
products.dropna(
    subset=[
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ],
    inplace=True
)

# keep delivery date nulls (canceled / incomplete orders)
# keep review comment nulls (not needed for numeric analysis)


# ================================
# 🔁 Duplicate Check
# ================================
def check_duplicates(df, name):
    print(f"{name} — duplicates:", df.duplicated().sum())

check_duplicates(orders, "orders")
check_duplicates(order_items, "order_items")
check_duplicates(products, "products")
check_duplicates(customers, "customers")
check_duplicates(payments, "payments")
check_duplicates(reviews, "reviews")
check_duplicates(sellers, "sellers")
check_duplicates(geolocation, "geolocation")


# ================================
# 🔠 Data Types Check
# ================================
def check_dtypes(df, name):
    print(f"\nDtypes in {name}:")
    print(df.dtypes)

check_dtypes(orders, "orders")
check_dtypes(order_items, "order_items")
check_dtypes(products, "products")
check_dtypes(customers, "customers")
check_dtypes(payments, "payments")
check_dtypes(reviews, "reviews")
check_dtypes(sellers, "sellers")
check_dtypes(geolocation, "geolocation")


# ================================
# 🕒 Convert Date Columns
# ================================
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

orders[date_cols] = orders[date_cols].apply(pd.to_datetime, errors="coerce")

# shipping limit date
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"], errors="coerce"
)

# ================================
# 🔢 Fix ZIP Code Types
# ================================
customers["customer_zip_code_prefix"] = customers["customer_zip_code_prefix"].astype(str)
sellers["seller_zip_code_prefix"] = sellers["seller_zip_code_prefix"].astype(str)


# ================================
# 📝 Convert Review Dates
# ================================
reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"], errors="coerce"
)
reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"], errors="coerce"
)
