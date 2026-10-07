"""
Purpose:
    Prepare customer churn data for machine learning.

Flow:
    MySQL
       ↓
    Extract data
       ↓
    Separate features (X) and target (y)
       ↓
    Remove CustomerID
       ↓
    Encode categorical features
       ↓
    Convert Churn Yes/No to 1/0
       ↓
    ML-ready data
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.extract_data import extract_customer_data


def prepare_data():
    """
    Extract and transform the customer churn data.

    Returns:
        X: ML features
        y: ML target
        customer_ids: Customer IDs kept separately for identification
    """

    # ---------------------------------------------------------
    # 1. Extract data from MySQL
    # ---------------------------------------------------------
    df = extract_customer_data()

    # ---------------------------------------------------------
    # 2. Keep CustomerID separately.
    #    CustomerID is an identifier, not a useful ML feature.
    # ---------------------------------------------------------
    customer_ids = df["CustomerID"]

    # ---------------------------------------------------------
    # 3. Separate target from input features.
    #    Churn is what we want the model to predict.
    # ---------------------------------------------------------
    y = df["Churn"].map({
        "No": 0,
        "Yes": 1
    })

    X = df.drop(columns=["CustomerID", "Churn"])

    # ---------------------------------------------------------
    # 4. Identify categorical columns.
    # ---------------------------------------------------------
    categorical_columns = [
        "ContractType",
        "PaymentMethod"
    ]

    # ---------------------------------------------------------
    # 5. Identify numerical columns.
    # ---------------------------------------------------------
    numerical_columns = [
        "Age",
        "TenureMonths",
        "MonthlyCharges",
        "SupportCalls"
    ]

    # ---------------------------------------------------------
    # 6. One-Hot Encode categorical columns.
    #
    # Example:
    # Annual  → ContractType_Annual = 1
    # Monthly → ContractType_Monthly = 1
    # ---------------------------------------------------------
    encoder = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )

    encoded_data = encoder.fit_transform(
        X[categorical_columns]
    )

    encoded_columns = encoder.get_feature_names_out(
        categorical_columns
    )

    encoded_df = pd.DataFrame(
        encoded_data,
        columns=encoded_columns,
        index=X.index
    )

    # ---------------------------------------------------------
    # 7. Keep numerical columns and combine them
    #    with the encoded categorical columns.
    # ---------------------------------------------------------
    X_prepared = pd.concat(
        [
            X[numerical_columns],
            encoded_df
        ],
        axis=1
    )

    return X_prepared, y, customer_ids


def main():
    """
    Test the data-preparation process.
    """

    X, y, customer_ids = prepare_data()

    print("Data preparation successful!")
    print("--------------------------------")

    print(f"Number of records: {len(X)}")
    print(f"Number of ML features: {X.shape[1]}")

    print("\nFeature columns:")
    for column in X.columns:
        print(f"- {column}")

    print("\nFirst 5 prepared records:")
    print(X.head())

    print("\nTarget values:")
    print(y.value_counts())

    print("\nCustomer IDs kept separately:")
    print(customer_ids.head())


if __name__ == "__main__":
    main()