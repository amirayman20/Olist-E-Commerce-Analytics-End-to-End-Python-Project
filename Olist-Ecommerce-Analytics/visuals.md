# 🎨 Olist E‑Commerce — Full Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل (20 Visualization) التي تم إنتاجها وحفظها تلقائياً أثناء مرحلة التحليل الاستكشافي (EDA). تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية سهلة الفهم لدعم اتخاذ القرار التجاري والتشغيلي.

---

## 📌 1) Order & Time-Series Visualizations

### 📊 1.1 Order Status Distribution
![Order Status](./data/images/order_status_bar_chart.png)
**💡 Insight:** أكثر من **96%** من الطلبات تم توصيلها بنجاح، مما يعكس استقراراً في البنية التشغيلية العامة للمنصة.

---

### 📈 1.2 Monthly Orders Trend
![Monthly Trend](./data/images/monthly_orders_line_chart.png)
**💡 Insight:** اتجاه تصاعدي قوي في حجم الطلبات عبر الأشهر، مما يؤكد نمو الحصة السوقية للمنصة.

---

### 📉 1.3 Daily Demand Pattern
![Daily Pattern](./data/images/daily_pattern_line_chart.png)
**💡 Insight:** ذروة الطلبات بين اليوم 5 و25 من الشهر، مرتبطة بدورات الرواتب الشهرية.

---

### 📅 1.4 Weekly Transaction Activity
![Weekly Pattern](./data/images/weekly_pattern.png)
**💡 Insight:** انخفاض النشاط الشرائي في عطلة نهاية الأسبوع، مما يتيح إعادة تنظيم عمليات الشحن.

---

### ⏰ 1.5 Hourly Order Distribution
![Hourly Orders](./data/images/hourly_orders.png)
**💡 Insight:** الذروة اليومية بين الساعة **10 صباحاً** و**4 مساءً**، الوقت المثالي للعروض السريعة.

---

## 📌 2) Financial & Payment Visualizations

### 💳 2.1 Payment Type Distribution
![Payment Type](./data/images/payment_type_pie.png)
**💡 Insight:** البطاقات الائتمانية تمثل **75%** من إجمالي العمليات، يليها Boleto بنسبة **19%**.

---

### 📈 2.2 Installments Distribution Analysis
![Installments](./data/images/installments_distribution.png)
**💡 Insight:** أغلب العملاء يفضلون التقسيط على **1–3 أقساط**، مما يقلل مخاطر الائتمان طويلة المدى.

---

## 📌 3) Order Value & Freight Metrics

### 💰 3.1 Average Order Value (AOV)
![Order Value](./data/images/order_value_histogram.png)
**💡 Insight:** متوسط الطلب **180 BRL**، مع وجود شريحة Premium صغيرة ترفع الإيرادات.

---

### 🚚 3.2 Freight Cost Variance
![Freight Value](./data/images/freight_value_distribution.png)
**💡 Insight:** متوسط تكلفة الشحن **20 BRL**، وتشكل عبئاً على قرار الشراء.

---

### ⚖️ 3.3 Product Price vs Freight Value
![Price vs Freight](./data/images/price_vs_freight.png)
**💡 Insight:** لا توجد علاقة خطية بين السعر وتكلفة الشحن، بل تعتمد على الحجم والوزن.

---

### 📦 3.4 Product Volume vs Freight Cost
![Volume vs Freight](./data/images/volume_vs_freight.png)
**💡 Insight:** علاقة طردية قوية بين حجم المنتج وتكلفة الشحن.

---

## 📌 4) Product & Category Intelligence

### 🏆 4.1 Top Performing Product Categories
![Top Categories](./data/images/top_categories.png)
**💡 Insight:** ثلاث فئات فقط (`bed_bath_table`, `health_beauty`, `sports_leisure`) تمثل **60%** من المبيعات.

---

### 💵 4.2 Category Revenue Contribution
![Category Revenue](./data/images/category_revenue.png)
**💡 Insight:** فئة `bed_bath_table` الأعلى إيراداً وتشكل محور الحملات التسويقية.

---

### ⚖️ 4.3 Product Physical Weight Distribution
![Product Weight](./data/images/product_weight.png)
**💡 Insight:** معظم المنتجات أقل من **2 كجم**، مما يسهل عمليات التخزين والتوصيل.

---

## 📌 5) Geospatial & Demographic Analysis

### 🏙️ 5.1 Top Order-Generating Cities
![Top Cities](./data/images/top_cities.png)
**💡 Insight:** São Paulo أكبر سوق استهلاكي بفارق كبير عن باقي المدن.

---

### 🗺️ 5.2 Regional Customer Density by State
![Customer Distribution](./data/images/customer_state_distribution.png)
**💡 Insight:** 70% من الطلبات في ولايات SP وMG وRJ، مما يعكس تركّز النشاط التجاري.

---

### 🏭 5.3 Merchant/Seller Geographical Cluster
![Seller Distribution](./data/images/seller_distribution.png)
**💡 Insight:** أغلب البائعين في SP، مما يمنح ميزة لوجستية محلية.

---

## 📌 6) Logistics & Delivery Analytics

### 🚚 6.1 Total Delivery Lead Time Distribution
![Delivery Time](./data/images/delivery_time.png)
**💡 Insight:** متوسط التوصيل **12 يوم**، وهي فترة طويلة نسبيًا في معايير التجارة الإلكترونية.

---

### 🚨 6.2 Variance of Freight Delays
![Delivery Delay](./data/images/delivery_delay.png)
**💡 Insight:** يوضح عدد الأيام التي تتجاوز فيها الشحنات الموعد المتوقع للتسليم.

---

### 🗺️ 6.3 State-wise Delivery Latency Breakdown
![Delivery by State](./data/images/delivery_by_state.png)
**💡 Insight:** الولايات الشمالية تتأخر أكثر من الجنوبية، مما يستدعي مراكز توزيع إقليمية.

---

## 📌 7) Customer Sentiment & Experience

### ⭐ 7.1 Review Score Frequency
![Review Score](./data/images/review_score_distribution.png)
**💡 Insight:** تقييم **5 نجوم** هو الأكثر تكرارًا، مما يدل على رضا العملاء عن جودة المنتجات.

---

### 📉 7.2 Correlation: Shipping Delay vs Review Score
![Review vs Delay](./data/images/delivery_delay_vs_review_score.png)
**💡 Insight:** كلما زاد التأخير، انخفض التقييم إلى نجمة أو اثنتين.

---

### 📝 7.3 Review Text Length Distribution
![Review Text Length](./data/images/review_text_length.png)
**💡 Insight:** التقييمات السلبية أطول في النص، مما يجعلها مثالية لتحليل المشاعر.

---

## 🏁 Summary Matrix
يغطي هذا المعرض **20 مخططاً بيانياً** متكاملاً تم ربطها بخط معالجة البيانات (Data Pipeline)، وتوفر مرجعاً بصرياً ممتازاً لأي عرض تقديمي أو مناقشة فنية للمشروع.
