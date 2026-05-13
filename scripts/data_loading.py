# ============================================
# 📂 1) Define Data Path
# ============================================
path = r"F:\olist/"


# ============================================
# 📥 2) Load All CSV Files
# ============================================
orders = pd.read_csv(path + "olist_orders_dataset.csv")
order_items = pd.read_csv(path + "olist_order_items_dataset.csv")
products = pd.read_csv(path + "olist_products_dataset.csv")
customers = pd.read_csv(path + "olist_customers_dataset.csv")
payments = pd.read_csv(path + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(path + "olist_order_reviews_dataset.csv")
sellers = pd.read_csv(path + "olist_sellers_dataset.csv")
geolocation = pd.read_csv(path + "olist_geolocation_dataset.csv")
category_translation = pd.read_csv(path + "product_category_name_translation.csv")


# ============================================
# 📏 3) Confirm Loaded Shapes
# ============================================
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Products:", products.shape)
print("Customers:", customers.shape)
print("Payments:", payments.shape)
print("Reviews:", reviews.shape)
print("Sellers:", sellers.shape)
print("Geolocation:", geolocation.shape)
print("Category Translation:", category_translation.shape)


# ============================================
# 🔗 4) Merge: Orders + Customers
# ============================================
orders_full = orders.merge(customers, on="customer_id", how="left")


# ============================================
# 🔗 5) Merge: Payments Summary
# ============================================
payment_summary = (
    payments.groupby("order_id")
    .agg({
        "payment_value": "sum",
        "payment_installments": "max",
        "payment_type": lambda x: x.mode()[0] if not x.mode().empty else None
    })
    .reset_index()
)

orders_full = orders_full.merge(payment_summary, on="order_id", how="left")


# ============================================
# 🔗 6) Merge: Reviews
# ============================================
orders_full = orders_full.merge(
    reviews[["order_id", "review_score", "review_comment_message", "review_creation_date"]],
    on="order_id",
    how="left"
)


# ============================================
# 🔗 7) Merge: Order Items (freight, price, product, seller)
# ============================================
orders_full = orders_full.merge(
    order_items[["order_id", "freight_value", "price", "product_id", "seller_id"]],
    on="order_id",
    how="left"
)


# ============================================
# 🔗 8) Merge: Products + Category Translation
# ============================================
product_info = products.merge(category_translation, on="product_category_name", how="left")
orders_full = orders_full.merge(product_info, on="product_id", how="left")


# ============================================
# 🔗 9) Merge: Sellers
# ============================================
orders_full = orders_full.merge(sellers, on="seller_id", how="left")


# ============================================
# 🔗 10) Prepare Geolocation Summary
# ============================================
geo_summary = (
    geolocation.groupby("geolocation_zip_code_prefix")
    .agg({
        "geolocation_lat": "mean",
        "geolocation_lng": "mean"
    })
    .reset_index()
)

# ensure dtype match
orders_full["customer_zip_code_prefix"] = orders_full["customer_zip_code_prefix"].astype(str)
geo_summary["geolocation_zip_code_prefix"] = geo_summary["geolocation_zip_code_prefix"].astype(str)


# ============================================
# 🔗 11) Merge: Geolocation (avg lat/lng per ZIP)
# ============================================
orders_full = orders_full.merge(
    geo_summary,
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix",
    how="left"
)


# ============================================
# 📏 12) Final Shape Check
# ============================================
print("orders_full shape:", orders_full.shape)
orders_full.head()
