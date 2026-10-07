"""
Purpose:
    Validate the customer churn data before ML processing.

Checks:
    1. Expected number of records
    2. Required columns
    3. Missing values
    4. Valid Churn values
    5. Duplicate Customer IDs
"""

from src.extract_data import extract_customer_data


def main():
    """
    Run all basic data-quality validations.
    """

    # Extract the latest data from MySQL.
    df = extract_customer_data()

    print("Starting data validation...")
    print("---------------------------")

    # ---------------------------------------------------------
    # Validation 1: Record count
    # ---------------------------------------------------------

    expected_records = 30

    actual_records = len(df)

    print(f"Record count: {actual_records}")

    assert actual_records == expected_records, (
        f"Expected {expected_records} records, "
        f"but found {actual_records}"
    )

    print("PASS - Record count")


    # ---------------------------------------------------------
    # Validation 2: Required columns
    # ---------------------------------------------------------

    required_columns = [
        "CustomerID",
        "Age",
        "TenureMonths",
        "MonthlyCharges",
        "SupportCalls",
        "ContractType",
        "PaymentMethod",
        "Churn"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    assert not missing_columns, (
        f"Missing columns: {missing_columns}"
    )

    print("PASS - Required columns")


    # ---------------------------------------------------------
    # Validation 3: Missing values
    # ---------------------------------------------------------

    total_missing = df.isnull().sum().sum()

    print(f"Total missing values: {total_missing}")

    assert total_missing == 0, (
        f"Found {total_missing} missing values"
    )

    print("PASS - No missing values")


    # ---------------------------------------------------------
    # Validation 4: Churn values
    # ---------------------------------------------------------

    valid_churn_values = {"Yes", "No"}

    actual_churn_values = set(df["Churn"].unique())

    assert actual_churn_values.issubset(valid_churn_values), (
        f"Unexpected Churn values: {actual_churn_values}"
    )

    print("PASS - Churn values")


    # ---------------------------------------------------------
    # Validation 5: Duplicate Customer IDs
    # ---------------------------------------------------------

    duplicate_count = df["CustomerID"].duplicated().sum()

    print(f"Duplicate Customer IDs: {duplicate_count}")

    assert duplicate_count == 0, (
        f"Found {duplicate_count} duplicate Customer IDs"
    )

    print("PASS - No duplicate Customer IDs")


    print("\nAll data validations passed successfully!")


if __name__ == "__main__":
    main()