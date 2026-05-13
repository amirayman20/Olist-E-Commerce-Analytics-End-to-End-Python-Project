  # 🧪 Olist E‑Commerce — Analytical Methodology & Data Pipeline

يوثق هذا الملف المنهجية العلمية والخطوات التقنية المتبعة في هندسة البيانات وتحليلها لمشروع **Olist**. تم تصميم مسار العمل بناءً على المعيار العالمي **CRISP-DM** (Cross-industry standard process for data mining) لضمان بناء مشروع تحليلي منظم، موثوق، وقابل لإعادة الإنتاج (Reproducible Data Pipeline).

---

## 🏗️ 1) Analytical Framework (CRISP-DM Workflow)

يتكون خط الأنابيب التحليلي (Data Pipeline) من 6 مراحل مترابطة تم تنفيذها برمجياً عبر مجلد `scripts/`:

```text
  [1. Business Understanding] ──► [2. Data Understanding] ──► [3. Data Preparation]
                                                                     │
  [6. Deployment & Report]    ◄── [5. Evaluation & Insights]  ◄── [4. Advanced EDA]
```

1. **Business Understanding:** تحديد مؤشرات الأداء اللوجستية والمالية (KPIs) لقطاع التجارة الإلكترونية.
2. **Data Understanding:** فحص 9 جداول علائقية واستكشاف أنواع الحقول والروابط بينها.
3. **Data Preparation:** تنظيف البيانات، ومعالجة القيم المفقودة، وبناء النموذج الموحد.
4. **Advanced EDA:** تطبيق الأساليب الإحصائية واستخراج الارتباطات وتوزيعات المؤشرات.
5. **Evaluation & Insights:** ترجمة الأنماط الإحصائية إلى توصيات استراتيجية قابلة للتنفيذ.
6. **Deployment & Report:** توثيق المستودع البرمجي وإنتاج معرض الرسومات التفاعلية.

---

## 🧹 2) Rigorous Data Cleaning & Preprocessing

تمت معالجة البيانات وتنظيفها عبر سكريبت `scripts/data_loading.py` لرفع مستوى جودة البيانات (Data Quality Score):

* **Deduplication:** فحص وإزالة كافة السجلات المكررة بالكامل على مستوى المعرّفات الفريدة (`order_id`, `customer_id`).
* **Datatype Standardisation:** تحويل الحقول النصية الخاصة بالتواريخ من صيغة Object/String إلى صيغة طوابع زمنية حقيقية (`datetime64[ns]`) لتمكين العمليات الحسابية الزمنية.
* **Missing Value Imputation Stratgy:** 
  * في جدول التقييمات (`order_reviews`): تم ملء نصوص التعليقات المفقودة بنص ناصع مثل `'No Review Written'` لمنع أخطاء الـ Parsing أثناء الـ EDA مع الإبقاء على التقييم الرقمي.
  * في التواريخ اللوجستية: تم استبعاد الطلبات ذات التواريخ الناقصة عند حساب الفروق التشغيلية الدقيقة لضمان عدم تشويه التوزيع الإحصائي.
* **Text Normalisation:** تحويل أسماء المدن والفئات التجارية إلى أحرف صغيرة (Lowercase) وتطهيرها من الرموز الخاصة لتوحيد عمليات التجميع (Aggregation).

---

## 🧱 3) Advanced Feature Engineering

تم اشتقاق ميزات ومؤشرات إحصائية جديدة (Derived Features) داخل سكريبت `scripts/data_merging.py` لتوفير أبعاد تحليلية أعمق للعمليات التجارية:

* **`delivery_days_actual`:** يحسب الوقت الفعلي المستغرق للتوصيل:
  $$\text{order\_delivered\_customer\_date} - \text{order\_purchase\_timestamp}$$
* **`delivery_days_estimated`:** يحسب فترة التوصيل التي وعدت بها المنصة العميل:
  $$\text{order\_estimated\_delivery\_date} - \text{order\_purchase\_timestamp}$$
* **`delivery_delay_days`:** يحسب صافي أيام التأخير التشغيلي (إذا كانت القيمة موجبة):
  $$\text{order\_delivered\_customer\_date} - \text{order\_estimated\_delivery\_date}$$
* **`is_late`:** مؤشر ثنائي البنية (Boolean Indicator: 0 أو 1) يتم تفعيله تلقائياً إذا تجاوز تاريخ التسليم الفعلي الموعد المتوقع، ويستخدم كركيزة أساسية لتحليل الـ Churn والتقييمات السلبية.
* **`product_volume_cm3`:** حساب الحجم الفيزيائي للمنتج لتمكين التحليل اللوجستي الحجمي:
  $$\text{length} \times \text{width} \times \text{height}$$

---

## 🔍 4) Exploratory Data Analysis (EDA) Target Axis

تمت هندسة العمليات الإحصائية في سكريبت `scripts/eda_analysis.py` لتركز على 4 محاور تشغيلية:

### 📦 4.1 Order Lifecycle & Velocity Analysis
* دراسة حجم الطلبات ومعدلات النمو الشهرية (MoM Growth Rate).
* تحليل الأنماط الموسمية (Seasonality) والنشاط الشرائي على مدار ساعات اليوم وأيام الأسبوع.

### 🚚 4.2 Logistics & Supply Chain Diagnostics
* تحليل التوزيع التكراري لأوقات الشحن ورصد الاختناقات الجغرافية.
* قياس مدى التزام شركات الشحن باتفاقية مستوى الخدمة (SLA).
* دراسة معامل الارتباط (Correlation) بين تأخر الشحنات وتدني تقييمات العملاء.

### 🛒 4.3 Product Intelligence & Revenue Drivers
* تطبيق تحليل باريتو (Pareto 80/20 Rule) لعزل الفئات القائدة للإيرادات.
* دراسة التوزيع الإحصائي للأسعار وتكلفة الشحن ومقارنة أوزان وأحجام السلع.

### 👥 4.4 Geospatial & Demographic Clustering
* رسم الخرائط الجغرافية لتحديد الكثافة الاستهلاكية للمشترين وتمركز الموردين (Sellers).
* تحديد المدن ذات الأولوية اللوجستية العالية لتوجيه استثمارات الشحن السريع.

---

## 🛠️ 5) Production Toolchain

* **Programming Language:** Python 3.9+
* **Data Engineering Libraries:** Pandas, NumPy
* **Statistical Visualization:** Matplotlib, Seaborn
* **Environment & Version Control:** Jupyter Notebooks, Git & GitHub Documentation
