# 🎨 Olist E‑Commerce — Full Visualizations Gallery

يحتوي هذا الملف على معرض الرسومات البيانية الكامل التي تم إنتاجها وحفظها تلقائياً أثناء مرحلة التحليل الاستكشافي (EDA). تم تصميم هذه المخططات لترجمة العلاقات الإحصائية المعقدة إلى مؤشرات مرئية سهلة الفهم لدعم اتخاذ القرار التجاري والتشغيلي.

---

## 📌 1) Order & Time-Series Visualizations

### 📊 1.1 Order Status Distribution
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**

![Order Status](https://githubusercontent.com)

* **💡 Operational Insight:** أكثر من **96%** من الطلبات تم توصيلها بنجاح إلى العملاء، مما يعكس استقراراً في البنية التشغيلية العامة للمنصة وقدرتها على إتمام دورة الطلب.

### 📈 1.2 Monthly Orders Trend
* **📊 المخطط البياني:** `Time-Series Line Chart`
* **📁 المعاينة المرئية:**

![Monthly Trend](https://githubusercontent.com)

* **💡 Operational Insight:** يوضح المخطط اتجاهاً تصاعدياً قوياً ومستقراً (Strong Upward Trend) في حجم الطلبات الإجمالي عبر الأشهر، مما يؤكد نمو الحصة السوقية للمنصة وزيادة اعتماد المستهلكين عليها.

### 📉 1.3 Daily Demand Pattern
* **📊 المخطط البياني:** `Cyclical Line Chart`
* **📁 المعاينة المرئية:**

![Daily Pattern](https://githubusercontent.com)

* **💡 Operational Insight:** تتركز ذروة الطلبات بشكل واضح في الفترة الممتدة من يوم 5 إلى يوم 25 من كل شهر، وهو سلوك شرائي مرتبط بدورات استلام الرواتب الشهرية وتوفر السيولة لدى المستهلكين.

---

## 📌 2) Financial & Price Visualizations

### 💰 2.1 Distribution of Average Order Value (AOV)
* **📊 المخطط البياني:** `Right-Skewed Histogram`
* **📁 المعاينة المرئية:**

![Order Value](https://githubusercontent.com)

* **💡 Operational Insight:** يبلغ متوسط قيمة الطلب **180 BRL**، بينما يقل الوسيط (Median) عن ذلك بشكل ملحوظ، مما يؤكد تركز معظم المبيعات في المنتجات منخفضة ومتوسطة السعر مع وجود شريحة Premium تحرك الإيرادات الإجمالية.

### 💵 2.2 Price Distribution Analysis
* **📊 المخطط البياني:** `Price Distribution Plot`
* **📁 المعاينة المرئية:**

![Price Distribution](https://githubusercontent.com)

* **💡 Operational Insight:** تحليل توزيع الأسعار يوضح النطاقات السعرية الأكثر مبيعاً ونسبة المنتجات الفاخرة المتاحة على المنصة لتحديد الفئات السعرية المستهدفة بدقة.

### 📈 2.3 Price Range Distribution Percentages
* **📊 المخطط البياني:** `Distribution Percentage Chart`
* **📁 المعاينة المرئية:**

![Price Range](https://githubusercontent.com)

* **💡 Operational Insight:** يوفر تفصيلاً مئوياً لشرائح الأسعار المختلفة، مما يساعد في وضع استراتيجيات التسعير وتحديد هوامش الربح التنافسية.

---

## 📌 3) Freight & Logistics Metrics

### 🚚 3.1 Freight Cost Variance
* **📊 المخطط البياني:** `Density Plot`
* **📁 المعاينة المرئية:**

![Freight Value](https://githubusercontent.com)

* **💡 Operational Insight:** يتمركز متوسط تكلفة الشحن عند **20 BRL** للطلب الواحد، وتشكل مصاريف الشحن عبئاً مالياً إضافياً قد يؤثر على قرار العميل بإتمام عملية الشراء (Cart Abandonment).

### 📦 3.2 Product Volumetrics vs. Weight
* **📊 المخطط البياني:** `Scatter Plot`
* **📁 المعاينة المرئية:**

![Volume vs Weight](https://githubusercontent.com)

* **💡 Operational Insight:** يكشف المخطط العلاقة بين وزن المنتج وحجمه الفعلي، وهي المحدد الأساسي الذي تعتمد عليه شركات اللوجستيات لحساب تكاليف الشحن الحجمي.

### 🚨 3.3 Actual vs. Estimated Delivery Comparison
* **📊 المخطط البياني:** `Comparison Plot`
* **📁 المعاينة المرئية:**

![Actual vs Estimated](https://githubusercontent.com)

* **💡 Operational Insight:** يقارن بين أوقات التوصيل الفعلية والمواعيد المتوقعة الموعود بها للعميل لتحديد نسب الكفاءة والقصور التشغيلي لدى مزودي خدمات الشحن.

### ⏳ 3.4 Delivery Time Histogram
* **📊 المخطط البياني:** `Delivery Time Histogram`
* **📁 المعاينة المرئية:**

![Delivery Time Histogram](https://githubusercontent.com)

* **💡 Operational Insight:** يحلل التوزيع التكراري للفترات الزمنية الفعلية المستغرقة في الشحن من المصدر للمستهلك.

### ⏳ 3.5 Estimated Delivery Time Distribution
* **📊 المخطط البياني:** `Estimated Time Histogram`
* **📁 المعاينة المرئية:**

![Estimated Delivery Time](https://githubusercontent.com)

* **💡 Operational Insight:** يوضح توزيع الفترات الزمنية المتوقعة للشحن التي تظهر للمستخدم قبل إتمام الشراء، ومدى دقتها وتأثيرها على توقعات تجربة المستخدم.

### ⏱️ 3.6 Delivery Delay Variance
* **📊 المخطط البياني:** `Delay Histogram`
* **📁 المعاينة المرئية:**

![Delivery Delay](https://githubusercontent.com)

* **💡 Operational Insight:** يوضح المخطط حجم وعدد الأيام التي تتجاوز فيها الشحنات الموعد المتوقع للتسليم، وهي البيانات المستخدمة كمدخلات رئيسية لبناء نظام الإنذار المبكر (Early Warning System).

### 🏁 3.7 On-Time vs. Late Delivery Rate
* **📊 المخطط البياني:** `Rate Comparison Chart`
* **📁 المعاينة المرئية:**

![On Time vs Late](https://githubusercontent.com)

* **💡 Operational Insight:** يقدم نسبة مئوية واضحة للطلبات التي وصلت في موعدها المحدد تماماً مقابل الطلبات المتأخرة، وهو مؤشر الأداء الرئيسي (KPI) لتقييم كفاءة سلاسل الإمداد.

---

## 📌 4) Product & Category Intelligence

### 🏆 4.1 Top Performing Product Categories
* **📊 المخطط البياني:** `Horizontal Bar Chart`
* **📁 المعاينة المرئية:**

![Top Categories](https://githubusercontent.com)

* **💡 Operational Insight:** يثبت المخطط صحة مبدأ باريتو (Pareto Principle)، حيث تسيطر فئات رئيسية محددة على حجم المبيعات الإجمالي للمنصة.

### 🛒 4.2 Top Products by Orders & Quantity Sold
* **📊 المخطط البياني:** `Volume Charts`
* **📁 المعاينة المرئية:**

![Products by Orders](https://githubusercontent.com)

![Products by Quantity](https://githubusercontent.com)

* **💡 Operational Insight:** يوضح تفصيلاً دقيقاً لأكثر المنتجات تكراراً في سلات المشتريات والكميات الفعلية المباعة منها لتأمين مستويات المخزون المناسبة.

### 💵 4.3 Top Products by Revenue & Best Selling
* **📊 المخطط البياني:** `Revenue Charts`
* **📁 المعاينة المرئية:**

![Products by Revenue](https://githubusercontent.com)

![Top Selling](https://githubusercontent.com)

* **💡 Operational Insight:** يحدد المنتجات الأعلى توليداً للأرباح والإيرادات الإجمالية، والتي قد تختلف عن المنتجات الأكثر مبيعاً من حيث الكمية، مما يساعد في إعادة توجيه الحملات التسويقية الفاخرة.

---

## 📌 5) Geospatial & Operational Clustering

### 🗺️ 5.1 Regional Customer Density Map
* **📊 المخطط البياني:** `Geospatial Choropleth Map`
* **📁 المعاينة المرئية:**

![Customer Distribution](https://githubusercontent.com)

* **💡 Operational Insight:** تتركز الكتلة الاستهلاكية الكبرى في ولايات المثلث التجاري للبرازيل، مما يعكس الفجوة الكبيرة في التوزيع الجغرافي للطلب ويوجه خطط التوسع اللوجستي الإقليمي.

### 🏙️ 5.2 Top Customer Cities
* **📊 المخطط البياني:** `Bar Chart`
* **📁 المعاينة المرئية:**

![Top Cities](https://githubusercontent.com)

* **💡 Operational Insight:** يحدد المدن الأعلى طلباً وإيراداً لتخصيص خطوط شحن سريعة ومباشرة ومستودعات محلية مصغرة لخدمة هذه الكثافة السكانية المرتفعة.

### 📦 5.3 Single vs. Multi-Item Orders Analysis
* **📊 المخطط البياني:** `Order Composition Chart`
* **📁 المعاينة المرئية:**

![Order Composition](https://githubusercontent.com)

* **💡 Operational Insight:** يحلل سلوك العميل عند بناء السلة؛ هل يميل لشراء منتج واحد في الشحنة أم منتجات متعددة، وهو أساس ممتاز لتطوير استراتيجيات الـ Cross-selling.

---

## 📌 6) Customer Sentiment & Experience

### ⭐ 6.1 Review Score Frequency
* **📊 المخطط البياني:** `Categorical Bar Chart`
* **📁 المعاينة المرئية:**

![Review Score](https://githubusercontent.com)

* **💡 Operational Insight:** يوفر نظرة عامة على مدى رضا العملاء، حيث يظهر تقييم 5 نجوم كالأكثر تكراراً، مما يدل على جودة المنتجات المتاحة فور وصولها للعميل بسلام.

### 📉 6.2 Customer Evaluation Average
* **📊 المخطط البياني:** `Score Metrics`
* **📁 المعاينة المرئية:**

![Average Review Score](https://githubusercontent.com)

* **💡 Operational Insight:** يمثل خط الأساس لقياس جودة تجربة المستخدم العامة على المنصة ومراقبة تذبذب التقييمات عبر الفترات التشغيلية المختلفة.

### 🚨 6.3 Correlation: Shipping Delay vs. Review Score
* **📊 المخطط البياني:** `Bivariate Heatmap`
* **📁 المعاينة المرئية:**

![Review vs Delay](https://githubusercontent.com)

* **💡 Operational Insight:** تظهر طردية العلاقة بشكل قاطع؛ فكلما زادت أيام التأخير عن الموعد الموعود، تضاعفت احتمالية هبوط التقييم إلى نجمة واحدة أو نجمتين، مما يثبت أن اللوجستيات هي المحرك الأول لسمعة المنصة.
