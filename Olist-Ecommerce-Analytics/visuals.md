# 🎨 Olist E‑Commerce — Full Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل التي تم إنتاجها وحفظها تلقائياً أثناء مرحلة التحليل الاستكشافي (EDA). تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية سهلة الفهم لدعم اتخاذ القرار التجاري والتشغيلي.

---

## 📌 1) Order & Time-Series Visualizations

### 📊 1.1 Order Status Distribution
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**

![Order Status](data/images/order_status_bar_chart.png)

* **💡 Operational Insight:** أكثر من **96%** من الطلبات تم توصيلها بنجاح إلى العملاء، مما يعكس استقراراً في البنية التشغيلية العامة للمنصة وقدرتها على إتمام دورة الطلب.

### 📈 1.2 Monthly Orders Trend
* **📊 المخطط البياني:** `Time-Series Line Chart`
* **📁 المعاينة المرئية:**

![Monthly Trend](data/images/monthly_orders_line_chart.png)

* **💡 Operational Insight:** يوضح المخطط اتجاهاً تصاعدياً قوياً ومستقراً (Strong Upward Trend) في حجم الطلبات الإجمالي عبر الأشهر، مما يؤكد نمو الحصة السوقية للمنصة وزيادة اعتماد المستهلكين عليها.

### 📉 1.3 Daily Demand Pattern
* **📊 المخطط البياني:** `Cyclical Line Chart`
* **📁 المعاينة المرئية:**

![Daily Pattern](data/images/daily_pattern_line_chart.png)

* **💡 Operational Insight:** تتركز ذروة الطلبات بشكل واضح في الفترة الممتدة من يوم 5 إلى يوم 25 من كل شهر، وهو سلوك شرائي مرتبط بدورات استلام الرواتب الشهرية وتوفر السيولة لدى المستهلكين.

---

## 📌 2) Financial & Price Visualizations

### 💰 2.1 Distribution of Average Order Value (AOV)
* **📊 المخطط البياني:** `Right-Skewed Histogram`
* **📁 المعاينة المرئية:**

![Order Value](data/images/order_value_histogram.png)

* **💡 Operational Insight:** يبلغ متوسط قيمة الطلب **180 BRL**، بينما يقل الوسيط (Median) عن ذلك بشكل ملحوظ، مما يؤكد تركز معظم المبيعات في المنتجات منخفضة ومتوسطة السعر مع وجود شريحة Premium تحرك الإيرادات الإجمالية.

### 💵 2.2 Price Distribution Analysis
* **📊 المخطط البياني:** `Price Distribution Plot`
* **📁 المعاينة المرئية:**

![Price Distribution](data/images/price_distribution.png)

* **💡 Operational Insight:** تحليل توزيع الأسعار يوضح النطاقات السعرية الأكثر مبيعاً ونسبة المنتجات الفاخرة المتاحة على المنصة لتحديد الفئات السعرية المستهدفة بدقة.

### 📈 2.3 Price Range Distribution Percentages
* **📊 المخطط البياني:** `Distribution Percentage Chart`
* **📁 المعاينة المرئية:**

![Price Range](data/images/price_range_distribution_percent.png)

* **💡 Operational Insight:** يوفر تفصيلاً مئوياً لشرائح الأسعار المختلفة، مما يساعد في وضع استراتيجيات التسعير وتحديد هوامش الربح التنافسية.

---

## 📌 3) Freight & Logistics Metrics

### 🚚 3.1 Freight Cost Variance
* **📊 المخطط البياني:** `Density Plot`
* **📁 المعاينة المرئية:**

![Freight Value](data/images/freight_value_distribution.png)

* **💡 Operational Insight:** يتمركز متوسط تكلفة الشحن عند **20 BRL** للطلب الواحد، وتشكل مصاريف الشحن عبئاً مالياً إضافياً قد يؤثر على قرار العميل بإتمام عملية الشراء (Cart Abandonment).

### 📦 3.2 Product Volumetrics vs. Weight
* **📊 المخطط البياني:** `Scatter Plot`
* **📁 المعاينة المرئية:**

![Volume vs Weight](data/images/product_volume_vs_weight.png)

* **💡 Operational Insight:** يكشف المخطط العلاقة بين وزن المنتج وحجمه الفعلي، وهي المحدد الأساسي الذي تعتمد عليه شركات اللوجستيات لحساب تكاليف الشحن الحجمي.

### 🚨 3.3 Actual vs. Estimated Delivery Comparison
* **📊 المخطط البياني:** `Comparison Plot`
* **📁 المعاينة المرئية:**

![Actual vs Estimated](data/images/actual_vs_estimated_delivery_comparison.png)

* **💡 Operational Insight:** يقارن بين أوقات التوصيل الفعلية والمواعيد المتوقعة الموعود بها للعميل لتحديد نسب الكفاءة والقصور التشغيلي لدى مزودي خدمات الشحن.

### ⏳ 3.4 Delivery Time Histogram
* **📊 المخطط البياني:** `Delivery Time Histogram`
* **📁 المعاينة المرئية:**

![Delivery Time Histogram](data/images/delivery_time_histogram.png)

* **💡 Operational Insight:** يحلل التوزيع التكراري للفترات الزمنية الفعلية المستغرقة في الشحن من المصدر للمستهلك.

### ⏳ 3.5 Estimated Delivery Time Distribution
* **📊 المخطط البياني:** `Estimated Time Histogram`
* **📁 المعاينة المرئية:**

![Estimated Delivery Time](data/images/estimated_delivery_time_histogram.png)

* **💡 Operational Insight:** يوضح توزيع الفترات الزمنية المتوقعة للشحن التي تظهر للمستخدم قبل إتمام الشراء، ومدى دقتها وتأثيرها على توقعات تجربة المستخدم.

### ⏱️ 3.6 Delivery Delay Variance
* **📊 المخطط البياني:** `Delay Histogram`
* **📁 المعاينة المرئية:**

![Delivery Delay](data/images/delivery_delay_histogram.png)

* **💡 Operational Insight:** يوضح المخطط حجم وعدد الأيام التي تتجاوز فيها الشحنات الموعد المتوقع للتسليم، وهي البيانات المستخدمة كمدخلات رئيسية لبناء نظام الإنذار المبكر (Early Warning System).

### 🏁 3.7 On-Time vs. Late Delivery Rate
* **📊 المخطط البياني:** `Rate Comparison Chart`
* **📁 المعاينة المرئية:**

![On Time vs Late](data/images/on_time_vs_late_delivery_rate.png)

* **💡 Operational Insight:** يقدم نسبة مئوية واضحة للطلبات التي وصلت في موعدها المحدد تماماً مقابل الطلبات المتأخرة، وهو مؤشر الأداء الرئيسي (KPI) لتقييم كفاءة سلاسل الإمداد.

---

## 📌 4) Product & Category Intelligence

### 🏆 4.1 Top Performing Product Categories
* **📊 المخطط البياني:** `Horizontal Bar Chart`
* **📁 المعاينة المرئية:**

![Top Categories](data/images/top_product_categories.png)

* **💡 Operational Insight:** يثبت المخطط صحة مبدأ باريتو (Pareto Principle)، حيث تسيطر فئات رئيسية محددة على حجم المبيعات الإجمالي للمنصة.

### 🛒 4.2 Top Products by Orders & Quantity Sold
* **📊 المخطط البياني:** `Volume Charts`
* **📁 المعاينة المرئية:**

![Products by Orders](data/images/top_products_by_orders.png)

![Products by Quantity](data/images/top_products_by_quantity_sold.png)

* **💡 Operational Insight:** يوضح تفصيلاً دقيقاً لأكثر المنتجات تكراراً في سلات المشتريات والكميات الفعلية المباعة منها لتأمين مستويات المخزون المناسبة.

### 💵 4.3 Top Products by Revenue & Best Selling
* **📊 المخطط البياني:** `Revenue Charts`
* **📁 المعاينة المرئية:**

![Products by Revenue](data/images/top_products_by_revenue.png)

![Top Selling](data/images/top_selling_products.png)

* **💡 Operational Insight:** يحدد المنتجات الأعلى توليداً للأرباح للإيرادات الإجمالية، والتي قد تختلف عن المنتجات الأكثر مبيعاً من حيث الكمية، مما يساعد في إعادة توجيه الحملات التسويقية الفاخرة.

---

## 📌 5) Geospatial & Operational Clustering

### 🗺️ 5.1 Regional Customer Density Map
* **📊 المخطط البياني:** `Geospatial Choropleth Map`
* **📁 المعاينة المرئية:**

![Customer Distribution](data/images/customer_distribution_map.png)

* **💡 Operational Insight:** تتركز الكتلة الاستهلاكية الكبرى في ولايات المثلث التجاري للبرازيل، مما يعكس الفجوة الكبيرة في التوزيع الجغرافي للطلب ويوجه خطط التوسع اللوجستي الإقليمي.

### 🏙️ 5.2 Top Customer Cities
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**

![Top Cities](data/images/top_customer_cities.png)

* **💡 Operational Insight:** يحدد المدن الأعلى طلباً وإيراداً لتخصيص خطوط شحن سريعة ومباشرة ومستودعات محلية مصغرة لخدمة هذه الكثافة السكانية المرتفعة.

### 📦 5.3 Single vs. Multi-Item Orders Analysis
* **📊 المخطط البياني:** `Order Composition Chart`
* **📁 المعاينة المرئية:**

![Order Composition](data/images/single_vs_multi_item_orders.png)

* **💡 Operational Insight:** يحلل سلوك العميل عند بناء السلة؛ هل يميل لشراء منتج واحد في الشحنة أم منتجات متعددة، وهو أساس ممتاز لتطوير استراتيجيات الـ Cross-selling.

---

## 📌 6) Customer Sentiment & Experience

### ⭐ 6.1 Review Score Frequency
* **📊 المخطط البياني:** `Categorical Bar Chart`
* **📁 المعاينة المرئية:**

![Review Score](data/images/Review_score_distribution.png)

* **💡 Operational Insight:** يوفر نظرة عامة على مدى رضا العملاء، حيث يظهر تقييم 5 نجوم كالأكثر تكراراً، مما يدل على جودة المنتجات المتاحة فور وصولها للعميل بسلام.

### 📉 6.2 Customer Evaluation Average
* **📊 المخطط البياني:** `Score Metrics`
* **📁 المعاينة المرئية:**

![Average Review Score](data/images/average_review_score.png)

* **💡 Operational Insight:** يمثل خط الأساس لقياس جودة تجربة المستخدم العامة على المنصة ومراقبة تذبذب التقييمات عبر الفترات التشغيلية المختلفة.

### 🚨 6.3 Correlation: Shipping Delay vs. Review Score
* **📊 المخطط البياني:** `Bivariate Heatmap`
* **📁 المعاينة المرئية:**

![Review vs Delay](data/images/delivery_delay_vs_review_score.png)

* **💡 Operational Insight:** تظهر طردية العلاقة بشكل قاطع؛ فكلما زادت أيام التأخير عن الموعد الموعود، تضاعفت احتمالية هبوط التقييم إلى نجمة واحدة أو نجمتين، مما يثبت أن اللوجستيات هي المحرك الأول لسمعة المنصة.
