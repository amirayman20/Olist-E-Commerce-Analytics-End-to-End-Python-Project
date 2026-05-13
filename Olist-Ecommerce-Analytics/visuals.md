# 🎨 Olist E‑Commerce — Full Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل (20 Visualization) التي تم إنتاجها أثناء مرحلة التحليل الاستكشافي (EDA).  
تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية سهلة الفهم لدعم اتخاذ القرار التجاري والتشغيلي.

---

## 📌 1) Orders & Time Series

### 1.1 Order Status Distribution  
![Order Status](data/images/order_status_bar_chart.png)  
**Insight:** توزيع حالات الطلبات (تم التوصيل، ملغي، قيد الشحن) يوضح نسبة الطلبات الناجحة مقابل الملغاة.

### 1.2 Monthly Orders Trend  
![Monthly Orders](data/images/monthly_orders_line_chart.png)  
**Insight:** اتجاه عدد الطلبات عبر الشهور يوضح نمو نشاط المنصة بشكل مستمر.

### 1.3 Daily Pattern Line Chart  
![Daily Pattern](data/images/daily_pattern_line_chart.png)  
**Insight:** ذروة الطلبات بين اليوم 5 و 25 من الشهر — سلوك مرتبط بدورات الرواتب.

### 1.4 On‑time vs Late Delivery Rate  
![On‑time vs Late](data/images/on_time_vs_late_delivery_rate.png)  
**Insight:** مقارنة نسبة الطلبات التي وصلت في الموعد مقابل المتأخرة.

### 1.5 Single vs Multi‑item Orders  
![Single vs Multi](data/images/single_vs_multi_item_orders.png)  
**Insight:** نسبة الطلبات بمنتج واحد مقابل عدة منتجات تؤثر على تكلفة الشحن والتخزين.

---

## 📌 2) Delivery & Logistics

### 2.1 Delivery Time Histogram  
![Delivery Time](data/images/delivery_time_histogram.png)  
**Insight:** توزيع زمن التوصيل الفعلي لكل طلب.

### 2.2 Estimated Delivery Time Histogram  
![Estimated Delivery Time](data/images/estimated_delivery_time_histogram.png)  
**Insight:** الزمن المتوقع للتوصيل كما يظهر للعميل — مقارنة مع الفعلي توضح دقة الوعود.

### 2.3 Actual vs Estimated Delivery Comparison  
![Actual vs Estimated](data/images/actual_vs_estimated_delivery_comparison.png)  
**Insight:** مقارنة الزمن الفعلي والتقديري تُظهر الفجوة اللوجستية في بعض الولايات.

### 2.4 Delivery Delay Histogram  
![Delivery Delay](data/images/delivery_delay_histogram.png)  
**Insight:** توزيع عدد أيام التأخير عن الموعد المتوقع.

### 2.5 Delivery Delay vs Review Score  
![Delay vs Review](data/images/delivery_delay_vs_review_score.png)  
**Insight:** كلما زاد التأخير، انخفض التقييم — علاقة طردية واضحة بين اللوجستيات والرضا العميل.

---

## 📌 3) Customer & Geography

### 3.1 Customer Distribution Map  
![Customer Map](data/images/customer_distribution_map.png)  
**Insight:** التوزيع الجغرافي للعملاء على خريطة البرازيل يُظهر تمركز الطلب في الجنوب الشرقي.

### 3.2 Top Customer Cities  
![Top Customer Cities](data/images/top_customer_cities.png)  
**Insight:** São Paulo هي أكبر سوق استهلاكي تليها Belo Horizonte و Rio de Janeiro.

---

## 📌 4) Products & Categories

### 4.1 Top Product Categories  
![Top Product Categories](data/images/top_product_categories.png)  
**Insight:** ثلاث فئات (`bed_bath_table`, `health_beauty`, `sports_leisure`) تمثل 60% من المبيعات.

### 4.2 Top Products by Orders  
![Top Products by Orders](data/images/top_products_by_orders.png)  
**Insight:** المنتجات الأكثر طلبًا من حيث عدد الطلبات.

### 4.3 Top Products by Quantity Sold  
![Top Products by Quantity](data/images/top_products_by_quantity_sold.png)  
**Insight:** المنتجات الأعلى من حيث إجمالي الكمية المباعة.

### 4.4 Top Products by Revenue  
![Top Products by Revenue](data/images/top_products_by_revenue.png)  
**Insight:** المنتجات الأعلى مساهمة في الإيرادات الإجمالية.

### 4.5 Top Selling Products (Overall)  
![Top Selling Products](data/images/top_selling_products.png)  
**Insight:** نظرة مجمعة على أقوى المنتجات أداءً في المنصة.

### 4.6 Product Volume vs Weight  
![Product Volume vs Weight](data/images/product_volume_vs_weight.png)  
**Insight:** العلاقة بين حجم المنتج ووزنه تؤثر على تكلفة الشحن والتخزين.

---

## 📌 5) Pricing & Value

### 5.1 Order Value Histogram  
![Order Value](data/images/order_value_histogram.png)  
**Insight:** توزيع قيمة الطلبات (AOV) وتحديد الطلبات ذات القيمة العالية.

### 5.2 Price Distribution  
![Price Distribution](data/images/price_distribution.png)  
**Insight:** توزيع أسعار المنتجات الفردية يوضح التركيز على المنتجات متوسطة السعر.

### 5.3 Price Range Distribution (Percent)  
![Price Range Percent](data/images/price_range_distribution_percent.png)  
**Insight:** نسبة المنتجات في كل شريحة سعرية (منخفضة / متوسطة / مرتفعة).

### 5.4 Freight Value Distribution  
![Freight Value](data/images/freight_value_distribution.png)  
**Insight:** توزيع تكلفة الشحن لكل طلب يوضح تأثير حجم المنتج على السعر النهائي.

---

## 📌 6) Reviews & Experience

### 6.1 Review Score Distribution  
![Review Score Distribution](data/images/Review_score_distribution.png)  
**Insight:** توزيع تقييمات العملاء (1–5 نجوم) يُظهر أن 5 نجوم هي الأكثر شيوعًا.

### 6.2 Average Review Score  
![Average Review Score](data/images/average_review_score.png)  
**Insight:** المتوسط العام لتقييمات العملاء يشير إلى رضا مرتفع عن المنتجات.

---

## 🏁 Summary

يغطي هذا المعرض جميع الرسومات المحفوظة في `data/images/` كما هي بأسمائها الحقيقية،  
ويُعد مرجعًا بصريًا جاهزًا للعروض التقديمية والـ Portfolio.
