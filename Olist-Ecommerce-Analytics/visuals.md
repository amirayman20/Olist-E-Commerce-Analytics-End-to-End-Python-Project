# 📊 Olist E‑Commerce — Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل للتحليل الاستكشافي (EDA). تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية تدعم صناع القرار في تحسين سلاسل الإمداد والمبيعات.

---

## 🟦 1) Orders & Time‑Series Analytics

### 1.1 Order Status Distribution
![Order Status](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/order_status_bar_chart.png)
* **💡 Operational Insight:** يوضح المخطط أن أكثر من **96%** من الطلبات تم توصيلها بنجاح، مما يعكس استقراراً في البنية التشغيلية وإتمام دورة الطلب.

### 1.2 Monthly Orders Trend
![Monthly Orders](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/monthly_orders_line_chart.png)
* **💡 Business Trend:** يكشف تحليل السلسلة الزمنية عن اتجاه تصاعدي قوي (Strong Upward Trend) في حجم المبيعات الإجمالي، مما يؤكد نمو الحصة السوقية للمنصة.

### 1.3 Daily Pattern of Orders
![Daily Pattern](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/daily_pattern_line_chart.png)
* **💡 Customer Behavior:** تتركز ذروة الطلبات شهرياً بين يومي 5 و 25، وهو سلوك شرائي مرتبط بدورة استلام الرواتب الشهرية وتوفر السيولة لدى المستهلك البرازيلي.

### 1.4 On‑Time vs Late Delivery Rate
![On Time vs Late](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/on_time_vs_late_delivery_rate.png)
* **💡 Supply Chain KPI:** مؤشر أداء رئيسي يقدم نسبة مئوية دقيقة للشحنات الناجحة في الالتزام بالوقت مقابل الشحنات المتأخرة لتقييم كفاءة شركات الشحن المتعاقد معها.

### 1.5 Single vs Multi‑Item Orders
![Single vs Multi](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/single_vs_multi_item_orders.png)
* **💡 Basket Composition:** يحلل سلوك العميل عند بناء السلة لتحديد مدى نجاح استراتيجيات البيع المتقاطع (Cross-selling) ونسبة الطلبات متعددة المنتجات.

---

## 🟩 2) Delivery & Logistics Performance

### 2.1 Delivery Time Distribution
![Delivery Time](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/delivery_time_histogram.png)
* **💡 Logistics Analytics:** يوضح التوزيع التكراري أن متوسط زمن التوصيل الفعلي يبلغ **12 يوماً**، وهي فترة طويلة تتطلب مراجعة لوجستية لتحسين تجربة المستخدم.

### 2.2 Estimated Delivery Time Distribution
![Estimated Delivery](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/estimated_delivery_time_histogram.png)
* **💡 Customer Expectations:** يحلل الفترات الزمنية المتوقعة التي تظهر للعميل قبل إتمام الشراء، وكيف تؤثر هذه التوقعات التشغيلية على قراره بالشراء.

### 2.3 Actual vs Estimated Delivery
![Actual vs Estimated](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/actual_vs_estimated_delivery_comparison.png)
* **💡 Predictive Accuracy:** يقيس مدى دقة الخوارزميات الحالية للمنصة في التنبؤ بمواعيد الشحن مقارنة بما حدث على أرض الواقع لتحديد فجوات القصور التشغيلي.

### 2.4 Delivery Delay Distribution
![Delivery Delay](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/delivery_delay_histogram.png)
* **💡 Risk Management:** يحدد حجم أيام التأخير التكرارية خارج إطار الوعد المحدد للعميل، وهو المدخل الأساسي لبناء نظام الإنذار المبكر (Early Warning System).

### 2.5 Delivery Delay vs Review Score
![Delay vs Review](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/delivery_delay_vs_review_score.png)
* **💡 Correlation Analysis:** يثبت إحصائياً وجود ارتباط طردي قوي بين تأخر الشحن لأكثر من 5 أيام وهبوط التقييمات تلقائياً إلى (1-2 نجوم)، مما يعني أن اللوجستيات هي المحرك الأول لسمعة المنصة.

---

## 🟨 3) Customer & Geographic Insights

### 3.1 Customer Distribution Map
![Customer Map](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/customer_distribution_map.png)
* **💡 Geospatial Insight:** يكشف التوزيع الجغرافي عن تركز **70%** من القوة الشرائية في المثلث التجاري الجنوبي الشرقي (SP, MG, RJ)، مما يوجه خطط التوسع الإقليمي.

### 3.2 Top Customer Cities
![Top Cities](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_customer_cities.png)
* **💡 Market Penetration:** يحدد المدن الأعلى توليداً للطلبات والإيرادات (وعلى رأسها São Paulo) لتركيز مستودعات التوزيع المحلية المصغرة (Micro-Fulfillment Center) لخدمتها.

---

## 🟧 4) Product & Category Intelligence

### 4.1 Top Product Categories
![Top Categories](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_product_categories.png)
* **💡 Pareto Principle:** يثبت صحة مبدأ باريتو، حيث تسيطر 3 فئات فقط (`bed_bath_table`, `health_beauty`, `sports_leisure`) على الكتلة الأكبر من مبيعات المنصة.

### 4.2 Top Products by Orders
![Top Products Orders](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_products_by_orders.png)
* **💡 Inventory Control:** يحدد السلع الأكثر تكراراً في عمليات الشراء المستقلة لضمان استقرار سلاسل الإمداد الخاصة بها ومنع انقطاع المخزون.

### 4.3 Top Products by Quantity Sold
![Top Products Quantity](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_products_by_quantity_sold.png)
* **💡 Volume Logistics:** يحلل السلع ذات الحجم الاستهلاكي الضخم ككميات مباعة لتجهيز خطوط التعبئة والتغليف السريع وتسهيل حركتها التشغيلية.

### 4.4 Top Products by Revenue
![Top Products Revenue](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_products_by_revenue.png)
* **💡 Revenue Optimization:** يفرز السلع الأعلى تحقيقاً للأرباح النقدية والإيرادات، والتي قد تختلف عن المنتجات الأكثر مبيعاً ككمية، لدعم حملات التسويق الموجهة لفئات الـ Premium.

### 4.5 Top Selling Products (Overall)
![Top Selling](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/top_selling_products.png)
* **💡 Merchandising Strategy:** يقدم لوحة الصدارة الشاملة للمنتجات القائدة لحركة التجارة على المنصة لتحديد السلع الاستراتيجية والأكثر جذباً للعملاء الجدد.

### 4.6 Product Volume vs Weight
![Volume vs Weight](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/product_volume_vs_weight.png)
* **💡 Dimensional Metrics:** يدرس العلاقة بين حجم المنتج ووزنه الفعلي، وهي المحدد الهندسي الذي تعتمد عليه شركات الشحن لفرض تسعير تكلفة الشحن الحجمي للطرود الكبيرة.

---

## 🟥 5) Pricing & Value Metrics

### 5.1 Order Value Distribution
![Order Value](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/order_value_histogram.png)
* **💡 Statistical Metric:** يوضح توزيع قيم الطلبات (Right-Skewed Distribution) أن متوسط الطلب يبلغ **180 BRL**، بينما الوسيط أقل من ذلك، مما يعني تركز البيع في المنتجات المتوسطة والاقتصادية.

### 5.2 Product Price Distribution
![Price Distribution](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/price_distribution.png)
* **💡 Pricing Strategy:** يحلل البنية السعرية لكافة السلع المدرجة من البائعين على المنصة لتقييم تنافسية الأسعار وملاءمتها للقدرة الشرائية للجمهور المستهدف.

### 5.3 Price Range Distribution (%)
![Price Range](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/price_range_distribution_percent.png)
* **💡 Market Segmentation:** يقسم المنتجات إلى شرائح مئوية بناءً على فئاتها السعرية، مما يساعد إدارة المنصة في تحديد الأسواق والقطاعات السعرية الأكثر نشاطاً وتوليداً للأرباح.

### 5.4 Freight Value Distribution
![Freight Value](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/freight_value_distribution.png)
* **💡 Cost Leakage Analysis:** يوضح أن متوسط شحن الطلب يتمركز عند **20 BRL**، وهو عبء مالي إضافي يتطلب مراجعة استراتيجيات الشحن المجاني المشروط لتقليل نسب التخلي عن السلة (Cart Abandonment).

---

## 🟪 6) Customer Experience & Reviews

### 6.1 Review Score Distribution
![Review Score](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/Review_score_distribution.png)
* **💡 Sentiment Analysis:** يظهر أن تقييم 5 نجوم هو الأكثر تكراراً، مما يعكس رضا العملاء العام عن جودة المنتجات نفسها عندما تصل في ظروف شحن سليمة ومثالية.

### 6.2 Average Review Score
![Average Review Score](https://raw.githubusercontent.com/amirayman20/Olist-E-Commerce-Analytics-End-to-End-Python-Project/main/data/images/average_review_score.png)
* **💡 Experience Baseline:** يمثل خط الأساس الرقمي لقياس جودة تجربة المستخدم العامة ومراقبة أداء المنصة التشغيلي عبر الفترات الزمنية المختلفة.
