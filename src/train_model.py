"""
Purpose:
    Train a Logistic Regression model and make predictions.

Flow:
    MySQL
       ↓
    Data preparation
       ↓
    Train/Test Split
       ↓
    Logistic Regression
       ↓
    Training
       ↓
    Prediction
       ↓
    Model Evaluation
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
from sklearn.model_selection import train_test_split

from src.prepare_data import prepare_data


def main():
    """
    Prepare data, train the model, make predictions,
    and evaluate the model.
    """

    # ---------------------------------------------------------
    # 1. Prepare the ML-ready data.
    # ---------------------------------------------------------
    X, y, customer_ids = prepare_data()

    # ---------------------------------------------------------
    # 2. Split data into training and testing datasets.
    # ---------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # ---------------------------------------------------------
    # 3. Create the Logistic Regression model.
    # ---------------------------------------------------------
    model = LogisticRegression(
        max_iter=1000
    )

    # ---------------------------------------------------------
    # 4. Train the model.
    # ---------------------------------------------------------
    model.fit(X_train, y_train)

    print("Model training successful!")
    print("--------------------------------")
    print(f"Training records: {len(X_train)}")
    print(f"Testing records: {len(X_test)}")
    print(f"Number of features: {X_train.shape[1]}")

    print("\nModel:")
    print(model)

    print("\nModel training completed successfully!")

    # ---------------------------------------------------------
    # 5. Predict churn for unseen test data.
    # ---------------------------------------------------------
    y_pred = model.predict(X_test)

    print("\nActual churn values:")
    print(y_test.values)

    print("\nPredicted churn values:")
    print(y_pred)

    # ---------------------------------------------------------
    # 6. Evaluate the model.
    # ---------------------------------------------------------
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    print("\nModel Evaluation")
    print("----------------")
    print(f"Accuracy : {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall   : {recall:.2f}")
    print(f"F1 Score : {f1:.2f}")

    # ---------------------------------------------------------
    # 7. Generate confusion matrix.
    # ---------------------------------------------------------
    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)


if __name__ == "__main__":
    main()