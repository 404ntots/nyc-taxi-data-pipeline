import pandas as pd
import os

def transform(df):
    # Specify column names for green taxi dataset
    pickup_col = "lpep_pickup_datetime"
    dropoff_col = "lpep_dropoff_datetime"

    # Parse datetime columns
    df["pickup_parsed"] = pd.to_datetime(df[pickup_col], errors="coerce")
    df["dropoff_parsed"] = pd.to_datetime(df[dropoff_col], errors="coerce")

    # Extract pickup hour
    df["pickup_hour"] = df["pickup_parsed"].dt.hour

    # Compute trip duration in minutes
    df["trip_duration"] = (
        df["dropoff_parsed"] - df["pickup_parsed"]
    ).dt.total_seconds() / 60

    # Remove rows with invalid time values
    df = df.dropna(subset=["pickup_hour", "trip_duration"])

    # Filter unrealistic trip durations
    df = df[df["trip_duration"] > 0]
    df = df[df["trip_duration"] <= 300]

    return df


if __name__ == "__main__":
    input_path = "data/processed/clean_taxi.csv"
    output_path = "data/processed/transformed_taxi.csv"

    # Ensure output directory exists
    os.makedirs("data/processed", exist_ok=True)

    # Load cleaned data
    df = pd.read_csv(input_path, low_memory=False)
    print(f"Input shape: {df.shape}")

    # Transform data
    df_transformed = transform(df)
    print(f"Output shape: {df_transformed.shape}")

    # Save transformed data
    df_transformed.to_csv(output_path, index=False)
    print(f"Saved transformed data to {output_path}")