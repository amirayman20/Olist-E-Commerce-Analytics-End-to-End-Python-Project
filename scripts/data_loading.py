path = "F:\olist/" 

# ============================
# 2) Load كل الملفات
# ============================

orders = pd.read_csv(path + "olist_orders_dataset.csv")
order_items = pd.read_csv(path + "olist_order_items_dataset.csv")
products = pd.read_csv(path + "olist_products_dataset.csv")
customers = pd.read_csv(path + "olist_customers_dataset.csv")
payments = pd.read_csv(path + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(path + "olist_order_reviews_dataset.csv")
sellers = pd.read_csv(path + "olist_sellers_dataset.csv")
geolocation = pd.read_csv(path + "olist_geolocation_dataset.csv")
category_translation = pd.read_csv(path + "product_category_name_translation.csv")

# ============================
# 3) تأكيد التحميل
# ============================

print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Products:", products.shape)
print("Customers:", customers.shape)
print("Payments:", payments.shape)
print("Reviews:", reviews.shape)
print("Sellers:", sellers.shape)
print("Geolocation:", geolocation.shape)
print("Category Translation:", category_translation.shape)
# merge orders with customers
orders_full = orders.merge(customers, on="customer_id", how="left")

# merge payments (sum value, max installments, mode payment type)
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

# merge reviews
orders_full = orders_full.merge(
    reviews[["order_id", "review_score", "review_comment_message", "review_creation_date"]],
    on="order_id",
    how="left"
)

# merge order_items (freight, price, product, seller)
orders_full = orders_full.merge(
    order_items[["order_id", "freight_value", "price", "product_id", "seller_id"]],
    on="order_id",
    how="left"
)

# merge products with category translation
product_info = products.merge(category_translation, on="product_category_name", how="left")
orders_full = orders_full.merge(product_info, on="product_id", how="left")

# merge sellers
orders_full = orders_full.merge(sellers, on="seller_id", how="left")

# ensure zip prefixes have the same dtype before merging
orders_full["customer_zip_code_prefix"] = orders_full["customer_zip_code_prefix"].astype(str)
geo_summary["geolocation_zip_code_prefix"] = geo_summary["geolocation_zip_code_prefix"].astype(str)

# merge geolocation (avg lat/lng per zip prefix)
orders_full = orders_full.merge(
    geo_summary,
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix",
    how="left"
)
orders_full = orders_full.merge(
    geo_summary,
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix",
    how="left"
)

# final shape check
print("orders_full shape:", orders_full.shape)
orders_full.head()
