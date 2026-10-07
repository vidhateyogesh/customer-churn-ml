"""
Purpose:
    Validate that the Python ML environment is working correctly.

This is our first project-level environment test.
"""

# Pandas is used for working with tabular data.
import pandas as pd

# NumPy is used for numerical calculations.
import numpy as np

# Scikit-learn is our main machine-learning library.
import sklearn

# Matplotlib is used for creating charts.
import matplotlib

# Seaborn is used for statistical visualizations.
import seaborn as sns

# MySQL Connector allows Python to communicate with MySQL.
import mysql.connector

# Joblib will later be used to save and load our trained ML model.
import joblib


def main():
    """
    Display the installed versions of our main libraries.
    """

    print("ML Environment Validation")
    print("-------------------------")

    print(f"Pandas: {pd.__version__}")
    print(f"NumPy: {np.__version__}")
    print(f"Scikit-learn: {sklearn.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"Seaborn: {sns.__version__}")
    print(f"MySQL Connector: {mysql.connector.__version__}")
    print(f"Joblib: {joblib.__version__}")

    print("\nEnvironment validation successful!")


# Execute the main function when this file is run directly.
if __name__ == "__main__":
    main()