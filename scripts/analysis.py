import pandas as pd
import os
import matplotlib.pyplot as plt

def analyze(df):
    # Ensure required columns exist
    required_cols = ["pickup_hour", "fare_amount"]
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"Missing required column: {col}")

    # Convert columns to numeric (invalid values become NaN)
    df["pickup_hour"] = pd.to_numeric(df["pickup_hour"], errors="coerce")
    df["fare_amount"] = pd.to_numeric(df["fare_amount"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["pickup_hour", "fare_amount"])

    # Compute average fare by pickup hour
    result = df.groupby("pickup_hour")["fare_amount"].mean().sort_index()

    print("Analysis result:")
    print(result)

    return result


if __name__ == "__main__":
    input_path = "data/processed/transformed_taxi.csv"
    output_dir = "outputs/figures"
    output_path = f"{output_dir}/fare_by_hour.png"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load transformed data
    df = pd.read_csv(input_path, low_memory=False)

    # Run analysis
    result = analyze(df)

    # Plot results if data exists
    if result.empty:
        print("No valid numeric data available to plot.")
    else:
        plt.figure(figsize=(8, 5))
        result.plot()
        plt.xlabel("Pickup Hour")
        plt.ylabel("Average Fare Amount")
        plt.title("Average Fare by Pickup Hour")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

        print(f"Saved figure to {output_path}")