# 📦 Olist Brazilian E‑Commerce — End-to-End Analytics & Enterprise Insights

[![Python](https://shields.io)](https://python.org)
[![Pandas](https://shields.io)](https://pydata.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Contributions-Welcome](https://shields.io)](CONTRIBUTING.md)

تحليل شامل لمنصة Olist البرازيلية باستخدام Python. يتضمن المشروع بناء نموذج بيانات موحد (Data Model)، وهندسة الميزات (Feature Engineering)، واستخراج رؤى تشغيلية وتجارية لرفع كفاءة سلاسل الإمداد والمبيعات.

---

## 📌 1) Executive Summary & Key Insights

لإبراز القيمة التجارية للمشروع فوراً أمام مسؤولي التوظيف، إليك ملخص سريع لأهم النتائج التشغيلية المستخرجة:

* **Revenue Drivers:** تمثل البطاقات الائتمانية **75%** من إجمالي وسائل الدفع، ومتوسط قيمة الطلب الواحد تبلغ **180 BRL**.
* **Logistics Bottleneck:** يستغرق متوسط زمن التوصيل **12 يوماً**. أثبت التحليل الإحصائي وجود علاقة طردية قوية بين تأخر الشحن وانخفاض تقييمات العملاء (Reviews) إلى نجمة واحدة.
* **Top Categories:** تتركز 60% من المبيعات في 3 فئات رئيسية: *bed_bath_table, health_beauty, sports_leisure*.

---

## 🎯 2) Project Objectives

يهدف المشروع إلى حل مشكلات تجارية حقيقية في قطاع التجارة الإلكترونية عبر:
* **Data Architecture:** بناء Data Model علاقي موحد يربط 9 جداول منفصلة بكفاءة عالية.
* **Customer Journey Mapping:** تتبع رحلة الطلب بالدقيقة من لحظة الشراء، الدفع، التجهيز، الشحن، وحتى التوصيل والتقييم.
* **Supply Chain Optimization:** تحديد الولايات والمدن التي تعاني من اختناقات تشغيلية وتأخر في التوصيل.
* **Actionable Insights:** تحويل البيانات الصماء إلى توصيات استراتيجية تدعم صناع القرار.

---

## 🗂 3) Dataset Architecture & Data Model

البيانات الأصلية متاحة على منصة Kaggle: 
🔗 [Brazilian E-Commerce Public Dataset by Olist](https://kaggle.com)

تم ربط الجداول التالية لبناء المستودع التحليلي:
* `orders` & `order_items` (العمليات الأساسية)
* `products` & `category_name_translation` (بيانات المنتجات)
* `customers` & `sellers` & `geolocation` (البيانات الجغرافية)
* `payments` & `reviews` (المالية وتقييم الجودة)

> 💡 للاطلاع على المخطط التفصيلي والعلاقات بين الجداول (ERD)، يرجى زيارة ملف [data_model.md](data_model.md).

---

## 🛠 4) Technical Stack & Tools

* **Core Language:** Python (v3.9+)
* **Data Manipulation:** Pandas, NumPy
* **Geospatial Analysis:** GeoPandas (لتحليل التوزيع الجغرافي للمبيعات في البرازيل)
* **Data Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebooks & Modular Python Scripts (`.py`)

---

## 📁 5) Project Structure

تم تنظيم المشروع بأسلوب المستودعات البرمجية الاحترافية (Production-Grade Structure):

```text
Olist-Ecommerce-Analytics/
│
├── README.md               # واجهة المشروع الرئيسية
├── insights.md             # التقرير التحليلي المفصل والتوصيات التجارية
├── visuals.md              # معرض الرسومات البيانية والتوضيحية
├── data_model.md           # توثيق الـ Data Model والعلاقات
├── methodology.md          # منهجية العمل وتجهيز البيانات
│
├── data/
│   └── README.md           # طريقة وضع ملفات الداتا المفصلة
│
├── images/
│   └── (all generated charts & plots)
│
├── notebooks/
│   └── olist_analysis.ipynb # كشكول العمليات الاستكشافية EDA
│
└── scripts/                # سكريبتات برمجية منظمة وقابلة لإعادة الاستخدام
    ├── data_loading.py     # استدعاء البيانات ومعالجة أنواعها
    ├── data_merging.py     # دمج الجداول وبناء النموذج الموحد
    ├── eda_analysis.py     # العمليات الإحصائية واستخراج المؤشرات
    └── visualization.py    # توليد وحفظ الرسومات البيانية تلقائياً
```

---

## 🔍 6) Analytics Methodology

يتتبع المشروع منهجية علمية صارمة في تحليل البيانات:
1. **Data Cleaning:** معالجة القيم المفقودة (Missing Values)، دمج التواريخ، وحذف السجلات المكررة.
2. **Feature Engineering:** حساب أوقات التوصيل الفعلية مقابل المتوقعة، واستخراج فترات التأخير.
3. **Exploratory Data Analysis (EDA):** دراسة سلوك المستهلك الإحصائي وتوزيعات الشحن والقيم التشغيلية.
4. **Visualizations:** إنتاج أكثر من 20 مخططاً بيانياً (Histograms, Pie Charts, Time-Series Plots).

---

## ▶️ 7) How to Run & Reproduce

اتبع الخطوات التالية لتشغيل المشروع محلياً على جهازك:

### 1. استنساخ المستودع (Clone the Repository)
```bash
git clone github.com
cd Olist-Ecommerce-Analytics
```

### 2. تحميل البيانات
* قم بتنزيل ملفات البيانات من [Kaggle](https://kaggle.com).
* فك الضغط عن الملفات وضعها داخل مجلد `data/`.

### 3. تشغيل التحليل عبر السكريبت الرئيسي
يمكنك تشغيل خط الأنابيب (Pipeline) بالكامل واستخراج النتائج عبر الـ Terminal:
```bash
python -c "
from scripts.data_loading import load_data
from scripts.data_merging import build_orders_full
from scripts.eda_analysis import run_full_eda
from scripts.visualization import generate_all_plots

print('⚙️ Processing Olist Data Pipeline...')
# تشغيل العمليات بالتتابع
"
```
*(أو قم بفتح المفكرة `notebooks/olist_analysis.ipynb` لتتبع التحليل خطوة بخطوة).*

---

## # 📬 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/amir-ayman-664513103/" target="_blank">
    <img src="https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/amirayman20" target="_blank">
    <img src="https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>
