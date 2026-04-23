![Result](outputs/figures/fare_by_hour.png)

---

# 🚕 NYC Taxi Demand Analysis & Driver Allocation Optimization

## 📌 Project Overview
This project analyzes NYC taxi trip data to uncover demand patterns, identify inefficiencies in driver allocation, and provide actionable insights to improve operational performance.

A reproducible data pipeline was built to clean, transform, and analyze the dataset, simulating a real-world data workflow.

---

## 🎯 Business Problem
How can taxi companies better align driver supply with passenger demand to reduce idle time and maximize revenue?

---

## 📂 Dataset
- Source: NYC Taxi Trip Data  
- Size: ~83,000 trips  
- Features:
  - Trip distance  
  - Fare amount  
  - Pickup & dropoff timestamps  
  - Location IDs  
  - Payment type  
  - Tip amount  

---

## ⚙️ Project Structure

nyc-taxi-project/  
├── data/  
│   ├── raw/  
│   └── processed/  
├── docs/  
│   ├── trip_data_dictionary.pdf  
│   └── eda.pdf  
├── notebooks/  
│   └── eda.ipynb  
├── outputs/  
│   └── figures/  
│       └── fare_by_hour.png  
├── scripts/  
│   ├── clean_data.py  
│   ├── transform.py  
│   └── analysis.py  
├── README.md  
└── requirements.txt  

---

## 🔄 Data Pipeline

Raw Data → Cleaning → Transformation → Analysis → Visualization  

---

### 🧹 1. Data Cleaning (`clean_data.py`)
- Removed missing and invalid records  
- Filtered unrealistic values:
  - trip_distance > 0  
  - fare_amount > 0  
- Removed outliers:
  - trip_distance ≤ 100  
  - fare_amount ≤ 500  

👉 Result: Improved data reliability and reduced noise for analysis  

---

### 🔧 2. Data Transformation (`transform.py`)
- Parsed datetime fields  
- Extracted features:
  - pickup_hour  
  - trip_duration (minutes)  
- Filtered unrealistic trips:
  - duration > 0  
  - duration ≤ 300  

👉 Result: Created structured features for time-based analysis  

---

### 📊 3. Analysis & Visualization (`analysis.py`)
- Aggregated demand by hour  
- Computed average fare trends  
- Generated visualizations for insight communication  

---

## 🧮 SQL Analysis (Added for scalability)

```sql
SELECT 
    EXTRACT(HOUR FROM pickup_datetime) AS hour,
    COUNT(*) AS trip_count
FROM trips
GROUP BY hour
ORDER BY trip_count DESC;
```

---

## 🧹 Data Cleaning
Data quality issues were addressed through:

- Removing invalid values:
  - Negative fares  
  - Zero or negative trip distance  
  - Zero or negative duration  

- Filtering extreme outliers:
  - Distance > 50 miles  
  - Duration > 180 minutes  
  - Fare > $200  

This significantly improved statistical stability and removed unrealistic records.

---

## 📈 Key Analyses & Insights

### 1️⃣ Peak Demand Analysis
- Demand increases after 6 AM
- Peak demand observed around late morning and early afternoon
### 👉 Insight: Driver supply should increase during daytime hours to meet demand

### 2️⃣ Weekly Demand Trends
- Highest demand on Friday
- Lowest demand on Sunday
### 👉 Insight: Demand is strongly tied to workweek patterns

### 3️⃣ Geographic Concentration
- Trips are concentrated in a few key zones
### 👉 Insight: Indicates inefficient driver distribution across regions

### 4️⃣ Payment Behavior
- Credit card: ~58%
- Cash: ~42%
### 👉 Insight: Digital payment dominates → opportunity for targeted promotions

### 5️⃣ Tip Behavior
- Majority of tips between 10%–30%
- Many zero-tip cases
### 👉 Insight: Tipping patterns are consistent but vary by trip context

### 6️⃣ Fare vs Distance
- Strong positive correlation
- Increased variance for longer trips
### 👉 Insight: Pricing influenced by both distance and external factors (traffic, surcharges)

### 7️⃣ Temporal Heatmap
- Peak demand during weekday daytime
- Friday consistently high
### 👉 Insight: Demand is a function of both time and weekday

---

## 🧠 Key Takeaways
- 🚕 Demand is highly time-dependent (peak hours)
- 📍 Geographic imbalance suggests inefficient driver allocation
- 💳 Payment behavior indicates shift toward digital transactions
- 📊 Data-driven strategies can improve revenue and efficiency

---

## 🚀 Business Recommendations
- Implement dynamic driver allocation during peak hours
- Redistribute drivers to high-demand zones
- Introduce surge pricing strategies during high-demand periods
- Use historical data to build predictive demand models

---

## ▶️ How to Run

From the project root directory:

```bash
pip install -r requirements.txt

python3 scripts/clean_data.py
python3 scripts/transform.py
python3 scripts/analysis.py
```

---

## 🛠️ Tools Used
Python
Pandas
NumPy
Matplotlib
Seaborn
SQL

---

## ⚠️ Limitations
Location IDs are not mapped to actual geographic zones
Threshold-based cleaning may remove valid extreme trips
Dataset is a sample and may not represent all NYC trips

---

## 🚀 Future Work
Map locations to real NYC zones
Build demand forecasting model
Add dashboard (Streamlit / Tableau)
Extend pipeline to larger datasets (Spark)

---

## 📄 Additional Notes
Detailed exploratory analysis is available in docs/eda.pdf.

---

## 👤 Author
Shengqiang Huang
UCLA Data Theory
