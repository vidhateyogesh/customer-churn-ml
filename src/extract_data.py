"""
Purpose:
    Extract customer churn data from MySQL.

Flow:
    MySQL
       ↓
    SQL SELECT
       ↓
    MySQL Connector
       ↓
    Pandas DataFrame
       ↓
    Display data for validation
"""

# Pandas is used to store and work with tabular data.
import pandas as pd

# Import our reusable MySQL connection function.
from src.db_connection import create_engine_connection


def extract_customer_data():
    """
    Extract customer churn data from MySQL
    and return it as a Pandas DataFrame.
    """

    # SQL query used to extract the required customer data.
    query = """
        SELECT
            CustomerID,
            Age,
            TenureMonths,
            MonthlyCharges,
            SupportCalls,
            ContractType,
            PaymentMethod,
            Churn
        FROM customer_churn
        ORDER BY CustomerID;
    """

    # Create a connection to MySQL.
    
    engine = create_engine_connection()

    try:
        # Execute the SQL query and load the result
        # directly into a Pandas DataFrame.
        df = pd.read_sql(query, engine)

        return df

    finally:
        # Always close the database connection after extraction.
        


def main():
    """
    Run the data extraction and perform basic validation.
    """

    # Extract customer data from MySQL.
    df = extract_customer_data()

    print("Customer data extracted successfully!")
    print("--------------------------------------")

    # Display the number of rows and columns.
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nFirst 5 records:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nChurn distribution:")
    print(df["Churn"].value_counts())


# Execute main() when this script is run directly.
if __name__ == "__main__":
    main()