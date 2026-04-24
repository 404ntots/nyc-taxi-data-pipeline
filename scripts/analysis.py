import pandas as pd
import os
import matplotlib.pyplot as plt

def analyze(df):
    # Ensure numeric
    df["total_amount"] = pd.to_numeric(df["total_amount"], errors="coerce")
    df["trip_distance"] = pd.to_numeric(df["trip_distance"], errors="coerce")
    df["tip_amount"] = pd.to_numeric(df["tip_amount"], errors="coerce")
    df["fare_amount"] = pd.to_numeric(df["fare_amount"], errors="coerce")


    df = df.dropna(subset=["pickup_hour", "total_amount"])

    results = {}

    # Revenue by hour
    revenue_by_hour = df.groupby("pickup_hour")["total_amount"].mean()
    results["revenue_by_hour"] = revenue_by_hour

    #  Tip behavior
    tip_by_payment = df.groupby("payment_type")["tip_amount"].mean()
    results["tip_by_payment"] = tip_by_payment

    #  Distance vs revenue
    results["distance"] = df["trip_distance"]
    results["fare"] = df["total_amount"]

    #  Trip count by hour (demand)
    trip_count_by_hour = df.groupby("pickup_hour").size()
    results["trip_count_by_hour"] = trip_count_by_hour

    # Fare by hour
    fare_by_hour = df.groupby("pickup_hour")["fare_amount"].mean()
    results["fare_by_hour"] = fare_by_hour

        # Weekday demand
    df["pickup_parsed"] = pd.to_datetime(df["lpep_pickup_datetime"], errors="coerce")
    df["pickup_weekday"] = df["pickup_parsed"].dt.day_name()

    weekday_order = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    trips_by_weekday = df["pickup_weekday"].value_counts().reindex(weekday_order)
    results["trips_by_weekday"] = trips_by_weekday

    # Top pickup locations
    top_pickup_locations = df["PULocationID"].value_counts().head(10)
    results["top_pickup_locations"] = top_pickup_locations

    # Payment type distribution
    payment_counts = df["payment_type"].value_counts().sort_index()
    results["payment_counts"] = payment_counts


    return results


def plot_results(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Plot 1: revenue by hour
    plt.figure()
    results["revenue_by_hour"].plot()
    plt.title("Average Revenue by Hour")
    plt.savefig(f"{output_dir}/revenue_by_hour.png")
    plt.close()

    # Plot 2: tip by payment
    plt.figure()
    results["tip_by_payment"].plot(kind="bar")
    plt.title("Tip by Payment Type")
    plt.savefig(f"{output_dir}/tip_by_payment.png")
    plt.close()

    # Plot 3: distance vs fare
    plt.figure()
    plt.scatter(results["distance"], results["fare"], alpha=0.3)
    plt.title("Distance vs Fare")
    plt.xlabel("Distance")
    plt.ylabel("Fare")
    plt.savefig(f"{output_dir}/distance_vs_fare.png")
    plt.close()

    # Plot 4: trip count by hour
    plt.figure()
    results["trip_count_by_hour"].plot()
    plt.title("Trip Count by Hour")
    plt.savefig(f"{output_dir}/trip_count_by_hour.png")
    plt.close()

    # Plot 5: fare by hour
    plt.figure()
    results["fare_by_hour"].plot()
    plt.title("Average Fare by Hour")
    plt.savefig(f"{output_dir}/fare_by_hour.png")
    plt.close()

    # Plot 6: trips by weekday
    plt.figure()
    results["trips_by_weekday"].plot(kind="bar")
    plt.title("Trips by Weekday")
    plt.xlabel("Weekday")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/trips_by_weekday.png")
    plt.close()

    # Plot 7: top pickup locations
    plt.figure()
    results["top_pickup_locations"].plot(kind="bar")
    plt.title("Top 10 Pickup Locations")
    plt.xlabel("Pickup Location ID")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_pickup_locations.png")
    plt.close()

    # Plot 8: payment type distribution
    plt.figure()
    results["payment_counts"].plot(kind="bar")
    plt.title("Payment Type Distribution")
    plt.xlabel("Payment Type")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/payment_type_distribution.png")
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv("data/processed/transformed_taxi.csv")

    results = analyze(df)
    plot_results(results, "outputs/figures")

    print("Analysis complete. Charts saved.")