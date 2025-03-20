import pandas as pd
import numpy as np

# Function to generate daily sales data for a given date range
def generate_daily_sales_data(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    sales = np.random.randint(4000, 5000, size=len(dates))  # Random sales values between 1000 and 5000
    data = {'Date': dates, 'Sales': sales}
    df = pd.DataFrame(data)
    return df

# Function to save sales data to CSV file
def save_sales_data_to_csv(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Daily sales data saved to '{output_file}'.")

if __name__ == "__main__":
    # Specify the date range for generating daily sales data
    start_date = '2024-01-01'
    end_date = '2024-03-31'
    
    # Generate daily sales data for the specified date range
    daily_sales_data = generate_daily_sales_data(start_date, end_date)
    
    # Define output file path for daily sales data CSV
    output_file_path = 'daily_sales_data.csv'
    
    # Save daily sales data to CSV file
    save_sales_data_to_csv(daily_sales_data, output_file_path)
