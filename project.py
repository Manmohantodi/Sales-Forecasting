#Sales Forecasting Project
#Group N0. -- 16

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Function to read sales data from CSV file
def read_sales_data(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    return df

# Function to calculate daily forecasted sales using a rolling average
def calculate_rolling_forecast(df, window_size=2):
    df['Rolling Sales Mean'] = df['Sales'].rolling(window=window_size, min_periods=1).mean()
    df['Forecasted Sales'] = df['Rolling Sales Mean']
    return df

# Function to calculate Root Mean Square Error (RMSE)
def calculate_rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# Function to calculate Mean Absolute Percentage Error (MAPE)
def calculate_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Function to print comparison values
def print_comparison_values(actual, forecasted):
    print("Comparison Values:")
    print("===================")
    print(f"Mean Actual Sales: {actual.mean()}")
    print(f"Mean Forecasted Sales: {forecasted.mean()}")
    print(f"Max Actual Sales: {actual.max()}")
    print(f"Max Forecasted Sales: {forecasted.max()}")
    print(f"Min Actual Sales: {actual.min()}")
    print(f"Min Forecasted Sales: {forecasted.min()}")
    print("===================")

# Function to plot comparison of actual sales with forecasted sales
def plot_sales_comparison(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Sales'], label='Actual Sales', color='green')
    plt.plot(df['Date'], df['Forecasted Sales'], label='Forecasted Sales', color='red')
    plt.title('Actual vs. Forecasted Sales')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
   # plt.tight_layout()
    plt.show()

# Function to save forecasted data to CSV file
def save_forecasted_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Forecasted data saved to '{output_file}'.")

# Main function to read, process, and save data
def main(input_file, output_file):
    # Read sales data
    sales_data = read_sales_data(input_file)
    
    # Calculate rolling forecasted sales
    sales_data_forecasted = calculate_rolling_forecast(sales_data.copy())
    
    # Calculate RMSE
    rmse = calculate_rmse(sales_data['Sales'], sales_data_forecasted['Forecasted Sales'])
    print(f"Root Mean Square Error (RMSE): {rmse:.2f}")
    
    # Calculate MAPE
    mape = calculate_mape(sales_data['Sales'], sales_data_forecasted['Forecasted Sales'])
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
    
    # Print additional comparison values
    print_comparison_values(sales_data['Sales'], sales_data_forecasted['Forecasted Sales'])
    
    # Save forecasted data to CSV file
    save_forecasted_data(sales_data_forecasted, output_file)
    
    # Plot comparison of actual sales with forecasted sales
    plot_sales_comparison(sales_data_forecasted)

if __name__ == "__main__":
    # Input and output file paths
    input_file_path = 'daily_sales_data.csv'
    output_file_path = 'forecasted_sales_data.csv'
    
    # Run the main function to process data and save forecasted sales to CSV
    main(input_file_path, output_file_path)
