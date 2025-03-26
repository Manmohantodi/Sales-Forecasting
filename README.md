# Sales Forecasting Project

## Overview

This project focuses on forecasting daily sales using Python and machine learning techniques. The goal is to analyze past sales data and predict future trends to help businesses make informed decisions.

## Features

- Reads sales data from a CSV file.
- Uses a rolling average method to forecast sales.
- Calculates error metrics like Root Mean Square Error (RMSE) and Mean Absolute Percentage Error (MAPE).
- Generates comparison values between actual and forecasted sales.
- Plots sales trends for visualization.
- Saves forecasted sales data to a CSV file.
- Includes a script to generate sample sales data.

## Technologies Used

- **Python** (pandas, numpy, matplotlib, sklearn)
- **Machine Learning** (Rolling Average Forecasting)
- **Data Visualization** (Matplotlib)
- **File Handling** (CSV)

## Project Structure

```
/Sales-Forecasting-Project
│── project.py              # Main forecasting script
│── project_csv.py          # Script to generate sample sales data
│── README.md               # Project documentation
│── requirements.txt        # Dependencies
│── .gitignore              # Ignore unnecessary files
│── LICENSE                 # License information (optional)
```

## Installation & Usage

1. Clone the repository
```bash
git clone https://github.com/Manmohantodi/Sales-Forecasting-Project.git
cd Sales-Forecasting-Project
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Generate Sample Sales Data
```bash
python project_csv.py
```

4. Run Sales Forecasting Model
```bash
python project.py
```

5. View Forecasted Results
- Open the `forecasted_sales_data.csv` file to view the predicted sales.
- Check the plotted graph for actual vs. forecasted sales.

## Future Enhancements

- Implement advanced machine learning models (ARIMA, LSTM).
- Improve accuracy with additional forecasting techniques.
- Develop an interactive dashboard for visualization.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
If you find this project useful, give it a star!

