# NYC Taxi Trip Data Analysis

## 📌 Objective
This project analyzes NYC taxi trip data to uncover patterns in trip demand, temporal trends, geographic hotspots, and tipping behavior.

---
## Dataset is not included due to size


## 📊 Dataset
- Source: NYC Taxi Trip Data
- Size: ~83,000 trips
- Features:
  - Trip distance
  - Fare amount
  - Pickup & dropoff time
  - Location IDs
  - Payment type
  - Tip amount

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

## 📈 Key Analyses

### 1. Trips by Hour
- Peak demand at **11 AM (~5,769 trips)**
- Demand rises after 6 AM and declines after 8 PM

👉 Insight: Strong mid-morning and daytime demand driven by commuting and business activity.

---

### 2. Trips by Weekday
- Highest demand on **Friday (~14,292 trips)**
- Lowest demand on Sunday

👉 Insight: Taxi usage increases toward the end of the workweek.

---

### 3. Geographic Distribution
- Trips are highly concentrated in a few pickup and dropoff zones

👉 Insight: Indicates strong urban hubs and travel corridors.

---

### 4. Payment Type Distribution
- Credit card: ~58%
- Cash: ~42%
- Others: <1%

👉 Insight: Digital payments dominate taxi transactions.

---

### 5. Tip Behavior (Credit Card Only)
- Most tips fall between **10%–30%**
- Peak around **15%–25%**
- Many zero-tip cases exist

👉 Insight: Tipping follows consistent social norms.

---

### 6. Fare vs Distance
- Strong positive correlation
- Higher variance for longer trips

👉 Insight: Pricing is distance-based but influenced by other factors (traffic, route, surcharges).

---

### 7. Heatmap (Weekday × Hour)
- Peak demand during weekday daytime hours
- Friday consistently high, Sunday lowest

👉 Insight: Demand depends on both time and weekday simultaneously.

---

## 🧠 Key Takeaways
- Demand peaks during mid-morning and weekdays
- Taxi usage is geographically concentrated
- Payment behavior is dominated by credit cards
- Tipping follows predictable patterns

---

## ⚠️ Limitations
- Location IDs are not mapped to actual geographic zones
- Threshold-based cleaning may remove valid extreme trips
- Dataset is a sample and may not represent all NYC trips

---

## 🚀 Future Work
- Map locations to real NYC zones
- Build demand forecasting model
- Analyze surge pricing and driver earnings

---

## 🛠️ Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn