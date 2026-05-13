# 🧩 Olist E‑Commerce — Data Model & Schema Documentation

يشرح هذا الملف التصميم الهيكلي لنموذج البيانات (Data Model) المستخدم في المستودع التحليلي لمشروع **Olist**. يتضمن التوثيق المخطط العلاقتي، وتوصيف الجداول، وتحديد المفاتيح الأساسية والأجنبية لضمان سلامة البيانات (Referential Integrity).

---

## 🗺️ 1) Entity‑Relationship Diagram (ERD)

المخطط التالي يوضح البنية العلاقتية وقواعد العمل (Business Logic) التي تربط المكونات التشغيلية للمنصة:

```text
  [Customers] (1) ───► (🔀) [Orders] (1) ───► (1) [Order Reviews]
                                 │
                                 ▼ (1)
                               (🔀)
                           [Order Items]
                                 ▲ (🔀)
                                 │ (1)
                             [Products]
```

### 💡 قواعد الربط التشغيلي (Business Logic Rules):
* **Customers to Orders `(1:N)`:** يمكن للعميل الواحد إجراء طلب واحد أو عدة طلبات، بينما ينتمي الطلب لعميل واحد فقط.
* **Orders to Order Items `(1:N)`:** يحتوي الطلب الواحد على عنصر (منتج) واحد أو أكثر في سلة الشراء.
* **Products to Order Items `(1:N)`:** يمكن أن يتكرر المنتج الواحد في عدة طلبات وعمليات شراء مختلفة.
* **Orders to Order Reviews `(1:1)`:** يمتلك كل طلب كود تقييم جودة وتجربة مستخدم واحد فريد ملحق به.

---

## 🧱 2) Relational Schema & Data Dictionary

### 📑 2.1 Customers Table (`customers`)
يحتوي على البيانات الديموغرافية والتعريفية للمشترين.


| اسم الحقل | نوع المفتاح | الوصف التجريي والتقني |
| :--- | :--- | :--- |
| `customer_id` | **PK** | المعرّف الفريد للعملية التشغيلية (يرتبط بالطلبات) |
| `customer_unique_id` | Unique ID | المعرّف الحقيقي والدائم للعميل (يستخدم لحساب الـ Retention) |
| `customer_city` | Dimension | المدينة الجغرافية المسجل بها حساب العميل |
| `customer_state` | Dimension | الولاية البرازيلية التابع لها العميل |

* **🔗 Linkage:** `customers.customer_id` ───► `orders.customer_id`

---

### 📑 2.2 Orders Table (`orders`)
الجدول المحوري للعمليات (Fact Table) الذي يتتبع دورة حياة الطلبات.


| اسم الحقل | نوع المفتاح | الوصف التجاري والتقني |
| :--- | :--- | :--- |
| `order_id` | **PK** | المعرّف الفريد لكل حركية شراء على المنصة |
| `customer_id` | **FK** | يشير إلى جدول العملاء لمعرفة صاحب الطلب |
| `order_status` | Status | الحالة الحالية للطلب (delivered, canceled, shipped...) |
| `order_purchase_timestamp` | Timestamp | الطابع الزمني اللحظي لإتمام العميل لعملية الشراء |
| `order_delivered_customer_date` | Timestamp | التاريخ الفعلي لاستلام العميل للشحنة من شركة النقل |

* **🔗 Linkage:** 
  * `orders.customer_id` ◄─── `customers.customer_id`
  * `orders.order_id` ───► `order_items.order_id`
  * `orders.order_id` ───► `order_reviews.order_id`

---

### 📑 2.3 Order Items Table (`order_items`)
جدول تفصيلي يربط العمليات بالمنتجات المبيعة واللوجستيات المالية.


| اسم الحقل | نوع المفتاح | الوصف التجاري والتقني |
| :--- | :--- | :--- |
| `order_id` | **FK** | يشير إلى الطلب الرئيسي التابع له هذا العنصر |
| `order_item_id` | Composite | الرقم التسلسلي للعنصر داخل نفس السلة الإعلانية |
| `product_id` | **FK** | يشير إلى كود المنتج التابع لجدول المنتجات |
| `price` | Metric | السعر المادي الصافي للمنتج بالعملة المحلية (BRL) |
| `freight_value` | Metric | تكلفة الشحن واللوجستيات المفروضة على هذا العنصر |

* **🔗 Linkage:**
  * `order_items.order_id` ◄─── `orders.order_id`
  * `order_items.product_id` ───► `products.product_id`

---

### 📑 2.4 Products Table (`products`)
كتالوج المنتجات وخصائصها الفيزيائية.


| اسم الحقل | نوع المفتاح | الوصف التجاري والتقني |
| :--- | :--- | :--- |
| `product_id` | **PK** | المعرّف الفريد للمنتج داخل الكتالوج |
| `product_category_name` | Dimension | اسم الفئة التجارية التابع لها المنتج (بالبرتغالية الأصلية) |
| `product_weight_g` | Feature | الوزن الصافي للمنتج بالجرام (محدد أساسي للشحن المادي) |
| `product_volume_cm3` | Feature | الحجم التكعيبي للمنتج بالسنتيمتر المكعب (حساب السعة الحجمية) |

* **🔗 Linkage:** `products.product_id` ◄─── `order_items.product_id`

---

### 📑 2.5 Order Reviews Table (`order_reviews`)
مستودع قياس جودة الخدمة وتجربة ورضا العملاء (Sentiment Baseline).


| اسم الحقل | نوع المفتاح | الوصف التجاري والتقني |
| :--- | :--- | :--- |
| `review_id` | **PK** | المعرّف الفريد لاستمارة التقييم المستلمة |
| `order_id` | **FK** | يشير إلى الطلب محل التقييم |
| `review_score` | Metric | تقييم العميل لتجربته الكلية على مقياس إحصائي من 1 إلى 5 |
| `review_comment_title` | Text | العنوان الرئيسي المكتوب للشكوى أو الثناء |
| `review_comment_message` | Text | النص التفصيلي للمراجعة (المستخدم في معالجة اللغات الطبيعية NLP) |

* **🔗 Linkage:** `order_reviews.order_id` ◄─── `orders.order_id`

---

## 🔗 3) Summary of Model Relationships


| الجدول المصدر (Source) | الجدول الهدف (Target) | نوع العلاقة (Type) | حقل الربط المشترك |
| :--- | :--- | :--- | :--- |
| `customers` | `orders` | **One‑to‑Many `(1:N)`** | `customer_id` |
| `orders` | `order_items` | **One‑to‑Many `(1:N)`** | `order_id` |
| `products` | `order_items` | **One‑to‑Many `(1:N)`** | `product_id` |
| `orders` | `order_reviews` | **One‑to-One `(1:1)`** | `order_id` |

---

## 📝 4) Technical Implementation Notes

* **Data Denormalization:** تم استخدام نموذج النجمة المعدّل (Modified Star-Schema) أثناء تنظيف البيانات ودمجها برمجياً عبر ملف `data_merging.py` لتسريع الجداول وتحسين أداء العمليات الاستكشافية EDA والرسومات البيانية.
* **Feature Engineering:** تم اشتقاق حقول جديدة تعتمد على خصائص الأبعاد المتاحة مثل حساب الحجم التكعيبي للمنتج وضبط فترات التأخير الزمني بالدقائق والساعات دعمًا لدقة التحليل التجاري والتشغيلي.
