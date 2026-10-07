"""
Purpose:
    Split the ML-ready data into training and testing datasets.

Flow:
    Prepared Data
        ↓
    X (Features) + y (Target)
        ↓
    Train/Test Split
        ↓
    Training Data + Testing Data

Why:
    The model learns from training data and is evaluated
    using unseen testing data.
"""

from sklearn.model_selection import train_test_split

from src.prepare_data import prepare_data


def main():
    """
    Prepare the data and split it into training and testing sets.
    """

    # ---------------------------------------------------------
    # 1. Get ML-ready features, target and Customer IDs.
    # ---------------------------------------------------------
    X, y, customer_ids = prepare_data()

    # ---------------------------------------------------------
    # 2. Split the data.
    #
    # test_size=0.20:
    #   20% of records are reserved for testing.
    #
    # random_state=42:
    #   Makes the split repeatable.
    #
    # stratify=y:
    #   Keeps the Yes/No churn distribution balanced
    #   between training and testing datasets.
    # ---------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # ---------------------------------------------------------
    # 3. Display the results.
    # ---------------------------------------------------------
    print("Train/Test Split Successful!")
    print("--------------------------------")

    print(f"Total records: {len(X)}")
    print(f"Training records: {len(X_train)}")
    print(f"Testing records: {len(X_test)}")

    print("\nTraining target distribution:")
    print(y_train.value_counts())

    print("\nTesting target distribution:")
    print(y_test.value_counts())

    print("\nTraining feature shape:")
    print(X_train.shape)

    print("\nTesting feature shape:")
    print(X_test.shape)


if __name__ == "__main__":
    main()