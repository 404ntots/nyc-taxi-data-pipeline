import pandas as pd
import os

def clean_data(df):
    # Print original dataset size
    print(f"Original shape: {df.shape}")

    # Keep only rows where key columns are not missing
    required_cols = [
        "lpep_pickup_datetime",
        "lpep_dropoff_datetime",
        "trip_distance",
        "fare_amount"
    ]
    df = df.dropna(subset=required_cols)
    print(f"After dropping missing required columns: {df.shape}")

    # Convert columns to numeric (invalid values become NaN)
    df["trip_distance"] = pd.to_numeric(df["trip_distance"], errors="coerce")
    df["fare_amount"] = pd.to_numeric(df["fare_amount"], errors="coerce")

    # Remove rows where numeric conversion failed
    df = df.dropna(subset=["trip_distance", "fare_amount"])
    print(f"After numeric conversion cleanup: {df.shape}")

    # Keep only positive values
    df = df[df["trip_distance"] > 0]
    df = df[df["fare_amount"] > 0]
    print(f"After filtering positive values: {df.shape}")

    # Remove extreme outliers (basic thresholding)
    df = df[df["trip_distance"] <= 100]
    df = df[df["fare_amount"] <= 500]
    print(f"After outlier filtering: {df.shape}")

    return df


if __name__ == "__main__":
    input_path = "data/raw/taxi_tripdata.csv"
    output_path = "data/processed/clean_taxi.csv"

    # Ensure output directory exists
    os.makedirs("data/processed", exist_ok=True)

    # Load raw data
    df = pd.read_csv(input_path, low_memory=False)

    # Clean data
    df_clean = clean_data(df)

    # Save cleaned data
    df_clean.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")