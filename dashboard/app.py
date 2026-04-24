import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("data/processed/transformed_taxi.csv", low_memory=False)

# Prepare date features
df["pickup_parsed"] = pd.to_datetime(df["lpep_pickup_datetime"], errors="coerce")
df["pickup_weekday"] = df["pickup_parsed"].dt.day_name()

# Payment type mapping
payment_map = {
    1.0: "Credit card",
    2.0: "Cash",
    3.0: "No charge",
    4.0: "Dispute",
    5.0: "Unknown",
    6.0: "Voided trip",
}
df["payment_type_name"] = df["payment_type"].map(payment_map)

# Page title
st.title("🚕 NYC Taxi Dashboard")
st.write(
    "This dashboard explores taxi demand, revenue patterns, payment behavior, "
    "and fare-distance relationships."
)

# 1. Trip Count by Hour
st.header("Trip Count by Hour")
trip_count = df.groupby("pickup_hour").size()
st.line_chart(trip_count)

# 2. Revenue by Hour
st.header("Revenue by Hour")
revenue_by_hour = df.groupby("pickup_hour")["total_amount"].mean()
st.line_chart(revenue_by_hour)

# 3. Average Fare by Hour
st.header("Average Fare by Hour")
fare_by_hour = df.groupby("pickup_hour")["fare_amount"].mean()
st.line_chart(fare_by_hour)

# 4. Trips by Weekday
st.header("Trips by Weekday")

weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

trips_by_weekday = (
    df["pickup_weekday"]
    .value_counts()
    .reindex(weekday_order)
    .reset_index()
)

trips_by_weekday.columns = ["weekday", "trips"]

weekday_chart = alt.Chart(trips_by_weekday).mark_bar().encode(
    x=alt.X("weekday:N", sort=weekday_order, title="Weekday"),
    y=alt.Y("trips:Q", title="Number of Trips")
)

st.altair_chart(weekday_chart, use_container_width=True)

# 5. Top 10 Pickup Locations
st.header("Top 10 Pickup Locations")

top_pickup_locations = (
    df["PULocationID"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_pickup_locations.columns = ["pickup_location_id", "trips"]
top_pickup_locations["pickup_location_id"] = top_pickup_locations["pickup_location_id"].astype(str)

pickup_chart = alt.Chart(top_pickup_locations).mark_bar().encode(
    x=alt.X("trips:Q", title="Number of Trips"),
    y=alt.Y("pickup_location_id:N", sort="-x", title="Pickup Location ID")
)

st.altair_chart(pickup_chart, use_container_width=True)


# 6. Payment Type Distribution
st.header("Payment Type Distribution")
payment_counts = df["payment_type_name"].value_counts()

payment_df = payment_counts.reset_index()
payment_df.columns = ["payment_type", "trips"]

st.bar_chart(
    payment_df,
    x="payment_type",
    y="trips"
)

# 7. Tip by Payment Type
st.header("Tip by Payment Type")
st.write(
    "Note: cash tips are not fully captured in the dataset, so tip analysis is "
    "most reliable for credit card payments."
)

tip_by_payment = df.groupby("payment_type_name")["tip_amount"].mean()

tip_df = tip_by_payment.reset_index()
tip_df.columns = ["payment_type", "avg_tip"]

st.bar_chart(
    tip_df,
    x="payment_type",
    y="avg_tip"
)

# 8. Distance vs Fare
st.header("Distance vs Fare")

scatter_df = df[["trip_distance", "fare_amount"]].dropna()

# Sample data for cleaner visualization
if len(scatter_df) > 5000:
    scatter_df = scatter_df.sample(5000, random_state=42)

st.scatter_chart(
    scatter_df,
    x="trip_distance",
    y="fare_amount"
)