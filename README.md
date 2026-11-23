# PRICEIQ – Retail Pricing Intelligence System

## Project Overview

PRICEIQ is a data-driven retail pricing intelligence system developed using Python and Streamlit.

The application analyses retail transaction data to estimate price elasticity, identify product pricing opportunities, understand customer segments, and support informed pricing decisions.

## Key Features

PRICEIQ consists of six interactive dashboard sections:

1. **Executive Overview:** Presents key business and pricing performance indicators.
2. **Product Intelligence:** Identifies products and categories with potential pricing opportunities.
3. **Customer Segments:** Explores customer purchasing behaviour and demographic characteristics.
4. **Pricing Simulator:** Simulates potential revenue impacts resulting from price changes.
5. **Profitability Analysis:** Provides insights into product and portfolio profitability.
6. **Custom Elasticity Estimator:** Allows users to estimate price elasticity for selected products.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy

## Project Structure

```text
elasticity-model/
│
├── app.py
├── requirements.txt
├── README.md
├── PRICEIQ_Final_Project_Report.docx
│
└── pricing_dashboard_data/
    └── CSV data files
```

## Installation Requirements

Before running PRICEIQ, ensure that you have:

- Python 3.10 or later
- pip (Python package installer)

## How to Run PRICEIQ

### 1. Download the Project

Clone the GitHub repository or download the project as a ZIP file.

### 2. Open the Project Folder

Open a terminal inside the project directory.

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

### 5. Launch the Application

Run:

```bash
python -m streamlit run app.py
```

### 6. Access the Dashboard

Open your browser and navigate to:

```text
http://localhost:8501
```

The PRICEIQ dashboard should now be running.

To stop the application, press `Ctrl + C` in the terminal.

## Important Notes

- Keep the `pricing_dashboard_data` folder in the project directory.
- Do not rename or move the required CSV files.
- PRICEIQ is a decision-support tool. Pricing recommendations should be reviewed before implementation.
- Model estimates are based on historical data and should not be interpreted as guaranteed business outcomes.

## Author

**Prosper Tasiyana**

PRICEIQ – Retail Pricing Intelligence System