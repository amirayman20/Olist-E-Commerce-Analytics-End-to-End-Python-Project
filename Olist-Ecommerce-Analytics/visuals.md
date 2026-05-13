# 🎨 Olist E‑Commerce — Full Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل (20 Visualization) التي تم إنتاجها وحفظها تلقائياً أثناء مرحلة التحليل الاستكشافي (EDA). تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية سهلة الفهم لدعم اتخاذ القرار التجاري والتشغيلي.

---

## 📌 1) Order & Time-Series Visualizations

### 📊 1.1 Order Status Distribution
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**
![Order Status](./images/order_status_bar_chart.png)
* **💡 Operational Insight:** أكثر من **96%** من الطلبات تم توصيلها بنجاح إلى العملاء، مما يعكس استقراراً في البنية التشغيلية العامة للمنصة وقدرتها على إتمام دورة الطلب.

### 📈 1.2 Monthly Orders Trend
* **📊 المخطط البياني:** `Time-Series Line Chart`
* **📁 المعاينة المرئية:**
![Monthly Trend](./images/monthly_orders_line_chart.png)
* **💡 Operational Insight:** يوضح المخطط اتجاهاً تصاعدياً قوياً ومستقراً (Strong Upward Trend) في حجم الطلبات الإجمالي عبر الأشهر، مما يؤكد نمو الحصة السوقية للمنصة وزيادة اعتماد المستهلكين عليها.

### 📉 1.3 Daily Demand Pattern
* **📊 المخطط البياني:** `Cyclical Line Chart`
* **📁 المعاينة المرئية:**
![Daily Pattern](./images/daily_pattern_line_chart.png)
* **💡 Operational Insight:** تتركز ذروة الطلبات بشكل واضح في الفترة الممتدة من يوم 5 إلى يوم 25 من كل شهر، وهو سلوك شرائي مرتبط بدورات استلام الرواتب الشهرية وتوفر السيولة لدى المستهلكين.

### 📅 1.4 Weekly Transaction Activity
* **📊 المخطط البياني:** `Day-of-Week Bar Chart`
* **📁 المعاينة المرئية:**
![Weekly Pattern](./images/weekly_pattern.png)
* **💡 Operational Insight:** تسجل أيام السبت والأحد انخفاضاً ملحوظاً في النشاط الشرائي مقارنة بأيام منتصف الأسبوع، مما يتيح فرصة لشركات الشحن لإعادة تنظيم طاقاتها الاستيعابية خلال عطلة نهاية الأسبوع.

### ⏰ 1.5 Hourly Order Distribution
* **📊 المخطط البياني:** `Hourly Heatmap / Line Chart`
* **📁 المعاينة المرئية:**
![Hourly Orders](./images/hourly_orders.png)
* **💡 Operational Insight:** تبلغ حركة الشراء ذروتها اليومية بين الساعة **10:00 صباحاً** والساعة **04:00 مساءً**، مما يحدد التوقيت المثالي لإطلاق الإشعارات الفورية (Push Notifications) أو العروض السريعة (Flash Sales).

---

## 📌 2) Financial & Payment Visualizations

### 💳 2.1 Payment Type Distribution
* **📊 المخطط البياني:** `Pie Chart / Donut Chart`
* **📁 المعاينة المرئية:**
![Payment Type](./images/payment_type_pie.png)
* **💡 Operational Insight:** تستحوذ البطاقات الائتمانية على **75%** من إجمالي العمليات المالية، يليها نظام الفواتير (Boleto Bancário) بنسبة **19%**، مما يبرز تفضيل المستهلك لخيارات الدفع المؤجل أو التقسيط.

### 📈 2.2 Installments Distribution Analysis
* **📊 المخطط البياني:** `Frequency Histogram`
* **📁 المعاينة المرئية:**
![Installments](./images/installments_distribution.png)
* **💡 Operational Insight:** يوضح التوزيع أن الكتلة النقدية الأكبر من العملاء تفضل تقسيط المشتريات على فترات قصيرة تتراوح بين **1 إلى 3 أقساط**، مما يقلل من مخاطر الائتمان طويلة المدى على بوابات الدفع.

---

## 📌 3) Order Value & Freight Metrics

### 💰 3.1 Distribution of Average Order Value (AOV)
* **📊 المخطط البياني:** `Right-Skewed Histogram with KDE`
* **📁 المعاينة المرئية:**
![Order Value](./images/order_value_histogram.png)
* **💡 Operational Insight:** يبلغ متوسط قيمة الطلب **180 BRL**، بينما يقل الوسيط (Median) عن ذلك بشكل ملحوظ، مما يؤكد تركز معظم المبيعات في المنتجات منخفضة ومتوسطة السعر مع وجود شريحة Premium تحرك الإيرادات الإجمالية.

### 🚚 3.2 Freight Cost Variance
* **📊 المخطط البياني:** `Density Plot`
* **📁 المعاينة المرئية:**
![Freight Value](./images/freight_value_distribution.png)
* **💡 Operational Insight:** يتمركز متوسط تكلفة الشحن عند **20 BRL** للطلب الواحد، وتشكل مصاريف الشحن عبئاً مالياً إضافياً قد يؤثر على قرار العميل بإتمام عملية الشراء (Cart Abandonment).

### ⚖️ 3.3 Product Price vs. Freight Value
* **📊 المخطط البياني:** `Scatter Plot`
* **📁 المعاينة المرئية:**
![Price vs Freight](./images/price_vs_freight.png)
* **💡 Operational Insight:** يظهر المخطط عدم وجود علاقة خطية مباشرة بين سعر المنتج وتكلفة شحنه، حيث ترتبط تكاليف الشحن بأبعاد المنتج ووزنه الجغرافي وليس بقيمته المادية.

### 📦 3.4 Product Volumetrics vs. Freight Cost
* **📊 المخطط البياني:** `Scatter Plot with Regression Line`
* **📁 المعاينة المرئية:**
![Volume vs Freight](./images/volume_vs_freight.png)
* **💡 Operational Insight:** تكشف العلاقة الطردية القوية أن حجم المنتج (`product_volume`) هو المحرك الأساسي لارتفاع أسعار الشحن، مما يتطلب استراتيجيات تعبئة وتغليف أكثر كفاءة لتقليل التكلفة الحجمية.

---

## 📌 4) Product & Category Intelligence

### 🏆 4.1 Top Performing Product Categories
* **📊 المخطط البياني:** `Horizontal Bar Chart`
* **📁 المعاينة المرئية:**
![Top Categories](./images/top_categories.png)
* **💡 Operational Insight:** يثبت المخطط صحة مبدأ باريتو (Pareto Principle)، حيث تسيطر 3 فئات رئيسية فقط (`bed_bath_table`, `health_beauty`, `sports_leisure`) على ما يقرب من **60%** من حجم المبيعات الإجمالي للمنصة.

### 💵 4.2 Category Revenue Contribution
* **📊 المخطط البياني:** `Treemap / Stacked Bar Chart`
* **📁 المعاينة المرئية:**
![Category Revenue](./images/category_revenue.png)
* **💡 Operational Insight:** تتربع فئة `bed_bath_table` على رأس قائمة الفئات الأكثر توليداً للإيرادات، مما يجعلها النواة الأساسية للأعمال الاستراتيجية للمنصة ومحور حملات التسويق الكبرى.

### ⚖️ 4.3 Product Physical Weight Distribution
* **📊 المخطط البياني:** `Log-scaled Histogram`
* **📁 المعاينة المرئية:**
![Product Weight](./images/product_weight.png)
* **💡 Operational Insight:** الغالبية العظمى من المنتجات المباعة تزن أقل من **2 كيلوجرام**، وهو ما يسهل عمليات المعالجة اللوجستية والتخزين السريع في المستودعات (Micro-Fulfillment).

---

## 📌 5) Geospatial & Demographic Analysis

### 🏙️ 5.1 Top Order-Generating Cities
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**
![Top Cities](./images/top_cities.png)
* **💡 Operational Insight:** تظهر مدينة **São Paulo** كأضخم سوق استهلاكي للمنصة بفارق شاسع عن بقية المدن البرازيلية الأخرى، مما يجعلها المركز الرئيسي للعمليات التشغيلية.

### 🗺️ 5.2 Regional Customer Density by State
* **📊 المخطط البياني:** `Choropleth Map / Geospatial Plot`
* **📁 المعاينة المرئية:**
![Customer Distribution](./images/customer_state_distribution.png)
* **💡 Operational Insight:** تتركز **70%** من الطلبات الاستهلاكية في المثلث التجاري للبرازيل المكون من ولايات (SP, MG, RJ)، مما يعكس الفجوة الكبيرة في التوزيع الجغرافي بين الجنوب الشرقي والولايات الشمالية والطرفية.

### 🏭 5.3 Merchant/Seller Geographical Cluster
* **📊 المخطط البياني:** `Scatter Density / Geo-Plot`
* **📁 المعاينة المرئية:**
![Seller Distribution](./images/seller_distribution.png)
* **💡 Operational Insight:** يتطابق توزيع البائعين مع توزيع المشترين، حيث يتمركز أغلب الموردين في ولاية **SP**، مما يمنح ميزة لوجستية محلية لهذه المنطقة ويصعّب عمليات الشحن للمناطق البعيدة.

---

## 📌 6) Logistics & Delivery Analytics

### 🚚 6.1 Total Delivery Lead Time Distribution
* **📊 المخطط البياني:** `Histogram with Median Line`
* **📁 المعاينة المرئية:**
![Delivery Time](./images/delivery_time.png)
* **💡 Operational Insight:** يستغرق متوسط زمن التوصيل الفعلي **12 يوماً**، وهي فترة طويلة نسبياً في معايير التجارة الإلكترونية الحديثة وتشكل نقطة ضعف أساسية في تجربة المستخدم.

### 🚨 6.2 Variance of Freight Delays
* **📊 المخطط البياني:** `Bar Plot`
* **📁 المعاينة المرئية:**
![Delivery Delay](./images/delivery_delay.png)
* **💡 Operational Insight:** يوضح المخطط حجم وعدد الأيام التي تتجاوز فيها الشحنات الموعد المتوقع للتسليم، وهي البيانات المستخدمة كمدخلات رئيسية لبناء نظام الإنذار المبكر (Early Warning System).

### 🗺️ 6.3 State-wise Delivery Latency Breakdown
* **📊 المخطط البياني:** `Box Plot (Sorted by Median)`
* **📁 المعاينة المرئية:**
![Delivery by State](./images/delivery_by_state.png)
* **💡 Operational Insight:** يكشف المخطط تبايناً حاداً؛ حيث يتم التوصيل في ولاية SP خلال أيام معدودة، بينما يتجاوز وسيط التوصيل حاجز الـ **20 يوماً** في الولايات الشمالية والنائية، مما يؤكد الحاجة لمراكز توزيع إقليمية مصغرة.

---

## 📌 7) Customer Sentiment & Experience

### ⭐ 7.1 Review Score Frequency
* **📊 المخطط البياني:** `Categorical Bar Chart`
* **📁 المعاينة المرئية:**
![Review Score](./images/review_score_distribution.png)
* **💡 Operational Insight:** على الرغم من المشكلات اللوجستية، فإن تقييم **5 نجوم** هو الأكثر تكراراً، مما يدل على رضا العملاء عن جودة المنتجات نفسها عندما تصل في ظروف سليمة.

### 📉 7.2 Correlation: Shipping Delay vs. Review Score
* **📊 المخطط البياني:** `Bivariate Heatmap / Box Plot`
* **📁 المعاينة المرئية:**
![Review vs Delay](./images/review_vs_delay.png)
* **💡 Operational Insight:** تظهر طردية العلاقة بشكل قاطع؛ فكلما زادت أيام التأخير عن الموعد الموعود، تضاعفت احتمالية هبوط التقييم إلى **نجمة واحدة أو نجمتين**، مما يثبت أن اللوجستيات هي المحرك الأول لسمعة المنصة.

### 📝 7.3 Review Text Length Distribution
* **📊 المخطط البياني:** `Histogram`
* **📁 المعاينة المرئية:**
![Review Text Length](./images/review_text_length.png)
* **💡 Operational Insight:** يثبت التحليل أن العملاء الذين يتركون تقييمات سلبية (1-Star) يكتبون نصوصاً أطول وبشرح تفصيلي للمشكلة مقارنة بأصحاب التقييمات الإيجابية، مما يجعل هذه النصوص منجماً لعمليات تحليل المشاعر (Sentiment Analysis).

---

## 🏁 Summary Matrix
يغطي هذا المعرض **20 مخططاً بيانياً** متكاملاً تم ربطها برمجياً بخط معالجة البيانات (Data Pipeline)، وهي توفر مرجعاً بصرياً ممتازاً لأي عرض تقديمي (Presentation) أو مناقشة فنية للمشروع.
